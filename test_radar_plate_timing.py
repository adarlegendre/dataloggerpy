#!/usr/bin/env python3
"""
Dumb logger: radar + camera events to a file.
Same connections as radaranprvms.py. Run on Pi, Ctrl+C to stop, share the file.

  python3 -u test_radar_plate_timing.py

Output: timing_log.txt
"""

import sys
import json
import re
import socket
import time
import threading
from datetime import datetime

# Same as radaranprvms.py
ONLY_NEGATIVE_DIRECTION = True  # True = only log negative (A-) radar
RADAR_PORT = '/dev/ttyAMA0'
RADAR_BAUDRATE = 9600
RECEIVE_ALARM_DATA_PORT = 8090
LOG_FILE = "timing_log.txt"
CAMERA_IP = '192.168.2.13'
CAMERA_PORT = 80
RECEIVE_ALARM_DATA_IP = "192.168.2.101"
CAMERA_USERNAME = 'admin'
CAMERA_PASSWORD = 'kObliha12@'
DURATION = 300
CAMERA_URL = f'http://{CAMERA_IP}:{CAMERA_PORT}/LAPI/V1.0/System/Event/Subscription'


def out(msg):
    """Print to console (stderr = unbuffered)"""
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()

def write(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    line = f"{ts} | {msg}\n"
    out(line.strip())
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)


def plate_from_json(j):
    try:
        v = j.get("StructureInfo", {}).get("ObjInfo", {}).get("VehicleInfoList", [])
        if v:
            p = v[0].get("PlateAttributeInfo", {}).get("PlateNo", "")
            if p and p != "Unknown":
                return p
    except (KeyError, TypeError):
        pass
    return None


def main():
    out("Starting...")
    open(LOG_FILE, "w").write("")
    write("START")
    write("")

    # Radar - same as radaranprvms
    try:
        import serial
        out("Opening radar...")
        ser = serial.Serial(port=RADAR_PORT, baudrate=RADAR_BAUDRATE, timeout=0.1)
        has_radar = True
        write(f"radar ok {RADAR_PORT}")
    except Exception as e:
        out(f"Radar: {e}")
        write(f"radar fail {e}")
        has_radar = False
        ser = None

    # Camera - bind first, then subscribe (same as radaranprvms)
    out("Binding camera port...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.settimeout(1.0)
    server.bind(("", RECEIVE_ALARM_DATA_PORT))
    server.listen(99)
    write(f"camera listen {RECEIVE_ALARM_DATA_PORT}")

    # Subscribe to camera so it sends plate events here
    out("Subscribing to camera...")
    try:
        from requests.auth import HTTPDigestAuth
        import requests
        sub_data = {
            "AddressType": 0,
            "IPAddress": RECEIVE_ALARM_DATA_IP,
            "Port": RECEIVE_ALARM_DATA_PORT,
            "Duration": DURATION
        }
        headers = {"Content-Type": "application/json", "Host": f"{CAMERA_IP}:{CAMERA_PORT}", "Connection": "Close"}
        r = requests.post(CAMERA_URL, headers=headers, data=json.dumps(sub_data),
                         auth=HTTPDigestAuth(CAMERA_USERNAME, CAMERA_PASSWORD), timeout=5)
        if r.status_code == 200:
            sub_id = r.json()["Response"]["Data"]["ID"]
            write("camera subscribed")
            out(f"Subscribed (ID: {sub_id})")

            def keepalive():
                while True:
                    try:
                        requests.put(f"{CAMERA_URL}/{sub_id}", headers=headers, data=json.dumps({"Duration": DURATION}),
                                    auth=HTTPDigestAuth(CAMERA_USERNAME, CAMERA_PASSWORD), timeout=5)
                    except Exception:
                        pass
                    time.sleep(DURATION / 2)

            threading.Thread(target=keepalive, daemon=True).start()
        else:
            out(f"Subscribe failed: {r.status_code}")
            write("camera subscribe failed")
    except Exception as e:
        out(f"Subscribe error: {e}")
        write(f"camera subscribe error {e}")
    write("")

    buf = b""
    cur, cur_dir = [], None

    def on_radar(d, s):
        nonlocal cur, cur_dir
        ts = datetime.now().isoformat()
        r = {"speed": s, "dir": d, "ts": ts}
        write(f"radar {d}{s:03d}")

        if s == 0:
            if not cur:
                return
            cur.append(r)
            if len(cur) >= 3 and all(x["speed"] == 0 for x in cur[-3:]):
                sp = [x for x in cur if x["speed"] > 0]
                if sp:
                    pk = max(x["speed"] for x in sp)
                    pk_ts = next(x["ts"] for x in reversed(sp) if x["speed"] == pk)
                    write(f"radar_done peak={pk} peak_ts={pk_ts} end_ts={ts}")
                cur, cur_dir = [], None
            return
        if not cur:
            cur, cur_dir = [r], d
        elif cur_dir == d:
            cur.append(r)
        else:
            sp = [x for x in cur if x["speed"] > 0]
            if sp:
                pk = max(x["speed"] for x in sp)
                pk_ts = next(x["ts"] for x in reversed(sp) if x["speed"] == pk)
                write(f"radar_done peak={pk} peak_ts={pk_ts} end_ts={cur[-1]['ts']}")
            cur, cur_dir = [r], d

    def radar_loop():
        nonlocal buf
        while True:
            try:
                d = ser.read(32)
                if d:
                    buf += d
                    while len(buf) >= 5:
                        ch, buf = buf[:5], buf[5:]
                        if ch[0] == ord("A") and ch[1] in (ord("+"), ord("-")):
                            try:
                                dd = "+" if ch[1] == ord("+") else "-"
                                ss = int(ch[2:].decode())
                                if ONLY_NEGATIVE_DIRECTION and ss > 0 and dd != "-":
                                    pass  # skip positive speed readings
                                else:
                                    on_radar(dd, ss)
                            except (ValueError, UnicodeDecodeError):
                                pass
                        elif b"A" in ch:
                            buf = ch[ch.index(b"A"):] + buf
                        break
            except Exception:
                pass
            time.sleep(0.1)

    def camera_loop():
        while True:
            try:
                client, _ = server.accept()
                data = b""
                client.settimeout(10.0)
                for _ in range(100):
                    t = client.recv(16384)
                    if not t:
                        break
                    data += t
                    if b"\r\n\r\n" in data and len(data) > 100:
                        raw = data.decode("utf-8", errors="ignore")
                        hdr_end = raw.find("\r\n\r\n")
                        if hdr_end > 0:
                            m = re.search(r"Content-Length:\s*(\d+)", raw[:hdr_end], re.I)
                            if m and len(data) - hdr_end - 4 >= int(m.group(1)):
                                break
                client.close()
                if len(data) < 50:
                    continue
                write(f"camera_event {len(data)} bytes")
                raw = data.decode("utf-8", errors="ignore")
                body = raw.split("\r\n\r\n", 1)[1] if "\r\n\r\n" in raw else raw
                body = re.sub(r"[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]", "", body)
                try:
                    j = json.loads(body)
                except json.JSONDecodeError:
                    a, b = body.find("{"), body.rfind("}")
                    if a >= 0 and b > a:
                        j = json.loads(body[a : b + 1])
                    else:
                        continue
                plate = plate_from_json(j)
                write(f"plate {plate or '(none)'}")
            except socket.timeout:
                pass
            except Exception:
                pass

    if has_radar:
        threading.Thread(target=radar_loop, daemon=True).start()
    threading.Thread(target=camera_loop, daemon=True).start()
    out("Running. Ctrl+C to stop.")

    try:
        last_beat = time.time()
        while True:
            time.sleep(1)
            if time.time() - last_beat >= 10:
                out(f"... {datetime.now().strftime('%H:%M:%S')} still waiting")
                last_beat = time.time()
    except KeyboardInterrupt:
        write("")
        write("STOP")
        out(f"Saved to {LOG_FILE}")


if __name__ == "__main__":
    try:
        sys.stderr.write("test_radar_plate_timing starting\n")
        sys.stderr.flush()
        main()
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.stderr.flush()
        raise
