#!/usr/bin/env python3
"""
Camera Data Listener - Listen for vehicle/plate data from camera server
"""

import socket
import threading
import time
import json
import requests
from datetime import datetime
import struct

class CameraDataListener:
    def __init__(self, camera_ip="192.168.2.13", camera_port=None):
        self.camera_ip = camera_ip
        self.camera_port = camera_port
        self.running = False
        self.socket = None
        self.listen_thread = None
        self.received_data = []
        
    def test_connection(self, port, timeout=5):
        """Test connection to camera server"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((self.camera_ip, port))
            sock.close()
            return result == 0
        except Exception as e:
            print(f"❌ Connection test failed: {e}")
            return False
    
    def listen_tcp(self, port, timeout=30):
        """Listen for TCP data from camera server"""
        print(f"🎧 Listening for TCP data on {self.camera_ip}:{port}")
        
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(timeout)
            self.socket.connect((self.camera_ip, port))
            
            print(f"✅ Connected to camera server on port {port}")
            print(f"📡 Waiting for vehicle detection data...")
            print(f"⏱️  Timeout: {timeout} seconds (set to 0 for infinite)")
            
            while self.running:
                try:
                    # Try to receive data
                    data = self.socket.recv(1024)
                    
                    if data:
                        timestamp = datetime.now()
                        self.process_data(data, timestamp)
                    else:
                        print("📡 No data received, connection may be closed")
                        break
                        
                except socket.timeout:
                    print(f"⏱️  Timeout waiting for data on port {port}")
                    break
                except Exception as e:
                    print(f"❌ Error receiving data: {e}")
                    break
                    
        except Exception as e:
            print(f"❌ Failed to connect to {self.camera_ip}:{port}: {e}")
        finally:
            if self.socket:
                self.socket.close()
                print(f"🔌 Disconnected from {self.camera_ip}:{port}")
    
    def listen_udp(self, port, timeout=30):
        """Listen for UDP data from camera server"""
        print(f"🎧 Listening for UDP data on {self.camera_ip}:{port}")
        
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.settimeout(timeout)
            self.socket.bind(('', port))  # Listen on any interface
            
            print(f"✅ UDP socket bound to port {port}")
            print(f"📡 Waiting for vehicle detection data...")
            print(f"⏱️  Timeout: {timeout} seconds (set to 0 for infinite)")
            
            while self.running:
                try:
                    data, addr = self.socket.recvfrom(1024)
                    
                    if data and addr[0] == self.camera_ip:
                        timestamp = datetime.now()
                        self.process_data(data, timestamp, addr)
                    elif data:
                        print(f"📡 Received data from {addr[0]}:{addr[1]} (not our camera)")
                        
                except socket.timeout:
                    print(f"⏱️  Timeout waiting for UDP data on port {port}")
                    break
                except Exception as e:
                    print(f"❌ Error receiving UDP data: {e}")
                    break
                    
        except Exception as e:
            print(f"❌ Failed to bind UDP socket to port {port}: {e}")
        finally:
            if self.socket:
                self.socket.close()
                print(f"🔌 UDP socket closed on port {port}")
    
    def process_data(self, raw_data, timestamp, addr=None):
        """Process received data and extract vehicle/plate information"""
        try:
            # Try to decode as text
            try:
                text_data = raw_data.decode('utf-8', errors='ignore')
                print(f"📄 Text data: {text_data}")
            except:
                print(f"📄 Raw data: {raw_data}")
            
            # Try to parse as JSON
            try:
                json_data = json.loads(text_data)
                print(f"📋 JSON data: {json.dumps(json_data, indent=2)}")
                
                # Extract vehicle information
                vehicle_info = self.extract_vehicle_info(json_data)
                if vehicle_info:
                    self.received_data.append({
                        'timestamp': timestamp,
                        'raw_data': raw_data,
                        'parsed_data': json_data,
                        'vehicle_info': vehicle_info,
                        'source': f"{self.camera_ip}:{self.camera_port}",
                        'addr': addr
                    })
                    
                    print(f"🚗 Vehicle detected:")
                    for key, value in vehicle_info.items():
                        print(f"  {key}: {value}")
                
            except json.JSONDecodeError:
                # Not JSON, try other formats
                self.parse_binary_data(raw_data, timestamp)
                
        except Exception as e:
            print(f"❌ Error processing data: {e}")
    
    def extract_vehicle_info(self, json_data):
        """Extract vehicle information from JSON data"""
        vehicle_info = {}
        
        # Common field names for vehicle data
        field_mappings = {
            'plate_number': ['plate', 'number_plate', 'license_plate', 'plate_number', 'registration'],
            'confidence': ['confidence', 'score', 'accuracy'],
            'timestamp': ['timestamp', 'time', 'datetime'],
            'speed': ['speed', 'velocity'],
            'direction': ['direction', 'bearing'],
            'location': ['location', 'position', 'coordinates'],
            'vehicle_type': ['vehicle_type', 'type', 'class'],
            'color': ['color', 'vehicle_color'],
            'make': ['make', 'brand'],
            'model': ['model']
        }
        
        # Extract fields
        for field, possible_names in field_mappings.items():
            for name in possible_names:
                if name in json_data:
                    vehicle_info[field] = json_data[name]
                    break
        
        return vehicle_info if vehicle_info else None
    
    def parse_binary_data(self, raw_data, timestamp):
        """Parse binary data format"""
        print(f"🔢 Binary data ({len(raw_data)} bytes): {raw_data.hex()}")
        
        # Try common binary formats
        if len(raw_data) >= 4:
            # Try as length-prefixed data
            try:
                length = struct.unpack('>I', raw_data[:4])[0]
                if length == len(raw_data) - 4:
                    payload = raw_data[4:]
                    text_payload = payload.decode('utf-8', errors='ignore')
                    print(f"📄 Length-prefixed data: {text_payload}")
            except:
                pass
        
        # Store raw binary data
        self.received_data.append({
            'timestamp': timestamp,
            'raw_data': raw_data,
            'parsed_data': None,
            'vehicle_info': None,
            'source': f"{self.camera_ip}:{self.camera_port}",
            'addr': None,
            'data_type': 'binary'
        })
    
    def start_listening(self, port, protocol='tcp', timeout=30):
        """Start listening for camera data"""
        if self.running:
            print("❌ Already listening")
            return
        
        self.camera_port = port
        self.running = True
        
        print(f"🚀 Starting camera data listener...")
        print(f"📡 Target: {self.camera_ip}:{port}")
        print(f"🔌 Protocol: {protocol.upper()}")
        
        if protocol.lower() == 'tcp':
            self.listen_thread = threading.Thread(
                target=self.listen_tcp, 
                args=(port, timeout),
                daemon=True
            )
        elif protocol.lower() == 'udp':
            self.listen_thread = threading.Thread(
                target=self.listen_udp, 
                args=(port, timeout),
                daemon=True
            )
        else:
            print(f"❌ Unknown protocol: {protocol}")
            return
        
        self.listen_thread.start()
        
        try:
            # Wait for the listening thread
            self.listen_thread.join()
        except KeyboardInterrupt:
            print("\n⏹️  Stopping listener...")
            self.stop_listening()
    
    def stop_listening(self):
        """Stop the listener"""
        self.running = False
        if self.socket:
            self.socket.close()
        print("🛑 Listener stopped")
    
    def get_received_data(self):
        """Get all received data"""
        return self.received_data.copy()
    
    def clear_data(self):
        """Clear received data"""
        self.received_data.clear()
        print("🗑️  Cleared received data")

def main():
    print("=== Camera Data Listener ===\n")
    
    # Test connection first
    print("🔍 Testing connection to camera server...")
    
    # Common ports to test
    test_ports = [8080, 8000, 5000, 9000, 4444, 7777, 8888, 9999]
    
    listener = CameraDataListener("192.168.2.13")
    
    open_ports = []
    for port in test_ports:
        if listener.test_connection(port):
            open_ports.append(port)
            print(f"✅ Port {port} is accessible")
        else:
            print(f"❌ Port {port} is not accessible")
    
    if not open_ports:
        print("\n❌ No accessible ports found")
        print("🔍 Please run the network scanner first to find open ports")
        return
    
    print(f"\n✅ Found {len(open_ports)} accessible ports: {open_ports}")
    
    # Let user choose port and protocol
    print(f"\n🎯 Select a port to listen on:")
    for i, port in enumerate(open_ports):
        print(f"  {i+1}. Port {port}")
    
    try:
        choice = int(input(f"Enter choice (1-{len(open_ports)}): ")) - 1
        if 0 <= choice < len(open_ports):
            selected_port = open_ports[choice]
        else:
            print("❌ Invalid choice")
            return
    except ValueError:
        print("❌ Invalid input")
        return
    
    protocol = input("Protocol (tcp/udp) [tcp]: ").lower() or 'tcp'
    
    timeout_input = input("Timeout in seconds [30, 0 for infinite]: ")
    try:
        timeout = int(timeout_input) if timeout_input else 30
    except ValueError:
        timeout = 30
    
    print(f"\n🚀 Starting listener on {listener.camera_ip}:{selected_port} ({protocol.upper()})")
    print(f"⏱️  Timeout: {timeout} seconds")
    print(f"📡 Press Ctrl+C to stop\n")
    
    try:
        listener.start_listening(selected_port, protocol, timeout)
    except KeyboardInterrupt:
        print("\n⏹️  Stopped by user")
    finally:
        listener.stop_listening()
        
        # Show received data
        data = listener.get_received_data()
        if data:
            print(f"\n📊 Received {len(data)} data packets:")
            for i, item in enumerate(data):
                print(f"\n📦 Packet {i+1}:")
                print(f"  Time: {item['timestamp']}")
                print(f"  Source: {item['source']}")
                if item['vehicle_info']:
                    print(f"  Vehicle Info: {item['vehicle_info']}")
                else:
                    print(f"  Data Type: {item.get('data_type', 'text')}")
        else:
            print("\n📊 No data received")

if __name__ == "__main__":
    main()
