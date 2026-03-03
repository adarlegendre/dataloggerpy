#!/usr/bin/env python3
"""
Raw Serial Radar Reader
Reads from radar every 0.2s. Displays + and - in two columns.
"""

import serial
import time
from datetime import datetime

PORT = '/dev/ttyAMA0'
BAUDRATE = 9600
READ_INTERVAL = 0.2
COLLAPSE_IDENTICAL = True
COL_WIDTH = 38


def fmt(raw, count):
    s = f"{raw} {int(raw[2:])} km/h"
    return f"{s} (x{count})" if count > 1 else s


def main():
    print("Radar reader - two columns. Ctrl+C to stop.\n")
    try:
        ser = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=0.1)
        print(f"Connected to {PORT}\n")
    except Exception as e:
        print(f"Error: {e}")
        return

    header = f"  {'+ (→)':<{COL_WIDTH}}  |  {'- (←)':<{COL_WIDTH}}  "
    print(header)
    print("  " + "-" * COL_WIDTH + "  |  " + "-" * COL_WIDTH)

    buffer = b""
    last_plus, count_plus = None, 0
    last_minus, count_minus = None, 0

    def flush_plus():
        nonlocal last_plus, count_plus
        if last_plus is not None:
            ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            left = f"{ts} {fmt(last_plus, count_plus)}"
            print(f"  {left:<{COL_WIDTH}}  |  {'':<{COL_WIDTH}}  ")
            last_plus, count_plus = None, 0

    def flush_minus():
        nonlocal last_minus, count_minus
        if last_minus is not None:
            ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            right = f"{ts} {fmt(last_minus, count_minus)}"
            print(f"  {'':<{COL_WIDTH}}  |  {right:<{COL_WIDTH}}  ")
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
        print("\nStopped")
    finally:
        ser.close()


if __name__ == "__main__":
    main()
