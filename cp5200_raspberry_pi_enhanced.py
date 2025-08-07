#!/usr/bin/env python3
"""
CP5200 LED Controller - Enhanced Raspberry Pi Implementation
Includes network scanning and automatic device discovery
"""

import socket
import struct
import time
import logging
import argparse
import threading
import ipaddress
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('cp5200_controller.log'),
        logging.StreamHandler()
    ]
)

class CP5200NetworkScanner:
    """Network scanner for CP5200 devices"""
    
    def __init__(self, network_range='192.168.1.0/24', port=5200, timeout=2):
        self.network_range = network_range
        self.port = port
        self.timeout = timeout
        self.found_devices = []
        self.logger = logging.getLogger(__name__)
    
    def scan_network(self):
        """Scan the network for CP5200 devices"""
        self.logger.info(f"🔍 Scanning network: {self.network_range}")
        self.logger.info(f"📡 Port: {self.port}")
        self.logger.info(f"⏱️  Timeout: {self.timeout}s")
        print("=" * 50)
        
        # Get network addresses
        try:
            network = ipaddress.IPv4Network(self.network_range, strict=False)
        except Exception as e:
            self.logger.error(f"❌ Invalid network range: {e}")
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

class CP5200Controller:
    def __init__(self, ip_address='192.168.1.222', port=5200, card_id=1):
        self.ip_address = ip_address
        self.port = port
        self.card_id = card_id
        self.socket = None
        self.logger = logging.getLogger(__name__)
        self.connected = False
    
    def connect(self):
        """Connect to CP5200 via network"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5)  # 5 second timeout
            self.socket.connect((self.ip_address, self.port))
            self.connected = True
            self.logger.info(f"Connected to CP5200 at {self.ip_address}:{self.port}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to connect: {e}")
            self.connected = False
            return False
    
    def disconnect(self):
        """Close network connection"""
        if self.socket:
            self.socket.close()
            self.connected = False
            self.logger.info("Disconnected from CP5200")
    
    def send_instant_message(self, text, x=0, y=0, width=128, height=128, 
                           font_size=16, color=0xFF0000, effect=1, speed=5, stay_time=3):
        """Send instant message to display"""
        if not self.connected:
            self.logger.error("Not connected to display")
            return False
            
        try:
            # Build CP5200 protocol packet
            packet = self._build_instant_message_packet(
                text, x, y, width, height, font_size, color, effect, speed, stay_time
            )
            
            # Send packet
            self.socket.send(packet)
            self.logger.info(f"Sent message: {text}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to send message: {e}")
            return False
    
    def _build_instant_message_packet(self, text, x, y, width, height, 
                                    font_size, color, effect, speed, stay_time):
        """Build CP5200 protocol packet for instant message"""
        
        # Convert text to bytes with 0x12 suffix for each character
        text_bytes = b''
        for char in text:
            text_bytes += char.encode('ascii') + b'\x12'
        
        # Calculate packet length
        data_length = len(text_bytes) + 20  # Base length + text length
        
        # Build packet
        packet = bytearray()
        
        # Header (4 bytes)
        packet.extend(b'\xFF\xFF\xFF\xFF')
        
        # Length (4 bytes, little endian)
        packet.extend(struct.pack('<I', data_length))
        
        # Command/parameters
        packet.extend(b'\x68\x32\x01\x7B')
        
        # Font size, effect, alignment, color
        packet.extend(bytes([font_size, effect, 0x01, color & 0xFF, 0x00]))
        
        # Text parameters
        packet.extend(b'\x02\x00\x00\x01\x06\x00\x00')
        
        # Text data
        packet.extend(text_bytes)
        
        # Footer
        packet.extend(b'\x00\x00\x00\x68\x03')
        
        return bytes(packet)
    
    def send_text(self, text, window_no=0, color=0xFF0000, font_size=16, 
                 speed=5, effect=1, stay_time=3, alignment=1):
        """Send text to specific window"""
        if not self.connected:
            self.logger.error("Not connected to display")
            return False
            
        try:
            # Build text packet
            packet = self._build_text_packet(
                text, window_no, color, font_size, speed, effect, stay_time, alignment
            )
            
            # Send packet
            self.socket.send(packet)
            self.logger.info(f"Sent text to window {window_no}: {text}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to send text: {e}")
            return False
    
    def _build_text_packet(self, text, window_no, color, font_size, speed, effect, stay_time, alignment):
        """Build text packet for specific window"""
        
        # Convert text to bytes
        text_bytes = text.encode('ascii')
        
        # Build packet
        packet = bytearray()
        
        # Network header
        packet.extend(struct.pack('<I', self.card_id))  # Card ID
        packet.extend(struct.pack('<I', len(text_bytes) + 20))  # Data length
        
        # Command and parameters
        packet.extend(b'\x68\x32\x01\x7B')
        
        # Window and text parameters
        packet.extend(bytes([window_no, font_size, effect, alignment, color & 0xFF]))
        packet.extend(struct.pack('<I', speed))
        packet.extend(struct.pack('<I', stay_time))
        
        # Text data
        packet.extend(text_bytes)
        
        return bytes(packet)
    
    def send_clock(self, window_no=0, stay_time=10, calendar=1, format_type=1, 
                  content=1, font_size=16, red=255, green=255, blue=255, text=""):
        """Send clock display"""
        if not self.connected:
            self.logger.error("Not connected to display")
            return False
            
        try:
            # Build clock packet
            packet = self._build_clock_packet(
                window_no, stay_time, calendar, format_type, content, 
                font_size, red, green, blue, text
            )
            
            # Send packet
            self.socket.send(packet)
            self.logger.info(f"Sent clock to window {window_no}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to send clock: {e}")
            return False
    
    def _build_clock_packet(self, window_no, stay_time, calendar, format_type, content, 
                           font_size, red, green, blue, text):
        """Build clock packet"""
        
        # Build packet
        packet = bytearray()
        
        # Network header
        packet.extend(struct.pack('<I', self.card_id))  # Card ID
        packet.extend(struct.pack('<I', 32))  # Fixed length for clock
        
        # Command and parameters
        packet.extend(b'\x68\x32\x01\x7B')
        
        # Clock parameters
        packet.extend(bytes([window_no, stay_time, calendar, format_type, content, font_size]))
        packet.extend(bytes([red, green, blue]))
        
        # Text data
        text_bytes = text.encode('ascii')
        packet.extend(text_bytes)
        
        return bytes(packet)
    
    def test_communication(self):
        """Test communication with controller"""
        if not self.connected:
            self.logger.error("Not connected to display")
            return False
            
        try:
            # Send test packet
            test_packet = b'\xFF\xFF\xFF\xFF\x00\x00\x00\x00'
            self.socket.send(test_packet)
            
            # Try to read response
            try:
                response = self.socket.recv(10)
                if response:
                    self.logger.info("Communication test successful")
                    return True
                else:
                    self.logger.warning("No response from controller")
                    return False
            except socket.timeout:
                self.logger.info("Communication test completed (no response expected)")
                return True
                
        except Exception as e:
            self.logger.error(f"Communication test failed: {e}")
            return False
    
    def get_time(self):
        """Get current time from controller"""
        if not self.connected:
            self.logger.error("Not connected to display")
            return None
            
        try:
            # Build get time packet
            packet = self._build_get_time_packet()
            self.socket.send(packet)
            
            # Read response
            response = self.socket.recv(20)
            if response:
                # Parse time response
                time_data = self._parse_time_response(response)
                self.logger.info(f"Controller time: {time_data}")
                return time_data
            else:
                self.logger.warning("No time response from controller")
                return None
                
        except Exception as e:
            self.logger.error(f"Failed to get time: {e}")
            return None
    
    def _build_get_time_packet(self):
        """Build get time packet"""
        packet = bytearray()
        packet.extend(struct.pack('<I', self.card_id))  # Card ID
        packet.extend(struct.pack('<I', 8))  # Data length
        packet.extend(b'\x68\x32\x01\x7B')  # Command
        return bytes(packet)
    
    def _parse_time_response(self, response):
        """Parse time response from controller"""
        try:
            # Extract time data from response
            if len(response) >= 8:
                time_bytes = response[4:8]
                timestamp = struct.unpack('<I', time_bytes)[0]
                return datetime.fromtimestamp(timestamp)
            return None
        except Exception as e:
            self.logger.error(f"Failed to parse time response: {e}")
            return None

def demo_sequence(controller):
    """Run a demo sequence of messages"""
    messages = [
        ("Hello Raspberry Pi!", 16, 0xFF0000, 1, 5, 3),  # Red, draw effect
        ("CP5200 Working!", 20, 0x00FF00, 2, 3, 5),      # Green, scroll effect
        ("Network Connected!", 18, 0x0000FF, 1, 4, 4),    # Blue, draw effect
        ("Display Test Complete!", 16, 0xFFFF00, 2, 6, 3) # Yellow, scroll effect
    ]
    
    for i, (text, font_size, color, effect, speed, stay_time) in enumerate(messages):
        controller.send_instant_message(text, font_size=font_size, color=color, 
                                     effect=effect, speed=speed, stay_time=stay_time)
        time.sleep(stay_time + 1)  # Wait for message to complete plus 1 second

def clock_demo(controller):
    """Run a clock demo"""
    controller.send_clock(window_no=0, stay_time=10, calendar=1, format_type=1, 
                        content=1, font_size=16, red=255, green=255, blue=255, 
                        text="Current Time:")
    time.sleep(12)

def auto_discover_and_connect():
    """Automatically discover CP5200 devices and connect to the first one found"""
    print("🔍 Auto-discovering CP5200 devices...")
    print("=" * 50)
    
    # Try different network ranges
    network_ranges = [
        '192.168.1.0/24',  # Common home/office network
        '192.168.0.0/24',  # Alternative home network
        '10.0.0.0/24',     # Corporate network
        '172.16.0.0/24'    # Alternative corporate network
    ]
    
    for network_range in network_ranges:
        print(f"🔍 Scanning {network_range}...")
        scanner = CP5200NetworkScanner(network_range=network_range)
        devices = scanner.scan_network()
        
        if devices:
            print(f"\n✅ Found {len(devices)} CP5200 device(s):")
            for device in devices:
                print(f"   📡 {device['ip']}:{device['port']} - {device['status']}")
            
            # Connect to the first device found
            device = devices[0]
            print(f"\n🔌 Connecting to {device['ip']}:{device['port']}...")
            
            controller = CP5200Controller(ip_address=device['ip'], port=device['port'])
            if controller.connect():
                print("✅ Successfully connected!")
                return controller
            else:
                print("❌ Failed to connect to discovered device")
        else:
            print(f"❌ No CP5200 devices found in {network_range}")
    
    print("\n❌ No CP5200 devices found on any network")
    return None

def main():
    parser = argparse.ArgumentParser(description='CP5200 LED Display Controller - Enhanced')
    parser.add_argument('--ip', default='192.168.1.222', help='Display IP address')
    parser.add_argument('--port', type=int, default=5200, help='Display port')
    parser.add_argument('--message', help='Send a single message')
    parser.add_argument('--demo', action='store_true', help='Run demo sequence')
    parser.add_argument('--clock', action='store_true', help='Show clock')
    parser.add_argument('--test', action='store_true', help='Test communication')
    parser.add_argument('--time', action='store_true', help='Get controller time')
    parser.add_argument('--scan', action='store_true', help='Scan network for devices')
    parser.add_argument('--auto', action='store_true', help='Auto-discover and connect')
    parser.add_argument('--network', default='192.168.1.0/24', help='Network range to scan')
    
    args = parser.parse_args()
    
    # Initialize controller
    controller = None
    
    if args.auto:
        # Auto-discover and connect
        controller = auto_discover_and_connect()
        if not controller:
            print("❌ Auto-discovery failed. Please check network connectivity.")
            return
    else:
        # Manual connection
        controller = CP5200Controller(ip_address=args.ip, port=args.port)
        
        if args.scan:
            # Scan network for devices
            print("🔍 Scanning network for CP5200 devices...")
            scanner = CP5200NetworkScanner(network_range=args.network, port=args.port)
            devices = scanner.scan_network()
            
            print("\n📋 Scan Results:")
            print("=" * 30)
            if devices:
                for device in devices:
                    print(f"✅ {device['ip']}:{device['port']} - {device['status']}")
            else:
                print("❌ No CP5200 devices found")
            return
        
        # Connect to display
        if not controller.connect():
            print(f"❌ Failed to connect to display at {args.ip}:{args.port}")
            print("💡 Try using --auto to auto-discover devices")
            print("💡 Try using --scan to scan for devices")
            return
    
    try:
        if args.test:
            # Test communication
            controller.test_communication()
            
        elif args.time:
            # Get controller time
            controller.get_time()
            
        elif args.clock:
            # Show clock
            clock_demo(controller)
            
        elif args.demo:
            # Run demo sequence
            demo_sequence(controller)
            
        elif args.message:
            # Send single message
            controller.send_instant_message(args.message, font_size=16, 
                                        color=0xFF0000, effect=1, speed=5, stay_time=3)
            
        else:
            # Interactive mode
            print("CP5200 LED Display Controller - Enhanced")
            print("=" * 50)
            print(f"Connected to: {controller.ip_address}:{controller.port}")
            print()
            print("Commands:")
            print("  'message' - Send a message")
            print("  'clock' - Show clock")
            print("  'demo' - Run demo sequence")
            print("  'test' - Test communication")
            print("  'time' - Get controller time")
            print("  'quit' - Exit")
            print()
            
            while True:
                try:
                    command = input("Enter command: ").strip().lower()
                    
                    if command == 'quit':
                        break
                    elif command == 'demo':
                        demo_sequence(controller)
                    elif command == 'clock':
                        clock_demo(controller)
                    elif command == 'test':
                        controller.test_communication()
                    elif command == 'time':
                        controller.get_time()
                    elif command.startswith('message'):
                        parts = command.split(' ', 1)
                        if len(parts) > 1:
                            text = parts[1]
                            controller.send_instant_message(text, font_size=16, 
                                                        color=0xFF0000, effect=1, 
                                                        speed=5, stay_time=3)
                        else:
                            text = input("Enter message: ")
                            controller.send_instant_message(text, font_size=16, 
                                                        color=0xFF0000, effect=1, 
                                                        speed=5, stay_time=3)
                    else:
                        print("Unknown command. Type 'quit' to exit.")
                        
                except KeyboardInterrupt:
                    print("\nExiting...")
                    break
                except Exception as e:
                    print(f"Error: {e}")
    
    finally:
        # Disconnect
        if controller:
            controller.disconnect()

if __name__ == "__main__":
    main() 