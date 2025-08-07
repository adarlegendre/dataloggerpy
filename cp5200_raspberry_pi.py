#!/usr/bin/env python3
"""
CP5200 LED Controller - Raspberry Pi Implementation
For display at IP: 192.168.1.222
"""

import socket
import struct
import time
import logging
import argparse
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

def main():
    parser = argparse.ArgumentParser(description='CP5200 LED Display Controller')
    parser.add_argument('--ip', default='192.168.1.222', help='Display IP address')
    parser.add_argument('--port', type=int, default=5200, help='Display port')
    parser.add_argument('--message', help='Send a single message')
    parser.add_argument('--demo', action='store_true', help='Run demo sequence')
    parser.add_argument('--clock', action='store_true', help='Show clock')
    parser.add_argument('--test', action='store_true', help='Test communication')
    parser.add_argument('--time', action='store_true', help='Get controller time')
    
    args = parser.parse_args()
    
    # Initialize controller
    controller = CP5200Controller(ip_address=args.ip, port=args.port)
    
    # Connect to display
    if controller.connect():
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
                print("CP5200 LED Display Controller")
                print("=" * 40)
                print(f"Connected to: {args.ip}:{args.port}")
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
            controller.disconnect()
    else:
        print(f"Failed to connect to display at {args.ip}:{args.port}")
        print("Please check:")
        print("1. Display is powered on and connected to network")
        print("2. IP address is correct")
        print("3. Port 5200 is open")
        print("4. Network connectivity (try: ping 192.168.1.222)")

if __name__ == "__main__":
    main() 