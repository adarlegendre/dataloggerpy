from requests.auth import HTTPDigestAuth
from threading import Thread, Lock
import requests
import json
import time
import socket
import re
import subprocess
import os

# Camera configuration
username = 'admin'
password = 'kObliha12@'
cameraIP = '192.168.2.13'
cameraPort = 80
receiveAlarmDataIP = "192.168.2.101"
receiveAlarmDataPort = 8090
duration = 300
suscribID = -1
url = f'http://{cameraIP}:{cameraPort}/LAPI/V1.0/System/Event/Subscription'

# HTTP request header
headers = {
    'Content-Type': 'application/json',
    'Host': f'{cameraIP}:{cameraPort}',
    'Connection': 'Close',
}

# VMS Configuration (CP5200 Display)
VMS_IP = "192.168.1.222"
VMS_PORT = 5200
VMS_WINDOW = 0
# Color parameter (1-16): Controls display inversion
# Try: 1 = Normal (ON LEDs show text), 3 = Inverted (OFF LEDs show text)
# If currently inverted, try: 1, 2, 4, 5, 6, 7, 8, or 9-16
VMS_COLOR = 3  # Changed from 3 to 1 for normal (ON LEDs) display
VMS_FONT_SIZE = 18
VMS_SPEED = 5
VMS_EFFECT = 1
VMS_STAY_TIME = 3  # Display for 3 seconds, then clear
VMS_ALIGNMENT = 1

# Possible paths for sendcp5200 executable
SENDCP5200_PATHS = [
    "./sendcp5200/dist/Debug/GNU-Linux/sendcp5200",
    "./sendcp5200/dist/Release/GNU-Linux/sendcp5200",
    "/etc/1prog/sendcp5200k",
    "sendcp5200",
    "/usr/local/bin/sendcp5200",
    "/usr/bin/sendcp5200"
]

# Cache for sendcp5200 executable path
_sendcp5200_executable_cache = None

# VMS Display Queue Management (for handling tailgating/queued vehicles)
_vms_lock = Lock()
_pending_clear_thread = None
_current_display_plate = None
_display_start_time = None

def keepalive():
    while True:
        keepaliveUrl = f"{url}/{suscribID}"
        data = {'Duration': duration}
        jsonStr = json.dumps(data)
        
        try:
            response = requests.put(url=keepaliveUrl, headers=headers, data=jsonStr, 
                                  auth=HTTPDigestAuth(username, password), timeout=5)
            if response.status_code != 200:
                print(f'Keepalive failure: {response.status_code}')
                raise SystemExit(0)
        except Exception as e:
            print(f'Keepalive error: {e}')
            raise SystemExit(0)
        
        time.sleep(duration / 2)

def find_sendcp5200_executable():
    """Find the sendcp5200 executable in common locations (cached)"""
    global _sendcp5200_executable_cache
    
    # Return cached result if available
    if _sendcp5200_executable_cache is not None:
        return _sendcp5200_executable_cache
    
    # First check direct paths
    for path in SENDCP5200_PATHS:
        if os.path.exists(path) and os.access(path, os.X_OK):
            _sendcp5200_executable_cache = path
            return path
    
    # Check if it's in PATH (Unix/Linux)
    try:
        result = subprocess.run(['which', 'sendcp5200'], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            found_path = result.stdout.strip()
            if found_path:
                _sendcp5200_executable_cache = found_path
                return found_path
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    # Check if it's in PATH (Windows)
    try:
        result = subprocess.run(['where', 'sendcp5200'], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            found_path = result.stdout.strip().split('\n')[0]
            if found_path:
                _sendcp5200_executable_cache = found_path
                return found_path
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    # Cache None to avoid repeated searches
    _sendcp5200_executable_cache = None
    return None

def clear_vms_display():
    """Clear VMS display by sending empty string"""
    executable = find_sendcp5200_executable()
    if not executable:
        return False
    
    # Build command to send empty string: sendcp5200 0 [IP] [port] 2 0 "" 1 18 5 1 10 1
    cmd = [
        executable,
        "0",  # debug mode: 0 = no debug + network
        VMS_IP,
        str(VMS_PORT),
        "2",  # function 2 = SendText
        str(VMS_WINDOW),
        "",   # empty string to clear display
        "1",  # color
        str(VMS_FONT_SIZE),
        str(VMS_SPEED),
        str(VMS_EFFECT),
        "10",  # stay time (not critical for clear)
        str(VMS_ALIGNMENT)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        return result.returncode == 0
    except:
        return False

def cancel_pending_clear():
    """Cancel any pending clear operation"""
    global _pending_clear_thread
    with _vms_lock:
        _pending_clear_thread = None

def send_plate_to_vms(plate_number):
    """Send plate number to VMS display using sendcp5200, then clear after 3 seconds.
    Handles tailgating/queued vehicles by canceling pending clears when new plate arrives."""
    global _pending_clear_thread, _current_display_plate, _display_start_time
    
    executable = find_sendcp5200_executable()
    if not executable:
        print(f"Warning: sendcp5200 executable not found. Plate '{plate_number}' not sent to VMS.")
        return False
    
    with _vms_lock:
        # Cancel any pending clear operation (new vehicle detected - don't clear yet)
        if _pending_clear_thread is not None:
            _pending_clear_thread = None
            print(f"  → New vehicle detected, canceling pending clear")
        
        # Check if we're interrupting a current display
        if _current_display_plate is not None and _current_display_plate != plate_number:
            elapsed = time.time() - _display_start_time if _display_start_time else 0
            print(f"  → Interrupting display of '{_current_display_plate}' (was showing for {elapsed:.1f}s)")
        
        # Update current display state
        _current_display_plate = plate_number
        _display_start_time = time.time()
    
    # Build command: sendcp5200 [debug] [IP] [port] [function] [window] [text] [color] [font] [speed] [effect] [stay] [alignment]
    # Function 2 = SendText
    cmd = [
        executable,
        "0",  # debug mode: 0 = no debug + network
        VMS_IP,
        str(VMS_PORT),
        "2",  # function 2 = SendText
        str(VMS_WINDOW),
        plate_number,  # text to display
        str(VMS_COLOR),
        str(VMS_FONT_SIZE),
        str(VMS_SPEED),
        str(VMS_EFFECT),
        str(VMS_STAY_TIME),
        str(VMS_ALIGNMENT)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"✓ Sent '{plate_number}' to VMS at {VMS_IP}:{VMS_PORT} (will clear in {VMS_STAY_TIME}s)")
            
            # Schedule display clear after stay time (with cancellation support)
            def clear_after_delay(plate_id):
                """Clear display after delay, but only if this plate is still current"""
                time.sleep(VMS_STAY_TIME)
                
                with _vms_lock:
                    # Only clear if this is still the current plate (not interrupted by new vehicle)
                    if _current_display_plate == plate_id and _pending_clear_thread is not None:
                        if clear_vms_display():
                            print(f"✓ Cleared VMS display (was showing '{plate_id}')")
                        else:
                            print(f"Warning: Failed to clear VMS display")
                        _current_display_plate = None
                        _display_start_time = None
                        _pending_clear_thread = None
                    else:
                        # Another vehicle arrived, don't clear
                        print(f"  → Skipped clear (new vehicle displayed)")
            
            # Start clear timer in background thread (non-blocking)
            with _vms_lock:
                _pending_clear_thread = Thread(target=clear_after_delay, args=(plate_number,))
                _pending_clear_thread.daemon = True
                _pending_clear_thread.start()
            
            return True
        else:
            print(f"Warning: Failed to send '{plate_number}' to VMS. Return code: {result.returncode}")
            if result.stderr:
                print(f"  Error: {result.stderr}")
            with _vms_lock:
                _current_display_plate = None
                _display_start_time = None
            return False
    except subprocess.TimeoutExpired:
        print(f"Warning: Timeout sending '{plate_number}' to VMS")
        with _vms_lock:
            _current_display_plate = None
            _display_start_time = None
        return False
    except Exception as e:
        print(f"Warning: Error sending '{plate_number}' to VMS: {e}")
        with _vms_lock:
            _current_display_plate = None
            _display_start_time = None
        return False

def extract_plate_number(data_json):
    """Extract plate number from event data"""
    try:
        if "StructureInfo" in data_json:
            structure_info = data_json.get("StructureInfo", {})
            obj_info = structure_info.get("ObjInfo", {})
            vehicle_info_list = obj_info.get("VehicleInfoList", [])
            
            if isinstance(vehicle_info_list, list) and vehicle_info_list:
                vehicle_info = vehicle_info_list[0]
                plate_no = vehicle_info.get("PlateAttributeInfo", {}).get("PlateNo", None)
                # Only return valid plate numbers (not None, not "Unknown", not empty)
                if plate_no and plate_no != "Unknown" and plate_no.strip():
                    return plate_no
        return None
    except Exception:
        return None

def listen():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = ('', receiveAlarmDataPort)
        server_socket.bind(server_address)
        server_socket.listen(99)
        print(f'Listening for camera events on port {receiveAlarmDataPort}...')
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
                # Split HTTP headers and body
                raw_data_str = data.decode('utf-8', errors='ignore')
                body = raw_data_str.split('\r\n\r\n', 1)[1] if '\r\n\r\n' in raw_data_str else raw_data_str
                
                # Clean JSON: Remove control characters but preserve valid JSON structure
                body = re.sub(r'[\x00-\x1F\x7F]', '', body)
                data_json = json.loads(body)
                
                # Extract and print plate number
                plate_no = extract_plate_number(data_json)
                if plate_no:
                    print(plate_no, flush=True)
                    # Immediately send to VMS
                    send_plate_to_vms(plate_no)
            
            except json.JSONDecodeError:
                pass  # Silently ignore JSON decode errors
            except Exception:
                pass  # Silently ignore other errors
            
            client_socket.close()
        
        except Exception:
            continue

def main():
    print("Starting plate number capture...")
    
    # Check for sendcp5200 executable
    executable = find_sendcp5200_executable()
    if executable:
        print(f"✓ Found sendcp5200: {executable}")
        print(f"  VMS Target: {VMS_IP}:{VMS_PORT}")
    else:
        print("⚠ Warning: sendcp5200 executable not found. VMS sending will be disabled.")
        print("  Searched paths:")
        for path in SENDCP5200_PATHS:
            print(f"    - {path}")
    
    # Step 1: Subscribe
    data = {
        "AddressType": 0,
        "IPAddress": receiveAlarmDataIP,
        "Port": receiveAlarmDataPort,
        "Duration": duration
    }
    jsonStr = json.dumps(data)

    try:
        response = requests.post(url=url, headers=headers, data=jsonStr, 
                               auth=HTTPDigestAuth(username, password), timeout=5)
        if response.status_code == 200:
            suscribeResJson = json.loads(response.text)
            global suscribID
            suscribID = suscribeResJson['Response']['Data']['ID']
            print(f'Subscribed successfully. Waiting for plate numbers...\n')
            
            # Step 2: Start keepalive thread
            t1 = Thread(target=keepalive)
            t1.daemon = True
            t1.start()
            
            # Step 3: Start listen thread
            t2 = Thread(target=listen)
            t2.daemon = True
            t2.start()
            
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
        print("\nScript terminated by user")
        raise SystemExit(0)
    except Exception as e:
        print(f"Error: {e}")
        raise SystemExit(1)

