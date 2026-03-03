#!/usr/bin/env python3
"""
Log radar + plate events to a file. Run it, let traffic pass, Ctrl+C to stop.
Share the output file to tune matching logic.

  python test_radar_plate_timing.py

Output: timing_log.txt (in same folder)
"""

import json
import re
import socket
import sys
import time
from datetime import datetime

# Same as radaranprvms.py (Linux)
RADAR_PORT = '/dev/ttyAMA0'
RECEIVE_ALARM_DATA_PORT = 8090
LOG_FILE = "timing_log.txt"


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    line = f"{ts} | {msg}\n"
    print(line.strip())
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)


def extract_plate(data_json):
    try:
        vlist = data_json.get("StructureInfo", {}).get("ObjInfo", {}).get("VehicleInfoList", [])
        if vlist:
            plate = vlist[0].get("PlateAttributeInfo", {}).get("PlateNo", "")
            if plate and plate != "Unknown":
                return plate
    except (KeyError, TypeError):
        pass
    return None


def main():
    open(LOG_FILE, "w").write("")  # Clear
    log("START - recording radar + plate events. Ctrl+C to stop.")
    log("")

    try:
        import serial
        ser = serial.Serial(port=RADAR_PORT, baudrate=9600, timeout=0.1)
        has_radar = True
        log(f"Radar on {RADAR_PORT}")
    except Exception as e:
        log(f"Radar: {e} (camera only)")
        has_radar = False
        ser = None

    buffer = b""
    current_det = []
    current_dir = None

    def process_radar(direction, speed):
        nonlocal current_det, current_dir
        ts = datetime.now().isoformat()
        r = {"speed": speed, "dir": direction, "ts": ts}
        log(f"RADAR  {direction}{speed:03d}")

        if speed == 0:
            if not current_det:
                return
            current_det.append(r)
            if len(current_det) >= 3 and all(x["speed"] == 0 for x in current_det[-3:]):
                speeds = [x for x in current_det if x["speed"] > 0]
                if speeds:
                    peak = max(s["speed"] for s in speeds)
                    peak_ts = next(s["ts"] for s in reversed(speeds) if s["speed"] == peak)
                    log(f"RADAR_DONE peak={peak}km/h peak_time={peak_ts} end_time={ts}")
                current_det, current_dir = [], None
            return
        if not current_det:
            current_det, current_dir = [r], direction
        elif current_dir == direction:
            current_det.append(r)
        else:
            speeds = [x for x in current_det if x["speed"] > 0]
            if speeds:
                peak = max(s["speed"] for s in speeds)
                peak_ts = next(s["ts"] for s in reversed(speeds) if s["speed"] == peak)
                log(f"RADAR_DONE peak={peak}km/h peak_time={peak_ts} end_time={current_det[-1]['ts']}")
            current_det, current_dir = [r], direction

    def radar_loop():
        nonlocal buffer
        while True:
            try:
                data = ser.read(32)
                if data:
                    buffer += data
                    while len(buffer) >= 5:
                        chunk, buffer = buffer[:5], buffer[5:]
                        if chunk[0] == ord("A") and chunk[1] in (ord("+"), ord("-")):
                            try:
                                d = "+" if chunk[1] == ord("+") else "-"
                                s = int(chunk[2:].decode())
                                process_radar(d, s)
                            except (ValueError, UnicodeDecodeError):
                                pass
                        elif b"A" in chunk:
                            i = chunk.index(b"A")
                            buffer = chunk[i:] + buffer
                        break
            except Exception:
                pass
            time.sleep(0.1)

    def camera_loop():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.settimeout(1.0)
        server.bind(("", RECEIVE_ALARM_DATA_PORT))
        server.listen(5)
        log("Listening for camera on port " + str(RECEIVE_ALARM_DATA_PORT))
        while True:
            try:
                client, _ = server.accept()
                data = b""
                client.settimeout(5.0)
                while True:
                    t = client.recv(16384)
                    if not t:
                        break
                    data += t
                    if b"\r\n\r\n" in data:
                        break
                client.close()
                if len(data) < 50:
                    continue
                raw = data.decode("utf-8", errors="ignore")
                body = raw.split("\r\n\r\n", 1)[1] if "\r\n\r\n" in raw else raw
                body = re.sub(r"[\x00-\x1f\x7f]", "", body)
                try:
                    j = json.loads(body)
                except json.JSONDecodeError:
                    a, b = body.find("{"), body.rfind("}")
                    if a >= 0 and b > a:
                        j = json.loads(body[a : b + 1])
                    else:
                        continue
                plate = extract_plate(j)
                log(f"PLATE  {plate or '(none)'}")
            except (socket.timeout, Exception):
                pass

    import threading
    if has_radar:
        threading.Thread(target=radar_loop, daemon=True).start()
    threading.Thread(target=camera_loop, daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log("")
        log("STOP")
        print(f"\nSaved to {LOG_FILE} - share this file to tune logic.")
