#!/usr/bin/env python3
"""
Corrected CP5200 Controller - Based on Real Device Examples
Uses the exact packet structure from the user's device
"""

import socket
import struct
import time
import argparse

class CP5200Controller:
    """CP5200 LED Display Controller - Corrected Version"""
    
    def __init__(self, ip_address='192.168.1.222', port=5200):
        self.ip_address = ip_address
        self.port = port
        self.socket = None
        self.connected = False
    
    def connect(self):
        """Connect to the CP5200 device"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5)
            self.socket.connect((self.ip_address, self.port))
            self.connected = True
            print(f"✅ Connected to {self.ip_address}:{self.port}")
            return True
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            self.connected = False
            return False
    
    def disconnect(self):
        """Disconnect from the device"""
        if self.socket:
            self.socket.close()
            self.connected = False
            print("✅ Disconnected")
    
    def send_message(self, text, font_size=16, effect_type=1, justify=2):
        """
        Send a message to the display
        Based on real device examples provided by user
        """
        if not self.connected:
            print("❌ Not connected to device")
            return False
        
        try:
            # Build text bytes with 0x32 suffix (from examples)
            text_bytes = b''
            for char in text:
                text_bytes += char.encode('ascii') + b'\x32'
            
            # Calculate packet length (based on examples)
            # Base length: 20 bytes + text length
            base_length = 20
            total_length = base_length + len(text_bytes)
            
            # Build packet based on real examples
            packet = bytearray()
            packet.extend(b'\xFF\xFF\xFF\xFF')  # Header
            packet.extend(struct.pack('<I', total_length))  # Length
            packet.extend(b'\x68\x32\x01\x7B')  # Command
            
            # Parameters (from examples: 01 1C 00 00 00)
            packet.extend(bytes([0x01, 0x1C, 0x00, 0x00, 0x00]))
            
            # Text parameters (from examples: 02 00 00 02 00 00 03)
            packet.extend(b'\x02\x00\x00\x02\x00\x00\x03')
            
            # Text data
            packet.extend(text_bytes)
            
            # Footer (from examples: 00 00 00 93 03)
            packet.extend(b'\x00\x00\x00\x93\x03')
            
            print(f"📦 Sending packet: {packet.hex()}")
            self.socket.send(bytes(packet))
            print(f"✅ Message sent: '{text}'")
            
            return True
            
        except Exception as e:
            print(f"❌ Send failed: {e}")
            return False
    
    def send_number(self, number, font_size=16, effect_type=1, justify=2):
        """Send a number to the display"""
        return self.send_message(str(number), font_size, effect_type, justify)
    
    def send_clear(self):
        """Send clear command (empty space)"""
        return self.send_message(" ", font_size=16, effect_type=1, justify=2)
    
    def test_connection(self):
        """Test the connection with a simple message"""
        if not self.connect():
            return False
        
        # Test with examples from user
        test_messages = [
            "123.45",
            "999.99", 
            "00",
            "HELLO"
        ]
        
        for message in test_messages:
            print(f"\n🧪 Testing: '{message}'")
            self.send_message(message)
            time.sleep(2)
        
        self.disconnect()
        return True

def main():
    parser = argparse.ArgumentParser(description='Corrected CP5200 Controller')
    parser.add_argument('--ip', default='192.168.1.222', help='Device IP address')
    parser.add_argument('--port', type=int, default=5200, help='Device port')
    parser.add_argument('--message', help='Message to send')
    parser.add_argument('--number', help='Number to send')
    parser.add_argument('--test', action='store_true', help='Run connection test')
    parser.add_argument('--clear', action='store_true', help='Clear display')
    
    args = parser.parse_args()
    
    controller = CP5200Controller(args.ip, args.port)
    
    if args.test:
        print("🧪 Running connection test...")
        controller.test_connection()
    
    elif args.message:
        if controller.connect():
            controller.send_message(args.message)
            controller.disconnect()
    
    elif args.number:
        if controller.connect():
            controller.send_number(args.number)
            controller.disconnect()
    
    elif args.clear:
        if controller.connect():
            controller.send_clear()
            controller.disconnect()
    
    else:
        print("🎯 Corrected CP5200 Controller")
        print("=" * 40)
        print("Usage:")
        print("  python cp5200_corrected.py --test")
        print("  python cp5200_corrected.py --message 'HELLO'")
        print("  python cp5200_corrected.py --number '123.45'")
        print("  python cp5200_corrected.py --clear")

if __name__ == "__main__":
    main() 