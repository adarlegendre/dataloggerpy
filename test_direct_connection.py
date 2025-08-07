#!/usr/bin/env python3
"""
Direct Connection Test for CP5200 Device
Tests different connection methods to your device
"""

import socket
import struct
import time

def test_direct_connection(ip, port=5200):
    """Test direct connection to the device"""
    print(f"🔍 Testing direct connection to {ip}:{port}")
    print("=" * 50)
    
    # Test 1: Basic socket connection
    print("1️⃣ Testing basic socket connection...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, port))
        print("   ✅ Socket connection successful")
        sock.close()
    except Exception as e:
        print(f"   ❌ Socket connection failed: {e}")
        return False
    
    # Test 2: Send different test packets
    print("2️⃣ Testing different protocols...")
    
    test_packets = [
        ("Null packet", b'\x00\x00\x00\x00'),
        ("All ones", b'\xFF\xFF\xFF\xFF'),
        ("CP5200 header", b'\xFF\xFF\xFF\xFF\x08\x00\x00\x00\x68\x32\x01\x7B'),
        ("Simple CP5200", b'\xFF\xFF\xFF\xFF\x04\x00\x00\x00\x68\x32'),
        ("Text command", b'TEST\r\n'),
        ("Status command", b'STATUS\r\n'),
        ("Info command", b'INFO\r\n')
    ]
    
    for name, packet in test_packets:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((ip, port))
            
            print(f"   Testing {name}...")
            sock.send(packet)
            
            # Try to read response
            try:
                response = sock.recv(10)
                if response:
                    print(f"      ✅ Got response: {response.hex()}")
                else:
                    print(f"      ⚠️  No response")
            except socket.timeout:
                print(f"      ⚠️  No response (timeout)")
            
            sock.close()
            time.sleep(0.5)  # Small delay between tests
            
        except Exception as e:
            print(f"      ❌ Error: {e}")
    
    # Test 3: Try sending a simple message
    print("3️⃣ Testing simple message...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, port))
        
        # Build a simple message packet
        message = "TEST"
        text_bytes = b''
        for char in message:
            text_bytes += char.encode('ascii') + b'\x12'
        
        data_length = len(text_bytes) + 20
        packet = bytearray()
        packet.extend(b'\xFF\xFF\xFF\xFF')
        packet.extend(struct.pack('<I', data_length))
        packet.extend(b'\x68\x32\x01\x7B')
        packet.extend(bytes([16, 1, 0x01, 0xFF, 0x00]))
        packet.extend(b'\x02\x00\x00\x01\x06\x00\x00')
        packet.extend(text_bytes)
        packet.extend(b'\x00\x00\x00\x68\x03')
        
        print(f"   Sending message packet...")
        sock.send(bytes(packet))
        
        try:
            response = sock.recv(10)
            if response:
                print(f"      ✅ Got response: {response.hex()}")
            else:
                print(f"      ⚠️  No response")
        except socket.timeout:
            print(f"      ⚠️  No response (timeout)")
        
        sock.close()
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n✅ Direct connection test completed!")
    print("💡 If any protocol worked, you can try connecting with:")
    print(f"   python cp5200_raspberry_pi_enhanced.py --ip {ip} --port {port}")
    
    return True

def main():
    import sys
    
    # Default IP
    ip = '192.168.1.222'
    port = 5200
    
    if len(sys.argv) > 1:
        ip = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    
    print("🔍 CP5200 Direct Connection Test")
    print("=" * 40)
    print(f"Testing device: {ip}:{port}")
    print()
    
    test_direct_connection(ip, port)

if __name__ == "__main__":
    main() 