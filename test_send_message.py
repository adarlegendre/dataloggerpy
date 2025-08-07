#!/usr/bin/env python3
"""
Test Send Message to CP5200 Device
Sends a simple message to see if it displays on the LED screen
"""

import socket
import struct
import time

def send_test_message(ip, port=5200, message="HELLO WORLD"):
    """Send a test message to the CP5200 device"""
    print(f"📤 Sending message to {ip}:{port}")
    print(f"💬 Message: '{message}'")
    print("=" * 50)
    
    try:
        # Create socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, port))
        print("✅ Connected to device")
        
        # Build CP5200 message packet
        text_bytes = b''
        for char in message:
            text_bytes += char.encode('ascii') + b'\x12'
        
        data_length = len(text_bytes) + 20
        packet = bytearray()
        packet.extend(b'\xFF\xFF\xFF\xFF')  # Header
        packet.extend(struct.pack('<I', data_length))  # Length
        packet.extend(b'\x68\x32\x01\x7B')  # Command
        packet.extend(bytes([16, 1, 0x01, 0xFF, 0x00]))  # Parameters
        packet.extend(b'\x02\x00\x00\x01\x06\x00\x00')  # Text parameters
        packet.extend(text_bytes)  # Text data
        packet.extend(b'\x00\x00\x00\x68\x03')  # Footer
        
        print(f"📦 Sending packet: {packet.hex()}")
        sock.send(bytes(packet))
        print("✅ Message sent!")
        
        # Wait a moment to see if anything happens
        time.sleep(2)
        
        sock.close()
        print("✅ Connection closed")
        
        print("\n🎯 Check your LED display!")
        print("   If you see the message, the device is working!")
        print("   If not, we might need to adjust the protocol.")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def send_multiple_messages(ip, port=5200):
    """Send multiple test messages"""
    messages = [
        "HELLO",
        "TEST 123",
        "CP5200 WORKING",
        "LED DISPLAY"
    ]
    
    for i, message in enumerate(messages, 1):
        print(f"\n🔢 Message {i}/{len(messages)}")
        print("=" * 30)
        send_test_message(ip, port, message)
        time.sleep(3)  # Wait between messages

def main():
    import sys
    
    # Default IP
    ip = '192.168.1.222'
    port = 5200
    
    if len(sys.argv) > 1:
        ip = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    
    print("🎯 CP5200 Message Test")
    print("=" * 30)
    print(f"Device: {ip}:{port}")
    print()
    
    # Send single test message
    send_test_message(ip, port)
    
    # Ask if user wants to send multiple messages
    print("\n" + "=" * 50)
    print("💡 Want to try multiple messages?")
    print("   Run: python test_send_message.py --multiple")
    print("   Or: python test_send_message.py 192.168.1.222 5200 --multiple")

if __name__ == "__main__":
    import sys
    
    if "--multiple" in sys.argv:
        # Remove --multiple from args
        args = [arg for arg in sys.argv if arg != "--multiple"]
        
        ip = '192.168.1.222'
        port = 5200
        
        if len(args) > 1:
            ip = args[1]
        if len(args) > 2:
            port = int(args[2])
        
        print("🎯 CP5200 Multiple Messages Test")
        print("=" * 40)
        print(f"Device: {ip}:{port}")
        print()
        
        send_multiple_messages(ip, port)
    else:
        main() 