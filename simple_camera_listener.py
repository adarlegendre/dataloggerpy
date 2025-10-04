#!/usr/bin/env python3
"""
Simple Camera Listener - Connect to camera port 5000 and monitor for data
"""

import socket
import threading
import time
from datetime import datetime

class SimpleCameraListener:
    def __init__(self, camera_ip="192.168.2.13", camera_port=5000, username="admin", password="kObliha12@"):
        self.camera_ip = camera_ip
        self.camera_port = camera_port
        self.username = username
        self.password = password
        self.running = False
        self.socket = None
        self.received_data = []
        
    def connect_and_listen(self, timeout=300):
        """Connect to camera and listen for data"""
        print(f"🔌 Connecting to camera at {self.camera_ip}:{self.camera_port}")
        
        try:
            # Create socket connection
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(30)
            self.socket.connect((self.camera_ip, self.camera_port))
            
            print(f"✅ Connected to camera successfully!")
            
            # Try to login
            self.try_login()
            
            # Listen for data
            print(f"🎧 Listening for data on port {self.camera_port}...")
            print(f"⏱️  Timeout: {timeout} seconds")
            print(f"📡 Press Ctrl+C to stop")
            
            self.running = True
            start_time = time.time()
            
            while self.running and (timeout == 0 or time.time() - start_time < timeout):
                try:
                    # Receive data
                    data = self.socket.recv(4096)
                    
                    if data:
                        timestamp = datetime.now()
                        print(f"📄 [{timestamp.strftime('%H:%M:%S')}] Received {len(data)} bytes:")
                        
                        # Try to decode as text
                        try:
                            text_data = data.decode('utf-8', errors='ignore')
                            print(f"📝 Text: {text_data}")
                            
                            # Check for vehicle-related keywords
                            vehicle_keywords = ['plate', 'number', 'license', 'vehicle', 'detection', 'speed', 'direction']
                            if any(keyword in text_data.lower() for keyword in vehicle_keywords):
                                print(f"🚗 *** VEHICLE DATA DETECTED! ***")
                                print(f"   Data: {text_data}")
                            
                        except:
                            # Show as hex if not text
                            print(f"🔢 Hex: {data[:50].hex()}")
                        
                        # Store data
                        self.received_data.append({
                            'timestamp': timestamp,
                            'data_size': len(data),
                            'data': data,
                            'text': data.decode('utf-8', errors='ignore') if data else ''
                        })
                        
                        print(f"📊 Total messages received: {len(self.received_data)}")
                        print("-" * 50)
                    
                    else:
                        print("📡 No data received")
                        time.sleep(1)
                        
                except socket.timeout:
                    print("⏱️  Timeout waiting for data")
                    continue
                except Exception as e:
                    print(f"❌ Error receiving data: {e}")
                    break
                    
        except Exception as e:
            print(f"❌ Failed to connect to camera: {e}")
        finally:
            self.running = False
            if self.socket:
                self.socket.close()
                print("🔌 Disconnected from camera")
    
    def try_login(self):
        """Try different login methods"""
        print(f"🔐 Attempting to login with username: {self.username}")
        
        # Try different login commands
        login_commands = [
            f"LOGIN {self.username} {self.password}\r\n",
            f"AUTH {self.username}:{self.password}\r\n",
            f"USER {self.username}\r\nPASS {self.password}\r\n",
            f"admin:{self.password}\r\n",
            f"{self.username}:{self.password}\r\n"
        ]
        
        for i, cmd in enumerate(login_commands, 1):
            try:
                print(f"🔐 Trying login method {i}...")
                self.socket.send(cmd.encode('utf-8'))
                
                # Wait for response
                time.sleep(1)
                response = self.socket.recv(1024)
                if response:
                    text_response = response.decode('utf-8', errors='ignore')
                    print(f"📄 Response: {text_response}")
                    
                    # Check if login was successful
                    if any(success in text_response.lower() for success in ['success', 'ok', 'welcome', 'connected', 'authenticated']):
                        print(f"✅ Login successful with method {i}")
                        return True
                    elif 'fail' in text_response.lower() or 'error' in text_response.lower():
                        print(f"❌ Login failed with method {i}")
                    else:
                        print(f"⚠️  Unclear response with method {i}")
                else:
                    print(f"⚠️  No response to method {i}")
                    
            except Exception as e:
                print(f"❌ Login method {i} error: {e}")
        
        print(f"⚠️  Login status unclear, continuing to monitor...")
        return False
    
    def get_received_data(self):
        """Get all received data"""
        return self.received_data.copy()
    
    def show_summary(self):
        """Show summary of received data"""
        print(f"\n📊 Data Summary:")
        print(f"  Total messages: {len(self.received_data)}")
        
        if self.received_data:
            print(f"  First message: {self.received_data[0]['timestamp']}")
            print(f"  Last message: {self.received_data[-1]['timestamp']}")
            
            # Count vehicle-related messages
            vehicle_messages = 0
            for data in self.received_data:
                if any(keyword in data['text'].lower() for keyword in ['plate', 'vehicle', 'detection']):
                    vehicle_messages += 1
            
            print(f"  Vehicle-related messages: {vehicle_messages}")
            
            if vehicle_messages > 0:
                print(f"\n🚗 Vehicle Detection Messages:")
                for i, data in enumerate(self.received_data[-5:]):  # Show last 5
                    if any(keyword in data['text'].lower() for keyword in ['plate', 'vehicle', 'detection']):
                        print(f"  {i+1}. {data['timestamp']}: {data['text'][:100]}...")

def main():
    print("=== Simple Camera Listener ===\n")
    
    # Camera settings from the image
    camera_ip = "192.168.2.13"
    camera_port = 5000
    username = "admin"
    password = "kObliha12@"
    
    print(f"📷 Camera Configuration:")
    print(f"  IP: {camera_ip}")
    print(f"  Port: {camera_port}")
    print(f"  Username: {username}")
    print(f"  Password: {password}")
    
    listener = SimpleCameraListener(camera_ip, camera_port, username, password)
    
    # Get timeout
    timeout_input = input(f"\nTimeout in seconds [300, 0 for infinite]: ")
    try:
        timeout = int(timeout_input) if timeout_input else 300
    except ValueError:
        timeout = 300
    
    try:
        # Connect and listen
        listener.connect_and_listen(timeout)
    except KeyboardInterrupt:
        print("\n⏹️  Stopped by user")
    finally:
        # Show summary
        listener.show_summary()
        
        # Show any vehicle data found
        vehicle_data = listener.get_received_data()
        vehicle_messages = [d for d in vehicle_data if any(keyword in d['text'].lower() for keyword in ['plate', 'vehicle', 'detection'])]
        
        if vehicle_messages:
            print(f"\n🎉 Found {len(vehicle_messages)} vehicle detection messages!")
            print("📋 This data can now be integrated into the Django application")
        else:
            print(f"\n📊 No vehicle detection messages found")
            print("💡 The camera may not be sending vehicle data yet, or it uses a different format")

if __name__ == "__main__":
    main()
