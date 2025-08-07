#!/usr/bin/env python3
"""
CP5200 LED Controller - Data Reader
Reads data from the CP5200 LED display using SDK functions
"""

import socket
import struct
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('cp5200_reader.log'),
        logging.StreamHandler()
    ]
)

class CP5200Reader:
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
            self.socket.settimeout(5)
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
    
    def read_time(self):
        """Read current time from controller using SDK CP5200_MakeReadTimeData"""
        if not self.connected:
            return None
            
        try:
            # Build packet based on SDK function
            packet = bytearray()
            packet.extend(struct.pack('<I', self.card_id))  # Card ID
            packet.extend(struct.pack('<I', 8))  # Data length
            packet.extend(b'\x68\x32\x01\x7B')  # Command
            
            self.socket.send(packet)
            response = self.socket.recv(20)
            
            if response and len(response) >= 8:
                time_bytes = response[4:8]
                timestamp = struct.unpack('<I', time_bytes)[0]
                return datetime.fromtimestamp(timestamp)
            return None
                
        except Exception as e:
            self.logger.error(f"Failed to read time: {e}")
            return None
    
    def read_temperature_humidity(self):
        """Read temperature and humidity using SDK CP5200_MakeGetTempHumiData"""
        if not self.connected:
            return None
            
        try:
            # Build packet based on SDK function
            packet = bytearray()
            packet.extend(struct.pack('<I', self.card_id))  # Card ID
            packet.extend(struct.pack('<I', 12))  # Data length
            packet.extend(b'\x68\x32\x01\x7B')  # Command
            packet.extend(bytes([0, 0, 0, 0]))  # Flag and padding
            
            self.socket.send(packet)
            response = self.socket.recv(20)
            
            if response and len(response) >= 8:
                temp_bytes = response[4:6]
                humi_bytes = response[6:8]
                
                temperature = struct.unpack('<H', temp_bytes)[0] / 10.0
                humidity = struct.unpack('<H', humi_bytes)[0] / 10.0
                
                return {
                    'temperature': temperature,
                    'humidity': humidity,
                    'temperature_f': temperature * 9/5 + 32
                }
            return None
                
        except Exception as e:
            self.logger.error(f"Failed to read temp/humi: {e}")
            return None
    
    def read_version_info(self):
        """Read version information using SDK CP5200_MakeReadVersionData"""
        if not self.connected:
            return None
            
        try:
            # Build packet based on SDK function
            packet = bytearray()
            packet.extend(struct.pack('<I', self.card_id))  # Card ID
            packet.extend(struct.pack('<I', 8))  # Data length
            packet.extend(b'\x68\x32\x01\x7B')  # Command
            
            self.socket.send(packet)
            response = self.socket.recv(50)
            
            if response and len(response) >= 8:
                version_bytes = response[4:]
                version_str = version_bytes.decode('ascii', errors='ignore').strip('\x00')
                return version_str
            return None
                
        except Exception as e:
            self.logger.error(f"Failed to read version: {e}")
            return None
    
    def test_communication(self):
        """Test communication with controller"""
        if not self.connected:
            return False
            
        try:
            test_packet = b'\xFF\xFF\xFF\xFF\x00\x00\x00\x00'
            self.socket.send(test_packet)
            
            try:
                response = self.socket.recv(10)
                return bool(response)
            except socket.timeout:
                return True  # No response expected
                
        except Exception as e:
            self.logger.error(f"Communication test failed: {e}")
            return False

def main():
    print("CP5200 Data Reader")
    print("=" * 40)
    
    reader = CP5200Reader()
    
    if reader.connect():
        try:
            print("Reading data from CP5200 controller...")
            print()
            
            # Test communication
            print("1. Testing communication...")
            if reader.test_communication():
                print("   ✓ Communication successful")
            else:
                print("   ✗ Communication failed")
                return
            
            # Read time
            print("\n2. Reading controller time...")
            time_data = reader.read_time()
            if time_data:
                print(f"   ✓ Controller time: {time_data}")
            else:
                print("   ✗ Failed to read time")
            
            # Read temperature and humidity
            print("\n3. Reading temperature and humidity...")
            temp_humi_data = reader.read_temperature_humidity()
            if temp_humi_data:
                print(f"   ✓ Temperature: {temp_humi_data['temperature']}°C ({temp_humi_data['temperature_f']}°F)")
                print(f"   ✓ Humidity: {temp_humi_data['humidity']}%")
            else:
                print("   ✗ Failed to read temperature/humidity")
            
            # Read version
            print("\n4. Reading version information...")
            version_data = reader.read_version_info()
            if version_data:
                print(f"   ✓ Version: {version_data}")
            else:
                print("   ✗ Failed to read version")
            
            print("\n" + "=" * 40)
            print("Reading complete!")
            
        finally:
            reader.disconnect()
    else:
        print(f"Failed to connect to display at {reader.ip_address}:{reader.port}")

if __name__ == "__main__":
    main() 