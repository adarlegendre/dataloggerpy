#!/usr/bin/env python3
"""
Script to check what processes are using the serial port
"""

import os
import subprocess
import sys

def check_port_usage():
    """Check what processes are using the serial port"""
    print("Checking port usage...")
    
    try:
        # On Windows, check for processes using COM ports
        if sys.platform == "win32":
            print("Windows detected - checking COM port usage...")
            try:
                result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
                lines = result.stdout.split('\n')
                com_ports = [line for line in lines if 'COM' in line or 'tty' in line]
                if com_ports:
                    print("Active COM/serial connections:")
                    for line in com_ports:
                        print(f"  {line}")
                else:
                    print("No active COM/serial connections found")
            except Exception as e:
                print(f"Could not check COM ports: {e}")
        
        # On Linux/Raspberry Pi, check for processes using tty devices
        else:
            print("Linux/Raspberry Pi detected - checking tty usage...")
            try:
                # Check if /dev/ttyAMA0 exists
                if os.path.exists('/dev/ttyAMA0'):
                    print("✅ /dev/ttyAMA0 exists")
                    
                    # Check permissions
                    stat_info = os.stat('/dev/ttyAMA0')
                    print(f"Device permissions: {oct(stat_info.st_mode)[-3:]}")
                    
                    # Check if device is accessible
                    try:
                        with open('/dev/ttyAMA0', 'rb') as f:
                            print("✅ Device is accessible for reading")
                    except PermissionError:
                        print("❌ Permission denied - you may need to run with sudo")
                    except Exception as e:
                        print(f"❌ Device access error: {e}")
                else:
                    print("❌ /dev/ttyAMA0 does not exist")
                    
                # Check for processes using tty devices
                try:
                    result = subprocess.run(['lsof', '/dev/ttyAMA0'], capture_output=True, text=True)
                    if result.stdout:
                        print("Processes using /dev/ttyAMA0:")
                        print(result.stdout)
                    else:
                        print("No processes currently using /dev/ttyAMA0")
                except FileNotFoundError:
                    print("lsof not available - cannot check process usage")
                except Exception as e:
                    print(f"Could not check process usage: {e}")
                    
            except Exception as e:
                print(f"Error checking device: {e}")
    
    except Exception as e:
        print(f"Error checking port usage: {e}")

def main():
    print("Serial Port Usage Checker")
    print("========================")
    print()
    
    check_port_usage()
    
    print("\nTroubleshooting tips:")
    print("1. Make sure no other Python scripts are running that access the serial port")
    print("2. If on Raspberry Pi, you may need to run Django with sudo")
    print("3. Check if the radar device is properly connected")
    print("4. Try running the test_port_access.py script first")

if __name__ == "__main__":
    main()
