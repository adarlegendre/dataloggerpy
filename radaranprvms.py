#!/usr/bin/env python3
"""
Radar-ANPR-VMS Integration System
Combines radar detection, ANPR (camera plate recognition), and VMS display.
Displays all detected license plates on VMS display.
Stores all detections in daily JSON files.
"""

from requests.auth import HTTPDigestAuth
from threading import Thread, Lock
from queue import Queue, Empty
import requests
import json
import time
import socket
import re
import subprocess
import os
import serial
import sys
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
RADAR_TIMEOUT = 0.1  # Increased timeout to prevent blocking
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

# Detection storage - Queue-based file writer
_detections_queue = Queue()
_detections_lock = Lock()
_current_date = None
_detections_file = None
_file_writer_running = False

# VMS display state
_vms_clear_thread = None
_vms_lock = Lock()
_speed_violation_active = False  # Track if speed violation is currently displayed
_speed_violation_lock = Lock()
_matched_radar_detections = set()  # Track radar detection end_times that have been matched with plates
_matched_detections_lock = Lock()
_max_matched_detections = 100  # Maximum number of matched detections to keep

# VMS command cache
_VMS_BASE_CMD = [
    SENDCP5200_PATH,
    "0", VMS_IP, str(VMS_PORT),
    "2", "0", "",  # Text will be inserted here
    "-1", "22", "0", "0", "10", "1"
]

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

def _file_writer_worker():
    """Background worker thread that efficiently writes detections to file"""
    global _current_date, _detections_file, _file_writer_running
    
    _file_writer_running = True
    ensure_detections_folder()
    
    # Cache for batch writing
    pending_detections = []
    last_write_time = time.time()
    batch_timeout = 0.5  # Write batch every 0.5 seconds or when queue is empty
    
    while _file_writer_running:
        try:
            # Get detection from queue with timeout
            try:
                detection_data = _detections_queue.get(timeout=batch_timeout)
                pending_detections.append(detection_data)
            except Empty:
                pass  # Timeout - check if we should flush pending
            
            # Check if we should write (timeout or enough items)
            should_write = (
                pending_detections and 
                (time.time() - last_write_time >= batch_timeout or len(pending_detections) >= 10)
            )
            
            if should_write:
                # Update file path if date changed
                today = datetime.now().date()
                if _current_date != today or _detections_file is None:
                    with _detections_lock:
                        _current_date = today
                        _detections_file = get_daily_json_path()
                
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
                    
                    # Add all pending detections
                    detections.extend(pending_detections)
                    
                    # Write to file
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(detections, f, indent=2, ensure_ascii=False)
                        f.flush()
                        os.fsync(f.fileno())
                    
                    # Log saved detections
                    for detection in pending_detections:
                        plate = detection.get('plate_number')
                        speed = detection.get('speed', 0)
                        direction = detection.get('direction', 'Unknown')
                        if plate:
                            sys.stdout.write(f"💾 Saved: {plate} | {speed}km/h | {direction} → {os.path.basename(filepath)}\n")
                        else:
                            sys.stdout.write(f"💾 Saved: Radar-only | {speed}km/h | {direction} → {os.path.basename(filepath)}\n")
                        sys.stdout.flush()
                    
                    pending_detections.clear()
                    last_write_time = time.time()
                    
                except Exception as e:
                    print(f"Error saving detections: {e}")
                    # Keep pending detections for retry
                    
        except Exception as e:
            print(f"File writer error: {e}")
            time.sleep(0.1)

def save_detection(detection_data: Dict[str, Any]):
    """Save a detection to today's JSON file via queue (non-blocking)"""
    _detections_queue.put(detection_data)

def _start_file_writer():
    """Start the file writer thread"""
    global _file_writer_running
    if not _file_writer_running:
        writer_thread = Thread(target=_file_writer_worker, daemon=True)
        writer_thread.start()
        time.sleep(0.1)  # Give thread time to start

# ============================================================================
# RADAR FUNCTIONS - Vehicle Detection Tracking
# ============================================================================

def _complete_detection(direction_sign: str, direction_name: str, peak_speed: int, 
                        detection_readings: list, start_time: str) -> Dict[str, Any]:
    """Helper to complete a detection and add to queue - thread-safe"""
    global _completed_detections
    
    completed = {
        'direction_sign': direction_sign,
        'direction_name': direction_name,
        'peak_speed': peak_speed,
        'readings_count': len(detection_readings),
        'start_time': start_time,
        'end_time': datetime.now().isoformat(),
        'timestamp': datetime.now().isoformat()
    }
    
    # Thread-safe append to completed detections
    with _radar_lock:
        _completed_detections.append(completed)
        if len(_completed_detections) > _max_completed_detections:
            _completed_detections.pop(0)
    
    # Save radar detection even without plate (for vehicles 8km/h and above)
    if peak_speed >= 8:  # Save all vehicle detections 8km/h and above
        radar_only_data = {
            'timestamp': datetime.now().isoformat(),
            'plate_number': None,
            'speed': peak_speed,
            'direction': direction_name,
            'radar_direction_sign': direction_sign,
            'vms_displayed': 'no',
            'radar_readings_count': len(detection_readings),
            'radar_detection_start': start_time,
            'radar_detection_end': completed['end_time']
        }
        save_detection(radar_only_data)
        sys.stdout.write(f"\n📡 Radar Detection: {direction_name} {peak_speed}km/h | 💾 Saving...\n")
        sys.stdout.flush()
    else:
        print(f"\n📡 Radar Detection: {direction_name} {peak_speed}km/h | ⏭️  Not saved (<8km/h)")
    
    # Check for speed violation (no plate detected, speed > limit) - non-blocking
    if peak_speed > SPEED_LIMIT:
        sys.stdout.write(f"  ⚠️  Speed violation detected: {peak_speed}km/h > {SPEED_LIMIT}km/h - Checking for plate...\n")
        sys.stdout.flush()
        Thread(target=_check_and_display_speed_violation, args=(completed,), daemon=True).start()
    
    return completed

def process_radar_reading(direction_sign: str, speed: int):
    """
    Process radar reading and track complete vehicle detections (0 -> peak -> 0)
    Detects when a vehicle passes: 0 -> rising -> peak -> falling -> 0
    Tracks Gaussian-like pattern and extracts peak speed
    Optimized for minimal lock time to ensure real-time streaming
    """
    global _current_detection, _current_direction
    
    # Create timestamp once outside lock
    timestamp = datetime.now().isoformat()
    
    with _radar_lock:
        reading = {
            'speed': speed,
            'direction_sign': direction_sign,
            'timestamp': timestamp
        }
        
        # Handle zero speed (end of detection)
        if speed == 0:
            if not _current_detection:
                return  # No active detection, ignore zeros
            
            _current_detection.append(reading)
            
            # Check for consecutive zeros to complete detection
            if len(_current_detection) >= CONSECUTIVE_ZEROS_THRESHOLD:
                recent_readings = _current_detection[-CONSECUTIVE_ZEROS_THRESHOLD:]
                if all(r['speed'] == 0 for r in recent_readings):
                    # Complete the detection
                    vehicle_readings = [r for r in _current_detection if r['speed'] > 0]
                    if vehicle_readings:
                        peak_speed = max(r['speed'] for r in vehicle_readings)
                        direction_name = POSITIVE_DIRECTION_NAME if _current_direction == '+' else NEGATIVE_DIRECTION_NAME
                        detection_copy = _current_detection.copy()
                        direction_copy = _current_direction
                        start_time = _current_detection[0]['timestamp']
                        
                        # Reset before completing (outside lock)
                        _current_detection = []
                        _current_direction = None
                        
                        # Complete detection outside lock to minimize blocking
                        _complete_detection(
                            direction_copy, direction_name, peak_speed,
                            detection_copy, start_time
                        )
                    else:
                        # Reset for next detection
                        _current_detection = []
                        _current_direction = None
            return
        
        # Non-zero speed - vehicle detected
        if not _current_detection:
            # Start new detection
            _current_detection = [reading]
            _current_direction = direction_sign
        elif _current_direction == direction_sign:
            # Same direction - continue detection
            _current_detection.append(reading)
        else:
            # Direction changed - complete old detection and start new
            vehicle_readings = [r for r in _current_detection if r['speed'] > 0]
            if vehicle_readings:
                peak_speed = max(r['speed'] for r in vehicle_readings)
                direction_name = POSITIVE_DIRECTION_NAME if _current_direction == '+' else NEGATIVE_DIRECTION_NAME
                detection_copy = _current_detection.copy()
                direction_copy = _current_direction
                start_time = _current_detection[0]['timestamp']
                
                # Start new detection with new direction
                _current_detection = [reading]
                _current_direction = direction_sign
                
                # Complete old detection outside lock
                _complete_detection(
                    direction_copy, direction_name, peak_speed,
                    detection_copy, start_time
                )
            else:
                # Start new detection with new direction
                _current_detection = [reading]
                _current_direction = direction_sign

def _check_and_display_speed_violation(radar_detection: Dict[str, Any]):
    """
    Check if speed violation should be displayed (no plate detected, speed > limit)
    Runs in background thread for fast response
    """
    global _speed_violation_active
    
    peak_speed = radar_detection['peak_speed']
    direction_name = radar_detection['direction_name']
    detection_id = radar_detection['end_time']
    
    # Wait briefly to see if camera detects a plate (1 second grace period)
    print(f"  ⏳ Waiting 1s to check if plate will be detected...")
    time.sleep(1.0)
    
    # Check if this detection was already matched with a plate
    with _matched_detections_lock:
        if detection_id in _matched_radar_detections:
            sys.stdout.write(f"  ✅ Plate detected - skipping speed violation\n")
            sys.stdout.flush()
            return  # Plate detected, skip violation
    
    # Check if detection is still recent
    try:
        detection_end_time = datetime.fromisoformat(radar_detection['end_time'])
        time_since_detection = (datetime.now() - detection_end_time).total_seconds()
    except Exception:
        return
    
    # Display violation if still within reasonable time window
    if time_since_detection <= 5:
        with _speed_violation_lock:
            if not _speed_violation_active:
                _speed_violation_active = True
                
                print(f"  🚨 No plate detected - Displaying speed violation")
                send_plate_to_vms("ZPOMAL!")
                print(f"⚠️  SPEED VIOLATION: {peak_speed}km/h > {SPEED_LIMIT}km/h ({direction_name}) | 📺 VMS: ZPOMAL! | ⏱️  Displaying for {VMS_DISPLAY_TIME}s")
                
                time.sleep(VMS_DISPLAY_TIME)
                print(f"  ✅ Speed violation display completed")
                with _speed_violation_lock:
                    _speed_violation_active = False
            else:
                sys.stdout.write(f"  ⏭️  Speed violation already active, skipping\n")
                sys.stdout.flush()
    else:
        sys.stdout.write(f"  ⏭️  Detection too old ({time_since_detection:.1f}s), skipping violation\n")
        sys.stdout.flush()

def get_latest_completed_detection(max_age_seconds: float = RADAR_CAMERA_TIME_WINDOW) -> Optional[Dict[str, Any]]:
    """
    Get the most recent completed vehicle detection (thread-safe, optimized for speed)
    Only returns detections that are within max_age_seconds of current time
    """
    global _completed_detections, _current_detection, _current_direction
    
    now = datetime.now()
    
    with _radar_lock:
        # Check in-progress detection first (most likely to match)
        if _current_detection and _current_direction:
            vehicle_readings = [r for r in _current_detection if r['speed'] > 0]
            if vehicle_readings:
                try:
                    latest_reading_time = datetime.fromisoformat(_current_detection[-1]['timestamp'])
                    time_diff = (now - latest_reading_time).total_seconds()
                    
                    if time_diff <= 5:
                        peak_speed = max(r['speed'] for r in vehicle_readings)
                        direction_name = POSITIVE_DIRECTION_NAME if _current_direction == '+' else NEGATIVE_DIRECTION_NAME
                        # Return immediately without copy for speed
                        return {
                            'direction_sign': _current_direction,
                            'direction_name': direction_name,
                            'peak_speed': peak_speed,
                            'readings_count': len(_current_detection),
                            'start_time': _current_detection[0]['timestamp'],
                            'end_time': _current_detection[-1]['timestamp'],
                            'timestamp': now.isoformat(),
                            'in_progress': True
                        }
                except (ValueError, KeyError):
                    pass
        
        # Check completed detections (most recent first) - fast path
        if not _completed_detections:
            return None
        
        # Check from most recent (reverse iteration is fast for small lists)
        for detection in reversed(_completed_detections):
            try:
                detection_end = datetime.fromisoformat(detection['end_time'])
                time_since_end = (now - detection_end).total_seconds()
                
                # Fast path: check end time first (most common case)
                if time_since_end <= max_age_seconds:
                    return detection.copy()
                elif time_since_end > max_age_seconds * 2:
                    # If too old, skip checking start time
                    continue
                
                # Only check start time if end time is borderline
                detection_start = datetime.fromisoformat(detection['start_time'])
                time_since_start = (now - detection_start).total_seconds()
                
                if time_since_start <= max_age_seconds:
                    return detection.copy()
            except (ValueError, KeyError):
                continue
        
        return None

def read_radar_data():
    """Read radar data from serial port - simplified for continuous reliable streaming"""
    print(f"Starting radar reader on {RADAR_PORT}...")
    
    ser = None
    retry_count = 0
    max_retries = 5
    buffer = b''
    last_data_time = time.time()
    last_watchdog_time = time.time()
    watchdog_interval = 3.0
    max_buffer_size = 1000  # Maximum buffer size to prevent memory issues
    processed_count = 0
    
    while True:
        try:
            if ser is None or not ser.is_open:
                print(f"Connecting to radar on {RADAR_PORT}...")
                ser = serial.Serial(
                    port=RADAR_PORT,
                    baudrate=RADAR_BAUDRATE,
                    timeout=RADAR_TIMEOUT
                )
                print(f"✓ Connected to radar on {RADAR_PORT}")
                retry_count = 0
                buffer = b''
                processed_count = 0
                last_watchdog_time = time.time()
            
            current_time = time.time()
            
            # Watchdog check - runs independently every 3 seconds regardless of data
            if current_time - last_watchdog_time >= watchdog_interval:
                sys.stdout.write(f"📡 [Watchdog] Thread alive | Buffer: {len(buffer)} bytes | Processed: {processed_count} | Last data: {current_time - last_data_time:.1f}s ago\n")
                sys.stdout.flush()
                last_watchdog_time = current_time
            
            # Simple read with timeout
            data = ser.read(32)
            
            if data:
                last_data_time = current_time
                buffer += data
                
                # Prevent buffer from growing too large
                if len(buffer) > max_buffer_size:
                    # Try to find last 'A' to keep valid data
                    last_a = buffer.rfind(b'A')
                    if last_a > 0 and last_a < len(buffer) - 4:
                        buffer = buffer[last_a:]
                        sys.stdout.write(f"📡 [Buffer cleared] Size exceeded, kept last {len(buffer)} bytes\n")
                        sys.stdout.flush()
                    else:
                        # No valid start found, clear buffer
                        buffer = b''
                        sys.stdout.write(f"📡 [Buffer cleared] No valid data found\n")
                        sys.stdout.flush()
                
                # Process messages - limit iterations to prevent getting stuck
                max_iterations = 50
                iteration = 0
                while len(buffer) >= 5 and iteration < max_iterations:
                    iteration += 1
                    chunk = buffer[:5]
                    buffer = buffer[5:]
                    
                    # Check if valid: A+XXX or A-XXX
                    if chunk[0] == ord('A') and len(chunk) == 5:
                        if chunk[1] == ord('+') or chunk[1] == ord('-'):
                            try:
                                direction_sign = '+' if chunk[1] == ord('+') else '-'
                                speed = int(chunk[2:].decode('utf-8'))
                                direction_name = POSITIVE_DIRECTION_NAME if direction_sign == '+' else NEGATIVE_DIRECTION_NAME
                                
                                # Display immediately - simple format (ALWAYS FIRST)
                                sys.stdout.write(f"📡 {direction_name} {speed:3d}km/h\n")
                                sys.stdout.flush()
                                processed_count += 1
                                
                                # Process in background thread to never block display
                                # This ensures radar display continues even if processing is slow
                                def process_async(direction, spd):
                                    try:
                                        process_radar_reading(direction, spd)
                                    except:
                                        pass
                                
                                Thread(target=process_async, args=(direction_sign, speed), daemon=True).start()
                            except:
                                pass
                        else:
                            # Invalid direction, look for next 'A'
                            if b'A' in chunk[1:]:
                                idx = chunk[1:].index(b'A') + 1
                                buffer = chunk[idx:] + buffer
                            break
                    else:
                        # Look for 'A' to realign
                        if b'A' in chunk:
                            idx = chunk.index(b'A')
                            buffer = chunk[idx:] + buffer
                        break
                
                # If we hit max iterations, clear buffer to prevent getting stuck
                if iteration >= max_iterations:
                    sys.stdout.write(f"📡 [Buffer cleared] Max iterations reached\n")
                    sys.stdout.flush()
                    buffer = b''
            
            # Small delay - but ensure watchdog can still run
            time.sleep(0.01)
            
            # Force watchdog check even during active reading
            current_check = time.time()
            if current_check - last_watchdog_time >= watchdog_interval:
                sys.stdout.write(f"📡 [Watchdog] Active | Buffer: {len(buffer)} bytes | Processed: {processed_count}\n")
                sys.stdout.flush()
                last_watchdog_time = current_check
                
        except serial.SerialException as e:
            if ser and ser.is_open:
                try:
                    ser.close()
                except:
                    pass
            ser = None
            retry_count += 1
            if retry_count <= max_retries:
                print(f"\n⚠️ Radar connection error (attempt {retry_count}/{max_retries}): {e}")
                print(f"   Retrying in 2 seconds...")
                time.sleep(2)
            else:
                print(f"\n✗ Radar connection failed after {max_retries} attempts")
                print(f"   Error: {e}")
                print("   Radar reading disabled. Continuing without radar data...")
                while True:
                    time.sleep(60)
                    retry_count = 0
        except Exception as e:
            print(f"\n⚠️ Radar read error: {e}")
            import traceback
            print(f"   Traceback: {traceback.format_exc()}")
            time.sleep(1)
            # Reset buffer on error to prevent getting stuck
            buffer = b''

# ============================================================================
# VMS FUNCTIONS
# ============================================================================

def _send_vms_command(display_text: str) -> bool:
    """Send command to VMS display (internal helper) - non-blocking"""
    cmd = _VMS_BASE_CMD.copy()
    cmd[6] = display_text  # Insert text at position 6
    
    # Show the exact command being sent
    cmd_str = ' '.join(f'"{arg}"' if ' ' in str(arg) else str(arg) for arg in cmd)
    sys.stdout.write(f"  📤 VMS Command: {cmd_str}\n")
    sys.stdout.flush()
    
    try:
        # Use Popen for truly non-blocking execution
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except Exception as e:
        sys.stdout.write(f"  ❌ VMS Command failed: {e}\n")
        sys.stdout.flush()
        return False

def send_plate_to_vms(plate_number: str):
    """Send plate number to VMS display - fully non-blocking and efficient"""
    global _vms_clear_thread
    
    display_text = plate_number if plate_number and plate_number.strip() else ""
    
    # Cancel any pending clear thread if new plate is being displayed
    with _vms_lock:
        if _vms_clear_thread is not None and display_text:
            _vms_clear_thread = None
    
    # Cancel speed violation if displaying a plate
    if display_text and display_text != "ZPOMAL!":
        with _speed_violation_lock:
            _speed_violation_active = False
    
    # Send command immediately (non-blocking)
    if display_text:
        sys.stdout.write(f"  📺 VMS: Sending '{display_text}' → Display for {VMS_DISPLAY_TIME}s\n")
    else:
        sys.stdout.write(f"  📺 VMS: Clearing display\n")
    sys.stdout.flush()
    
    success = _send_vms_command(display_text)
    
    if display_text:
        if success:
            sys.stdout.write(f"  ✅ VMS: Command sent successfully\n")
        else:
            sys.stdout.write(f"  ❌ VMS: Command failed\n")
        sys.stdout.flush()
        
        # Schedule auto-clear after display time
        def clear_after_delay():
            global _vms_clear_thread
            time.sleep(VMS_DISPLAY_TIME)
            
            with _vms_lock:
                if _vms_clear_thread is not None:
                    sys.stdout.write(f"  📺 VMS: Auto-clearing after {VMS_DISPLAY_TIME}s\n")
                    sys.stdout.flush()
                    _send_vms_command("")  # Clear display
                    _vms_clear_thread = None
    
    if display_text:
        with _vms_lock:
            _vms_clear_thread = Thread(target=clear_after_delay, daemon=True)
            _vms_clear_thread.start()
    
    return success

# ============================================================================
# CAMERA/ANPR FUNCTIONS
# ============================================================================

def extract_plate_number(data_json):
    """Extract plate number from camera event data"""
    try:
        structure_info = data_json.get("StructureInfo", {})
        if not structure_info:
            return None
            
        obj_info = structure_info.get("ObjInfo", {})
        if not obj_info:
            return None
            
        vehicle_info_list = obj_info.get("VehicleInfoList", [])
        if not isinstance(vehicle_info_list, list) or not vehicle_info_list:
            return None
        
        vehicle_info = vehicle_info_list[0]
        plate_attr = vehicle_info.get("PlateAttributeInfo", {})
        plate_no = plate_attr.get("PlateNo", None)
        
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
        
        try:
            response = requests.put(
                url=keepalive_url, 
                headers=headers, 
                data=json.dumps(data), 
                auth=HTTPDigestAuth(CAMERA_USERNAME, CAMERA_PASSWORD), 
                timeout=5
            )
            if response.status_code != 200:
                print(f'Keepalive failure: {response.status_code}')
                raise SystemExit(0)
        except Exception as e:
            print(f'Keepalive error: {e}')
            raise SystemExit(0)
        
        time.sleep(DURATION / 2)

def _handle_camera_client(client_socket, client_address):
    """Handle individual camera client connection - optimized for fast real-time processing"""
    global _matched_radar_detections
    
    try:
        data = b''
        client_socket.settimeout(10.0)  # Longer timeout to ensure all data arrives
        
        # Read all data - camera sends HTTP POST with JSON body
        # Strategy: Read until connection closes (recv returns empty) or we detect complete message
        max_reads = 100  # Safety limit to prevent infinite loop
        read_count = 0
        
        while read_count < max_reads:
            try:
                tmp = client_socket.recv(16384)  # Large buffer (16KB) for faster read
                if not tmp:
                    # Connection closed by camera - all data received
                    break
                data += tmp
                read_count += 1
                
                # Try to detect if we have complete HTTP message using Content-Length
                if b'\r\n\r\n' in data and len(data) > 100:
                    try:
                        raw_str = data.decode('utf-8', errors='ignore')
                        headers_end = raw_str.find('\r\n\r\n')
                        if headers_end > 0:
                            headers = raw_str[:headers_end]
                            # Look for Content-Length header
                            import re as re_module
                            content_length_match = re_module.search(r'Content-Length:\s*(\d+)', headers, re_module.IGNORECASE)
                            if content_length_match:
                                content_length = int(content_length_match.group(1))
                                body_start = headers_end + 4
                                body_received = len(data) - body_start
                                if body_received >= content_length:
                                    # We have all the data according to Content-Length
                                    break
                    except Exception:
                        pass
                        
            except socket.timeout:
                # Timeout - if we have data, assume it's complete (camera might have sent everything)
                if len(data) > 100:
                    break
                else:
                    print(f"⚠️ Camera timeout with insufficient data ({len(data)} bytes)")
                    break
            except Exception as e:
                print(f"⚠️ Camera recv error: {e}")
                break
        
        if read_count >= max_reads:
            print(f"⚠️ Reached max read limit ({max_reads}), may have incomplete data")
        
        if not data:
            client_socket.close()
            return
        
        # Show camera event received
        sys.stdout.write(f"📷 Camera event received ({len(data)} bytes)\n")
        sys.stdout.flush()
        
        try:
            # Parse HTTP message
            raw_data_str = data.decode('utf-8', errors='ignore')
            
            # Extract body from HTTP POST
            if '\r\n\r\n' in raw_data_str:
                body = raw_data_str.split('\r\n\r\n', 1)[1]
            else:
                body = raw_data_str
            
            # Clean control characters but preserve JSON structure
            body = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', body)
            
            # Try to parse JSON
            try:
                data_json = json.loads(body)
            except json.JSONDecodeError as json_err:
                # If JSON decode fails, try to find and extract just the JSON part
                json_start = body.find('{')
                json_end = body.rfind('}')
                if json_start >= 0 and json_end > json_start:
                    json_str = body[json_start:json_end+1]
                    data_json = json.loads(json_str)
                else:
                    sys.stdout.write(f"  ❌ JSON parse failed: {json_err}\n")
                    sys.stdout.flush()
                    raise  # Re-raise original error
            
            # Extract plate number
            plate_no = extract_plate_number(data_json)
            if plate_no:
                # Get latest completed radar detection (fast lookup)
                radar_detection = get_latest_completed_detection()
                
                # Create timestamp once
                timestamp = datetime.now().isoformat()
                
                # Prepare detection data efficiently
                if radar_detection:
                    # Mark this radar detection as matched (fast operation)
                    detection_id = radar_detection['end_time']
                    with _matched_detections_lock:
                        _matched_radar_detections.add(detection_id)
                        # Efficient cleanup - only when needed
                        if len(_matched_radar_detections) > _max_matched_detections:
                            sorted_items = sorted(_matched_radar_detections)
                            _matched_radar_detections = set(sorted_items[-_max_matched_detections // 2:])
                    
                    speed = radar_detection['peak_speed']
                    direction = radar_detection['direction_name']
                    vms_displayed = 'yes' if speed > MIN_SPEED_FOR_DISPLAY else 'no'
                    
                    detection_data = {
                        'timestamp': timestamp,
                        'plate_number': plate_no,
                        'speed': speed,
                        'direction': direction,
                        'radar_direction_sign': radar_detection['direction_sign'],
                        'vms_displayed': vms_displayed,
                        'radar_readings_count': radar_detection['readings_count'],
                        'radar_detection_start': radar_detection['start_time'],
                        'radar_detection_end': radar_detection['end_time']
                    }
                    
                    # Save detection (non-blocking via queue)
                    sys.stdout.write(f"🚗 Plate: {plate_no} | {speed}km/h | {direction} | 💾 Saving...\n")
                    sys.stdout.flush()
                    save_detection(detection_data)
                    
                    # Display on VMS immediately (non-blocking)
                    if speed > MIN_SPEED_FOR_DISPLAY:
                        send_plate_to_vms(plate_no)
                    else:
                        send_plate_to_vms("")
                        sys.stdout.write(f"  ⏭️  VMS: Not displaying (speed {speed}km/h <= {MIN_SPEED_FOR_DISPLAY}km/h)\n")
                        sys.stdout.flush()
                else:
                    speed = 0
                    detection_data = {
                        'timestamp': timestamp,
                        'plate_number': plate_no,
                        'speed': speed,
                        'direction': 'Unknown',
                        'radar_direction_sign': None,
                        'vms_displayed': 'no',
                        'radar_readings_count': 0,
                        'radar_detection_start': None,
                        'radar_detection_end': None
                    }
                    sys.stdout.write(f"🚗 Plate: {plate_no} | No radar match (outside {RADAR_CAMERA_TIME_WINDOW}s) | 💾 Saving...\n")
                    sys.stdout.flush()
                    save_detection(detection_data)
                    send_plate_to_vms("")
                    sys.stdout.write(f"  ⏭️  VMS: Not displaying (no speed data)\n")
                    sys.stdout.flush()
            else:
                # Camera event received but no plate detected
                sys.stdout.write(f"📷 Camera event: No plate detected\n")
                sys.stdout.flush()
                send_plate_to_vms("")
        
        except json.JSONDecodeError:
            pass  # Silently skip invalid JSON
        except Exception:
            pass  # Silently skip processing errors
    
    finally:
        try:
            client_socket.close()
        except:
            pass

def listen_camera_events():
    """Listen for camera ANPR events (non-blocking - each client handled in separate thread)"""
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.settimeout(1.0)
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
            client_thread = Thread(target=_handle_camera_client, args=(client_socket, client_address), daemon=True)
            client_thread.start()
        except socket.timeout:
            continue
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
    
    # Start file writer thread
    _start_file_writer()
    
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
    
    try:
        response = requests.post(
            url=CAMERA_URL, 
            headers=headers, 
            data=json.dumps(data), 
            auth=HTTPDigestAuth(CAMERA_USERNAME, CAMERA_PASSWORD), 
            timeout=5
        )
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
            
            # Keep main thread alive - show periodic status
            last_status_time = time.time()
            status_interval = 30  # Show status every 30 seconds
            
            while True:
                time.sleep(1)
                # Show periodic status to indicate system is alive
                current_time = time.time()
                if current_time - last_status_time >= status_interval:
                    print(f"\n[System active - {datetime.now().strftime('%H:%M:%S')}]")
                    last_status_time = current_time
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
