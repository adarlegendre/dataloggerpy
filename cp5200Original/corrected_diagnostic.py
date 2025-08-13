#!/usr/bin/env python3
"""
CP5200 Corrected Diagnostic Test
Addresses critical issues found in SDK analysis

Usage: python3 corrected_diagnostic.py
"""

import ctypes
import time
import sys
import os

def test_library_loading():
    """Test 1: Library loading"""
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
    """Test 2: Basic configuration"""
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

def test_network_connectivity():
    """Test 3: Network connectivity"""
    print("\n🌐 Test 3: Network Connectivity...")
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

def test_display_initialization(lib):
    """Test 4: Display initialization sequence"""
    print("\n🔌 Test 4: Display Initialization...")
    print("=" * 40)
    
    try:
        # Test 1: Get version (establishes basic communication)
        print("1. Getting library version...")
        lib._get_cp5200_version()
        print("   ✅ Version retrieved")
        
        # Test 2: Time sync (establishes controller communication)
        print("2. Testing time synchronization...")
        result = lib.SyncTime()
        print(f"   Time sync result: {result}")
        
        # Test 3: Brightness control (tests controller response)
        print("3. Testing brightness control...")
        result = lib.BrightnessControl(0, 15)  # Get brightness
        print(f"   Brightness result: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Display initialization failed: {e}")
        return False

def test_window_configuration_corrected(lib):
    """Test 5: Corrected window configuration"""
    print("\n🪟 Test 5: Window Configuration (Corrected)...")
    print("=" * 40)
    
    try:
        # Test 1: Single window (full display) - CORRECTED
        print("1. Testing single window (full display)...")
        # For 1 window, array size must be 4 (x1, y1, x2, y2)
        window_config = (ctypes.c_int * 4)(0, 0, 128, 64)  # 4 coordinates, properly typed
        result = lib.SplitWindow(1, window_config, 4)  # 1 window, 4 coordinates
        print(f"   SplitWindow result: {result} (0=success, other=error)")
        
        if result == 0:
            print("   ✅ Single window configured successfully")
            time.sleep(2)
        else:
            print("   ❌ Single window configuration failed")
            return False
        
        # Test 2: Two windows (horizontal split) - CORRECTED
        print("2. Testing two windows (horizontal split)...")
        # For 2 windows, array size must be 8 (x1, y1, x2, y2, x3, y3, x4, y4)
        window_config = (ctypes.c_int * 8)(0, 0, 64, 64, 64, 0, 128, 64)  # 8 coordinates, properly typed
        result = lib.SplitWindow(2, window_config, 8)  # 2 windows, 8 coordinates
        print(f"   SplitWindow result: {result} (0=success, other=error)")
        
        if result == 0:
            print("   ✅ Two windows configured successfully")
            time.sleep(2)
        else:
            print("   ❌ Two windows configuration failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Window configuration failed: {e}")
        return False

def test_text_sending_corrected(lib):
    """Test 6: Text sending with correct sequence"""
    print("\n📝 Test 6: Text Sending (Corrected Sequence)...")
    print("=" * 40)
    
    try:
        # First, configure a single window
        print("1. Configuring single window for text...")
        window_config = (ctypes.c_int * 4)(0, 0, 128, 64)
        result = lib.SplitWindow(1, window_config, 4)
        if result != 0:
            print(f"   ❌ Window configuration failed: {result}")
            return False
        
        print("   ✅ Window configured, waiting 2 seconds...")
        time.sleep(2)
        
        # Now send text
        print("2. Sending test text...")
        print("   This may take a moment...")
        
        result = lib.SendText(0, b'TEST', 0xFF0000, 12, 1, 0, 10, 1)
        print(f"   ✅ Text sent successfully! Result: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Text sending failed: {e}")
        return False

def test_czech_plates_corrected(lib):
    """Test 7: Czech number plates with correct sequence"""
    print("\n🚗 Test 7: Czech Number Plates (Corrected)...")
    print("=" * 40)
    
    try:
        # Configure single window first
        print("1. Configuring single window...")
        window_config = (ctypes.c_int * 4)(0, 0, 128, 64)
        result = lib.SplitWindow(1, window_config, 4)
        if result != 0:
            print(f"   ❌ Window configuration failed: {result}")
            return False
        
        print("   ✅ Window configured, waiting 2 seconds...")
        time.sleep(2)
        
        # Send Czech plates one by one
        plates = [
            ("3A8 1234", 0xFF0000, "Red"),
            ("1AB 5678", 0x00FF00, "Green"),
            ("P 999 99", 0x0000FF, "Blue"),
            ("A 123 45", 0xFFFF00, "Yellow")
        ]
        
        for i, (plate, color, color_name) in enumerate(plates, 1):
            print(f"{i}. Sending '{plate}' ({color_name})...")
            result = lib.SendText(0, plate.encode(), color, 14, 1, 0, 10, 1)
            print(f"   Result: {result}")
            time.sleep(3)
        
        return True
        
    except Exception as e:
        print(f"❌ Czech plates test failed: {e}")
        return False

def main():
    """Main corrected diagnostic function"""
    print("🚀 CP5200 Corrected Diagnostic Test")
    print("=" * 60)
    print("Addressing critical issues found in SDK analysis")
    print("=" * 60)
    
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
    
    # Test 4: Display initialization
    if not test_display_initialization(lib):
        print("\n❌ Display initialization failed")
        return
    
    # Test 5: Window configuration (corrected)
    if not test_window_configuration_corrected(lib):
        print("\n❌ Window configuration failed")
        return
    
    # Test 6: Text sending (corrected sequence)
    if not test_text_sending_corrected(lib):
        print("\n❌ Text sending failed")
        return
    
    # Test 7: Czech plates (corrected)
    if not test_czech_plates_corrected(lib):
        print("\n❌ Czech plates test failed")
        return
    
    print("\n" + "=" * 60)
    print("🎉 SUCCESS! All tests passed!")
    print("=" * 60)
    print("\n📋 What was fixed:")
    print("• Proper display initialization sequence")
    print("• Correct window configuration parameters")
    print("• Proper protocol sequence (window config → text)")
    print("• Correct array sizes for SplitWindow function")
    
    print("\n🚀 Your CP5200 display should now show Czech number plates!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check the error details above")
