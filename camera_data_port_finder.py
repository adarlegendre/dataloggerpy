#!/usr/bin/env python3
"""
Camera Data Port Finder - Find the actual port where camera sends vehicle data
"""

import socket
import threading
import time
import json
from datetime import datetime
import select

class CameraDataPortFinder:
    def __init__(self, camera_ip="192.168.2.13"):
        self.camera_ip = camera_ip
        self.found_data_ports = []
        self.listeners = {}
        self.running = False
        
    def scan_all_ports(self, start_port=1, end_port=65535, max_threads=50, timeout=2):
        """Scan all ports to find open ones"""
        print(f"🔍 Scanning all ports on {self.camera_ip} ({start_port}-{end_port})")
        print(f"⏱️  This may take a few minutes...")
        
        open_ports = []
        threads = []
        
        def scan_port_range(port_list):
            for port in port_list:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    result = sock.connect_ex((self.camera_ip, port))
                    sock.close()
                    
                    if result == 0:
                        open_ports.append(port)
                        print(f"✅ Port {port} is OPEN")
                except:
                    pass
        
        # Create thread chunks
        ports_per_thread = max(1, (end_port - start_port + 1) // max_threads)
        for i in range(max_threads):
            start = start_port + (i * ports_per_thread)
            end = min(start_port + ((i + 1) * ports_per_thread) - 1, end_port)
            port_chunk = list(range(start, end + 1))
            
            if port_chunk:
                thread = threading.Thread(target=scan_port_range, args=(port_chunk,))
                threads.append(thread)
                thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        return sorted(open_ports)
    
    def listen_on_port(self, port, protocol='tcp', timeout=30):
        """Listen for data on a specific port"""
        print(f"🎧 Listening on {protocol.upper()} port {port} for {timeout}s...")
        
        data_received = False
        received_bytes = 0
        
        try:
            if protocol.lower() == 'tcp':
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)
                sock.connect((self.camera_ip, port))
            else:  # UDP
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(timeout)
                sock.bind(('', 0))  # Bind to any available port
                # Try to connect to camera (UDP is connectionless, but this helps with routing)
                sock.connect((self.camera_ip, port))
            
            print(f"✅ Connected to {self.camera_ip}:{port}")
            
            start_time = time.time()
            while time.time() - start_time < timeout:
                try:
                    if protocol.lower() == 'tcp':
                        data = sock.recv(1024)
                    else:  # UDP
                        data, addr = sock.recvfrom(1024)
                    
                    if data:
                        data_received = True
                        received_bytes += len(data)
                        
                        # Try to decode as text
                        try:
                            text = data.decode('utf-8', errors='ignore')
                            print(f"📄 Text data: {text[:200]}...")
                            
                            # Check if it looks like vehicle data
                            vehicle_keywords = ['plate', 'number', 'license', 'vehicle', 'detection', 'speed', 'direction']
                            if any(keyword in text.lower() for keyword in vehicle_keywords):
                                print(f"🚗 VEHICLE DATA DETECTED!")
                                self.found_data_ports.append({
                                    'port': port,
                                    'protocol': protocol,
                                    'data': text,
                                    'timestamp': datetime.now()
                                })
                        except:
                            print(f"📄 Binary data: {data[:50].hex()}...")
                        
                except socket.timeout:
                    break
                except Exception as e:
                    print(f"❌ Error receiving data: {e}")
                    break
            
            sock.close()
            
            if data_received:
                print(f"✅ Port {port} ({protocol.upper()}): Received {received_bytes} bytes")
                return True, received_bytes
            else:
                print(f"❌ Port {port} ({protocol.upper()}): No data received")
                return False, 0
                
        except Exception as e:
            print(f"❌ Port {port} ({protocol.upper()}): Connection failed - {e}")
            return False, 0
    
    def monitor_multiple_ports(self, ports, protocols=['tcp', 'udp'], duration=60):
        """Monitor multiple ports simultaneously for data"""
        print(f"🎧 Monitoring {len(ports)} ports for {duration} seconds...")
        print(f"📡 Ports: {ports}")
        print(f"🔌 Protocols: {protocols}")
        
        self.running = True
        threads = []
        
        def monitor_port(port, protocol):
            data_received, bytes_received = self.listen_on_port(port, protocol, duration)
            if data_received:
                self.found_data_ports.append({
                    'port': port,
                    'protocol': protocol,
                    'bytes_received': bytes_received,
                    'timestamp': datetime.now()
                })
        
        # Start monitoring threads
        for port in ports:
            for protocol in protocols:
                thread = threading.Thread(
                    target=monitor_port,
                    args=(port, protocol),
                    daemon=True
                )
                threads.append(thread)
                thread.start()
        
        print(f"⏱️  Monitoring for {duration} seconds...")
        print(f"📡 Press Ctrl+C to stop early")
        
        try:
            time.sleep(duration)
        except KeyboardInterrupt:
            print("\n⏹️  Stopped by user")
        
        self.running = False
        
        # Wait for threads to finish
        for thread in threads:
            thread.join(timeout=5)
        
        return self.found_data_ports
    
    def create_data_catcher(self, ports, protocols=['tcp', 'udp']):
        """Create a data catcher that listens on multiple ports"""
        print(f"🎯 Creating data catcher for {len(ports)} ports...")
        
        self.running = True
        listeners = []
        
        def listen_forever(port, protocol):
            while self.running:
                try:
                    data_received, bytes_received = self.listen_on_port(port, protocol, 10)
                    if data_received:
                        print(f"🚗 DATA DETECTED on port {port} ({protocol.upper()})!")
                        self.found_data_ports.append({
                            'port': port,
                            'protocol': protocol,
                            'bytes_received': bytes_received,
                            'timestamp': datetime.now()
                        })
                except Exception as e:
                    if self.running:  # Only print error if we're still supposed to be running
                        print(f"❌ Error on port {port} ({protocol}): {e}")
                    time.sleep(1)
        
        # Start listeners
        for port in ports:
            for protocol in protocols:
                thread = threading.Thread(
                    target=listen_forever,
                    args=(port, protocol),
                    daemon=True
                )
                listeners.append(thread)
                thread.start()
        
        print(f"✅ Data catcher started on {len(listeners)} listeners")
        print(f"📡 Waiting for vehicle detection data...")
        print(f"⏹️  Press Ctrl+C to stop")
        
        try:
            while True:
                time.sleep(1)
                # Show status every 30 seconds
                if int(time.time()) % 30 == 0:
                    print(f"📊 Monitoring {len(ports)} ports... Found {len(self.found_data_ports)} data streams")
        except KeyboardInterrupt:
            print("\n⏹️  Stopping data catcher...")
            self.running = False
        
        return self.found_data_ports
    
    def test_camera_webhook_simulation(self, listener_port=8080):
        """Simulate camera sending data to help identify the pattern"""
        print(f"🧪 Testing camera data patterns...")
        
        # Common vehicle detection data formats
        test_formats = [
            # JSON format
            {
                'plate_number': 'ABC123',
                'confidence': 95.5,
                'timestamp': datetime.now().isoformat(),
                'speed': 45,
                'direction': 'north',
                'location': {'x': 100, 'y': 200}
            },
            # Simple text format
            "PLATE:ABC123,SPEED:45,DIRECTION:NORTH,CONFIDENCE:95.5",
            # CSV format
            "ABC123,45,NORTH,95.5,2025-01-01T12:00:00",
            # Custom format
            "VEHICLE_DETECTION|ABC123|45|NORTH|95.5|2025-01-01T12:00:00"
        ]
        
        print(f"📋 Common vehicle detection formats:")
        for i, format_data in enumerate(test_formats):
            print(f"  {i+1}. {format_data}")
        
        return test_formats

def main():
    print("=== Camera Data Port Finder ===\n")
    
    camera_ip = "192.168.2.13"
    finder = CameraDataPortFinder(camera_ip)
    
    print("🎯 Options:")
    print("1. Quick scan of common ports and monitor them")
    print("2. Full port scan (slow but thorough)")
    print("3. Monitor specific ports")
    print("4. Create data catcher for all possible ports")
    
    choice = input("\nSelect option (1-4): ").strip()
    
    if choice == "1":
        # Quick scan of common ports
        common_ports = [80, 8080, 8000, 5000, 9000, 4444, 7777, 8888, 9999, 1234, 3000, 8081]
        print(f"🔍 Quick scan of common ports: {common_ports}")
        
        open_ports = []
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((camera_ip, port))
                sock.close()
                
                if result == 0:
                    open_ports.append(port)
                    print(f"✅ Port {port} is open")
                else:
                    print(f"❌ Port {port} is closed")
            except:
                print(f"❌ Port {port} error")
        
        if open_ports:
            duration = int(input("Monitor duration in seconds [60]: ") or "60")
            finder.monitor_multiple_ports(open_ports, duration=duration)
        else:
            print("❌ No common ports found open")
    
    elif choice == "2":
        # Full port scan
        print("⚠️  Full port scan will take several minutes...")
        confirm = input("Continue? (y/n): ")
        if confirm.lower() == 'y':
            open_ports = finder.scan_all_ports(1, 65535, 50, 2)
            if open_ports:
                print(f"✅ Found {len(open_ports)} open ports: {open_ports}")
                duration = int(input("Monitor duration in seconds [60]: ") or "60")
                finder.monitor_multiple_ports(open_ports, duration=duration)
            else:
                print("❌ No open ports found")
    
    elif choice == "3":
        # Monitor specific ports
        ports_input = input("Enter ports to monitor (comma-separated): ")
        try:
            ports = [int(p.strip()) for p in ports_input.split(',')]
            duration = int(input("Monitor duration in seconds [60]: ") or "60")
            finder.monitor_multiple_ports(ports, duration=duration)
        except ValueError:
            print("❌ Invalid port numbers")
    
    elif choice == "4":
        # Data catcher for all possible ports
        print("⚠️  This will create listeners on many ports...")
        confirm = input("Continue? (y/n): ")
        if confirm.lower() == 'y':
            # Use a range of likely ports
            ports = list(range(8000, 8100)) + list(range(5000, 5100)) + list(range(9000, 9100))
            finder.create_data_catcher(ports)
    
    else:
        print("❌ Invalid choice")
        return
    
    # Show results
    if finder.found_data_ports:
        print(f"\n🎉 Found {len(finder.found_data_ports)} data streams:")
        for i, data_stream in enumerate(finder.found_data_ports):
            print(f"\n📦 Data Stream {i+1}:")
            print(f"  Port: {data_stream['port']}")
            print(f"  Protocol: {data_stream['protocol'].upper()}")
            print(f"  Time: {data_stream['timestamp']}")
            if 'bytes_received' in data_stream:
                print(f"  Bytes: {data_stream['bytes_received']}")
            if 'data' in data_stream:
                print(f"  Data: {data_stream['data']}")
    else:
        print("\n❌ No vehicle detection data found")
        print("💡 Suggestions:")
        print("  - Check camera configuration for webhook/API settings")
        print("  - Verify camera is detecting vehicles")
        print("  - Check if camera uses HTTP POST to send data")
        print("  - Try running the HTTP listener script")

if __name__ == "__main__":
    main()

