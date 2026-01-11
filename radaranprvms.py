#!/usr/bin/env python3
"""
Radar-ANPR-VMS Integration System
Combines radar detection, ANPR (camera plate recognition), and VMS display.
Displays all detected license plates on VMS display.
Stores all detections in daily JSON files.
"""

from requests.auth import HTTPDigestAuth
from threading import Thread, Lock
import requests
import json
import time
import socket
import re
import subprocess
import os
import serial
from datetime import datetime
from typing import Optional, Dict, Any

# ============================================================================
# CONFIGURATION
# ============================================================================

# Camera configuration
CAMERA_USERNAME = 'admin'
CAMERA_PASSWORD = 'kObliha12@'
CAMERA_IP = '192.168.2.13'
CAMERA_PORT = 80
RECEIVE_ALARM_DATA_IP = "192.168.2.101"
RECEIVE_ALARM_DATA_PORT = 8090
DURATION = 300
SUBSCRIPTION_ID = -1
CAMERA_URL = f'http://{CAMERA_IP}:{CAMERA_PORT}/LAPI/V1.0/System/Event/Subscription'

# Radar configuration
RADAR_PORT = '/dev/ttyAMA0'
RADAR_BAUDRATE = 9600
RADAR_TIMEOUT = 0.01
ONLY_POSITIVE_DIRECTION = False  # Set to False to display all directions
POSITIVE_DIRECTION_NAME = "IMR_KD-B"  # Name for positive direction (+)
NEGATIVE_DIRECTION_NAME = "IMR_KD-KO"  # Name for negative direction (-)
CONSECUTIVE_ZEROS_THRESHOLD = 3  # Number of consecutive zeros to end detection
MIN_SPEED_FOR_DISPLAY = 40  # Minimum speed (km/h) to display plate on VMS
SPEED_LIMIT = 50  # Speed limit (km/h) - vehicles above this speed without plate detection show "ZPOMAL!"
RADAR_CAMERA_TIME_WINDOW = 15  # Maximum seconds between radar detection and camera detection to consider them matched

# VMS Configuration (CP5200 Display)
VMS_IP = "192.168.1.222"
VMS_PORT = 5200
SENDCP5200_PATH = "./sendcp5200/dist/Debug/GNU-Linux/sendcp5200"
VMS_DISPLAY_TIME = 3  # Time in seconds to display plate before clearing

# Data storage
DETECTIONS_FOLDER = "detections"

# ============================================================================
# GLOBAL STATE
# ============================================================================

# HTTP request header
headers = {
    'Content-Type': 'application/json',
    'Host': f'{CAMERA_IP}:{CAMERA_PORT}',
    'Connection': 'Close',
}

# Radar state - Vehicle detection tracking
_radar_lock = Lock()
_current_detection = []  # List of readings for current vehicle (0 -> peak -> 0)
_current_direction = None  # '+' or '-' for current detection
_completed_detections = []  # Queue of completed detections with peak speed
_max_completed_detections = 10  # Keep last 10 completed detections

# Detection storage
_detections_lock = Lock()
_current_date = None
_detections_file = None

# VMS display state
_vms_clear_thread = None
_vms_lock = Lock()
_speed_violation_active = False  # Track if speed violation is currently displayed
_speed_violation_lock = Lock()
_matched_radar_detections = set()  # Track radar detection end_times that have been matched with plates
_matched_detections_lock = Lock()

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def ensure_detections_folder():
    """Ensure detections folder exists"""
    if not os.path.exists(DETECTIONS_FOLDER):
        os.makedirs(DETECTIONS_FOLDER)
        print(f"Created detections folder: {DETECTIONS_FOLDER}")

def get_daily_json_filename():
    """Get filename for today's detection JSON file (DD_MM_YYYY.json)"""
    return datetime.now().strftime('%d_%m_%Y.json')

def get_daily_json_path():
    """Get full path for today's detection JSON file"""
    filename = get_daily_json_filename()
    return os.path.join(DETECTIONS_FOLDER, filename)

def save_detection(detection_data: Dict[str, Any]):
    """Save a detection to today's JSON file immediately (append-only to prevent memory clogging)"""
    global _current_date, _detections_file
    
    ensure_detections_folder()
    
    # Check if date changed or file not initialized
    today = datetime.now().date()
    if _current_date != today or _detections_file is None:
        _current_date = today
        _detections_file = get_daily_json_path()
    
    with _detections_lock:
        filepath = _detections_file
        
        try:
            # Read existing detections (if file exists)
            detections = []
            if os.path.exists(filepath):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        detections = json.load(f)
                        if not isinstance(detections, list):
                            detections = []
                except (json.JSONDecodeError, IOError):
                    detections = []
            
            # Add new detection
            detections.append(detection_data)
            
            # Write immediately and flush to disk
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(detections, f, indent=2, ensure_ascii=False)
                f.flush()
                os.fsync(f.fileno())  # Force write to disk
            
            # Clear from memory immediately
            del detections
        except Exception as e:
            print(f"Error saving detection: {e}")

# ============================================================================
# RADAR FUNCTIONS - Vehicle Detection Tracking
# ============================================================================

def process_radar_reading(direction_sign: str, speed: int):
    """
    Process radar reading and track complete vehicle detections (0 -> peak -> 0)
    Detects when a vehicle passes: 0 -> rising -> peak -> falling -> 0
    Tracks Gaussian-like pattern and extracts peak speed
    """
    global _current_detection, _current_direction, _completed_detections
    
    with _radar_lock:
        # Add current reading to detection (always, even if 0)
        reading = {
            'speed': speed,
            'direction_sign': direction_sign,
            'timestamp': datetime.now().isoformat()
        }
        
        # If speed is 0
        if speed == 0:
            if not _current_detection:
                # No active detection, just ignore zeros
                return
            
            # We have an active detection - add the zero reading
            _current_detection.append(reading)
            
            # Check if we have enough consecutive zeros to complete detection
            # Look at last N readings
            if len(_current_detection) >= CONSECUTIVE_ZEROS_THRESHOLD:
                recent_readings = _current_detection[-CONSECUTIVE_ZEROS_THRESHOLD:]
                all_zeros = all(r['speed'] == 0 for r in recent_readings)
                
                if all_zeros:
                    # We have consecutive zeros - complete the detection
                    # Filter out zeros to find peak from actual vehicle readings
                    vehicle_readings = [r for r in _current_detection if r['speed'] > 0]
                    
                    if vehicle_readings:
                        peak_speed = max(r['speed'] for r in vehicle_readings)
                        direction_name = POSITIVE_DIRECTION_NAME if _current_direction == '+' else NEGATIVE_DIRECTION_NAME
                        completed = _create_completed_detection(
                            _current_direction, direction_name, peak_speed,
                            _current_detection, _current_detection[0]['timestamp']
                        )
                        
                        _completed_detections.append(completed)
                        if len(_completed_detections) > _max_completed_detections:
                            _completed_detections.pop(0)
                        
                        print(f"✓ Radar: {completed['direction_name']} | {peak_speed}km/h")
                        
                        # Check for speed violation (no plate detected, speed > limit)
                        try:
                            if peak_speed > SPEED_LIMIT:
                                Thread(target=_check_and_display_speed_violation, args=(completed,), daemon=True).start()
                        except Exception as e:
                            print(f"Warning: Error starting speed violation check: {e}")
                    
                    # Reset for next detection
                    _current_detection = []
                    _current_direction = None
            
            return
        
        # Non-zero speed - we have a vehicle
        if not _current_detection:
            # Start new detection (transition from 0 to non-zero)
            _current_detection = [reading]
            _current_direction = direction_sign
            # Vehicle detection started (suppress message for cleaner output)
        else:
            # Continue current detection
            if _current_direction == direction_sign:
                # Same direction - add to current detection
                _current_detection.append(reading)
            else:
                # Direction changed - complete old detection and start new
                vehicle_readings = [r for r in _current_detection if r['speed'] > 0]
                if vehicle_readings:
                    peak_speed = max(r['speed'] for r in vehicle_readings)
                    direction_name = POSITIVE_DIRECTION_NAME if _current_direction == '+' else NEGATIVE_DIRECTION_NAME
                    completed = _create_completed_detection(
                        _current_direction, direction_name, peak_speed,
                        _current_detection, _current_detection[0]['timestamp']
                    )
                    _completed_detections.append(completed)
                    if len(_completed_detections) > _max_completed_detections:
                        _completed_detections.pop(0)
                    print(f"✓ Radar: {completed['direction_name']} | {peak_speed}km/h")
                    
                    # Check for speed violation (no plate detected, speed > limit)
                    try:
                        if peak_speed > SPEED_LIMIT:
                            Thread(target=_check_and_display_speed_violation, args=(completed,), daemon=True).start()
                    except Exception as e:
                        print(f"Warning: Error starting speed violation check: {e}")
                
                # Start new detection with new direction
                _current_detection = [reading]
                _current_direction = direction_sign
                # Vehicle detection started (suppress message for cleaner output)

def _create_completed_detection(direction_sign: str, direction_name: str, peak_speed: int, 
                                detection_readings: list, start_time: str) -> Dict[str, Any]:
    """Create a completed detection dictionary"""
    return {
        'direction_sign': direction_sign,
        'direction_name': direction_name,
        'peak_speed': peak_speed,
        'readings_count': len(detection_readings),
        'start_time': start_time,
        'end_time': datetime.now().isoformat(),
        'timestamp': datetime.now().isoformat()
    }

def _check_and_display_speed_violation(radar_detection: Dict[str, Any]):
    """
    Check if speed violation should be displayed (no plate detected, speed > limit)
    Runs in background thread for fast response
    """
    global _speed_violation_active, _matched_radar_detections
    
    peak_speed = radar_detection['peak_speed']
    if peak_speed <= SPEED_LIMIT:
        return
    
    detection_id = radar_detection['end_time']
    
    # Wait a short time to see if camera detects a plate for this vehicle
    time.sleep(1.0)
    
    # Check if this detection was already matched with a plate
    with _matched_detections_lock:
        if detection_id in _matched_radar_detections:
            return  # Plate detected, skip violation
    
    # Check if detection is still recent
    try:
        detection_end_time = datetime.fromisoformat(radar_detection['end_time'])
        time_since_detection = (datetime.now() - detection_end_time).total_seconds()
    except Exception as e:
        return
    
    # Display violation if still within reasonable time window
    if time_since_detection <= 5:
        with _speed_violation_lock:
            if not _speed_violation_active:
                _speed_violation_active = True
                
                print(f"\n⚠️  SPEED VIOLATION: {peak_speed}km/h > {SPEED_LIMIT}km/h | {radar_detection['direction_name']} | Displaying 'ZPOMAL!'\n")
                
                try:
                    send_plate_to_vms("ZPOMAL!")
                except Exception as e:
                    print(f"Error sending speed violation: {e}")
                
                time.sleep(VMS_DISPLAY_TIME)
                with _speed_violation_lock:
                    _speed_violation_active = False

def get_latest_completed_detection(max_age_seconds: float = RADAR_CAMERA_TIME_WINDOW) -> Optional[Dict[str, Any]]:
    """
    Get the most recent completed vehicle detection (thread-safe)
    Only returns detections that are within max_age_seconds of current time
    """
    global _completed_detections, _current_detection, _current_direction
    
    with _radar_lock:
        # First check if there's an in-progress detection that might match
        if _current_detection and _current_direction:
            # Check if current detection has vehicle readings (non-zero speeds)
            vehicle_readings = [r for r in _current_detection if r['speed'] > 0]
            if vehicle_readings:
                # Get the most recent reading timestamp
                try:
                    latest_reading_time = datetime.fromisoformat(_current_detection[-1]['timestamp'])
                    time_diff = (datetime.now() - latest_reading_time).total_seconds()
                    
                    # If current detection is very recent (within 5 seconds), use it
                    if time_diff <= 5:
                        peak_speed = max(r['speed'] for r in vehicle_readings)
                        direction_name = POSITIVE_DIRECTION_NAME if _current_direction == '+' else NEGATIVE_DIRECTION_NAME
                        in_progress_detection = {
                            'direction_sign': _current_direction,
                            'direction_name': direction_name,
                            'peak_speed': peak_speed,
                            'readings_count': len(_current_detection),
                            'start_time': _current_detection[0]['timestamp'],
                            'end_time': _current_detection[-1]['timestamp'],
                            'timestamp': datetime.now().isoformat(),
                            'in_progress': True
                        }
                        return in_progress_detection
                except (ValueError, KeyError):
                    pass
        
        # Check completed detections - check from most recent to oldest
        if not _completed_detections:
            return None
        
        # Check recent detections (most recent first)
        now = datetime.now()
        for detection in reversed(_completed_detections):
            try:
                # Check both start_time and end_time to see if detection is within window
                detection_start = datetime.fromisoformat(detection['start_time'])
                detection_end = datetime.fromisoformat(detection['end_time'])
                
                # Calculate time differences
                time_since_start = (now - detection_start).total_seconds()
                time_since_end = (now - detection_end).total_seconds()
                
                # Accept if detection ended recently OR started recently (within window)
                # This handles cases where camera detects during or shortly after radar detection
                if time_since_end <= max_age_seconds or time_since_start <= max_age_seconds:
                    return detection.copy()
                    
            except (ValueError, KeyError) as e:
                # Skip this detection if timestamp parsing fails
                continue
        
        # No recent detections found
        if _completed_detections:
            latest = _completed_detections[-1]
            try:
                detection_end_time = datetime.fromisoformat(latest['end_time'])
                time_diff = (now - detection_end_time).total_seconds()
                print(f"  ⚠️  All radar detections too old (latest: {time_diff:.1f}s ago, max {max_age_seconds}s)")
            except:
                pass
        return None

def read_radar_data():
    """Read radar data from serial port in background thread"""
    print(f"Starting radar reader on {RADAR_PORT}...")
    
    try:
        ser = serial.Serial(
            port=RADAR_PORT,
            baudrate=RADAR_BAUDRATE,
            timeout=RADAR_TIMEOUT
        )
        print(f"✓ Connected to radar on {RADAR_PORT}")
        
        buffer = b''
        
        while True:
            try:
                data = ser.read(32)
                if data:
                    buffer += data
                    
                    # Process complete messages (5 bytes: A+XXX or A-XXX)
                    while len(buffer) >= 5:
                        chunk = buffer[:5]
                        buffer = buffer[5:]
                        
                        if chunk.startswith(b'A') and len(chunk) == 5:
                            try:
                                decoded = chunk.decode('utf-8', errors='ignore')
                                if decoded[1] in '+-':
                                    direction_sign = decoded[1]
                                    speed_str = decoded[2:]
                                    speed = int(speed_str)
                                    
                                    # Process radar reading (tracks complete vehicle detections)
                                    process_radar_reading(direction_sign, speed)
                                    # Debug: Print raw radar readings (can be removed later)
                                    # print(f"  Radar: {direction_sign} {speed}km/h")
                            except (ValueError, IndexError):
                                pass
                
                time.sleep(0.01)  # Small delay to prevent CPU spinning
                
            except Exception as e:
                print(f"Radar read error: {e}")
                time.sleep(1)
                
    except serial.SerialException as e:
        print(f"Radar connection error: {e}")
        print("Radar reading disabled. Continuing without radar data...")
    except Exception as e:
        print(f"Radar error: {e}")
        print("Radar reading disabled. Continuing without radar data...")

# ============================================================================
# VMS FUNCTIONS
# ============================================================================

def send_plate_to_vms(plate_number: str):
    """Send plate number to VMS display using direct command execution"""
    global _vms_clear_thread
    
    # Use empty string for clearing, otherwise use the plate number
    display_text = plate_number if plate_number and plate_number.strip() else ""
    
    # Cancel any pending clear thread if new plate is being displayed
    # Also cancel speed violation if displaying a plate
    with _vms_lock:
        if _vms_clear_thread is not None and display_text:
            _vms_clear_thread = None
        
        # If displaying a plate, cancel any speed violation
        if display_text and display_text != "ZPOMAL!":
            with _speed_violation_lock:
                _speed_violation_active = False
    
    # Build command: ./sendcp5200/dist/Debug/GNU-Linux/sendcp5200 0 192.168.1.222 5200 2 0 AHOJ -1 22 0 0 10 1
    cmd = [
        SENDCP5200_PATH,
        "0",
        VMS_IP,
        str(VMS_PORT),
        "2",
        "0",
        display_text,  # Plate number or empty string
        "-1",          # Color
        "22",          # Font size
        "0",           # Speed
        "0",           # Effect
        "10",          # Stay time
        "1"            # Alignment
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        
        if result.returncode == 0:
            if display_text:
                print(f"✓ VMS: '{display_text}' → {VMS_IP}:{VMS_PORT}")
                
                # Schedule auto-clear after display time
                def clear_after_delay(plate_id):
                    global _vms_clear_thread
                    time.sleep(VMS_DISPLAY_TIME)
                    
                    with _vms_lock:
                        # Only clear if this thread is still the active one (no new plate displayed)
                        if _vms_clear_thread is not None:
                            # Clear the display
                            clear_cmd = [
                                SENDCP5200_PATH,
                                "0",
                                VMS_IP,
                                str(VMS_PORT),
                                "2",
                                "0",
                                "",  # Empty string to clear
                                "-1",
                                "22",
                                "0",
                                "0",
                                "10",
                                "1"
                            ]
                            try:
                                subprocess.run(clear_cmd, capture_output=True, text=True, timeout=5)
                            except:
                                pass
                            _vms_clear_thread = None
                
                with _vms_lock:
                    _vms_clear_thread = Thread(target=clear_after_delay, args=(display_text,), daemon=True)
                    _vms_clear_thread.start()
            else:
                print(f"✓ Cleared VMS display")
            if result.stdout:
                print(f"  sendcp5200 output: {result.stdout.strip()}")
            return True
        else:
            if result.stdout:
                print(f"  sendcp5200 output: {result.stdout.strip()}")
            if result.stderr:
                print(f"  sendcp5200 error: {result.stderr.strip()}")
            print(f"✗ Failed to send to VMS")
            return False
    except Exception as e:
        print(f"Error sending to VMS: {e}")
        return False

# ============================================================================
# CAMERA/ANPR FUNCTIONS
# ============================================================================

def extract_plate_number(data_json):
    """Extract plate number from camera event data"""
    try:
        if "StructureInfo" in data_json:
            structure_info = data_json.get("StructureInfo", {})
            obj_info = structure_info.get("ObjInfo", {})
            vehicle_info_list = obj_info.get("VehicleInfoList", [])
            
            if isinstance(vehicle_info_list, list) and vehicle_info_list:
                vehicle_info = vehicle_info_list[0]
                plate_no = vehicle_info.get("PlateAttributeInfo", {}).get("PlateNo", None)
                if plate_no and plate_no != "Unknown" and plate_no.strip():
                    return plate_no
        return None
    except (KeyError, TypeError, AttributeError):
        return None

def keepalive():
    """Keep camera subscription alive"""
    while True:
        keepalive_url = f"{CAMERA_URL}/{SUBSCRIPTION_ID}"
        data = {'Duration': DURATION}
        json_str = json.dumps(data)
        
        try:
            response = requests.put(url=keepalive_url, headers=headers, data=json_str, 
                                  auth=HTTPDigestAuth(CAMERA_USERNAME, CAMERA_PASSWORD), timeout=5)
            if response.status_code != 200:
                print(f'Keepalive failure: {response.status_code}')
                raise SystemExit(0)
        except Exception as e:
            print(f'Keepalive error: {e}')
            raise SystemExit(0)
        
        time.sleep(DURATION / 2)

def listen_camera_events():
    """Listen for camera ANPR events"""
    global _matched_radar_detections
    
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = ('', RECEIVE_ALARM_DATA_PORT)
        server_socket.bind(server_address)
        server_socket.listen(99)
        print(f'Listening for camera events on port {RECEIVE_ALARM_DATA_PORT}...')
    except Exception as e:
        print(f"Socket setup error: {e}")
        raise SystemExit(1)
    
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            data = b''
            while True:
                tmp = client_socket.recv(1024)
                if not tmp:
                    break
                data += tmp
            
            if not data:
                client_socket.close()
                continue
            
            # Debug: Show that camera event was received
            print(f"📷 Camera event received from {client_address[0]}")
            
            try:
                raw_data_str = data.decode('utf-8', errors='ignore')
                body = raw_data_str.split('\r\n\r\n', 1)[1] if '\r\n\r\n' in raw_data_str else raw_data_str
                body = re.sub(r'[\x00-\x1F\x7F]', '', body)
                data_json = json.loads(body)
                
                # Extract plate number
                plate_no = extract_plate_number(data_json)
                if plate_no:
                    # Get latest completed radar detection (with peak speed)
                    radar_detection = get_latest_completed_detection()
                    
                    # Debug: Check if radar is working
                    if not radar_detection:
                        with _radar_lock:
                            has_completed = len(_completed_detections) > 0
                            has_in_progress = len(_current_detection) > 0
                            if has_completed:
                                latest = _completed_detections[-1]
                                try:
                                    end_time = datetime.fromisoformat(latest['end_time'])
                                    age = (datetime.now() - end_time).total_seconds()
                                    print(f"  ⚠️  No matching radar detection (latest completed: {age:.1f}s ago, peak: {latest.get('peak_speed', 0)}km/h)")
                                except:
                                    print(f"  ⚠️  No matching radar detection (completed: {has_completed}, in_progress: {has_in_progress})")
                            else:
                                print(f"  ⚠️  No radar detections available (in_progress: {has_in_progress})")
                    
                    # Prepare detection data
                    if radar_detection:
                        # Mark this radar detection as matched with a plate
                        with _matched_detections_lock:
                            _matched_radar_detections.add(radar_detection['end_time'])
                            # Keep only recent matches (last 100)
                            if len(_matched_radar_detections) > 100:
                                # Remove oldest entries (simple cleanup)
                                _matched_radar_detections = set(list(_matched_radar_detections)[-50:])
                        
                        speed = radar_detection['peak_speed']
                        detection_data = {
                            'timestamp': datetime.now().isoformat(),
                            'plate_number': plate_no,
                            'speed': speed,  # Use peak speed from complete detection
                            'direction': radar_detection['direction_name'],  # Use proper direction name
                            'radar_direction_sign': radar_detection['direction_sign'],
                            'vms_displayed': 'yes' if speed > MIN_SPEED_FOR_DISPLAY else 'no',
                            'radar_readings_count': radar_detection['readings_count'],
                            'radar_detection_start': radar_detection['start_time'],
                            'radar_detection_end': radar_detection['end_time']
                        }
                    else:
                        # No radar detection available - speed is 0, so don't display
                        speed = 0
                        detection_data = {
                            'timestamp': datetime.now().isoformat(),
                            'plate_number': plate_no,
                            'speed': speed,
                            'direction': 'Unknown',
                            'radar_direction_sign': None,
                            'vms_displayed': 'no',
                            'radar_readings_count': 0,
                            'radar_detection_start': None,
                            'radar_detection_end': None
                        }
                    
                    # Save detection immediately (before displaying)
                    save_detection(detection_data)
                    
                    # Show plate detection
                    print(f"\n🚗 PLATE: {plate_no} | {detection_data['speed']}km/h | {detection_data['direction']} | VMS: {detection_data['vms_displayed'].upper()}\n")
                    
                    # Display on VMS only if speed is above threshold
                    if speed > MIN_SPEED_FOR_DISPLAY:
                        send_plate_to_vms(plate_no)
                    else:
                        send_plate_to_vms("")  # Clear display
                else:
                    # Camera event received but no plate detected - clear display
                    send_plate_to_vms("")
            
            except json.JSONDecodeError as e:
                print(f"⚠️ Camera JSON decode error: {str(e)[:100]}")
            except Exception as e:
                print(f"⚠️ Error processing camera data: {e}")
            
            client_socket.close()
        
        except Exception as e:
            print(f"Socket accept error: {e}")
            continue

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    print("=" * 60)
    print("Radar-ANPR-VMS Integration System")
    print("=" * 60)
    print(f"Configuration:")
    print(f"  Camera: {CAMERA_IP}:{CAMERA_PORT}")
    print(f"  Radar: {RADAR_PORT} @ {RADAR_BAUDRATE} baud")
    print(f"  VMS: {VMS_IP}:{VMS_PORT}")
    print(f"  Only Positive Direction (A+): {ONLY_POSITIVE_DIRECTION}")
    print(f"  Detections Folder: {DETECTIONS_FOLDER}")
    print("=" * 60)
    
    # Ensure detections folder exists
    ensure_detections_folder()
    print(f"✓ Detections will be saved to: {get_daily_json_path()}")
    
    # Step 1: Start radar reader thread
    print("\nStarting radar reader...")
    radar_thread = Thread(target=read_radar_data, daemon=True)
    radar_thread.start()
    time.sleep(1)  # Give radar thread time to initialize
    
    # Step 2: Subscribe to camera events
    print("\nSubscribing to camera events...")
    data = {
        "AddressType": 0,
        "IPAddress": RECEIVE_ALARM_DATA_IP,
        "Port": RECEIVE_ALARM_DATA_PORT,
        "Duration": DURATION
    }
    json_str = json.dumps(data)
    
    try:
        response = requests.post(url=CAMERA_URL, headers=headers, data=json_str, 
                               auth=HTTPDigestAuth(CAMERA_USERNAME, CAMERA_PASSWORD), timeout=5)
        if response.status_code == 200:
            subscribe_res_json = json.loads(response.text)
            global SUBSCRIPTION_ID
            SUBSCRIPTION_ID = subscribe_res_json['Response']['Data']['ID']
            print(f'✓ Subscribed successfully (ID: {SUBSCRIPTION_ID})')
            
            # Step 3: Start keepalive thread
            keepalive_thread = Thread(target=keepalive, daemon=True)
            keepalive_thread.start()
            
            # Step 4: Start camera listener thread
            camera_thread = Thread(target=listen_camera_events, daemon=True)
            camera_thread.start()
            
            print("\n" + "=" * 60)
            print("System running. Waiting for detections...")
            print("Press Ctrl+C to stop")
            print("=" * 60 + "\n")
            
            # Keep main thread alive
            while True:
                time.sleep(1)
        else:
            print(f'Subscription Failure: {response.status_code} {response.text}')
            raise SystemExit(1)
    except Exception as e:
        print(f'Subscription error: {e}')
        raise SystemExit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nScript terminated by user")
        print(f"Today's detections saved to: {get_daily_json_path()}")
        raise SystemExit(0)
    except Exception as e:
        print(f"Error: {e}")
        raise SystemExit(1)
