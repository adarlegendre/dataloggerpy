#!/usr/bin/env python3
"""
Camera Network Scanner - Scan for camera server ports and test connections
"""

import socket
import threading
import time
import json
from datetime import datetime

class CameraNetworkScanner:
    def __init__(self, target_ip="192.168.2.13"):
        self.target_ip = target_ip
        self.open_ports = []
        self.common_ports = [
            80, 8080, 8000, 8001, 8002, 8003,  # Web servers
            5000, 5001, 5002, 5003,             # Flask/FastAPI
            3000, 3001, 3002, 3003,             # Node.js
            9000, 9001, 9002, 9003,             # Custom apps
            8081, 8082, 8083, 8084,             # Alternative web
            9999, 9998, 9997, 9996,             # Custom protocols
            4444, 4445, 4446, 4447,             # Camera protocols
            7777, 7778, 7779, 7780,             # Custom data
            1234, 1235, 1236, 1237,             # Common custom
            8888, 8889, 8890, 8891,             # Alternative
        ]
        
    def scan_port(self, port, timeout=2):
        """Scan a single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((self.target_ip, port))
            sock.close()
            
            if result == 0:
                return True, None
            else:
                return False, None
        except Exception as e:
            return False, str(e)
    
    def scan_ports(self, start_port=1, end_port=65535, max_threads=100):
        """Scan a range of ports with threading"""
        print(f"🔍 Scanning {self.target_ip} for open ports...")
        print(f"📡 Scanning ports {start_port}-{end_port} with {max_threads} threads")
        
        open_ports = []
        threads = []
        
        def scan_port_range(port_list):
            for port in port_list:
                is_open, error = self.scan_port(port)
                if is_open:
                    open_ports.append(port)
                    print(f"✅ Port {port} is OPEN")
                elif port in self.common_ports:  # Only show errors for common ports
                    print(f"❌ Port {port} closed: {error}")
        
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
        
        self.open_ports = sorted(open_ports)
        return self.open_ports
    
    def scan_common_ports(self):
        """Quick scan of common ports"""
        print(f"🚀 Quick scan of common ports on {self.target_ip}...")
        
        open_ports = []
        for port in self.common_ports:
            is_open, error = self.scan_port(port, timeout=3)
            if is_open:
                open_ports.append(port)
                print(f"✅ Port {port} is OPEN")
            else:
                print(f"❌ Port {port} closed")
        
        self.open_ports = open_ports
        return open_ports
    
    def test_http_connection(self, port):
        """Test if port responds to HTTP requests"""
        try:
            import requests
            url = f"http://{self.target_ip}:{port}"
            response = requests.get(url, timeout=5)
            return True, response.status_code, response.text[:200]
        except requests.exceptions.RequestException as e:
            return False, None, str(e)
        except ImportError:
            return False, None, "requests module not available"
    
    def test_tcp_connection(self, port):
        """Test raw TCP connection and try to read data"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((self.target_ip, port))
            
            # Try to read any initial data
            sock.settimeout(2)
            try:
                data = sock.recv(1024)
                if data:
                    return True, f"Received {len(data)} bytes", data[:100]
                else:
                    return True, "Connected but no data", None
            except socket.timeout:
                return True, "Connected but no immediate data", None
            finally:
                sock.close()
                
        except Exception as e:
            return False, None, str(e)
    
    def analyze_open_ports(self):
        """Analyze open ports to determine which might be the camera server"""
        if not self.open_ports:
            print("❌ No open ports found")
            return
        
        print(f"\n🔍 Analyzing {len(self.open_ports)} open ports...")
        
        for port in self.open_ports:
            print(f"\n📡 Testing port {port}:")
            
            # Test HTTP
            is_http, status, response = self.test_http_connection(port)
            if is_http:
                print(f"  ✅ HTTP server detected (status: {status})")
                print(f"  📄 Response preview: {response}")
            else:
                print(f"  ❌ Not an HTTP server: {response}")
            
            # Test raw TCP
            is_tcp, message, data = self.test_tcp_connection(port)
            if is_tcp:
                print(f"  ✅ TCP connection successful: {message}")
                if data:
                    print(f"  📄 Data preview: {data}")
            else:
                print(f"  ❌ TCP connection failed: {data}")
    
    def get_port_info(self, port):
        """Get information about a specific port"""
        port_info = {
            80: "HTTP (Web Server)",
            8080: "HTTP Alternative",
            8000: "HTTP Development",
            5000: "Flask/FastAPI",
            3000: "Node.js",
            9000: "Custom Application",
            8081: "HTTP Alternative",
            9999: "Custom Protocol",
            4444: "Camera Protocol",
            7777: "Custom Data",
            1234: "Custom Application",
            8888: "HTTP Alternative",
        }
        
        return port_info.get(port, "Unknown/Private Port")

def main():
    print("=== Camera Network Scanner ===\n")
    
    scanner = CameraNetworkScanner("192.168.2.13")
    
    # Quick scan of common ports first
    print("🚀 Step 1: Quick scan of common ports...")
    open_ports = scanner.scan_common_ports()
    
    if open_ports:
        print(f"\n✅ Found {len(open_ports)} open ports: {open_ports}")
        
        # Analyze the open ports
        scanner.analyze_open_ports()
        
        # Suggest likely camera ports
        print(f"\n🎯 Likely camera server ports:")
        for port in open_ports:
            info = scanner.get_port_info(port)
            print(f"  Port {port}: {info}")
    else:
        print("\n❌ No common ports found open")
        print("🔍 Would you like to do a full port scan? (This will take longer)")
        response = input("Full scan? (y/n): ")
        
        if response.lower() == 'y':
            print("\n🚀 Step 2: Full port scan...")
            open_ports = scanner.scan_ports(1, 65535, 50)
            if open_ports:
                print(f"\n✅ Found {len(open_ports)} open ports: {open_ports}")
                scanner.analyze_open_ports()
            else:
                print("\n❌ No open ports found in full scan")

if __name__ == "__main__":
    main()

