#!/usr/bin/env python3
"""
CP5200 Timeout Test Script
Tests with timeouts to identify hanging operations

Usage: python3 timeout_test.py
"""

import ctypes
import time
import sys
import os
import signal
import threading

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

def run_with_timeout(func, timeout_seconds=10):
    """Run a function with a timeout"""
    def target():
        try:
            result = func()
            return result
        except Exception as e:
            return e
    
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()
    thread.join(timeout_seconds)
    
    if thread.is_alive():
        return TimeoutError(f"Function timed out after {timeout_seconds} seconds")
    
    return thread.result if hasattr(thread, 'result') else None

def test_library_loading():
    """Test library loading with timeout"""
    print("🔍 Testing Library Loading...")
    print("=" * 40)
    
    def load_lib():
        return ctypes.CDLL('./libcp5200.so')
    
    result = run_with_timeout(load_lib, 5)
    
    if isinstance(result, TimeoutError):
        print(f"❌ Library loading timed out: {result}")
        return None
    elif isinstance(result, Exception):
        print(f"❌ Library loading failed: {result}")
        return None
    else:
        print("✅ Library loaded successfully")
        return result

def test_basic_config(lib):
    """Test basic configuration with timeout"""
    print("\n🔧 Testing Basic Configuration...")
    print("=" * 40)
    
    def config_lib():
        lib._set_cp5200_debug()
        lib._set_cp5200_send_mode(0)
        lib._set_cp5200_ipcomm(b'192.168.1.222', 5200)
        return True
    
    result = run_with_timeout(config_lib, 5)
    
    if isinstance(result, TimeoutError):
        print(f"❌ Configuration timed out: {result}")
        return False
    elif isinstance(result, Exception):
        print(f"❌ Configuration failed: {result}")
        return False
    else:
        print("✅ Configuration completed successfully")
        return True

def test_single_text_send(lib):
    """Test single text send with timeout"""
    print("\n📝 Testing Single Text Send...")
    print("=" * 40)
    
    def send_text():
        return lib.SendText(0, b'TEST', 0xFF0000, 12, 1, 0, 10, 1)
    
    print("Sending 'TEST' to window 0...")
    print("Setting 15 second timeout...")
    
    result = run_with_timeout(send_text, 15)
    
    if isinstance(result, TimeoutError):
        print(f"❌ Text sending timed out: {result}")
        print("This indicates the socket receive operation is hanging!")
        return False
    elif isinstance(result, Exception):
        print(f"❌ Text sending failed: {result}")
        return False
    else:
        print(f"✅ Text sent successfully! Result: {result}")
        return True

def test_network_connectivity():
    """Test network connectivity"""
    print("\n🌐 Testing Network Connectivity...")
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
    """Main timeout test function"""
    print("🚀 CP5200 Timeout Test")
    print("=" * 50)
    print("Testing with timeouts to identify hanging operations")
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
    print("\n⚠️  WARNING: About to test text sending with timeout...")
    print("If this times out, we've identified the hanging operation!")
    
    time.sleep(3)  # Give user time to read
    
    if test_single_text_send(lib):
        print("\n🎉 SUCCESS! Text sending works!")
    else:
        print("\n❌ Text sending failed or timed out")
    
    print("\n" + "=" * 50)
    print("🎯 TIMEOUT TEST COMPLETED")
    print("=" * 50)
    
    print("\n📋 Analysis:")
    print("• If text sending timed out: Socket receive operation is hanging")
    print("• If text sending failed: Parameter or configuration issue")
    print("• If text sending succeeded: The issue was temporary")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
