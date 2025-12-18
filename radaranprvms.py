#!/usr/bin/env python3
"""
Radar-ANPR-VMS Integration System
Combines radar detection, ANPR (camera plate recognition), and VMS display.
Only displays plates when radar detects vehicles moving in positive direction (A+).
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
import sys
import serial
from datetime import datetime
from queue import Queue
from typing import Optional, Dict, Any
from test_vms import send_text_to_vms

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

# VMS Configuration (CP5200 Display) - matching test_vms.py
VMS_IP = "192.168.1.222"
VMS_PORT = 5200
VMS_WINDOW = 0
VMS_COLOR = 3  # Color value (matching test_vms.py)
VMS_FONT_SIZE = 18
VMS_SPEED = 5  # Animation speed (matching test_vms.py)
VMS_EFFECT = 1  # Animation effect (matching test_vms.py)
VMS_STAY_TIME = 5  # Display for 5 seconds, then clear
VMS_ALIGNMENT = 1

# Data storage
DETECTIONS_FOLDER = "detections"

# Match the search order used in test_vms.py
SENDCP5200_PATHS = [
    "./sendcp5200/dist/Debug/GNU-Linux/sendcp5200",
    "./sendcp5200/dist/Release/GNU-Linux/sendcp5200",
    "/etc/1prog/sendcp5200k",
    "sendcp5200",  # In PATH
    "/usr/local/bin/sendcp5200",
    "/usr/bin/sendcp5200",
]

# ============================================================================
# GLOBAL STATE
# ============================================================================

# HTTP request header
headers = {
    'Content-Type': 'application/json',
    'Host': f'{CAMERA_IP}:{CAMERA_PORT}',
    'Connection': 'Close',
}

# VMS Display Queue Management
_vms_lock = Lock()
_pending_clear_thread = None
_current_display_plate = None
_display_start_time = None

# Radar state - Vehicle detection tracking
_radar_lock = Lock()
_current_detection = []  # List of readings for current vehicle (0 -> peak -> 0)
_current_direction = None  # '+' or '-' for current detection
_last_speed = 0  # Last speed reading
_completed_detections = []  # Queue of completed detections with peak speed
_max_completed_detections = 10  # Keep last 10 completed detections

# Detection storage
_detections_lock = Lock()
_current_date = None
_detections_file = None

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

def load_daily_detections():
    """Load today's detections from JSON file"""
    filepath = get_daily_json_path()
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

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

def find_sendcp5200_executable():
    """Find the sendcp5200 executable - matching test_vms.py"""
    for path in SENDCP5200_PATHS:
        if os.path.exists(path) and os.access(path, os.X_OK):
            return path
    
    # Try which/where command - matching test_vms.py
    try:
        if sys.platform == "win32":
            result = subprocess.run(['where', 'sendcp5200'], capture_output=True, text=True, timeout=2)
        else:
            result = subprocess.run(['which', 'sendcp5200'], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            found_path = result.stdout.strip().split('\n')[0]
            if found_path:
                return found_path
    except:
        pass
    
    return None

# ============================================================================
# RADAR FUNCTIONS - Vehicle Detection Tracking
# ============================================================================

def process_radar_reading(direction_sign: str, speed: int):
    """
    Process radar reading and track complete vehicle detections (0 -> peak -> 0)
    Detects when a vehicle passes: 0 -> rising -> peak -> falling -> 0
    Tracks Gaussian-like pattern and extracts peak speed
    """
    global _current_detection, _current_direction, _last_speed, _completed_detections
    
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
                _last_speed = 0
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
                        
                        completed = {
                            'direction_sign': _current_direction,
                            'direction_name': POSITIVE_DIRECTION_NAME if _current_direction == '+' else NEGATIVE_DIRECTION_NAME,
                            'peak_speed': peak_speed,
                            'readings_count': len(_current_detection),
                            'start_time': _current_detection[0]['timestamp'],
                            'end_time': datetime.now().isoformat(),
                            'timestamp': datetime.now().isoformat()
                        }
                        
                        _completed_detections.append(completed)
                        if len(_completed_detections) > _max_completed_detections:
                            _completed_detections.pop(0)
                        
                        print(f"✓ Vehicle detection complete: {completed['direction_name']} | Peak Speed: {peak_speed}km/h | Readings: {len(_current_detection)}")
                    
                    # Reset for next detection
                    _current_detection = []
                    _current_direction = None
            
            _last_speed = 0
            return
        
        # Non-zero speed - we have a vehicle
        if not _current_detection:
            # Start new detection (transition from 0 to non-zero)
            _current_detection = [reading]
            _current_direction = direction_sign
            _last_speed = speed
            print(f"→ Vehicle detection started: {POSITIVE_DIRECTION_NAME if direction_sign == '+' else NEGATIVE_DIRECTION_NAME} | Speed: {speed}km/h")
        else:
            # Continue current detection
            if _current_direction == direction_sign:
                # Same direction - add to current detection
                _current_detection.append(reading)
                _last_speed = speed
            else:
                # Direction changed - complete old detection and start new
                vehicle_readings = [r for r in _current_detection if r['speed'] > 0]
                if vehicle_readings:
                    peak_speed = max(r['speed'] for r in vehicle_readings)
                    completed = {
                        'direction_sign': _current_direction,
                        'direction_name': POSITIVE_DIRECTION_NAME if _current_direction == '+' else NEGATIVE_DIRECTION_NAME,
                        'peak_speed': peak_speed,
                        'readings_count': len(_current_detection),
                        'start_time': _current_detection[0]['timestamp'],
                        'end_time': datetime.now().isoformat(),
                        'timestamp': datetime.now().isoformat()
                    }
                    _completed_detections.append(completed)
                    if len(_completed_detections) > _max_completed_detections:
                        _completed_detections.pop(0)
                    print(f"✓ Vehicle detection complete: {completed['direction_name']} | Peak Speed: {peak_speed}km/h")
                
                # Start new detection with new direction
                _current_detection = [reading]
                _current_direction = direction_sign
                _last_speed = speed
                print(f"→ Vehicle detection started: {POSITIVE_DIRECTION_NAME if direction_sign == '+' else NEGATIVE_DIRECTION_NAME} | Speed: {speed}km/h")

def get_latest_completed_detection() -> Optional[Dict[str, Any]]:
    """Get the most recent completed vehicle detection (thread-safe)"""
    global _completed_detections
    
    with _radar_lock:
        if _completed_detections:
            return _completed_detections[-1].copy()
        return None

def is_latest_detection_positive() -> bool:
    """Check if the most recent completed detection was positive direction (A+)"""
    detection = get_latest_completed_detection()
    return detection is not None and detection['direction_sign'] == '+'

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

def clear_vms_display():
    """Clear VMS display by sending empty string"""
    executable = find_sendcp5200_executable()
    if not executable:
        print("ERROR: sendcp5200 executable not found!")
        print("Paths tried:")
        for p in SENDCP5200_PATHS:
            print(f"  - {p}")
        return False
    
    cmd = [
        executable, "0", VMS_IP, str(VMS_PORT), "2",
        str(VMS_WINDOW), "", str(VMS_COLOR), str(VMS_FONT_SIZE),
        str(VMS_SPEED), str(VMS_EFFECT), "10", str(VMS_ALIGNMENT)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        
        if result.returncode == 0:
            if result.stdout:
                print(f"sendcp5200 (clear) output: {result.stdout.strip()}")
            return True
        else:
            if result.stdout:
                print(f"sendcp5200 (clear) output: {result.stdout.strip()}")
            if result.stderr:
                print(f"sendcp5200 (clear) error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"Error clearing VMS: {e}")
        return False

def send_plate_to_vms(plate_number: str):
    """Send plate number to VMS display for 5 seconds, then clear and repeat"""
    global _pending_clear_thread, _current_display_plate, _display_start_time
    
    # Handle empty or None plate number - use "." to switch off
    display_text = plate_number if plate_number and plate_number.strip() else "."
    
    with _vms_lock:
        if _pending_clear_thread is not None:
            _pending_clear_thread = None
            print(f"  → New vehicle detected, canceling pending clear")
        
        if _current_display_plate is not None and _current_display_plate != display_text:
            elapsed = time.time() - _display_start_time if _display_start_time else 0
            print(f"  → Interrupting display of '{_current_display_plate}' (was showing for {elapsed:.1f}s)")
        
        _current_display_plate = display_text
        _display_start_time = time.time()
    
    # Use send_text_to_vms from test_vms.py (no color parameter - uses default from test_vms.py)
    success = send_text_to_vms(display_text, window=VMS_WINDOW, stay_time=VMS_STAY_TIME)
    
    if success:
        print(f"✓ Sent '{display_text}' to VMS at {VMS_IP}:{VMS_PORT} (will clear in {VMS_STAY_TIME}s)")
        
        def clear_after_delay(plate_id):
            global _current_display_plate, _display_start_time, _pending_clear_thread
            
            # Wait 5 seconds before clearing
            time.sleep(VMS_STAY_TIME)
            
            with _vms_lock:
                if _current_display_plate == plate_id and _pending_clear_thread is not None:
                    # Clear by sending empty string
                    if send_text_to_vms("", window=VMS_WINDOW, stay_time=VMS_STAY_TIME):
                        print(f"✓ Cleared VMS display (was showing '{plate_id}')")
                    else:
                        print(f"Warning: Failed to clear VMS display")
                    _current_display_plate = None
                    _display_start_time = None
                    _pending_clear_thread = None
                else:
                    print(f"  → Skipped clear (new vehicle displayed)")
        
        with _vms_lock:
            _pending_clear_thread = Thread(target=clear_after_delay, args=(display_text,))
            _pending_clear_thread.daemon = True
            _pending_clear_thread.start()
        
        return True
    else:
        print(f"✗ Failed to send '{display_text}' to VMS")
        with _vms_lock:
            _current_display_plate = None
            _display_start_time = None
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
    except Exception:
        return None

def keepalive():
    """Keep camera subscription alive"""
    while True:
        keepaliveUrl = f"{CAMERA_URL}/{SUBSCRIPTION_ID}"
        data = {'Duration': DURATION}
        jsonStr = json.dumps(data)
        
        try:
            response = requests.put(url=keepaliveUrl, headers=headers, data=jsonStr, 
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
                    
                    # Display all detected plates (removed positive direction only constraint)
                    should_display = True
                    
                    # Prepare detection data
                    if radar_detection:
                        detection_data = {
                            'timestamp': datetime.now().isoformat(),
                            'plate_number': plate_no,
                            'speed': radar_detection['peak_speed'],  # Use peak speed from complete detection
                            'direction': radar_detection['direction_name'],  # Use proper direction name
                            'radar_direction_sign': radar_detection['direction_sign'],
                            'vms_displayed': 'yes',
                            'radar_readings_count': radar_detection['readings_count'],
                            'radar_detection_start': radar_detection['start_time'],
                            'radar_detection_end': radar_detection['end_time']
                        }
                    else:
                        # No radar detection available
                        detection_data = {
                            'timestamp': datetime.now().isoformat(),
                            'plate_number': plate_no,
                            'speed': 0,
                            'direction': 'Unknown',
                            'radar_direction_sign': None,
                            'vms_displayed': 'yes',
                            'radar_readings_count': 0,
                            'radar_detection_start': None,
                            'radar_detection_end': None
                        }
                    
                    # Save detection immediately (before displaying)
                    save_detection(detection_data)
                    
                    # Show plate detection prominently in console
                    print("\n" + "=" * 60)
                    print(f"🚗 PLATE DETECTED: {plate_no}")
                    print(f"   Speed: {detection_data['speed']}km/h | Direction: {detection_data['direction']}")
                    if radar_detection:
                        print(f"   Radar: {radar_detection['direction_sign']} | Readings: {radar_detection['readings_count']}")
                    print(f"   VMS Display: {detection_data['vms_displayed'].upper()}")
                    print(f"   Saved to: {get_daily_json_path()}")
                    print("=" * 60 + "\n")
                    
                    # Display on VMS - all plates are displayed
                    send_plate_to_vms(plate_no)
                else:
                    # Camera event received but no plate detected - clear display
                    print("\n" + "=" * 60)
                    print("⚠️  CAMERA EVENT: NO PLATE DETECTED")
                    print("=" * 60 + "\n")
                    send_plate_to_vms("")  # Empty string will send "." to clear the display
            
            except json.JSONDecodeError:
                pass
            except Exception as e:
                print(f"Error processing camera data: {e}")
            
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
    
    # Check for sendcp5200 executable
    executable = find_sendcp5200_executable()
    if executable:
        print(f"✓ Found sendcp5200: {executable}")
    else:
        print("⚠ Warning: sendcp5200 executable not found. VMS sending will be disabled.")
    
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
    jsonStr = json.dumps(data)
    
    try:
        response = requests.post(url=CAMERA_URL, headers=headers, data=jsonStr, 
                               auth=HTTPDigestAuth(CAMERA_USERNAME, CAMERA_PASSWORD), timeout=5)
        if response.status_code == 200:
            suscribeResJson = json.loads(response.text)
            global SUBSCRIPTION_ID
            SUBSCRIPTION_ID = suscribeResJson['Response']['Data']['ID']
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
