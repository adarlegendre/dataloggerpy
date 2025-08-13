#!/usr/bin/env python3
"""
CP5200 Simple Diagnostic Test
Tests one function at a time to identify freezing points

Usage: python3 simple_diagnostic.py
"""

import ctypes
import time
import sys
import os

def test_library_loading():
    """Test 1: Just load the library"""
    print("🔍 Test 1: Library Loading...")
    print("=" * 40)
    
    try:
        lib = ctypes.CDLL('./libcp5200.so')
        print("✅ Library loaded successfully")
        return lib
    except Exception as e:
        print(f"❌ Failed to load library: {e}")
        return None

def test_basic_config(lib):
    """Test 2: Basic configuration only"""
    print("\n🔧 Test 2: Basic Configuration...")
    print("=" * 40)
    
    try:
        lib._set_cp5200_debug()
        print("✅ Debug mode set")
        
        lib._set_cp5200_send_mode(0)  # TCP mode
        print("✅ Send mode set to TCP")
        
        lib._set_cp5200_ipcomm(b'192.168.1.222', 5200)
        print("✅ IP communication configured")
        
        return True
    except Exception as e:
        print(f"❌ Configuration failed: {e}")
        return False

def test_single_text_send(lib):
    """Test 3: Send one simple text message"""
    print("\n📝 Test 3: Single Text Send...")
    print("=" * 40)
    
    try:
        print("Sending 'TEST' to window 0...")
        print("This may take a moment...")
        
        # Set a timeout for this operation
        result = lib.SendText(0, b'TEST', 0xFF0000, 12, 1, 0, 10, 1)
        
        print(f"✅ Text sent successfully! Result: {result}")
        return True
        
    except Exception as e:
        print(f"❌ Text sending failed: {e}")
        return False

def test_network_connectivity():
    """Test 4: Network connectivity test"""
    print("\n🌐 Test 4: Network Connectivity...")
    print("=" * 40)
    
    try:
        import subprocess
        import socket
        
        # Ping test
        print("1. Testing ping...")
        result = subprocess.run(['ping', '-c', '1', '192.168.1.222'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("   ✅ Ping successful")
        else:
            print("   ❌ Ping failed")
        
        # Port test
        print("2. Testing port 5200...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex(('192.168.1.222', 5200))
        sock.close()
        
        if result == 0:
            print("   ✅ Port 5200 accessible")
        else:
            print(f"   ❌ Port 5200 failed (error: {result})")
        
        return True
        
    except Exception as e:
        print(f"❌ Network test failed: {e}")
        return False

def main():
    """Main diagnostic function - one step at a time"""
    print("🚀 CP5200 Simple Diagnostic Test")
    print("=" * 50)
    print("Testing one step at a time to identify freezing point")
    print("=" * 50)
    
    # Test 1: Library loading
    lib = test_library_loading()
    if not lib:
        print("\n❌ Cannot proceed - library loading failed")
        return
    
    # Test 2: Basic configuration
    if not test_basic_config(lib):
        print("\n❌ Cannot proceed - configuration failed")
        return
    
    # Test 3: Network connectivity
    if not test_network_connectivity():
        print("\n❌ Network issues detected")
        return
    
    # Test 4: Single text send (this is where it froze before)
    print("\n⚠️  WARNING: About to test text sending...")
    print("If the script freezes here, we've found the problem!")
    print("Press Ctrl+C to stop if it hangs...")
    
    time.sleep(3)  # Give user time to read
    
    if test_single_text_send(lib):
        print("\n🎉 SUCCESS! Text sending works!")
    else:
        print("\n❌ Text sending failed")
    
    print("\n" + "=" * 50)
    print("🎯 DIAGNOSTIC COMPLETED")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
        print("This indicates the script was hanging/freezing")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
