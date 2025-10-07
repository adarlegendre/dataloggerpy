#!/usr/bin/env python3
"""
Multi-Port Data Listener - Listen on multiple ports simultaneously for camera data
"""

import socket
import threading
import time
import json
from datetime import datetime
import struct

class MultiPortDataListener:
    def __init__(self, camera_ip="192.168.2.13"):
        self.camera_ip = camera_ip
        self.running = False
        self.listeners = {}
        self.received_data = []
        self.data_lock = threading.Lock()
        
    def listen_on_port(self, port, protocol='tcp'):
        """Listen for data on a specific port"""
        print(f"🎧 Starting {protocol.upper()} listener on port {port}")
        
        try:
            if protocol.lower() == 'tcp':
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.bind(('', port))
                sock.listen(5)
                sock.settimeout(1.0)  # Non-blocking with timeout
                
                while self.running:
                    try:
                        client_socket, addr = sock.accept()
                        if addr[0] == self.camera_ip:
                            print(f"✅ Camera connected from {addr[0]}:{addr[1]}")
                            
                            # Handle client connection in separate thread
                            client_thread = threading.Thread(
                                target=self.handle_tcp_client,
                                args=(client_socket, port, addr),
                                daemon=True
                            )
                            client_thread.start()
                    except socket.timeout:
                        continue
                    except Exception as e:
                        if self.running:
                            print(f"❌ TCP listener error on port {port}: {e}")
                        break
                        
            else:  # UDP
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.bind(('', port))
                sock.settimeout(1.0)  # Non-blocking with timeout
                
                while self.running:
                    try:
                        data, addr = sock.recvfrom(4096)
                        if addr[0] == self.camera_ip:
                            self.process_data(data, port, protocol, addr)
                    except socket.timeout:
                        continue
                    except Exception as e:
                        if self.running:
                            print(f"❌ UDP listener error on port {port}: {e}")
                        break
            
            sock.close()
            print(f"🔌 {protocol.upper()} listener on port {port} stopped")
            
        except Exception as e:
            print(f"❌ Failed to start {protocol.upper()} listener on port {port}: {e}")
    
    def handle_tcp_client(self, client_socket, port, addr):
        """Handle TCP client connection"""
        try:
            while self.running:
                try:
                    data = client_socket.recv(4096)
                    if not data:
                        break
                    
                    self.process_data(data, port, 'tcp', addr)
                    
                except socket.timeout:
                    continue
                except Exception as e:
                    print(f"❌ TCP client error: {e}")
                    break
        finally:
            client_socket.close()
    
    def process_data(self, raw_data, port, protocol, addr):
        """Process received data"""
        timestamp = datetime.now()
        
        with self.data_lock:
            # Try to decode as text
            try:
                text_data = raw_data.decode('utf-8', errors='ignore')
                print(f"📄 [{protocol.upper()}:{port}] Text: {text_data[:200]}...")
                
                # Check for vehicle detection keywords
                vehicle_keywords = [
                    'plate', 'number', 'license', 'vehicle', 'detection',
                    'speed', 'direction', 'confidence', 'anpr', 'lpr'
                ]
                
                is_vehicle_data = any(keyword in text_data.lower() for keyword in vehicle_keywords)
                
                if is_vehicle_data:
                    print(f"🚗 VEHICLE DETECTION DATA FOUND!")
                    print(f"   Port: {port} ({protocol.upper()})")
                    print(f"   Source: {addr[0]}:{addr[1]}")
                    print(f"   Data: {text_data}")
                
                # Try to parse as JSON
                json_data = None
                try:
                    json_data = json.loads(text_data)
                    print(f"📋 JSON: {json.dumps(json_data, indent=2)}")
                except json.JSONDecodeError:
                    pass
                
                # Store data
                data_entry = {
                    'timestamp': timestamp,
                    'port': port,
                    'protocol': protocol,
                    'source': f"{addr[0]}:{addr[1]}",
                    'raw_data': raw_data,
                    'text_data': text_data,
                    'json_data': json_data,
                    'is_vehicle_data': is_vehicle_data,
                    'data_size': len(raw_data)
                }
                
                self.received_data.append(data_entry)
                
            except Exception as e:
                print(f"📄 [{protocol.upper()}:{port}] Binary: {raw_data[:50].hex()}...")
                
                # Store binary data
                data_entry = {
                    'timestamp': timestamp,
                    'port': port,
                    'protocol': protocol,
                    'source': f"{addr[0]}:{addr[1]}",
                    'raw_data': raw_data,
                    'text_data': None,
                    'json_data': None,
                    'is_vehicle_data': False,
                    'data_size': len(raw_data),
                    'data_type': 'binary'
                }
                
                self.received_data.append(data_entry)
    
    def start_listening(self, ports, protocols=['tcp', 'udp']):
        """Start listening on multiple ports"""
        self.running = True
        threads = []
        
        print(f"🚀 Starting multi-port listener...")
        print(f"📡 Camera IP: {self.camera_ip}")
        print(f"🔌 Ports: {ports}")
        print(f"📡 Protocols: {protocols}")
        
        # Start listeners for each port/protocol combination
        for port in ports:
            for protocol in protocols:
                thread = threading.Thread(
                    target=self.listen_on_port,
                    args=(port, protocol),
                    daemon=True
                )
                threads.append(thread)
                thread.start()
                time.sleep(0.1)  # Small delay to avoid port conflicts
        
        print(f"✅ Started {len(threads)} listeners")
        print(f"📡 Waiting for camera data...")
        print(f"⏹️  Press Ctrl+C to stop")
        
        try:
            # Monitor for data
            last_count = 0
            while True:
                time.sleep(10)
                
                with self.data_lock:
                    current_count = len(self.received_data)
                    vehicle_count = sum(1 for d in self.received_data if d.get('is_vehicle_data', False))
                
                if current_count != last_count:
                    print(f"📊 Status: {current_count} total packets, {vehicle_count} vehicle detections")
                    last_count = current_count
                
        except KeyboardInterrupt:
            print("\n⏹️  Stopping listeners...")
            self.stop_listening()
    
    def stop_listening(self):
        """Stop all listeners"""
        self.running = False
        print("🛑 All listeners stopped")
    
    def get_vehicle_data(self):
        """Get only vehicle detection data"""
        with self.data_lock:
            return [d for d in self.received_data if d.get('is_vehicle_data', False)]
    
    def get_all_data(self):
        """Get all received data"""
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
            total_packets = len(self.received_data)
            vehicle_packets = sum(1 for d in self.received_data if d.get('is_vehicle_data', False))
            
            print(f"\n📊 Data Summary:")
            print(f"  Total packets: {total_packets}")
            print(f"  Vehicle detections: {vehicle_packets}")
            
            if self.received_data:
                print(f"  Data sources:")
                sources = {}
                for d in self.received_data:
                    key = f"{d['port']}/{d['protocol'].upper()}"
                    sources[key] = sources.get(key, 0) + 1
                
                for source, count in sources.items():
                    print(f"    {source}: {count} packets")
            
            if vehicle_packets > 0:
                print(f"\n🚗 Vehicle Detection Data:")
                vehicle_data = [d for d in self.received_data if d.get('is_vehicle_data', False)]
                for i, data in enumerate(vehicle_data[-5:]):  # Show last 5
                    print(f"  {i+1}. Port {data['port']} ({data['protocol'].upper()}): {data['text_data'][:100]}...")

def main():
    print("=== Multi-Port Data Listener ===\n")
    
    camera_ip = "192.168.2.13"
    listener = MultiPortDataListener(camera_ip)
    
    print("🎯 Options:")
    print("1. Listen on common ports")
    print("2. Listen on specific ports")
    print("3. Listen on port range")
    print("4. Listen on all possible ports (intensive)")
    
    choice = input("\nSelect option (1-4): ").strip()
    
    if choice == "1":
        # Common ports
        ports = [80, 8080, 8000, 5000, 9000, 4444, 7777, 8888, 9999, 1234, 3000, 8081]
        protocols = ['tcp', 'udp']
        
    elif choice == "2":
        # Specific ports
        ports_input = input("Enter ports (comma-separated): ")
        try:
            ports = [int(p.strip()) for p in ports_input.split(',')]
        except ValueError:
            print("❌ Invalid port numbers")
            return
        
        protocol_input = input("Protocols (tcp,udp) [tcp,udp]: ").strip()
        protocols = protocol_input.split(',') if protocol_input else ['tcp', 'udp']
        
    elif choice == "3":
        # Port range
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))
        ports = list(range(start_port, end_port + 1))
        protocols = ['tcp', 'udp']
        
    elif choice == "4":
        # All possible ports (be careful!)
        print("⚠️  This will create many listeners and may impact system performance")
        confirm = input("Continue? (y/n): ")
        if confirm.lower() != 'y':
            return
        
        ports = (list(range(8000, 8100)) + 
                list(range(5000, 5100)) + 
                list(range(9000, 9100)) + 
                list(range(3000, 3100)))
        protocols = ['tcp', 'udp']
        
    else:
        print("❌ Invalid choice")
        return
    
    print(f"\n🚀 Starting listener on {len(ports)} ports...")
    
    try:
        listener.start_listening(ports, protocols)
    except KeyboardInterrupt:
        pass
    finally:
        listener.stop_listening()
        listener.show_summary()
        
        # Show vehicle data if any
        vehicle_data = listener.get_vehicle_data()
        if vehicle_data:
            print(f"\n🎉 Found {len(vehicle_data)} vehicle detection(s)!")
            print("📋 Vehicle data will be integrated into Django application")

if __name__ == "__main__":
    main()

