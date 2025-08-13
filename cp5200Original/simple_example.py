#!/usr/bin/env python3
"""
CP5200 Simple Example
Basic usage example for beginners

Usage: python3 simple_example.py
"""

import ctypes
import time

def main():
    """Simple example demonstrating basic CP5200 usage"""
    print("🚀 CP5200 Simple Example")
    print("=" * 40)
    
    # Step 1: Load the library
    print("1. Loading library...")
    try:
        lib = ctypes.CDLL('./libcp5200.so')
        print("✅ Library loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load library: {e}")
        print("Make sure to run build_cp5200_python.py first")
        return
    
    # Step 2: Setup function signatures
    print("\n2. Setting up functions...")
    try:
        # Basic configuration
        lib._set_cp5200_debug.argtypes = []
        lib._set_cp5200_debug.restype = None
        
        lib._set_cp5200_send_mode.argtypes = [ctypes.c_int]
        lib._set_cp5200_send_mode.restype = None
        
        lib._set_cp5200_ipcomm.argtypes = [ctypes.c_char_p, ctypes.c_int]
        lib._set_cp5200_ipcomm.restype = None
        
        # Text display
        lib.SendText.argtypes = [
            ctypes.c_int,      # window
            ctypes.c_char_p,   # text
            ctypes.c_int,      # color
            ctypes.c_int,      # font size
            ctypes.c_int,      # speed
            ctypes.c_int,      # effect
            ctypes.c_int,      # stay time
            ctypes.c_int       # alignment
        ]
        lib.SendText.restype = ctypes.c_int
        
        print("✅ Functions configured")
    except Exception as e:
        print(f"⚠ Function setup failed: {e}")
    
    # Step 3: Configure communication
    print("\n3. Configuring communication...")
    try:
        lib._set_cp5200_debug()                    # Enable debug
        lib._set_cp5200_send_mode(0)              # TCP mode
        lib._set_cp5200_ipcomm(b'192.168.1.222', 5200)  # Set IP and port
        print("✅ Communication configured")
    except Exception as e:
        print(f"❌ Communication setup failed: {e}")
        return
    
    # Step 4: Send simple text
    print("\n4. Sending text to display...")
    try:
        # Send "HELLO" in red, center aligned
        result = lib.SendText(0, b'HELLO', 0xFF0000, 16, 1, 0, 10, 2)
        
        if result == 0:
            print("✅ Text sent successfully!")
            print("Check your CP5200 display at 192.168.1.222:5200")
        else:
            print(f"⚠ Text sending returned: {result}")
            
    except Exception as e:
        print(f"❌ Text sending failed: {e}")
    
    # Step 5: Wait and send another message
    print("\n5. Waiting 5 seconds...")
    time.sleep(5)
    
    try:
        # Send "WORLD" in green, center aligned
        result = lib.SendText(0, b'WORLD', 0x00FF00, 16, 1, 0, 8, 2)
        
        if result == 0:
            print("✅ Second text sent successfully!")
        else:
            print(f"⚠ Second text sending returned: {result}")
            
    except Exception as e:
        print(f"❌ Second text sending failed: {e}")
    
    print("\n🎯 Simple example completed!")
    print("If you see text on your display, the SDK is working correctly!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Example interrupted by user")
    except Exception as e:
        print(f"\n❌ Example failed: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure CP5200 display is powered on")
        print("2. Check network connectivity to 192.168.1.222")
        print("3. Verify the library is compiled (run build_cp5200_python.py)")
        print("4. Check if port 5200 is accessible")
