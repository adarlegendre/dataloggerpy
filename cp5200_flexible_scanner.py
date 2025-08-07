#!/usr/bin/env python3
"""
Flexible CP5200 Scanner - Handles devices that don't respond to strict protocol tests
"""

import socket
import struct
import time
import threading
import ipaddress
import argparse
from datetime import datetime

class FlexibleCP5200Scanner:
    """Flexible scanner for CP5200 devices that might not respond to strict protocol tests"""
    
    def __init__(self, network_range='192.168.1.0/24', port=5200, timeout=2):
        self.network_range = network_range
        self.port = port
        self.timeout = timeout
        self.found_devices = []
        self.logger = logging.getLogger(__name__)
    
    def scan_network(self):
        """Scan the network for potential CP5200 devices"""
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
        """Test if a device is a potential CP5200 controller"""
        try:
            # Test TCP connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            result = sock.connect_ex((ip, self.port))
            if result == 0:
                # Port is open - test different protocols
                device_type = self._test_device_protocol(sock, ip)
                if device_type:
                    self.found_devices.append({
                        'ip': ip,
                        'port': self.port,
                        'status': device_type
                    })
                    print(f"✅ Found {device_type} at {ip}:{self.port}")
                else:
                    print(f"⚠️  Port {self.port} open at {ip} but protocol unknown")
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
    
    def _test_device_protocol(self, sock, ip):
        """Test different protocols to identify the device"""
        
        # Test 1: Standard CP5200 protocol
        if self._test_cp5200_protocol(sock, ip):
            return "CP5200 Device (Confirmed)"
        
        # Test 2: Alternative CP5200 protocol
        if self._test_alt_cp5200_protocol(sock, ip):
            return "CP5200 Device (Alternative Protocol)"
        
        # Test 3: Generic LED controller
        if self._test_generic_led_protocol(sock, ip):
            return "LED Controller (Generic)"
        
        # Test 4: Any response at all
        if self._test_any_response(sock, ip):
            return "Unknown Device (Port 5200 Open)"
        
        return None
    
    def _test_cp5200_protocol(self, sock, ip):
        """Test standard CP5200 protocol"""
        try:
            # Send standard CP5200 test packet
            test_packet = self._build_cp5200_test_packet()
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
    
    def _test_alt_cp5200_protocol(self, sock, ip):
        """Test alternative CP5200 protocol variations"""
        try:
            # Try different CP5200 packet variations
            test_packets = [
                self._build_cp5200_test_packet(),
                self._build_alt_cp5200_packet(),
                self._build_simple_cp5200_packet()
            ]
            
            for packet in test_packets:
                sock.send(packet)
                sock.settimeout(1)
                response = sock.recv(10)
                
                if response and len(response) > 0:
                    return True
            
            return False
            
        except Exception:
            return False
    
    def _test_generic_led_protocol(self, sock, ip):
        """Test for generic LED controller protocols"""
        try:
            # Try common LED controller commands
            test_commands = [
                b'TEST\r\n',
                b'STATUS\r\n',
                b'INFO\r\n',
                b'\x00\x00\x00\x00',  # Null packet
                b'\xFF\xFF\xFF\xFF'   # All ones
            ]
            
            for cmd in test_commands:
                sock.send(cmd)
                sock.settimeout(1)
                response = sock.recv(10)
                
                if response and len(response) > 0:
                    return True
            
            return False
            
        except Exception:
            return False
    
    def _test_any_response(self, sock, ip):
        """Test if device responds to any packet"""
        try:
            # Send a simple packet and see if we get any response
            test_packet = b'\x00\x00\x00\x00'
            sock.send(test_packet)
            
            sock.settimeout(1)
            response = sock.recv(10)
            
            return len(response) > 0
            
        except Exception:
            return False
    
    def _build_cp5200_test_packet(self):
        """Build standard CP5200 test packet"""
        packet = bytearray()
        packet.extend(b'\xFF\xFF\xFF\xFF')  # Header
        packet.extend(struct.pack('<I', 8))   # Length
        packet.extend(b'\x68\x32\x01\x7B')   # Command
        return bytes(packet)
    
    def _build_alt_cp5200_packet(self):
        """Build alternative CP5200 packet"""
        packet = bytearray()
        packet.extend(b'\xFF\xFF\xFF\xFF')  # Header
        packet.extend(struct.pack('<I', 4))   # Shorter length
        packet.extend(b'\x68\x32')           # Shorter command
        return bytes(packet)
    
    def _build_simple_cp5200_packet(self):
        """Build simple CP5200 packet"""
        packet = bytearray()
        packet.extend(b'\xFF\xFF\xFF\xFF')  # Header only
        return bytes(packet)
    
    def test_specific_device(self, ip, port=5200):
        """Test a specific device with detailed diagnostics"""
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
        
        # Test 3: Protocol tests
        print("3️⃣ Testing protocols...")
        protocols = [
            ("Standard CP5200", self._test_cp5200_protocol),
            ("Alternative CP5200", self._test_alt_cp5200_protocol),
            ("Generic LED", self._test_generic_led_protocol),
            ("Any Response", self._test_any_response)
        ]
        
        for name, test_func in protocols:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((ip, port))
                
                if test_func(sock, ip):
                    print(f"   ✅ {name} protocol works")
                else:
                    print(f"   ❌ {name} protocol failed")
                
                sock.close()
            except Exception as e:
                print(f"   ❌ {name} test error: {e}")
        
        # Test 4: Manual connection test
        print("4️⃣ Testing manual connection...")
        try:
            controller = CP5200Controller(ip_address=ip, port=port)
            if controller.connect():
                print("   ✅ Manual connection successful")
                controller.disconnect()
            else:
                print("   ❌ Manual connection failed")
        except Exception as e:
            print(f"   ❌ Manual connection error: {e}")
    
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

# Import the controller class from the enhanced file
try:
    from cp5200_raspberry_pi_enhanced import CP5200Controller
except ImportError:
    # Fallback if the enhanced file is not available
    class CP5200Controller:
        def __init__(self, ip_address='192.168.1.222', port=5200):
            self.ip_address = ip_address
            self.port = port
        
        def connect(self):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((self.ip_address, self.port))
                sock.close()
                return True
            except:
                return False
        
        def disconnect(self):
            pass

def main():
    parser = argparse.ArgumentParser(description='Flexible CP5200 Scanner')
    parser.add_argument('--scan', action='store_true', help='Scan network for devices')
    parser.add_argument('--test', metavar='IP', help='Test specific device')
    parser.add_argument('--network', default='192.168.1.0/24', help='Network range to scan')
    parser.add_argument('--port', type=int, default=5200, help='Port to test')
    
    args = parser.parse_args()
    
    scanner = FlexibleCP5200Scanner(network_range=args.network, port=args.port)
    
    if args.scan:
        print("🚀 Starting flexible network scan...")
        devices = scanner.scan_network()
        
        print("\n📋 Scan Results:")
        print("=" * 30)
        if devices:
            for device in devices:
                print(f"✅ {device['ip']}:{device['port']} - {device['status']}")
            
            print("\n💡 If you found a device, try connecting to it:")
            for device in devices:
                print(f"   python cp5200_raspberry_pi_enhanced.py --ip {device['ip']} --port {device['port']}")
        else:
            print("❌ No devices found")
    
    elif args.test:
        print("🚀 Testing specific device...")
        scanner.test_specific_device(args.test, args.port)
    
    else:
        print("🔍 Flexible CP5200 Scanner")
        print("=" * 30)
        print("Usage:")
        print("  python cp5200_flexible_scanner.py --scan")
        print("  python cp5200_flexible_scanner.py --test 192.168.1.222")
        print("  python cp5200_flexible_scanner.py --scan --network 192.168.0.0/24")

if __name__ == "__main__":
    main() 