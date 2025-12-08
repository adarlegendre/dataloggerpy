#!/usr/bin/env python3
"""
Simple test script to send text to VMS display
Uses the same logic as radaranprvms.py
"""

import subprocess
import os
import sys

# VMS Configuration (same as radaranprvms.py)
VMS_IP = "192.168.1.222"
VMS_PORT = 5200
VMS_WINDOW = 0
VMS_COLOR = 3
VMS_FONT_SIZE = 18
VMS_SPEED = 5
VMS_EFFECT = 1
VMS_STAY_TIME = 3
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

def find_sendcp5200_executable():
    """Find the sendcp5200 executable"""
    for path in SENDCP5200_PATHS:
        if os.path.exists(path) and os.access(path, os.X_OK):
            return path
    
    # Try which/where command
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

def send_text_to_vms(text: str):
    """Send text to VMS display"""
    executable = find_sendcp5200_executable()
    
    if not executable:
        print("ERROR: sendcp5200 executable not found!")
        print("\nTried paths:")
        for path in SENDCP5200_PATHS:
            print(f"  - {path}")
        print("\nTo build the executable:")
        print("  cd sendcp5200")
        print("  make")
        return False
    
    print(f"Using executable: {executable}")
    
    cmd = [
        executable, "0", VMS_IP, str(VMS_PORT), "2",
        str(VMS_WINDOW), text, str(VMS_COLOR),
        str(VMS_FONT_SIZE), str(VMS_SPEED), str(VMS_EFFECT),
        str(VMS_STAY_TIME), str(VMS_ALIGNMENT)
    ]
    
    print(f"\nSending command:")
    print(f"  {' '.join(cmd)}")
    print(f"\nText: '{text}'")
    print(f"VMS: {VMS_IP}:{VMS_PORT}")
    print(f"Will display for {VMS_STAY_TIME} seconds\n")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("✓ Successfully sent to VMS!")
            if result.stdout:
                print(f"Output: {result.stdout}")
            return True
        else:
            print(f"✗ Failed! Return code: {result.returncode}")
            if result.stderr:
                print(f"Error: {result.stderr}")
            if result.stdout:
                print(f"Output: {result.stdout}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def clear_vms_display():
    """Clear VMS display"""
    executable = find_sendcp5200_executable()
    if not executable:
        print("ERROR: sendcp5200 executable not found!")
        return False
    
    cmd = [
        executable, "0", VMS_IP, str(VMS_PORT), "2",
        str(VMS_WINDOW), "", "1", str(VMS_FONT_SIZE),
        str(VMS_SPEED), str(VMS_EFFECT), "10", str(VMS_ALIGNMENT)
    ]
    
    print(f"\nClearing VMS display...")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("✓ VMS cleared!")
            return True
        else:
            print(f"✗ Failed to clear. Return code: {result.returncode}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  python {sys.argv[0]} <text>")
        print(f"  python {sys.argv[0]} clear")
        print("\nExamples:")
        print(f"  python {sys.argv[0]} TEST")
        print(f"  python {sys.argv[0]} \"NOPLATE\"")
        print(f"  python {sys.argv[0]} clear")
        sys.exit(1)
    
    text = sys.argv[1]
    
    if text.lower() == "clear":
        clear_vms_display()
    else:
        send_text_to_vms(text)

