#!/usr/bin/env python3
"""
ANPR/Camera test - same implementation as radaranprvms.py
Subscribe to camera, receive plate events, display only. No radar, no VMS.
"""

import argparse
import json
import re
import socket
import sys
import time
import threading
from datetime import datetime
from requests.auth import HTTPDigestAuth
import requests

# Same as radaranprvms.py
CAMERA_USERNAME = 'admin'
CAMERA_PASSWORD = 'kObliha12@'
CAMERA_IP = '192.168.2.13'
CAMERA_PORT = 80
RECEIVE_ALARM_DATA_IP = "192.168.2.101"
RECEIVE_ALARM_DATA_PORT = 8090
DURATION = 300
CAMERA_URL = f'http://{CAMERA_IP}:{CAMERA_PORT}/LAPI/V1.0/System/Event/Subscription'

headers = {
    'Content-Type': 'application/json',
    'Host': f'{CAMERA_IP}:{CAMERA_PORT}',
    'Connection': 'Close',
}


def extract_plate_number(data_json):
    """Extract plate number from camera event data - same as radaranprvms.py"""
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


def extract_time_info(data_json):
    """Extract time/capture info from camera event - common Hikvision/LAPI fields"""
    for path in [
        ("StructureInfo", "ImageInfoList", 0, "CaptureTime"),
        ("StructureInfo", "ObjInfo", "Time"),
        ("StructureInfo", "ObjInfo", "TimeStamp"),
        ("StructureInfo", "ObjInfo", "DateTime"),
        ("StructureInfo", "Time"),
        ("StructureInfo", "TimeStamp"),
        ("Event", "Time"),
        ("Event", "TimeStamp"),
        ("Time",),
        ("TimeStamp",),
        ("DateTime",),
    ]:
        obj = data_json
        for key in path:
            if isinstance(key, int):
                obj = obj[key] if isinstance(obj, list) and 0 <= key < len(obj) else None
            else:
                obj = obj.get(key) if isinstance(obj, dict) else None
            if obj is None:
                break
        if obj and isinstance(obj, str):
            return obj
    # TimeStamp at top level is often Unix seconds (numeric)
    ts = data_json.get("TimeStamp")
    if ts is not None and isinstance(ts, (int, float)):
        try:
            return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        except (ValueError, OSError):
            pass
    return None


def keepalive(subscription_id):
    """Keep camera subscription alive - same as radaranprvms.py"""
    while True:
        try:
            keepalive_url = f"{CAMERA_URL}/{subscription_id}"
            response = requests.put(
                url=keepalive_url,
                headers=headers,
                data=json.dumps({'Duration': DURATION}),
                auth=HTTPDigestAuth(CAMERA_USERNAME, CAMERA_PASSWORD),
                timeout=5
            )
            if response.status_code != 200:
                print(f'Keepalive failure: {response.status_code}')
        except Exception as e:
            print(f'Keepalive error: {e}')
        time.sleep(DURATION / 2)


def handle_camera_client(client_socket, dump_json=False):
    """Handle camera connection - same logic as radaranprvms _handle_camera_client"""
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

        if dump_json:
            print("\n" + "=" * 60 + "\nRAW CAMERA JSON (for time extraction):\n" + "=" * 60)
            print(json.dumps(data_json, indent=2, ensure_ascii=False))
            print("=" * 60 + "\n")

        plate_no = extract_plate_number(data_json)
        ts_receive = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        ts_camera = extract_time_info(data_json)
        time_info = f" | camera_time: {ts_camera}" if ts_camera else ""
        if plate_no:
            print(f"{ts_receive} | PLATE: {plate_no}{time_info}")
        else:
            vlist = data_json.get("StructureInfo", {}).get("ObjInfo", {}).get("VehicleInfoList", [])
            print(f"{ts_receive} | event (no plate) VehicleInfoList={len(vlist) if isinstance(vlist, list) else '?'}{time_info}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            client_socket.close()
        except Exception:
            pass


DUMP_JSON = False


def listen_camera_events():
    """Listen for camera ANPR events - same as radaranprvms.py"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.settimeout(1.0)
    server_socket.bind(('', RECEIVE_ALARM_DATA_PORT))
    server_socket.listen(99)
    print(f'Listening on port {RECEIVE_ALARM_DATA_PORT}...')

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            threading.Thread(target=handle_camera_client, args=(client_socket, DUMP_JSON), daemon=True).start()
        except socket.timeout:
            continue
        except Exception as e:
            print(f"Accept error: {e}")


def main():
    global DUMP_JSON
    parser = argparse.ArgumentParser(description="ANPR/Camera test - receive plate events")
    parser.add_argument("--dump-json", action="store_true", help="Print raw JSON for each event (to inspect time fields)")
    args = parser.parse_args()
    DUMP_JSON = args.dump_json

    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(line_buffering=True)
        sys.stderr.reconfigure(line_buffering=True)

    print("=" * 50)
    print("ANPR/Camera Test - same as radaranprvms.py")
    print("=" * 50)
    print(f"Camera: {CAMERA_IP}:{CAMERA_PORT}")
    print(f"Receive: {RECEIVE_ALARM_DATA_IP}:{RECEIVE_ALARM_DATA_PORT}")
    print("=" * 50)

    # Bind first, then subscribe
    server_thread = threading.Thread(target=listen_camera_events, daemon=True)
    server_thread.start()
    time.sleep(0.5)

    print("Subscribing to camera...")
    try:
        sub_data = {
            "AddressType": 0,
            "IPAddress": RECEIVE_ALARM_DATA_IP,
            "Port": RECEIVE_ALARM_DATA_PORT,
            "Duration": DURATION
        }
        response = requests.post(
            url=CAMERA_URL,
            headers=headers,
            data=json.dumps(sub_data),
            auth=HTTPDigestAuth(CAMERA_USERNAME, CAMERA_PASSWORD),
            timeout=5
        )
        if response.status_code == 200:
            sub_id = response.json()['Response']['Data']['ID']
            print(f'Subscribed (ID: {sub_id})')
            threading.Thread(target=keepalive, args=(sub_id,), daemon=True).start()
        else:
            print(f'Subscribe failed: {response.status_code} {response.text}')
            return
    except Exception as e:
        print(f'Subscribe error: {e}')
        return

    if DUMP_JSON:
        print("(--dump-json: raw JSON will be printed for each event)\n")
    print("Waiting for plate events. Ctrl+C to stop.\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped")


if __name__ == "__main__":
    main()
