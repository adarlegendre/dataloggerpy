#!/usr/bin/env python3
"""
Raw Serial Radar Reader with ANPR
Reads from radar every 0.2s. Displays + and - in two columns.
Subscribes to camera for plate events. Dumps plates immediately and saves
radar + plate readings to a log file.
Settings from radaranprvms.py.
"""

import json
import os
import re
import serial
import socket
import sys
import threading
import time
from datetime import datetime
from requests.auth import HTTPDigestAuth
import requests

# Radar config (same as radaranprvms.py)
PORT = '/dev/ttyAMA0'
BAUDRATE = 9600
READ_INTERVAL = 0.2
COLLAPSE_IDENTICAL = True
COL_WIDTH = 38

# Camera config from radaranprvms.py
CAMERA_USERNAME = 'admin'
CAMERA_PASSWORD = 'kObliha12@'
CAMERA_IP = '192.168.2.13'
CAMERA_PORT = 80
RECEIVE_ALARM_DATA_IP = "192.168.2.101"
RECEIVE_ALARM_DATA_PORT = 8090
DURATION = 300
CAMERA_URL = f'http://{CAMERA_IP}:{CAMERA_PORT}/LAPI/V1.0/System/Event/Subscription'

HEADERS = {
    'Content-Type': 'application/json',
    'Host': f'{CAMERA_IP}:{CAMERA_PORT}',
    'Connection': 'Close',
}

# Log file for radar + plate instances
LOG_FOLDER = "radar_plates_logs"
LOG_FILE = None
_LOG_LOCK = threading.Lock()


def get_log_path():
    """Daily log file: radar_plates_logs/DD_MM_YYYY.log"""
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)
    return os.path.join(LOG_FOLDER, datetime.now().strftime('%d_%m_%Y.log'))


def log_write(line: str):
    """Append a line to the log file (thread-safe)."""
    global LOG_FILE
    with _LOG_LOCK:
        path = get_log_path()
        try:
            with open(path, 'a', encoding='utf-8') as f:
                f.write(line + '\n')
        except Exception as e:
            print(f"  [Log error] {e}", flush=True)


def extract_plate_number(data_json):
    """Extract plate number from camera event - same as radaranprvms.py"""
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


def extract_camera_capture_time(data_json):
    """Extract capture time from event - same as radaranprvms.py"""
    for path in [
        ("StructureInfo", "ImageInfoList", 0, "CaptureTime"),
        ("StructureInfo", "ObjInfo", "Time"),
        ("StructureInfo", "ObjInfo", "TimeStamp"),
    ]:
        obj = data_json
        for key in path:
            if isinstance(key, int):
                obj = obj[key] if isinstance(obj, list) and 0 <= key < len(obj) else None
            else:
                obj = obj.get(key) if isinstance(obj, dict) else None
            if obj is None:
                break
        if obj and isinstance(obj, str) and len(obj) >= 14:
            raw = obj.replace("-", "").replace(":", "").replace(".", "")
            if raw.isdigit():
                try:
                    y, m, d = int(raw[:4]), int(raw[4:6]), int(raw[6:8])
                    h, mi, s = int(raw[8:10]), int(raw[10:12]), int(raw[12:14])
                    ms = int(raw[14:17]) if len(raw) >= 17 else 0
                    return f"{y:04d}-{m:02d}-{d:02d} {h:02d}:{mi:02d}:{s:02d}.{ms:03d}"
                except (ValueError, IndexError):
                    pass
    return None


def keepalive(subscription_id):
    """Keep camera subscription alive."""
    while True:
        try:
            keepalive_url = f"{CAMERA_URL}/{subscription_id}"
            response = requests.put(
                url=keepalive_url,
                headers=HEADERS,
                data=json.dumps({'Duration': DURATION}),
                auth=HTTPDigestAuth(CAMERA_USERNAME, CAMERA_PASSWORD),
                timeout=5
            )
            if response.status_code != 200:
                print(f'Keepalive failure: {response.status_code}', flush=True)
        except Exception as e:
            print(f'Keepalive error: {e}', flush=True)
        time.sleep(DURATION / 2)


def handle_camera_client(client_socket):
    """Handle camera connection - extract plate, dump immediately, save to log."""
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
                            m = re.search(r'Content-Length:\s*(\d+)', raw_str[:headers_end], re.I)
                            if m:
                                content_length = int(m.group(1))
                                body_start = headers_end + 4
                                if len(data) - body_start >= content_length:
                                    break
                    except Exception:
                        pass
            except socket.timeout:
                if len(data) > 100:
                    break
                break
            except Exception:
                break

        if not data or len(data) < 50:
            client_socket.close()
            return

        raw_str = data.decode('utf-8', errors='ignore')
        body = raw_str.split('\r\n\r\n', 1)[1] if '\r\n\r\n' in raw_str else raw_str
        body = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', body)

        try:
            data_json = json.loads(body)
        except json.JSONDecodeError:
            json_start, json_end = body.find('{'), body.rfind('}')
            if json_start >= 0 and json_end > json_start:
                data_json = json.loads(body[json_start:json_end + 1])
            else:
                client_socket.close()
                return

        plate_no = extract_plate_number(data_json)
        ts_receive = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        capture_time = extract_camera_capture_time(data_json)

        if plate_no:
            # Dump plate immediately
            line = f"PLATE | {ts_receive} | {plate_no}"
            if capture_time:
                line += f" | capture: {capture_time}"
            print(f"\n  📷 {line}\n", flush=True)
            log_write(line)
        else:
            vlist = data_json.get("StructureInfo", {}).get("ObjInfo", {}).get("VehicleInfoList", [])
            log_write(f"EVENT | {ts_receive} | no plate | VehicleInfoList={len(vlist) if isinstance(vlist, list) else '?'}")

    except Exception as e:
        print(f"  Camera handler error: {e}", flush=True)
    finally:
        try:
            client_socket.close()
        except Exception:
            pass


def listen_camera_events():
    """Listen for camera ANPR events."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.settimeout(1.0)
    server_socket.bind(('', RECEIVE_ALARM_DATA_PORT))
    server_socket.listen(99)

    while True:
        try:
            client_socket, _ = server_socket.accept()
            threading.Thread(target=handle_camera_client, args=(client_socket,), daemon=True).start()
        except socket.timeout:
            continue
        except Exception as e:
            print(f"Accept error: {e}", flush=True)


def fmt(raw, count):
    s = f"{raw} {int(raw[2:])} km/h"
    return f"{s} (x{count})" if count > 1 else s


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(line_buffering=True)
        sys.stderr.reconfigure(line_buffering=True)

    print("Radar + ANPR reader. Plates dumped immediately, saved to", get_log_path(), flush=True)
    print("Ctrl+C to stop.\n", flush=True)

    # Start camera listener
    cam_thread = threading.Thread(target=listen_camera_events, daemon=True)
    cam_thread.start()
    time.sleep(0.5)

    # Subscribe to camera
    print("Subscribing to camera...", flush=True)
    try:
        sub_data = {
            "AddressType": 0,
            "IPAddress": RECEIVE_ALARM_DATA_IP,
            "Port": RECEIVE_ALARM_DATA_PORT,
            "Duration": DURATION
        }
        response = requests.post(
            url=CAMERA_URL,
            headers=HEADERS,
            data=json.dumps(sub_data),
            auth=HTTPDigestAuth(CAMERA_USERNAME, CAMERA_PASSWORD),
            timeout=5
        )
        if response.status_code == 200:
            sub_id = response.json()['Response']['Data']['ID']
            print(f'Subscribed (ID: {sub_id})', flush=True)
            threading.Thread(target=keepalive, args=(sub_id,), daemon=True).start()
        else:
            print(f'Subscribe failed: {response.status_code} {response.text}', flush=True)
    except Exception as e:
        print(f'Subscribe error: {e}', flush=True)

    header = f"  {'+ (→)':<{COL_WIDTH}}  |  {'- (←)':<{COL_WIDTH}}  "
    print(header)
    print("  " + "-" * COL_WIDTH + "  |  " + "-" * COL_WIDTH)

    try:
        ser = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=0.1)
        print(f"Connected to {PORT}\n", flush=True)
    except Exception as e:
        print(f"Error: {e}", flush=True)
        return

    buffer = b""
    last_plus, count_plus = None, 0
    last_minus, count_minus = None, 0

    def flush_plus():
        nonlocal last_plus, count_plus
        if last_plus is not None:
            ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            left = f"{ts} {fmt(last_plus, count_plus)}"
            print(f"  {left:<{COL_WIDTH}}  |  {'':<{COL_WIDTH}}  ", flush=True)
            log_write(f"RADAR | {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]} | {last_plus} {int(last_plus[2:])} km/h" + (f" (x{count_plus})" if count_plus > 1 else ""))
            last_plus, count_plus = None, 0

    def flush_minus():
        nonlocal last_minus, count_minus
        if last_minus is not None:
            ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            right = f"{ts} {fmt(last_minus, count_minus)}"
            print(f"  {'':<{COL_WIDTH}}  |  {right:<{COL_WIDTH}}  ", flush=True)
            log_write(f"RADAR | {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]} | {last_minus} {int(last_minus[2:])} km/h" + (f" (x{count_minus})" if count_minus > 1 else ""))
            last_minus, count_minus = None, 0

    try:
        while True:
            data = ser.read(32)
            if data:
                buffer += data
                while len(buffer) >= 5:
                    chunk = buffer[:5]
                    buffer = buffer[5:]
                    if chunk[0] == ord("A") and chunk[1] in (ord("+"), ord("-")):
                        try:
                            raw = chunk.decode("utf-8")
                            if raw[1] == "+":
                                if COLLAPSE_IDENTICAL:
                                    if raw == last_plus:
                                        count_plus += 1
                                    else:
                                        flush_plus()
                                        last_plus, count_plus = raw, 1
                                else:
                                    flush_plus()
                                    last_plus, count_plus = raw, 1
                                    flush_plus()
                            else:
                                if COLLAPSE_IDENTICAL:
                                    if raw == last_minus:
                                        count_minus += 1
                                    else:
                                        flush_minus()
                                        last_minus, count_minus = raw, 1
                                else:
                                    flush_minus()
                                    last_minus, count_minus = raw, 1
                                    flush_minus()
                        except (ValueError, UnicodeDecodeError):
                            pass
                    elif b"A" in chunk:
                        i = chunk.index(b"A")
                        buffer = chunk[i:] + buffer
                    else:
                        break
            time.sleep(READ_INTERVAL)
    except KeyboardInterrupt:
        flush_plus()
        flush_minus()
        print("\nStopped", flush=True)
    finally:
        ser.close()


if __name__ == "__main__":
    main()
