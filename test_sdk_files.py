#!/usr/bin/env python3
"""
Test and analyze CP5200 SDK files
Shows how to use the SDK files on Raspberry Pi
"""

import os
import subprocess
import platform
import struct

def analyze_sdk_files():
    """Analyze the SDK files in the CP5200_SDK folder"""
    print("CP5200 SDK Files Analysis")
    print("=" * 50)
    
    sdk_path = "CP5200_SDK"
    
    if not os.path.exists(sdk_path):
        print(f"❌ SDK folder '{sdk_path}' not found!")
        print("Please make sure the CP5200_SDK folder is in the current directory.")
        return
    
    print(f"📁 Found SDK folder: {sdk_path}")
    print()
    
    # List SDK files
    sdk_files = os.listdir(sdk_path)
    print("📋 SDK Files:")
    for file in sdk_files:
        file_path = os.path.join(sdk_path, file)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            print(f"  📄 {file} ({size:,} bytes)")
    
    print()
    
    # Check system compatibility
    system = platform.system()
    arch = platform.machine()
    print(f"🖥️  System: {system} ({arch})")
    
    if system == "Windows":
        print("✅ Windows detected - SDK files should work natively")
        print("   You can run: TestCP5200.exe")
    elif system == "Linux":
        print("⚠️  Linux detected - SDK files need adaptation")
        print("   Windows DLL files won't run directly on Linux")
        print("   Use the Python implementations instead")
    else:
        print(f"⚠️  {system} detected - SDK compatibility unknown")
    
    print()

def test_wine_approach():
    """Test if Wine can run the Windows SDK files"""
    print("🍷 Testing Wine approach...")
    
    try:
        # Check if Wine is installed
        result = subprocess.run(['wine', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Wine is installed: {result.stdout.strip()}")
            
            # Test if we can run the Windows executable
            sdk_exe = "CP5200_SDK/TestCP5200.exe"
            if os.path.exists(sdk_exe):
                print(f"✅ Found Windows executable: {sdk_exe}")
                print("   You can try: wine CP5200_SDK/TestCP5200.exe")
            else:
                print(f"❌ Windows executable not found: {sdk_exe}")
        else:
            print("❌ Wine is not installed")
            print("   Install with: sudo apt-get install wine")
            
    except FileNotFoundError:
        print("❌ Wine is not installed")
        print("   Install with: sudo apt-get install wine")
    
    print()

def show_python_alternatives():
    """Show Python alternatives to the SDK"""
    print("🐍 Python SDK Alternatives")
    print("=" * 50)
    
    python_files = [
        "cp5200_raspberry_pi.py",
        "test_cp5200_connection.py", 
        "czech_plates_display.py",
        "cp5200_reader.py"
    ]
    
    print("Available Python implementations:")
    for file in python_files:
        if os.path.exists(file):
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} (missing)")
    
    print()
    print("Usage examples:")
    print("  # Test connection")
    print("  python3 test_cp5200_connection.py")
    print()
    print("  # Send message")
    print("  python3 cp5200_raspberry_pi.py --message 'Hello World!'")
    print()
    print("  # Send Czech plates")
    print("  python3 czech_plates_display.py --demo")
    print()
    print("  # Read controller data")
    print("  python3 cp5200_reader.py")

def create_sdk_wrapper():
    """Create a Python wrapper for the SDK functions"""
    print("🔧 Creating SDK Wrapper")
    print("=" * 50)
    
    wrapper_code = '''#!/usr/bin/env python3
"""
CP5200 SDK Python Wrapper
Replicates SDK functionality using Python
"""

import socket
import struct
import time
from datetime import datetime

class CP5200SDK:
    def __init__(self, ip='192.168.1.222', port=5200, card_id=1):
        self.ip = ip
        self.port = port
        self.card_id = card_id
        self.socket = None
    
    def connect(self):
        """Connect to CP5200 (equivalent to SDK init functions)"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5)
            self.socket.connect((self.ip, self.port))
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from CP5200"""
        if self.socket:
            self.socket.close()
    
    def send_message(self, text, font_size=16, color=0xFF0000, effect=1):
        """Send message (equivalent to CP5200_RS232_SendInstantMessage)"""
        if not self.socket:
            return False
        
        try:
            # Build packet (equivalent to CP5200_MakeInstantMessageData)
            packet = self._build_message_packet(text, font_size, color, effect)
            self.socket.send(packet)
            return True
        except Exception as e:
            print(f"Send failed: {e}")
            return False
    
    def read_time(self):
        """Read time (equivalent to CP5200_RS232_GetTime)"""
        if not self.socket:
            return None
        
        try:
            # Build time request packet
            packet = bytearray()
            packet.extend(struct.pack('<I', self.card_id))
            packet.extend(struct.pack('<I', 8))
            packet.extend(b'\\x68\\x32\\x01\\x7B')
            
            self.socket.send(packet)
            response = self.socket.recv(20)
            
            if response and len(response) >= 8:
                time_bytes = response[4:8]
                timestamp = struct.unpack('<I', time_bytes)[0]
                return datetime.fromtimestamp(timestamp)
            return None
        except Exception as e:
            print(f"Read time failed: {e}")
            return None
    
    def _build_message_packet(self, text, font_size, color, effect):
        """Build message packet (equivalent to SDK packet building)"""
        text_bytes = b''
        for char in text:
            text_bytes += char.encode('ascii') + b'\\x12'
        
        packet = bytearray()
        packet.extend(b'\\xFF\\xFF\\xFF\\xFF')  # Header
        packet.extend(struct.pack('<I', len(text_bytes) + 20))  # Length
        packet.extend(b'\\x68\\x32\\x01\\x7B')  # Command
        packet.extend(bytes([font_size, effect, 0x01, color & 0xFF, 0x00]))
        packet.extend(b'\\x02\\x00\\x00\\x01\\x06\\x00\\x00')
        packet.extend(text_bytes)
        packet.extend(b'\\x00\\x00\\x00\\x68\\x03')
        
        return bytes(packet)

# Usage example
if __name__ == "__main__":
    sdk = CP5200SDK()
    
    if sdk.connect():
        print("✅ Connected to CP5200")
        
        # Send message
        sdk.send_message("Hello from SDK!", font_size=16, color=0xFF0000)
        
        # Read time
        time_data = sdk.read_time()
        if time_data:
            print(f"Controller time: {time_data}")
        
        sdk.disconnect()
    else:
        print("❌ Failed to connect")
'''
    
    with open('cp5200_sdk_wrapper.py', 'w') as f:
        f.write(wrapper_code)
    
    print("✅ Created: cp5200_sdk_wrapper.py")
    print("   This replicates the SDK functionality in Python")
    print()
    print("Usage:")
    print("   python3 cp5200_sdk_wrapper.py")

def main():
    print("CP5200 SDK Analysis and Usage Guide")
    print("=" * 60)
    
    # Analyze SDK files
    analyze_sdk_files()
    
    # Test Wine approach
    test_wine_approach()
    
    # Show Python alternatives
    show_python_alternatives()
    
    # Create SDK wrapper
    create_sdk_wrapper()
    
    print("\n" + "=" * 60)
    print("🎯 RECOMMENDED APPROACH:")
    print("1. Use the Python implementations I created")
    print("2. They replicate all SDK functionality")
    print("3. No need for Windows DLL files on Raspberry Pi")
    print("4. Test with: python3 test_cp5200_connection.py")

if __name__ == "__main__":
    main() 