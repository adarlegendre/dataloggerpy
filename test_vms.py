#!/usr/bin/env python3
"""
Simple test script to send text to VMS display
Uses the same logic as radaranprvms.py
"""

import subprocess
import os
import sys
import time

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

def send_text_to_vms(text: str, window=None, stay_time=None):
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
    
    # Use provided window or default
    if window is None:
        window = VMS_WINDOW
    
    # Use provided stay_time or default
    if stay_time is None:
        stay_time = VMS_STAY_TIME
    
    print(f"Using executable: {executable}")
    
    cmd = [
        executable, "0", VMS_IP, str(VMS_PORT), "2",
        str(window), text, str(VMS_COLOR),
        str(VMS_FONT_SIZE), str(VMS_SPEED), str(VMS_EFFECT),
        str(stay_time), str(VMS_ALIGNMENT)
    ]
    
    print(f"\nSending command:")
    print(f"  {' '.join(cmd)}")
    print(f"\nEquivalent shell command:")
    print(f"  {executable} 0 {VMS_IP} {VMS_PORT} 2 {window} \"{text}\" {VMS_COLOR} {VMS_FONT_SIZE} {VMS_SPEED} {VMS_EFFECT} {stay_time} {VMS_ALIGNMENT}")
    print(f"\nText: '{text}'")
    print(f"VMS: {VMS_IP}:{VMS_PORT}")
    print(f"Window: {window} | Color: {VMS_COLOR} | Font: {VMS_FONT_SIZE} | Speed: {VMS_SPEED} | Effect: {VMS_EFFECT} | Stay: {stay_time}s | Align: {VMS_ALIGNMENT}")
    print()
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("✓ Successfully sent to VMS!")
            if result.stdout:
                print(f"Output: {result.stdout.strip()}")
            return True
        else:
            print(f"✗ Failed! Return code: {result.returncode}")
            if result.stderr:
                print(f"Error: {result.stderr.strip()}")
            if result.stdout:
                print(f"Output: {result.stdout.strip()}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_all_windows(text="TEST", stay_time=10):
    """Test all windows 0, 1, 2 with the same text"""
    print("=" * 70)
    print("TESTING ALL WINDOWS (0, 1, 2)")
    print("=" * 70)
    print(f"Text: '{text}' | Stay time: {stay_time}s")
    print("=" * 70 + "\n")
    
    results = {}
    
    for window in [0, 1, 2]:
        print(f"\n{'='*70}")
        print(f"TESTING WINDOW {window}")
        print(f"{'='*70}")
        success = send_text_to_vms(text, window=window, stay_time=stay_time)
        results[window] = success
        
        if success:
            print(f"✓ Window {window}: SUCCESS - Check VMS display!")
        else:
            print(f"✗ Window {window}: FAILED")
        
        # Wait a bit between tests
        if window < 2:  # Don't wait after last test
            print(f"\nWaiting 3 seconds before next test...")
            time.sleep(3)
    
    # Summary
    print(f"\n{'='*70}")
    print("TEST SUMMARY")
    print(f"{'='*70}")
    for window, success in results.items():
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"Window {window}: {status}")
    print(f"{'='*70}\n")
    
    return results

def clear_vms_display(window=None):
    """Clear VMS display"""
    executable = find_sendcp5200_executable()
    if not executable:
        print("ERROR: sendcp5200 executable not found!")
        return False
    
    if window is None:
        window = VMS_WINDOW
    
    cmd = [
        executable, "0", VMS_IP, str(VMS_PORT), "2",
        str(window), "", "1", str(VMS_FONT_SIZE),
        str(VMS_SPEED), str(VMS_EFFECT), "10", str(VMS_ALIGNMENT)
    ]
    
    print(f"\nClearing VMS display (window {window})...")
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
        print(f"  python {sys.argv[0]} <text> [stay_time] [window]")
        print(f"  python {sys.argv[0]} clear [window]")
        print(f"  python {sys.argv[0]} test")
        print(f"  python {sys.argv[0]} testall [text] [stay_time]")
        print("\nExamples:")
        print(f"  python {sys.argv[0]} TEST")
        print(f"  python {sys.argv[0]} \"NOPLATE\" 10")
        print(f"  python {sys.argv[0]} \"NOPLATE\" 10 1  # Window 1")
        print(f"  python {sys.argv[0]} \"zeph dusan\" 10  # Match working example")
        print(f"  python {sys.argv[0]} clear")
        print(f"  python {sys.argv[0]} test  # Test with working parameters")
        print(f"  python {sys.argv[0]} testall  # Test windows 0, 1, 2")
        print(f"  python {sys.argv[0]} testall \"NOPLATE\" 10  # Test all windows with custom text")
        sys.exit(1)
    
    text = sys.argv[1]
    
    if text.lower() == "clear":
        window = int(sys.argv[2]) if len(sys.argv) > 2 else None
        clear_vms_display(window)
    elif text.lower() == "test":
        # Test with exact working parameters from README
        print("Testing with exact working command format...")
        send_text_to_vms("zeph dusan", window=0, stay_time=10)
    elif text.lower() == "testall":
        # Test all windows 0, 1, 2
        test_text = sys.argv[2] if len(sys.argv) > 2 else "TEST"
        test_stay = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        test_all_windows(test_text, test_stay)
    else:
        # Optional stay_time and window parameters
        stay_time = int(sys.argv[2]) if len(sys.argv) > 2 else None
        window = int(sys.argv[3]) if len(sys.argv) > 3 else None
        send_text_to_vms(text, window=window, stay_time=stay_time)

