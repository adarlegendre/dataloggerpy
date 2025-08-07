#!/usr/bin/env python3
"""
Quick Test Script for CP5200 Connection Issues
Run this to diagnose connection problems
"""

import socket
import struct
import time
import sys

def test_basic_connectivity(ip, port=5200):
    """Test basic network connectivity"""
    print(f"🔍 Testing basic connectivity to {ip}:{port}")
    print("=" * 50)
    
    try:
        # Test 1: Socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        
        print("1️⃣ Testing socket connection...")
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print("   ✅ Socket connection successful")
            
            # Test 2: Send test packet
            print("2️⃣ Testing CP5200 protocol...")
            test_packet = b'\xFF\xFF\xFF\xFF\x08\x00\x00\x00\x68\x32\x01\x7B'
            bytes_sent = sock.send(test_packet)
            print(f"   ✅ Sent {bytes_sent} bytes")
            
            # Test 3: Try to read response
            print("3️⃣ Testing response...")
            try:
                sock.settimeout(2)
                response = sock.recv(10)
                if response:
                    print(f"   ✅ Got response: {response.hex()}")
                else:
                    print("   ⚠️  No response (this might be normal)")
            except socket.timeout:
                print("   ⚠️  No response (timeout - this might be normal)")
            
            sock.close()
            return True
        else:
            print(f"   ❌ Socket connection failed (error code: {result})")
            sock.close()
            return False
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def test_different_ports(ip):
    """Test different ports"""
    print(f"\n🔍 Testing different ports on {ip}")
    print("=" * 50)
    
    ports = [5200, 23, 22, 80, 8080, 5000, 5001, 8081]
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip, port))
            
            if result == 0:
                print(f"   ✅ Port {port} is open")
            else:
                print(f"   ❌ Port {port} is closed")
            
            sock.close()
        except Exception as e:
            print(f"   ❌ Error testing port {port}: {e}")

def test_network_range(ip_base):
    """Test a range of IP addresses"""
    print(f"\n🔍 Testing IP range around {ip_base}")
    print("=" * 50)
    
    # Extract base IP
    parts = ip_base.split('.')
    if len(parts) == 4:
        base = '.'.join(parts[:3])
        
        for i in range(220, 226):  # Test 220-225
            test_ip = f"{base}.{i}"
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((test_ip, 5200))
                
                if result == 0:
                    print(f"   ✅ Found device at {test_ip}:5200")
                else:
                    print(f"   ❌ No device at {test_ip}:5200")
                
                sock.close()
            except Exception as e:
                print(f"   ❌ Error testing {test_ip}: {e}")

def test_cp5200_protocol(ip, port=5200):
    """Test CP5200 protocol specifically"""
    print(f"\n🔍 Testing CP5200 protocol on {ip}:{port}")
    print("=" * 50)
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, port))
        
        # Test different packet formats
        test_packets = [
            # Simple test packet
            b'\xFF\xFF\xFF\xFF\x08\x00\x00\x00\x68\x32\x01\x7B',
            
            # Text message packet
            b'\xFF\xFF\xFF\xFF\x1C\x00\x00\x00\x68\x32\x01\x7B\x10\x01\x01\xFF\x00\x02\x00\x00\x01\x06\x00\x00\x54\x12\x45\x12\x53\x12\x54\x12\x00\x00\x00\x68\x03',
            
            # Instant message packet
            b'\xFF\xFF\xFF\xFF\x20\x00\x00\x00\x68\x32\x01\x7B\x10\x01\x01\xFF\x00\x02\x00\x00\x01\x06\x00\x00\x48\x12\x65\x12\x6C\x12\x6C\x12\x6F\x12\x00\x00\x00\x68\x03'
        ]
        
        for i, packet in enumerate(test_packets, 1):
            print(f"   Testing packet {i}...")
            bytes_sent = sock.send(packet)
            print(f"      Sent {bytes_sent} bytes")
            
            # Try to read response
            try:
                sock.settimeout(1)
                response = sock.recv(10)
                if response:
                    print(f"      Got response: {response.hex()}")
                else:
                    print("      No response")
            except socket.timeout:
                print("      No response (timeout)")
        
        sock.close()
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def main():
    print("🚀 CP5200 Quick Test Script")
    print("=" * 50)
    
    # Default IP
    ip = '192.168.1.222'
    
    if len(sys.argv) > 1:
        ip = sys.argv[1]
    
    print(f"Testing device at: {ip}")
    print()
    
    # Test 1: Basic connectivity
    if test_basic_connectivity(ip, 5200):
        print("\n✅ Basic connectivity test passed!")
        
        # Test CP5200 protocol
        test_cp5200_protocol(ip, 5200)
    else:
        print("\n❌ Basic connectivity test failed!")
        
        # Test different ports
        test_different_ports(ip)
        
        # Test IP range
        test_network_range(ip)
    
    print("\n📋 Summary:")
    print("=" * 30)
    print("If basic connectivity failed:")
    print("1. Check if device is powered on")
    print("2. Check network cable connection")
    print("3. Verify IP address is correct")
    print("4. Check if device is on the same network")
    print("5. Try different ports (23, 80, 8080)")
    print("6. Scan for devices on different IP ranges")
    
    print("\nIf connectivity works but protocol fails:")
    print("1. Device might use different protocol")
    print("2. Try different packet formats")
    print("3. Check device documentation")
    print("4. Verify port number is correct")

if __name__ == "__main__":
    main() 