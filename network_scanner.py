#!/usr/bin/env python3
"""
Network Scanner for CP5200 LED Display
Scans the network to find and test CP5200 devices
"""

import socket
import struct
import time
import threading
import ipaddress
import argparse
from datetime import datetime

class CP5200Scanner:
    def __init__(self, network_range='192.168.1.0/24', port=5200, timeout=2):
        self.network_range = network_range
        self.port = port
        self.timeout = timeout
        self.found_devices = []
        
    def scan_network(self):
        """Scan the network for CP5200 devices"""
        print(f"🔍 Scanning network: {self.network_range}")
        print(f"📡 Port: {self.port}")
        print(f"⏱️  Timeout: {self.timeout}s")
        print("=" * 50)
        
        # Get network addresses
        try:
            network = ipaddress.IPv4Network(self.network_range, strict=False)
        except Exception as e:
            print(f"❌ Invalid network range: {e}")
            return []
        
        # Scan each IP in the network
        threads = []
        for ip in network.hosts():
            thread = threading.Thread(target=self._test_device, args=(str(ip),))
            threads.append(thread)
            thread.start()
            
            # Limit concurrent threads
            if len(threads) >= 50:
                for t in threads:
                    t.join()
                threads = []
        
        # Wait for remaining threads
        for t in threads:
            t.join()
        
        return self.found_devices
    
    def _test_device(self, ip):
        """Test if a device is a CP5200 controller"""
        try:
            # Test TCP connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            result = sock.connect_ex((ip, self.port))
            if result == 0:
                # Port is open, test if it's a CP5200
                if self._test_cp5200_protocol(sock, ip):
                    self.found_devices.append({
                        'ip': ip,
                        'port': self.port,
                        'status': 'CP5200 Device Found'
                    })
                    print(f"✅ Found CP5200 at {ip}:{self.port}")
                else:
                    print(f"⚠️  Port {self.port} open at {ip} but not CP5200")
            else:
                # Try common ports
                for port in [5200, 23, 22, 80, 8080]:
                    if port != self.port:
                        result = sock.connect_ex((ip, port))
                        if result == 0:
                            print(f"🔍 Port {port} open at {ip}")
                            break
            
            sock.close()
            
        except Exception as e:
            pass  # Silently ignore connection errors
    
    def _test_cp5200_protocol(self, sock, ip):
        """Test if the device responds to CP5200 protocol"""
        try:
            # Send a simple CP5200 test packet
            test_packet = self._build_test_packet()
            sock.send(test_packet)
            
            # Try to read response
            sock.settimeout(1)
            response = sock.recv(10)
            
            if response:
                # Check if response looks like CP5200
                if len(response) >= 4 and response[:4] == b'\xFF\xFF\xFF\xFF':
                    return True
            
            return False
            
        except Exception:
            return False
    
    def _build_test_packet(self):
        """Build a simple test packet"""
        packet = bytearray()
        packet.extend(b'\xFF\xFF\xFF\xFF')  # Header
        packet.extend(struct.pack('<I', 8))   # Length
        packet.extend(b'\x68\x32\x01\x7B')   # Command
        return bytes(packet)
    
    def test_specific_device(self, ip, port=5200):
        """Test a specific device"""
        print(f"🔍 Testing device: {ip}:{port}")
        print("=" * 40)
        
        # Test 1: Basic connectivity
        print("1️⃣ Testing basic connectivity...")
        if self._test_ping(ip):
            print("   ✅ Device responds to ping")
        else:
            print("   ❌ Device does not respond to ping")
        
        # Test 2: Port connectivity
        print("2️⃣ Testing port connectivity...")
        if self._test_port(ip, port):
            print(f"   ✅ Port {port} is open")
        else:
            print(f"   ❌ Port {port} is closed")
        
        # Test 3: CP5200 protocol
        print("3️⃣ Testing CP5200 protocol...")
        if self._test_cp5200_connection(ip, port):
            print("   ✅ CP5200 protocol works")
        else:
            print("   ❌ CP5200 protocol failed")
        
        # Test 4: Send test message
        print("4️⃣ Testing message sending...")
        if self._test_send_message(ip, port):
            print("   ✅ Message sent successfully")
        else:
            print("   ❌ Message sending failed")
    
    def _test_ping(self, ip):
        """Test if device responds to ping"""
        try:
            # Use socket to test connectivity
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, 80))  # Try HTTP port
            sock.close()
            return True  # If we can connect to any port, device is reachable
        except:
            return False
    
    def _test_port(self, ip, port):
        """Test if specific port is open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except:
            return False
    
    def _test_cp5200_connection(self, ip, port):
        """Test CP5200 protocol connection"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((ip, port))
            
            # Send test packet
            test_packet = self._build_test_packet()
            sock.send(test_packet)
            
            # Try to read response
            response = sock.recv(10)
            sock.close()
            
            return len(response) > 0
        except:
            return False
    
    def _test_send_message(self, ip, port):
        """Test sending a message to the device"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((ip, port))
            
            # Build a simple message packet
            message_packet = self._build_message_packet("TEST")
            sock.send(message_packet)
            
            sock.close()
            return True
        except:
            return False
    
    def _build_message_packet(self, text):
        """Build a simple message packet"""
        # Convert text to bytes with 0x12 suffix
        text_bytes = b''
        for char in text:
            text_bytes += char.encode('ascii') + b'\x12'
        
        # Calculate packet length
        data_length = len(text_bytes) + 20
        
        # Build packet
        packet = bytearray()
        packet.extend(b'\xFF\xFF\xFF\xFF')  # Header
        packet.extend(struct.pack('<I', data_length))  # Length
        packet.extend(b'\x68\x32\x01\x7B')  # Command
        packet.extend(bytes([16, 1, 0x01, 0xFF, 0x00]))  # Parameters
        packet.extend(b'\x02\x00\x00\x01\x06\x00\x00')  # Text parameters
        packet.extend(text_bytes)  # Text data
        packet.extend(b'\x00\x00\x00\x68\x03')  # Footer
        
        return bytes(packet)

def main():
    parser = argparse.ArgumentParser(description='CP5200 Network Scanner')
    parser.add_argument('--scan', action='store_true', help='Scan network for devices')
    parser.add_argument('--test', metavar='IP', help='Test specific device')
    parser.add_argument('--network', default='192.168.1.0/24', help='Network range to scan')
    parser.add_argument('--port', type=int, default=5200, help='Port to test')
    
    args = parser.parse_args()
    
    scanner = CP5200Scanner(network_range=args.network, port=args.port)
    
    if args.scan:
        print("🚀 Starting network scan...")
        devices = scanner.scan_network()
        
        print("\n📋 Scan Results:")
        print("=" * 30)
        if devices:
            for device in devices:
                print(f"✅ {device['ip']}:{device['port']} - {device['status']}")
        else:
            print("❌ No CP5200 devices found")
    
    elif args.test:
        print("🚀 Testing specific device...")
        scanner.test_specific_device(args.test, args.port)
    
    else:
        print("🔍 CP5200 Network Scanner")
        print("=" * 30)
        print("Usage:")
        print("  python network_scanner.py --scan")
        print("  python network_scanner.py --test 192.168.1.222")
        print("  python network_scanner.py --scan --network 192.168.0.0/24")

if __name__ == "__main__":
    main() 