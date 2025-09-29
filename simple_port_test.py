#!/usr/bin/env python3
"""
Simple port test to debug the connection issue
"""

import serial
import time
import os

def test_port_step_by_step():
    """Test port connection step by step"""
    print("=== Simple Port Test ===")
    
    # Step 1: Check if port exists
    print("Step 1: Checking if port exists...")
    if os.path.exists('/dev/ttyAMA0'):
        print("✅ /dev/ttyAMA0 exists")
    else:
        print("❌ /dev/ttyAMA0 does not exist")
        return False
    
    # Step 2: Check permissions
    print("\nStep 2: Checking permissions...")
    try:
        stat_info = os.stat('/dev/ttyAMA0')
        print(f"Permissions: {oct(stat_info.st_mode)[-3:]}")
        print("✅ Can access device file")
    except Exception as e:
        print(f"❌ Cannot access device file: {e}")
        return False
    
    # Step 3: Try to open port
    print("\nStep 3: Trying to open port...")
    try:
        ser = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=0.01)
        print("✅ Port opened successfully")
        print(f"Port details: {ser}")
    except Exception as e:
        print(f"❌ Failed to open port: {e}")
        print(f"Error type: {type(e)}")
        return False
    
    # Step 4: Try to read
    print("\nStep 4: Trying to read data...")
    try:
        data = ser.read(32)
        if data:
            print(f"✅ Read successful: {len(data)} bytes")
            print(f"Data: {data}")
        else:
            print("⚠️ No data read (but port opened)")
    except Exception as e:
        print(f"❌ Read failed: {e}")
        ser.close()
        return False
    
    # Step 5: Close port
    print("\nStep 5: Closing port...")
    try:
        ser.close()
        print("✅ Port closed successfully")
    except Exception as e:
        print(f"❌ Failed to close port: {e}")
        return False
    
    print("\n✅ All tests passed! Port should work with Django.")
    return True

def test_django_style_connection():
    """Test connection exactly like Django does"""
    print("\n=== Django-Style Connection Test ===")
    
    try:
        print("Testing Django-style connection...")
        
        # Add the 2-second delay like Django
        print("Waiting 2 seconds (like Django)...")
        time.sleep(2)
        
        # Use the exact same parameters as Django
        with serial.Serial(
            port='/dev/ttyAMA0',
            baudrate=9600,
            timeout=0.01
        ) as ser:
            print("✅ Django-style connection successful")
            
            # Test reading like Django does
            print("Testing Django-style reading...")
            for i in range(3):
                data = ser.read(32)
                if data:
                    print(f"  Read {len(data)} bytes")
                else:
                    print(f"  No data (attempt {i+1})")
                time.sleep(0.1)
        
        print("✅ Django-style test completed successfully")
        return True
        
    except Exception as e:
        print(f"❌ Django-style test failed: {e}")
        return False

def main():
    print("Port Connection Debugger")
    print("=======================")
    print()
    
    # Test 1: Basic port test
    basic_success = test_port_step_by_step()
    
    if basic_success:
        # Test 2: Django-style test
        django_success = test_django_style_connection()
        
        if django_success:
            print("\n🎉 All tests passed! Django should work now.")
        else:
            print("\n❌ Django-style test failed. There might be a timing issue.")
    else:
        print("\n❌ Basic port test failed. Check hardware connection.")

if __name__ == "__main__":
    main()
