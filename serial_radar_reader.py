#!/usr/bin/env python3
"""
Raw Serial Radar Reader
Reads raw data from radar serial port every 0.2 seconds. No processing.
"""

import serial
import time

PORT = '/dev/ttyAMA0'
BAUDRATE = 9600
READ_INTERVAL = 0.2


def main():
    print("Raw radar reader - no processing. Ctrl+C to stop.")
    try:
        ser = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=0.1)
        print(f"Connected to {PORT}")
    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        while True:
            data = ser.read(32)
            if data:
                print(data)
            time.sleep(READ_INTERVAL)
    except KeyboardInterrupt:
        print("\nStopped")
    finally:
        ser.close()


if __name__ == "__main__":
    main()
