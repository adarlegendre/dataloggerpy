#!/usr/bin/env python3
"""
VIID Camera Listener - Listen for VIID_2017 protocol data from camera
"""

import socket
import threading
import time
import json
import xml.etree.ElementTree as ET
import base64
from datetime import datetime
import hashlib
import hmac

class VIIDCameraListener:
    def __init__(self, camera_ip="192.168.2.13", camera_port=5000, username="admin", password="kObliha12@"):
        self.camera_ip = camera_ip
        self.camera_port = camera_port
        self.username = username
        self.password = password
        self.running = False
        self.socket = None
        self.received_data = []
        self.data_lock = threading.Lock()
        
    def connect_to_camera(self):
        """Connect to the VIID camera server and authenticate"""
        try:
            print(f"🔌 Connecting to VIID camera at {self.camera_ip}:{self.camera_port}")
            
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(30)
            self.socket.connect((self.camera_ip, self.camera_port))
            
            print(f"✅ Connected to VIID camera")
            
            # Authenticate with the camera
            if self.authenticate():
                print(f"✅ Authentication successful")
                return True
            else:
                print(f"❌ Authentication failed")
                self.socket.close()
                return False
            
        except Exception as e:
            print(f"❌ Failed to connect to VIID camera: {e}")
            return False
    
    def authenticate(self):
        """Authenticate with the VIID camera using multiple methods"""
        print(f"🔐 Authenticating with username: {self.username}")
        
        # Try different authentication methods
        auth_methods = [
            # Method 1: Simple AUTH command
            f"AUTH:{self.username}:{self.password}\r\n",
            # Method 2: Login command
            f"LOGIN {self.username} {self.password}\r\n",
            # Method 3: HTTP-style authentication
            f"GET /login?user={self.username}&pass={self.password} HTTP/1.1\r\nHost: {self.camera_ip}\r\n\r\n",
            # Method 4: VIID standard authentication
            f"VIID_AUTH {self.username}:{self.password}\r\n",
            # Method 5: Basic authentication header
            f"Authorization: Basic {base64.b64encode(f'{self.username}:{self.password}'.encode()).decode()}\r\n\r\n"
        ]
        
        for i, auth_message in enumerate(auth_methods, 1):
            try:
                print(f"🔐 Trying authentication method {i}...")
                self.socket.send(auth_message.encode('utf-8'))
                
                # Wait for response
                self.socket.settimeout(5)
                response = self.socket.recv(1024).decode('utf-8', errors='ignore')
                print(f"📄 Auth response: {response[:200]}...")
                
                # Check if authentication was successful
                if any(success_indicator in response.upper() for success_indicator in 
                       ["SUCCESS", "OK", "200", "AUTHENTICATED", "LOGIN SUCCESS", "WELCOME"]):
                    print(f"✅ Authentication successful with method {i}")
                    return True
                elif "FAIL" in response.upper() or "ERROR" in response.upper() or "401" in response:
                    print(f"❌ Authentication failed with method {i}: {response[:100]}")
                else:
                    print(f"⚠️  Unclear response with method {i}: {response[:100]}")
                    
            except Exception as e:
                print(f"❌ Authentication method {i} error: {e}")
                continue
        
        print(f"❌ All authentication methods failed")
        return False
    
    def send_keepalive(self):
        """Send keepalive message to maintain connection"""
        try:
            # VIID keepalive message format
            keepalive_msg = "KEEPALIVE\r\n"
            self.socket.send(keepalive_msg.encode('utf-8'))
            print(f"💓 Sent keepalive")
        except Exception as e:
            print(f"❌ Failed to send keepalive: {e}")
    
    def listen_for_vehicle_data(self, timeout=300):
        """Listen for vehicle detection data from camera"""
        print(f"🎧 Listening for VIID vehicle detection data on port {self.camera_port}...")
        print(f"⏱️  Timeout: {timeout} seconds")
        print(f"📡 Press Ctrl+C to stop")
        
        self.running = True
        buffer = ""
        last_keepalive = time.time()
        start_time = time.time()
        
        # Set socket to non-blocking for better responsiveness
        self.socket.settimeout(1.0)
        
        try:
            while self.running and (timeout == 0 or time.time() - start_time < timeout):
                try:
                    # Receive data
                    data = self.socket.recv(4096)
                    if not data:
                        print("📡 No data received, connection may be closed")
                        break
                    
                    # Add to buffer
                    buffer += data.decode('utf-8', errors='ignore')
                    
                    # Process complete messages (try different delimiters)
                    delimiters = ['\r\n', '\n', '\r', '</Message>', '</Vehicle>', '</Detection>']
                    
                    for delimiter in delimiters:
                        while delimiter in buffer:
                            message, buffer = buffer.split(delimiter, 1)
                            if message.strip():
                                self.process_viid_message(message.strip())
                    
                    # Send keepalive every 30 seconds
                    if time.time() - last_keepalive > 30:
                        self.send_keepalive()
                        last_keepalive = time.time()
                        
                except socket.timeout:
                    # This is normal for non-blocking socket
                    continue
                except Exception as e:
                    print(f"❌ Error receiving data: {e}")
                    break
                    
        except KeyboardInterrupt:
            print("\n⏹️  Stopped by user")
        finally:
            self.running = False
            if self.socket:
                self.socket.close()
                print("🔌 Disconnected from VIID camera")
    
    def process_viid_message(self, message):
        """Process VIID protocol message"""
        timestamp = datetime.now()
        print(f"📄 VIID Message: {message[:200]}...")
        
        try:
            # Try to parse as XML (VIID often uses XML format)
            if message.startswith('<?xml') or message.startswith('<'):
                self.parse_viid_xml(message, timestamp)
            else:
                # Try to parse as JSON
                if message.startswith('{'):
                    self.parse_viid_json(message, timestamp)
                else:
                    # Plain text format
                    self.parse_viid_text(message, timestamp)
                    
        except Exception as e:
            print(f"❌ Error processing VIID message: {e}")
    
    def parse_viid_xml(self, xml_message, timestamp):
        """Parse VIID XML message"""
        try:
            root = ET.fromstring(xml_message)
            
            # Look for vehicle detection elements
            vehicle_data = self.extract_vehicle_from_xml(root)
            
            if vehicle_data:
                print(f"🚗 Vehicle detected via XML:")
                for key, value in vehicle_data.items():
                    print(f"  {key}: {value}")
                
                with self.data_lock:
                    self.received_data.append({
                        'timestamp': timestamp,
                        'format': 'xml',
                        'raw_message': xml_message,
                        'vehicle_data': vehicle_data,
                        'source': f"{self.camera_ip}:{self.camera_port}"
                    })
            
        except ET.ParseError as e:
            print(f"❌ XML parse error: {e}")
    
    def parse_viid_json(self, json_message, timestamp):
        """Parse VIID JSON message"""
        try:
            data = json.loads(json_message)
            
            # Extract vehicle information
            vehicle_data = self.extract_vehicle_from_json(data)
            
            if vehicle_data:
                print(f"🚗 Vehicle detected via JSON:")
                for key, value in vehicle_data.items():
                    print(f"  {key}: {value}")
                
                with self.data_lock:
                    self.received_data.append({
                        'timestamp': timestamp,
                        'format': 'json',
                        'raw_message': json_message,
                        'vehicle_data': vehicle_data,
                        'source': f"{self.camera_ip}:{self.camera_port}"
                    })
            
        except json.JSONDecodeError as e:
            print(f"❌ JSON parse error: {e}")
    
    def parse_viid_text(self, text_message, timestamp):
        """Parse VIID plain text message"""
        # Look for vehicle detection keywords
        vehicle_keywords = ['vehicle', 'plate', 'number', 'license', 'detection', 'motor']
        
        if any(keyword in text_message.lower() for keyword in vehicle_keywords):
            print(f"🚗 Vehicle detection text message:")
            print(f"  Message: {text_message}")
            
            with self.data_lock:
                self.received_data.append({
                    'timestamp': timestamp,
                    'format': 'text',
                    'raw_message': text_message,
                    'vehicle_data': {'message': text_message},
                    'source': f"{self.camera_ip}:{self.camera_port}"
                })
    
    def extract_vehicle_from_xml(self, root):
        """Extract vehicle data from XML structure"""
        vehicle_data = {}
        
        # Common VIID XML paths for vehicle data
        paths = {
            'plate_number': ['.//PlateNumber', './/LicensePlate', './/Plate'],
            'confidence': ['.//Confidence', './/Score'],
            'timestamp': ['.//Time', './/Timestamp', './/DateTime'],
            'speed': ['.//Speed', './/Velocity'],
            'direction': ['.//Direction', './/Bearing'],
            'location': ['.//Location', './/Position'],
            'vehicle_type': ['.//VehicleType', './/Type'],
            'color': ['.//Color', './/VehicleColor'],
            'make': ['.//Make', './/Brand'],
            'model': ['.//Model']
        }
        
        for field, xpath_list in paths.items():
            for xpath in xpath_list:
                element = root.find(xpath)
                if element is not None and element.text:
                    vehicle_data[field] = element.text.strip()
                    break
        
        return vehicle_data if vehicle_data else None
    
    def extract_vehicle_from_json(self, data):
        """Extract vehicle data from JSON structure"""
        vehicle_data = {}
        
        # Common field mappings
        field_mappings = {
            'plate_number': ['plate_number', 'plateNumber', 'license_plate', 'licensePlate', 'plate'],
            'confidence': ['confidence', 'score', 'accuracy'],
            'timestamp': ['timestamp', 'time', 'datetime'],
            'speed': ['speed', 'velocity'],
            'direction': ['direction', 'bearing'],
            'location': ['location', 'position', 'coordinates'],
            'vehicle_type': ['vehicle_type', 'vehicleType', 'type'],
            'color': ['color', 'vehicle_color', 'vehicleColor'],
            'make': ['make', 'brand'],
            'model': ['model']
        }
        
        def extract_nested_value(obj, keys):
            """Extract value from nested object using key list"""
            for key in keys:
                if key in obj:
                    return obj[key]
            return None
        
        for field, possible_keys in field_mappings.items():
            value = extract_nested_value(data, possible_keys)
            if value is not None:
                vehicle_data[field] = value
        
        return vehicle_data if vehicle_data else None
    
    def get_vehicle_data(self):
        """Get all vehicle detection data"""
        with self.data_lock:
            return self.received_data.copy()
    
    def clear_data(self):
        """Clear received data"""
        with self.data_lock:
            self.received_data.clear()
        print("🗑️  Cleared received data")
    
    def show_summary(self):
        """Show summary of received data"""
        with self.data_lock:
            total_messages = len(self.received_data)
            vehicle_detections = sum(1 for d in self.received_data if d.get('vehicle_data'))
            
            print(f"\n📊 VIID Data Summary:")
            print(f"  Total messages: {total_messages}")
            print(f"  Vehicle detections: {vehicle_detections}")
            
            if self.received_data:
                print(f"  Message formats:")
                formats = {}
                for d in self.received_data:
                    fmt = d.get('format', 'unknown')
                    formats[fmt] = formats.get(fmt, 0) + 1
                
                for fmt, count in formats.items():
                    print(f"    {fmt}: {count} messages")
            
            if vehicle_detections > 0:
                print(f"\n🚗 Recent Vehicle Detections:")
                vehicle_data = [d for d in self.received_data if d.get('vehicle_data')]
                for i, data in enumerate(vehicle_data[-3:]):  # Show last 3
                    print(f"  {i+1}. {data['timestamp']}: {data['vehicle_data']}")

def main():
    print("=== VIID Camera Listener ===\n")
    
    camera_ip = "192.168.2.13"
    camera_port = 5000
    username = "admin"
    password = "kObliha12@"
    
    listener = VIIDCameraListener(camera_ip, camera_port, username, password)
    
    # Connect to camera
    if not listener.connect_to_camera():
        print("❌ Cannot connect to camera. Please check:")
        print(f"  - Camera IP: {camera_ip}")
        print(f"  - Camera Port: {camera_port}")
        print(f"  - Username: {username}")
        print(f"  - Password: {password}")
        print(f"  - Camera is online and configured correctly")
        return
    
    # Get timeout
    timeout_input = input("Timeout in seconds [300, 0 for infinite]: ")
    try:
        timeout = int(timeout_input) if timeout_input else 300
    except ValueError:
        timeout = 300
    
    start_time = time.time()
    
    try:
        # Listen for vehicle data
        listener.listen_for_vehicle_data(timeout)
    except KeyboardInterrupt:
        print("\n⏹️  Stopped by user")
    finally:
        listener.show_summary()
        
        # Show vehicle data
        vehicle_data = listener.get_vehicle_data()
        if vehicle_data:
            print(f"\n🎉 Successfully received {len(vehicle_data)} messages from VIID camera!")
            print("📋 Vehicle detection data will be integrated into Django application")

if __name__ == "__main__":
    main()
