#!/usr/bin/env python3
"""
Test script for Windows CP5200 DLL
This script demonstrates how to use the Windows DLL on Windows systems.
Note: This will NOT work on Raspberry Pi due to architecture differences.
"""

import ctypes
import socket
import struct
import sys
import os

def test_windows_dll():
    """Test the Windows CP5200 DLL functionality"""
    
    print("🔍 Testing Windows CP5200 DLL...")
    print("=" * 50)
    
    # Check if we're on Windows
    if os.name != 'nt':
        print("❌ This script is for Windows only!")
        print("   On Raspberry Pi, use the Python implementation instead.")
        return False
    
    # Check if DLL exists
    dll_path = './CP5200_SDK/CP5200.dll'
    if not os.path.exists(dll_path):
        print(f"❌ DLL not found at: {dll_path}")
        return False
    
    try:
        # Load the DLL
        print("📦 Loading CP5200.dll...")
        cp5200 = ctypes.CDLL(dll_path)
        print("✅ DLL loaded successfully!")
        
        # Define function signatures
        cp5200.CP5200_Net_Init.argtypes = [ctypes.c_ulong, ctypes.c_int, ctypes.c_ulong, ctypes.c_int]
        cp5200.CP5200_Net_Init.restype = ctypes.c_int
        
        cp5200.CP5200_Net_SendText.argtypes = [
            ctypes.c_int,      # nCardID
            ctypes.c_int,      # nWndNo
            ctypes.c_char_p,   # pText
            ctypes.c_ulong,    # crColor
            ctypes.c_int,      # nFontSize
            ctypes.c_int,      # nSpeed
            ctypes.c_int,      # nEffect
            ctypes.c_int,      # nStayTime
            ctypes.c_int       # nAlignment
        ]
        cp5200.CP5200_Net_SendText.restype = ctypes.c_int
        
        # Test network initialization
        print("\n🌐 Testing network initialization...")
        ip = socket.inet_aton('192.168.1.222')
        ip_int = struct.unpack('!I', ip)[0]
        
        result = cp5200.CP5200_Net_Init(ip_int, 5200, 0xFFFFFFFF, 600)
        print(f"   Network init result: {result}")
        
        if result >= 0:
            print("✅ Network initialization successful!")
            
            # Test sending text
            print("\n📝 Testing text sending...")
            text = "Hello from Windows DLL!"
            text_bytes = text.encode('ascii')
            
            result = cp5200.CP5200_Net_SendText(
                1,              # card_id
                0,              # window_no
                text_bytes,     # text
                0xFF0000,       # color (red)
                16,             # font_size
                0,              # speed
                3,              # effect (scroll)
                5,              # stay_time
                5               # alignment
            )
            print(f"   Send text result: {result}")
            
            if result >= 0:
                print("✅ Text sent successfully!")
            else:
                print("❌ Text sending failed!")
        else:
            print("❌ Network initialization failed!")
            
    except Exception as e:
        print(f"❌ DLL test failed: {e}")
        return False
    
    return True

def compare_approaches():
    """Compare Windows DLL vs Python implementation"""
    
    print("\n" + "=" * 50)
    print("🔄 COMPARISON: Windows DLL vs Python Implementation")
    print("=" * 50)
    
    print("\n📋 Windows DLL Approach:")
    print("   ✅ Uses official SDK")
    print("   ✅ Full feature support")
    print("   ✅ Optimized performance")
    print("   ❌ Windows only")
    print("   ❌ Architecture dependent")
    print("   ❌ Cannot run on Raspberry Pi")
    
    print("\n📋 Python Implementation Approach:")
    print("   ✅ Cross-platform (Windows, Linux, Raspberry Pi)")
    print("   ✅ No external dependencies")
    print("   ✅ Easy to modify and extend")
    print("   ✅ Real-time performance")
    print("   ✅ Lightweight")
    print("   ✅ Same functionality as DLL")
    print("   ❌ Manual packet building required")
    
    print("\n🎯 RECOMMENDATION:")
    print("   For Raspberry Pi: Use Python implementation")
    print("   For Windows development: Can use DLL for testing")

def main():
    """Main function"""
    
    print("🚀 CP5200 Windows DLL Test")
    print("=" * 50)
    
    # Test the DLL
    success = test_windows_dll()
    
    # Show comparison
    compare_approaches()
    
    if success:
        print("\n✅ DLL test completed successfully!")
    else:
        print("\n❌ DLL test failed!")
    
    print("\n💡 Next Steps:")
    print("   1. On Windows: Use DLL for development/testing")
    print("   2. On Raspberry Pi: Use Python implementation")
    print("   3. Transfer Python scripts to Raspberry Pi")

if __name__ == "__main__":
    main() 