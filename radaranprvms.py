#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Radar-ANPR-VMS Integration System
Combines radar detection, ANPR (camera plate recognition), and VMS display.
Displays all detected license plates on VMS display.
Stores all detections in daily JSON files.

NOTE: For best results on Raspberry Pi, run with: python3 -u radaranprvms.py
      The -u flag ensures unbuffered output for immediate display.
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
RADAR_TIMEOUT = 0.1
ONLY_POSITIVE_DIRECTION = False
POSITIVE_DIRECTION_NAME = "IMR_KD-B"
NEGATIVE_DIRECTION_NAME = "IMR_KD-KO"
MIN_SPEED_FOR_DISPLAY = 40
SPEED_LIMIT = 50
ZPOMAL_DEFER_SECONDS = 3
RADAR_DEFER_SAVE_SECONDS = 12
RADAR_READINGS_BUFFER_SECONDS = 60
RADAR_CAPTURE_WINDOW_BEFORE = 10
RADAR_CAPTURE_WINDOW_AFTER = 2
RADAR_CLUSTER_GAP_SECONDS = 5

# VMS Configuration
VMS_IP = "192.168.1.222"
VMS_PORT = 5200
SENDCP5200_PATH = "./sendcp5200/dist/Debug/GNU-Linux/sendcp5200"
VMS_DISPLAY_TIME = 3

# Data storage
DETECTIONS_FOLDER = "detections"

# ============================================================================
# GLOBAL STATE
# ============================================================================

headers = {
    'Content-Type': 'application/json',
    'Host': f'{CAMERA_IP}:{CAMERA_PORT}',
    'Connection': 'Close',
}

_radar_lock = Lock()
_detections_queue = Queue()
_detections_lock = Lock()
_current_date = None
_detections_file = None
_file_writer_running = False

_vms_clear_thread = None
_vms_lock = Lock()
_speed_violation_active = False
_speed_violation_lock = Lock()
_matched_capture_times = set()
_matched_detections_lock = Lock()
_max_matched_capture_times = 200
_positive_radar_readings = []
_negative_radar_readings = []
_current_cluster = []
_current_cluster_negative = []
_last_positive_reading_time = None
_last_negative_reading_time = None

_VMS_BASE_CMD = [
    SENDCP5200_PATH,
    "0", VMS_IP, str(VMS_PORT),
    "2", "0", "",
    "-1", "22", "0", "0", "10", "1"
]

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def ensure_detections_folder():
    if not os.path.exists(DETECTIONS_FOLDER):
        os.makedirs(DETECTIONS_FOLDER)
        print(f"Created detections folder: {DETECTIONS_FOLDER}")

def get_daily_json_filename():
    return datetime.now().strftime('%d_%m_%Y.json')

def get_daily_json_path():
    filename = get_daily_json_filename()
    return os.path.join(DETECTIONS_FOLDER, filename)

def _file_writer_worker():
    global _current_date, _detections_file, _file_writer_running
    
    _file_writer_running = True
    ensure_detections_folder()
    print("✅ File writer worker thread started and running", flush=True)
    
    pending_detections = []
    last_write_time = time.time()
    batch_timeout = 0.2
    
    while _file_writer_running:
        try:
            try:
                detection_data = _detections_queue.get(timeout=batch_timeout)
                pending_detections.append(detection_data)
                print(f"  📬 [File Writer] Received item from queue (total pending: {len(pending_detections)})", flush=True)
            except Empty:
                pass
            
            should_write = (
                pending_detections and 
                (time.time() - last_write_time >= batch_timeout or len(pending_detections) >= 10)
            )
            
            if should_write:
                print(f"📝 [File Writer] Writing {len(pending_detections)} detection(s) to file...", flush=True)
                today = datetime.now().date()
                if _current_date != today or _detections_file is None:
                    with _detections_lock:
                        _current_date = today
                        _detections_file = get_daily_json_path()
                
                filepath = _detections_file
                
                try:
                    detections = []
                    if os.path.exists(filepath):
                        try:
                            with open(filepath, 'r', encoding='utf-8') as f:
                                detections = json.load(f)
                                if not isinstance(detections, list):
                                    detections = []
                        except (json.JSONDecodeError, IOError):
                            detections = []
                    
                    detections.extend(pending_detections)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(detections, f, indent=2, ensure_ascii=False)
                        f.flush()
                        os.fsync(f.fileno())

                    sync_flag_path = os.path.join(DETECTIONS_FOLDER, '.sync_needed')
                    try:
                        with open(sync_flag_path, 'w', encoding='utf-8') as sf:
                            sf.write(json.dumps({"file": os.path.basename(filepath), "ts": datetime.now().isoformat()}))
                            sf.flush()
                    except Exception:
                        pass

                    for detection in pending_detections:
                        plate = detection.get('plate_number')
                        speed = detection.get('speed', 0)
                        direction = detection.get('direction', 'Unknown')
                        if plate:
                            print(f"💾 SAVED: {plate} | {speed}km/h | {direction} → {os.path.basename(filepath)}", flush=True)
                        else:
                            print(f"💾 SAVED: Radar-only | {speed}km/h | {direction} → {os.path.basename(filepath)}", flush=True)
                    
                    if pending_detections:
                        print(f"✅ File write complete: {len(pending_detections)} detection(s) saved to {os.path.basename(filepath)}", flush=True)
                    
                    pending_detections.clear()
                    last_write_time = time.time()
                    
                except Exception as e:
                    print(f"❌ Error saving detections: {e}", flush=True)
                    
        except Exception as e:
            print(f"File writer error: {e}", flush=True)
            time.sleep(0.1)

def save_detection(detection_data: Dict[str, Any]):
    _detections_queue.put(detection_data)
    plate = detection_data.get('plate_number', 'Radar-only')
    speed = detection_data.get('speed', 0)
    print(f"  📥 Queued for save: {plate} | {speed}km/h (queue size: {_detections_queue.qsize()})", flush=True)

def _start_file_writer():
    global _file_writer_running
    if not _file_writer_running:
        writer_thread = Thread(target=_file_writer_worker, daemon=True)
        writer_thread.start()
        time.sleep(0.1)
        print("✅ File writer thread started", flush=True)

# ============================================================================
# RADAR FUNCTIONS
# ============================================================================

def _cluster_matched_plate(cluster_start: float, cluster_end: float) -> bool:
    with _matched_detections_lock:
        for ct_str in list(_matched_capture_times):
            try:
                ct = datetime.fromisoformat(ct_str).timestamp()
                if (cluster_start - 2) <= ct <= (cluster_end + 2):
                    return True
            except (ValueError, TypeError):
                continue
    return False

def _deferred_cluster_check(cluster_readings: list, start_time: str, end_time: str, direction_sign: str = '+'):
    global _speed_violation_active
    if not cluster_readings:
        return
    peak_speed = max(s for _, s in cluster_readings)
    try:
        t_start = datetime.fromisoformat(start_time).timestamp()
        t_end = datetime.fromisoformat(end_time).timestamp()
    except (ValueError, TypeError):
        return

    time.sleep(ZPOMAL_DEFER_SECONDS)
    if _cluster_matched_plate(t_start, t_end):
        dir_name = POSITIVE_DIRECTION_NAME if direction_sign == '+' else NEGATIVE_DIRECTION_NAME
        print(f"\n  ⏭️  RADAR CLUSTER - skipped (plate matched): {peak_speed}km/h {dir_name}", flush=True)
        return
    
    if peak_speed > SPEED_LIMIT:
        with _speed_violation_lock:
            if not _speed_violation_active:
                _speed_violation_active = True
                print(f"  ⚠️  Speed violation: {peak_speed}km/h > {SPEED_LIMIT}km/h - displaying ZPOMAL!", flush=True)
                print(f"\n{'='*60}", flush=True)
                print(f"🚨 SPEED VIOLATION - NO PLATE DETECTED", flush=True)
                print(f"   Speed: {peak_speed}km/h (Limit: {SPEED_LIMIT}km/h)", flush=True)
                send_plate_to_vms("ZPOMAL!")
                print(f"{'='*60}\n", flush=True)
                time.sleep(VMS_DISPLAY_TIME)
                _speed_violation_active = False

    remaining = max(0, RADAR_DEFER_SAVE_SECONDS - ZPOMAL_DEFER_SECONDS)
    if remaining > 0:
        time.sleep(remaining)
    if _cluster_matched_plate(t_start, t_end):
        return
    
    if peak_speed >= 10:
        dir_name = POSITIVE_DIRECTION_NAME if direction_sign == '+' else NEGATIVE_DIRECTION_NAME
        vms_displayed = 'yes' if peak_speed > SPEED_LIMIT else 'no'
        radar_only_data = {
            'timestamp': datetime.now().isoformat(),
            'plate_number': None,
            'speed': peak_speed,
            'direction': dir_name,
            'radar_direction_sign': direction_sign,
            'vms_displayed': vms_displayed,
            'radar_readings_count': len(cluster_readings),
            'radar_detection_start': start_time,
            'radar_detection_end': end_time,
        }
        save_detection(radar_only_data)
        print(f"\n{'='*60}", flush=True)
        print(f"🚨 RADAR DETECTION - NO PLATE ({dir_name})", flush=True)
        print(f"   Speed: {peak_speed}km/h", flush=True)
        print(f"   Status: 💾 Saving to queue...", flush=True)
        print(f"{'='*60}\n", flush=True)
    if peak_speed < 10:
        print(f"\n📡 RADAR CLUSTER - too slow ({peak_speed}km/h), not saved", flush=True)

def process_radar_reading(direction_sign: str, speed: int):
    global _positive_radar_readings, _negative_radar_readings
    global _current_cluster, _current_cluster_negative
    global _last_positive_reading_time, _last_negative_reading_time

    timestamp = datetime.now().isoformat()
    now_ts = datetime.now().timestamp()
    cutoff = now_ts - RADAR_READINGS_BUFFER_SECONDS

    with _radar_lock:
        if direction_sign == '+' and speed > 0:
            if _last_positive_reading_time is not None:
                try:
                    last_ts = datetime.fromisoformat(_last_positive_reading_time).timestamp()
                    if (now_ts - last_ts) > RADAR_CLUSTER_GAP_SECONDS and _current_cluster:
                        cluster_copy = list(_current_cluster)
                        start_t = cluster_copy[0][0]
                        end_t = cluster_copy[-1][0]
                        _current_cluster = []
                        Thread(target=_deferred_cluster_check, args=(cluster_copy, start_t, end_t, '+'), daemon=True).start()
                except (ValueError, TypeError):
                    pass
            _last_positive_reading_time = timestamp
            _current_cluster.append((timestamp, speed))
            _positive_radar_readings.append((timestamp, speed))
            while _positive_radar_readings:
                try:
                    ts = datetime.fromisoformat(_positive_radar_readings[0][0]).timestamp()
                    if ts < cutoff:
                        _positive_radar_readings.pop(0)
                    else:
                        break
                except (ValueError, TypeError):
                    _positive_radar_readings.pop(0)

        if not ONLY_POSITIVE_DIRECTION and direction_sign == '-' and speed > 0:
            if _last_negative_reading_time is not None:
                try:
                    last_ts = datetime.fromisoformat(_last_negative_reading_time).timestamp()
                    if (now_ts - last_ts) > RADAR_CLUSTER_GAP_SECONDS and _current_cluster_negative:
                        cluster_copy = list(_current_cluster_negative)
                        start_t = cluster_copy[0][0]
                        end_t = cluster_copy[-1][0]
                        _current_cluster_negative = []
                        Thread(target=_deferred_cluster_check, args=(cluster_copy, start_t, end_t, '-'), daemon=True).start()
                except (ValueError, TypeError):
                    pass
            _last_negative_reading_time = timestamp
            _current_cluster_negative.append((timestamp, speed))
            _negative_radar_readings.append((timestamp, speed))
            while _negative_radar_readings:
                try:
                    ts = datetime.fromisoformat(_negative_radar_readings[0][0]).timestamp()
                    if ts < cutoff:
                        _negative_radar_readings.pop(0)
                    else:
                        break
                except (ValueError, TypeError):
                    _negative_radar_readings.pop(0)

def _readings_in_window(readings: list, t_min: float, t_max: float) -> list:
    """Get (ts, speed) pairs within time window."""
    candidates = []
    for ts_str, speed in readings:
        try:
            ts = datetime.fromisoformat(ts_str).timestamp()
            if t_min <= ts <= t_max:
                candidates.append((ts, speed))
        except (ValueError, TypeError):
            continue
    return candidates


def _cluster_by_gap(candidates: list, gap_seconds: float) -> list:
    """
    Group readings into clusters by time gap. Gap > gap_seconds starts new cluster.
    Returns list of (start_ts, end_ts, peak_speed, cluster_readings).
    """
    if not candidates:
        return []
    sorted_candidates = sorted(candidates, key=lambda x: x[0])
    clusters = []
    current = [sorted_candidates[0]]
    for i in range(1, len(sorted_candidates)):
        ts, _ = sorted_candidates[i]
        last_ts = current[-1][0]
        if ts - last_ts > gap_seconds:
            start_ts = current[0][0]
            end_ts = current[-1][0]
            peak_speed = max(s for _, s in current)
            clusters.append((start_ts, end_ts, peak_speed, list(current)))
            current = [sorted_candidates[i]]
        else:
            current.append(sorted_candidates[i])
    if current:
        start_ts = current[0][0]
        end_ts = current[-1][0]
        peak_speed = max(s for _, s in current)
        clusters.append((start_ts, end_ts, peak_speed, list(current)))
    return clusters


def get_best_radar_match_by_capture_time(capture_time: datetime) -> Optional[Dict[str, Any]]:
    """
    Match plate to radar by clustering readings in time window, then picking the cluster
    whose time best matches the plate (closest end_time to plate time; radar comes first).
    """
    global _positive_radar_readings, _negative_radar_readings

    if not isinstance(capture_time, datetime):
        return None

    with _radar_lock:
        pos_readings = list(_positive_radar_readings)
        neg_readings = list(_negative_radar_readings) if not ONLY_POSITIVE_DIRECTION else []

    t0 = capture_time.timestamp()
    t_min = t0 - RADAR_CAPTURE_WINDOW_BEFORE
    t_max = t0 + RADAR_CAPTURE_WINDOW_AFTER

    best_cluster = None  # (start_ts, end_ts, peak_speed, candidates, direction_sign, direction_name)

    for direction_sign, direction_name, readings in [
        ('+', POSITIVE_DIRECTION_NAME, pos_readings),
        ('-', NEGATIVE_DIRECTION_NAME, neg_readings),
    ]:
        if not readings and direction_sign == '-':
            continue
        if ONLY_POSITIVE_DIRECTION and direction_sign == '-':
            continue
        candidates = _readings_in_window(readings, t_min, t_max)
        clusters = _cluster_by_gap(candidates, RADAR_CLUSTER_GAP_SECONDS)
        for start_ts, end_ts, peak_speed, cluster_readings in clusters:
            # Pick cluster whose end_time is closest to plate time (radar comes first)
            dist = abs(end_ts - t0)
            if best_cluster is None or dist < best_cluster[4]:
                best_cluster = (start_ts, end_ts, peak_speed, cluster_readings, dist, direction_sign, direction_name)

    if best_cluster is None:
        try:
            all_readings = pos_readings + neg_readings
            if all_readings:
                buf_first = datetime.fromisoformat(all_readings[0][0])
                buf_last = datetime.fromisoformat(all_readings[-1][0])
                print(f"  📡 [Match] No overlap: search {capture_time.strftime('%H:%M:%S')} vs buffer {buf_first.strftime('%H:%M:%S')}–{buf_last.strftime('%H:%M:%S')} ({len(all_readings)} readings)", flush=True)
            else:
                print(f"  📡 [Match] Buffer empty - no readings in last {RADAR_READINGS_BUFFER_SECONDS}s", flush=True)
        except Exception:
            pass
        return None

    start_ts, end_ts, peak_speed, cluster_readings, _dist, direction_sign, direction_name = best_cluster
    peak_readings = [(t, s) for t, s in cluster_readings if s == peak_speed]
    peak_ts = min(peak_readings, key=lambda x: abs(x[0] - t0))[0]
    peak_time_str = datetime.fromtimestamp(peak_ts).isoformat()

    return {
        'direction_sign': direction_sign,
        'direction_name': direction_name,
        'peak_speed': peak_speed,
        'peak_time': peak_time_str,
        'readings_count': len(cluster_readings),
        'start_time': datetime.fromtimestamp(start_ts).isoformat(),
        'end_time': datetime.fromtimestamp(end_ts).isoformat(),
    }

def get_best_radar_match_by_receive_time(receive_time: datetime) -> Optional[Dict[str, Any]]:
    return get_best_radar_match_by_capture_time(receive_time)

def read_radar_data():
    print(f"Starting radar reader on {RADAR_PORT}...")
    
    ser = None
    retry_count = 0
    max_retries = 5
    buffer = b''
    max_buffer_size = 1000
    
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
            
            data = ser.read(32)
            
            if data:
                buffer += data
                
                if len(buffer) > max_buffer_size:
                    last_a = buffer.rfind(b'A')
                    if last_a > 0 and last_a < len(buffer) - 4:
                        buffer = buffer[last_a:]
                        print(f"📡 [Buffer cleared] Size exceeded, kept last {len(buffer)} bytes", flush=True)
                    else:
                        buffer = b''
                        print(f"📡 [Buffer cleared] No valid data found", flush=True)
                
                max_iterations = 50
                iteration = 0
                while len(buffer) >= 5 and iteration < max_iterations:
                    iteration += 1
                    chunk = buffer[:5]
                    buffer = buffer[5:]
                    
                    if chunk[0] == ord('A') and len(chunk) == 5:
                        if chunk[1] == ord('+') or chunk[1] == ord('-'):
                            try:
                                direction_sign = '+' if chunk[1] == ord('+') else '-'
                                speed = int(chunk[2:].decode('utf-8'))
                                
                                def process_async(direction, spd):
                                    try:
                                        process_radar_reading(direction, spd)
                                    except Exception as e:
                                        print(f"  ❌ Error processing radar reading: {e}", flush=True)
                                        import traceback
                                        traceback.print_exc()
                                
                                Thread(target=process_async, args=(direction_sign, speed), daemon=True).start()
                            except (ValueError, UnicodeDecodeError):
                                pass
                        else:
                            if b'A' in chunk[1:]:
                                idx = chunk[1:].index(b'A') + 1
                                buffer = chunk[idx:] + buffer
                            break
                    else:
                        if b'A' in chunk:
                            idx = chunk.index(b'A')
                            buffer = chunk[idx:] + buffer
                        break
                
                if iteration >= max_iterations:
                    print(f"📡 [Buffer cleared] Max iterations reached", flush=True)
                    buffer = b''
            
            time.sleep(0.3)
                
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
            buffer = b''

# ============================================================================
# VMS FUNCTIONS
# ============================================================================

def _send_vms_command(display_text: str) -> bool:
    cmd = _VMS_BASE_CMD.copy()
    cmd[6] = display_text
    
    cmd_str = ' '.join(f'"{arg}"' if ' ' in str(arg) else str(arg) for arg in cmd)
    print(f"  📤 VMS Command: {cmd_str}", flush=True)
    
    try:
        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except Exception as e:
        print(f"  ❌ VMS Command failed: {e}", flush=True)
        return False

def send_plate_to_vms(plate_number: str):
    global _vms_clear_thread
    
    display_text = plate_number if plate_number and plate_number.strip() else ""
    
    with _vms_lock:
        if _vms_clear_thread is not None and display_text:
            _vms_clear_thread = None
    
    if display_text and display_text != "ZPOMAL!":
        with _speed_violation_lock:
            _speed_violation_active = False
    
    if display_text:
        print(f"\n{'='*60}", flush=True)
        print(f"📺 VMS DISPLAY EVENT", flush=True)
        print(f"   Message: '{display_text}'", flush=True)
        print(f"   Duration: {VMS_DISPLAY_TIME}s", flush=True)
    else:
        print(f"\n📺 VMS: Clearing display", flush=True)
    
    success = _send_vms_command(display_text)
    
    if display_text:
        if success:
            print(f"   Status: ✅ Command sent successfully", flush=True)
            print(f"{'='*60}\n", flush=True)
        else:
            print(f"   Status: ❌ Command failed", flush=True)
            print(f"{'='*60}\n", flush=True)
        
        def clear_after_delay():
            global _vms_clear_thread
            time.sleep(VMS_DISPLAY_TIME)
            
            with _vms_lock:
                if _vms_clear_thread is not None:
                    sys.stdout.flush()
                    _send_vms_command("")
                    _vms_clear_thread = None
        
        with _vms_lock:
            _vms_clear_thread = Thread(target=clear_after_delay, daemon=True)
            _vms_clear_thread.start()
    
    return success

# ============================================================================
# CAMERA/ANPR FUNCTIONS
# ============================================================================

def extract_camera_capture_time(data_json) -> Optional[datetime]:
    for path in [
        ("StructureInfo", "ImageInfoList", 0, "CaptureTime"),
        ("StructureInfo", "ObjInfo", "Time"),
        ("StructureInfo", "ObjInfo", "TimeStamp"),
        ("StructureInfo", "ObjInfo", "DateTime"),
    ]:
        obj = data_json
        for key in path:
            if isinstance(key, int):
                if isinstance(obj, list) and 0 <= key < len(obj):
                    obj = obj[key]
                else:
                    obj = None
                    break
            else:
                if isinstance(obj, dict):
                    obj = obj.get(key)
                else:
                    obj = None
                    break
            if obj is None:
                break
        if obj and isinstance(obj, str) and len(obj) >= 14:
            raw = obj.replace("-", "").replace(":", "").replace(".", "")
            if raw.isdigit():
                try:
                    y, m, d = int(raw[:4]), int(raw[4:6]), int(raw[6:8])
                    h, mi, s = int(raw[8:10]), int(raw[10:12]), int(raw[12:14])
                    ms = int(raw[14:17]) if len(raw) >= 17 else 0
                    return datetime(y, m, d, h, mi, s, ms * 1000)
                except (ValueError, IndexError):
                    pass
    ts = data_json.get("TimeStamp")
    if ts is not None and isinstance(ts, (int, float)):
        try:
            return datetime.fromtimestamp(ts)
        except (ValueError, OSError):
            pass
    return None

def extract_plate_number(data_json):
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
        
        if plate_no:
            print(f"    🔍 Found PlateNo in JSON: '{plate_no}'", flush=True)
        
        if plate_no and plate_no != "Unknown" and plate_no.strip():
            return plate_no
        return None
    except (KeyError, TypeError, AttributeError) as e:
        print(f"    ❌ Plate extraction error: {e}", flush=True)
        return None

def keepalive():
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
    global _matched_capture_times
    
    try:
        data = b''
        client_socket.settimeout(10.0)
        
        max_reads = 100
        read_count = 0
        
        while read_count < max_reads:
            try:
                tmp = client_socket.recv(16384)
                if not tmp:
                    break
                data += tmp
                read_count += 1
                
                if b'\r\n\r\n' in data and len(data) > 100:
                    try:
                        raw_str = data.decode('utf-8', errors='ignore')
                        headers_end = raw_str.find('\r\n\r\n')
                        if headers_end > 0:
                            headers_str = raw_str[:headers_end]
                            content_length_match = re.search(r'Content-Length:\s*(\d+)', headers_str, re.IGNORECASE)
                            if content_length_match:
                                content_length = int(content_length_match.group(1))
                                body_start = headers_end + 4
                                body_received = len(data) - body_start
                                if body_received >= content_length:
                                    break
                    except Exception:
                        pass
                        
            except socket.timeout:
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
        
        print(f"📷 Camera event received ({len(data)} bytes)", flush=True)
        
        try:
            raw_data_str = data.decode('utf-8', errors='ignore')
            
            if '\r\n\r\n' in raw_data_str:
                body = raw_data_str.split('\r\n\r\n', 1)[1]
            else:
                body = raw_data_str
            
            body = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', body)
            
            try:
                data_json = json.loads(body)
            except json.JSONDecodeError as json_err:
                json_start = body.find('{')
                json_end = body.rfind('}')
                if json_start >= 0 and json_end > json_start:
                    json_str = body[json_start:json_end+1]
                    data_json = json.loads(json_str)
                else:
                    print(f"  ❌ JSON parse failed: {json_err}", flush=True)
                    raise
            
            plate_no = extract_plate_number(data_json)
            
            if plate_no:
                print(f"  ✅ Plate extracted: {plate_no}", flush=True)
            else:
                try:
                    structure_info = data_json.get("StructureInfo", {})
                    if structure_info:
                        obj_info = structure_info.get("ObjInfo", {})
                        vehicle_list = obj_info.get("VehicleInfoList", [])
                        print(f"  ⚠️  No plate: VehicleInfoList={len(vehicle_list) if isinstance(vehicle_list, list) else 'not list'}", flush=True)
                except:
                    print(f"  ⚠️  No plate: JSON structure issue", flush=True)
            
            if plate_no:
                capture_time = extract_camera_capture_time(data_json)
                plate_timestamp = capture_time if capture_time else datetime.now()
                timestamp = plate_timestamp.isoformat()

                receive_time = datetime.now()
                radar_detection = None
                radar_detection = get_best_radar_match_by_receive_time(receive_time)
                if radar_detection:
                    print(f"  📷 Receive-time sync: {receive_time.strftime('%H:%M:%S.%f')[:-3]} → {radar_detection['peak_speed']}km/h {radar_detection['direction_name']}", flush=True)
                if not radar_detection and capture_time:
                    radar_detection = get_best_radar_match_by_capture_time(capture_time)
                    if radar_detection:
                        print(f"  📷 Capture-time sync: {capture_time.strftime('%H:%M:%S.%f')[:-3]} → {radar_detection['peak_speed']}km/h {radar_detection['direction_name']}", flush=True)

                if radar_detection:
                    print(f"  🔗 Found radar match: {radar_detection['peak_speed']}km/h | {radar_detection['direction_name']}", flush=True)
                else:
                    print(f"  ⚠️  No radar match found for plate {plate_no}", flush=True)

                if radar_detection and capture_time:
                    with _matched_detections_lock:
                        _matched_capture_times.add(capture_time.isoformat())
                        if len(_matched_capture_times) > _max_matched_capture_times:
                            sorted_items = sorted(_matched_capture_times)
                            _matched_capture_times = set(sorted_items[-_max_matched_capture_times // 2:])
                    
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
                        'radar_detection_end': radar_detection['end_time'],
                        'radar_peak_time': radar_detection.get('peak_time'),
                    }
                    if capture_time:
                        detection_data['camera_capture_time'] = capture_time.isoformat()
                    
                    print(f"\n{'='*60}", flush=True)
                    print(f"✅ DETECTION WITH PLATE", flush=True)
                    print(f"   Plate: {plate_no}", flush=True)
                    print(f"   Speed: {speed}km/h", flush=True)
                    print(f"   Direction: {direction}", flush=True)
                    print(f"   Status: 💾 Saving...", flush=True)
                    save_detection(detection_data)
                    
                    if speed > MIN_SPEED_FOR_DISPLAY:
                        send_plate_to_vms(plate_no)
                    else:
                        send_plate_to_vms("")
                        print(f"   VMS: ⏭️  Not displaying (speed {speed}km/h <= {MIN_SPEED_FOR_DISPLAY}km/h)", flush=True)
                    print(f"{'='*60}\n", flush=True)
                else:
                    speed = 0
                    default_direction = 'IMR_KD'  # Fallback when plate misses radar
                    default_sign = None
                    detection_data = {
                        'timestamp': timestamp,
                        'plate_number': plate_no,
                        'speed': speed,
                        'direction': default_direction,
                        'radar_direction_sign': default_sign,
                        'vms_displayed': 'no',
                        'radar_readings_count': 0,
                        'radar_detection_start': None,
                        'radar_detection_end': None
                    }
                    if capture_time:
                        detection_data['camera_capture_time'] = capture_time.isoformat()
                    print(f"\n{'='*60}", flush=True)
                    print(f"⚠️  PLATE DETECTION - NO RADAR MATCH", flush=True)
                    print(f"   Plate: {plate_no}", flush=True)
                    print(f"   Reason: No radar match for capture time (window ±{RADAR_CAPTURE_WINDOW_BEFORE}/{RADAR_CAPTURE_WINDOW_AFTER}s)", flush=True)
                    print(f"   Status: 💾 Saving...", flush=True)
                    save_detection(detection_data)
                    send_plate_to_vms("")
                    print(f"   VMS: ⏭️  Not displaying (no speed data)", flush=True)
                    print(f"{'='*60}\n", flush=True)
            else:
                print(f"📷 Camera event: No plate detected", flush=True)
                send_plate_to_vms("")
        
        except json.JSONDecodeError:
            pass
        except Exception:
            pass
    
    finally:
        try:
            client_socket.close()
        except:
            pass

def listen_camera_events():
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
    print(f"  Directions: {'A+ only' if ONLY_POSITIVE_DIRECTION else 'A+ and A-'}")
    print(f"  ZPOMAL: {SPEED_LIMIT}+ km/h, defer {ZPOMAL_DEFER_SECONDS}s (immediate if no plate)")
    print(f"  Detections Folder: {DETECTIONS_FOLDER}")
    print("=" * 60)
    
    ensure_detections_folder()
    print(f"✓ Detections will be saved to: {get_daily_json_path()}")
    
    _start_file_writer()
    
    time.sleep(0.2)
    if _file_writer_running:
        print("✓ File writer is running")
    else:
        print("⚠️  WARNING: File writer may not be running!")
    
    print("\nStarting radar reader...")
    radar_thread = Thread(target=read_radar_data, daemon=True)
    radar_thread.start()
    time.sleep(1)
    
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
            
            keepalive_thread = Thread(target=keepalive, daemon=True)
            keepalive_thread.start()
            
            camera_thread = Thread(target=listen_camera_events, daemon=True)
            camera_thread.start()
            
            print("\n" + "=" * 60)
            print("System running. Waiting for detections...")
            print("Press Ctrl+C to stop")
            print("=" * 60 + "\n")
            
            last_status_time = time.time()
            status_interval = 30
            
            while True:
                time.sleep(1)
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
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(line_buffering=True)
        sys.stderr.reconfigure(line_buffering=True)
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nScript terminated by user", flush=True)
        print(f"Today's detections saved to: {get_daily_json_path()}", flush=True)
        raise SystemExit(0)
    except Exception as e:
        print(f"Error: {e}", flush=True)
        raise SystemExit(1)