#!/usr/bin/env python3
"""
CP5200 Diagnostic Test Script
Tests different parameters and configurations to troubleshoot display issues

Usage: python3 diagnostic_test.py
"""

import ctypes
import time
import sys
import os

def test_basic_connectivity():
    """Test basic library loading and network connectivity"""
    print("🔍 Testing Basic Connectivity...")
    print("=" * 50)
    
    try:
        # Load library
        lib = ctypes.CDLL('./libcp5200.so')
        print("✅ Library loaded successfully")
        
        # Setup basic configuration
        lib._set_cp5200_debug()
        lib._set_cp5200_send_mode(0)  # TCP mode
        lib._set_cp5200_ipcomm(b'192.168.1.222', 5200)
        print("✅ Basic configuration set")
        
        return lib
        
    except Exception as e:
        print(f"❌ Failed to load library: {e}")
        return None

def test_simple_text(lib):
    """Test sending simple text without window splitting"""
    print("\n📝 Testing Simple Text (No Window Split)...")
    print("=" * 50)
    
    try:
        # Test 1: Simple text to window 0
        print("1. Sending 'HELLO' to window 0 (red, small font)...")
        result = lib.SendText(0, b'HELLO', 0xFF0000, 10, 1, 0, 30, 1)
        print(f"   Result: {result} (0=success, other=error)")
        
        time.sleep(3)
        
        # Test 2: Different effect
        #print("2. Sending 'SCROLL' with scroll effect (green)...")
        #result = lib.SendText(0, b'SCROLL', 0x00FF00, 12, 1, 1, 25, 1)
        #print(f"   Result: {result} (0=success, other=error)")
        
        #time.sleep(3)
        
        # Test 3: Different window
        print("3. Sending 'WINDOW1' to window 1 (blue)...")
        result = lib.SendText(1, b'WINDOW1', 0x0000FF, 12, 1, 0, 20, 1)
        print(f"   Result: {result} (0=success, other=error)")
        
        time.sleep(3)
        
        return True
        
    except Exception as e:
        print(f"❌ Text sending failed: {e}")
        return False

def test_window_configuration(lib):
    """Test different window configurations"""
    print("\n🪟 Testing Window Configurations...")
    print("=" * 50)
    
    try:
        # Test 1: Single window covering entire display
        print("1. Testing single window (full display)...")
        window_config = [0, 0, 128, 64]  # x1, y1, x2, y2
        result = lib.SplitWindow(1, window_config, 4)
        print(f"   SplitWindow result: {result} (0=success, other=error)")
        
        if result == 0:
            print("   ✅ Single window configured successfully")
            # Send test text
            lib.SendText(0, b'SINGLE', 0xFFFF00, 14, 1, 0, 15, 1)
            time.sleep(3)
        else:
            print("   ❌ Single window configuration failed")
        
        # Test 2: Two windows (horizontal split)
        print("2. Testing two windows (horizontal split)...")
        window_config = [0, 0, 64, 64, 64, 0, 128, 64]  # 2 windows
        result = lib.SplitWindow(2, window_config, 8)
        print(f"   SplitWindow result: {result} (0=success, other=error)")
        
        if result == 0:
            print("   ✅ Two windows configured successfully")
            # Send test text to both windows
            lib.SendText(0, b'LEFT', 0xFF0000, 12, 1, 0, 10, 1)
            time.sleep(2)
            lib.SendText(1, b'RIGHT', 0x00FF00, 12, 1, 0, 10, 1)
            time.sleep(3)
        else:
            print("   ❌ Two windows configuration failed")
        
        return True
        
    except Exception as e:
        print(f"❌ Window configuration failed: {e}")
        return False

def test_different_parameters(lib):
    """Test different text parameters"""
    print("\n⚙️ Testing Different Parameters...")
    print("=" * 50)
    
    try:
        # Test different font sizes
        print("1. Testing different font sizes...")
        font_sizes = [10, 12, 14, 16]
        for size in font_sizes:
            print(f"   Font size {size}: ", end="")
            result = lib.SendText(0, f'FONT{size}'.encode(), 0xFF00FF, size, 1, 0, 8, 1)
            print(f"Result {result}")
            time.sleep(2)
        
        # Test different effects
        print("2. Testing different effects...")
        effects = [(0, "Static"), (1, "Scroll"), (2, "Blink")]
        for effect_code, effect_name in effects:
            print(f"   Effect {effect_code} ({effect_name}): ", end="")
            result = lib.SendText(0, effect_name.encode(), 0x00FFFF, 12, 1, effect_code, 8, 1)
            print(f"Result {result}")
            time.sleep(2)
        
        # Test different speeds
        print("3. Testing different speeds...")
        speeds = [1, 3, 5, 7]
        for speed in speeds:
            print(f"   Speed {speed}: ", end="")
            result = lib.SendText(0, f'SPEED{speed}'.encode(), 0xFFFF00, 12, speed, 1, 6, 1)
            print(f"Result {result}")
            time.sleep(2)
        
        return True
        
    except Exception as e:
        print(f"❌ Parameter testing failed: {e}")
        return False

def test_czech_plates_simple(lib):
    """Test Czech number plates with simple configuration"""
    print("\n🚗 Testing Czech Number Plates (Simple)...")
    print("=" * 50)
    
    try:
        # Configure single window first
        print("1. Configuring single window...")
        window_config = [0, 0, 128, 64]
        lib.SplitWindow(1, window_config, 4)
        
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

def test_network_connectivity():
    """Test network connectivity to the display"""
    print("\n🌐 Testing Network Connectivity...")
    print("=" * 50)
    
    try:
        import subprocess
        import socket
        
        # Test 1: Ping test
        print("1. Testing ping to 192.168.1.222...")
        result = subprocess.run(['ping', '-c', '1', '192.168.1.222'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("   ✅ Ping successful")
        else:
            print("   ❌ Ping failed")
            print(f"   Error: {result.stderr}")
        
        # Test 2: Port connectivity
        print("2. Testing port 5200 connectivity...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex(('192.168.1.222', 5200))
        sock.close()
        
        if result == 0:
            print("   ✅ Port 5200 is open and accessible")
        else:
            print(f"   ❌ Port 5200 connection failed (error code: {result})")
        
        return True
        
    except Exception as e:
        print(f"❌ Network test failed: {e}")
        return False

def main():
    """Main diagnostic function"""
    print("🚀 CP5200 Display Diagnostic Test")
    print("=" * 60)
    print("This script will test various configurations to identify display issues")
    print("Target: 192.168.1.222:5200")
    print("=" * 60)
    
    # Test 1: Basic connectivity
    lib = test_basic_connectivity()
    if not lib:
        print("\n❌ Basic connectivity failed. Cannot proceed.")
        return
    
    # Test 2: Network connectivity
    test_network_connectivity()
    
    # Test 3: Simple text (no window split)
    if test_simple_text(lib):
        print("\n✅ Simple text test completed")
    else:
        print("\n❌ Simple text test failed")
    
    # Test 4: Window configuration
    if test_window_configuration(lib):
        print("\n✅ Window configuration test completed")
    else:
        print("\n❌ Window configuration test failed")
    
    # Test 5: Different parameters
    if test_different_parameters(lib):
        print("\n✅ Parameter testing completed")
    else:
        print("\n❌ Parameter testing failed")
    
    # Test 6: Czech plates with simple config
    if test_czech_plates_simple(lib):
        print("\n✅ Czech plates test completed")
    else:
        print("\n❌ Czech plates test failed")
    
    # Final summary
    print("\n" + "=" * 60)
    print("🎯 DIAGNOSTIC TEST COMPLETED")
    print("=" * 60)
    print("\n📋 Summary:")
    print("• Check if any text appeared on your display")
    print("• Note which tests passed/failed")
    print("• Look for error codes in the results")
    print("\n🔧 Common Issues:")
    print("• Display not powered on")
    print("• Wrong IP address or port")
    print("• Display in wrong mode")
    print("• Invalid window configuration")
    print("• Unsupported parameters")
    print("\n💡 Next Steps:")
    print("• If no text appears, check display power and network")
    print("• If some tests fail, note the error codes")
    print("• Try different window configurations")
    print("• Check display manual for supported parameters")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check the error details above")
