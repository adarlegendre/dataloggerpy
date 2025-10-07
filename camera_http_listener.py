#!/usr/bin/env python3
"""
Camera HTTP Listener - Listen for HTTP-based vehicle/plate data from camera server
"""

import socket
import threading
import time
import json
import requests
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class CameraHTTPListener:
    def __init__(self, camera_ip="192.168.2.13", camera_port=80):
        self.camera_ip = camera_ip
        self.camera_port = camera_port
        self.received_data = []
        self.server = None
        self.server_thread = None
        self.listener_port = 8080  # Port for our HTTP listener
        
    def test_camera_http(self):
        """Test HTTP connection to camera and explore endpoints"""
        print(f"🔍 Testing HTTP connection to {self.camera_ip}:{self.camera_port}")
        
        try:
            # Test basic connection
            response = requests.get(f"http://{self.camera_ip}:{self.camera_port}", timeout=10)
            print(f"✅ HTTP connection successful (status: {response.status_code})")
            print(f"📄 Response length: {len(response.text)} characters")
            
            # Check for common API endpoints
            api_endpoints = [
                "/api", "/api/data", "/api/vehicles", "/api/plates", "/api/detection",
                "/data", "/vehicles", "/plates", "/detection", "/events",
                "/webhook", "/callback", "/notify", "/post", "/send",
                "/camera", "/anpr", "/license", "/numberplate"
            ]
            
            print(f"\n🔍 Testing common API endpoints...")
            found_endpoints = []
            
            for endpoint in api_endpoints:
                try:
                    url = f"http://{self.camera_ip}:{self.camera_port}{endpoint}"
                    resp = requests.get(url, timeout=5)
                    
                    if resp.status_code != 404:
                        found_endpoints.append({
                            'endpoint': endpoint,
                            'status': resp.status_code,
                            'content_type': resp.headers.get('content-type', 'unknown'),
                            'content_length': len(resp.text)
                        })
                        print(f"  ✅ {endpoint}: {resp.status_code} ({resp.headers.get('content-type', 'unknown')})")
                        
                        # If it's JSON, show preview
                        if 'json' in resp.headers.get('content-type', ''):
                            try:
                                data = resp.json()
                                print(f"     📄 JSON preview: {json.dumps(data, indent=2)[:200]}...")
                            except:
                                pass
                        
                except requests.exceptions.RequestException:
                    pass  # Endpoint not accessible
            
            if not found_endpoints:
                print("  ❌ No accessible API endpoints found")
            
            return found_endpoints
            
        except requests.exceptions.RequestException as e:
            print(f"❌ HTTP connection failed: {e}")
            return []
    
    def create_webhook_handler(self):
        """Create HTTP request handler for receiving camera data"""
        class CameraWebhookHandler(BaseHTTPRequestHandler):
            def __init__(self, *args, listener_instance=None, **kwargs):
                self.listener = listener_instance
                super().__init__(*args, **kwargs)
            
            def log_message(self, format, *args):
                # Suppress default logging
                pass
            
            def do_GET(self):
                """Handle GET requests"""
                timestamp = datetime.now()
                client_ip = self.client_address[0]
                
                print(f"📡 GET request from {client_ip}: {self.path}")
                
                # Parse query parameters
                parsed_url = urllib.parse.urlparse(self.path)
                query_params = urllib.parse.parse_qs(parsed_url.query)
                
                if query_params:
                    print(f"📋 Query parameters: {query_params}")
                
                # Send response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                response = {
                    'status': 'success',
                    'message': 'Camera data received',
                    'timestamp': timestamp.isoformat(),
                    'path': self.path,
                    'query_params': query_params
                }
                
                self.wfile.write(json.dumps(response).encode())
                
                # Store data if it looks like vehicle detection
                if self.is_vehicle_data(query_params):
                    self.listener.received_data.append({
                        'timestamp': timestamp,
                        'method': 'GET',
                        'path': self.path,
                        'query_params': query_params,
                        'client_ip': client_ip,
                        'data_type': 'vehicle_detection'
                    })
            
            def do_POST(self):
                """Handle POST requests"""
                timestamp = datetime.now()
                client_ip = self.client_address[0]
                content_length = int(self.headers.get('Content-Length', 0))
                
                print(f"📡 POST request from {client_ip}: {self.path}")
                print(f"📄 Content-Length: {content_length}")
                print(f"📋 Content-Type: {self.headers.get('Content-Type', 'unknown')}")
                
                # Read POST data
                post_data = self.rfile.read(content_length)
                
                # Try to parse as JSON
                json_data = None
                if post_data:
                    try:
                        json_data = json.loads(post_data.decode('utf-8'))
                        print(f"📋 JSON data: {json.dumps(json_data, indent=2)}")
                    except json.JSONDecodeError:
                        print(f"📄 Raw data: {post_data.decode('utf-8', errors='ignore')}")
                
                # Send response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                response = {
                    'status': 'success',
                    'message': 'Camera data received',
                    'timestamp': timestamp.isoformat(),
                    'path': self.path
                }
                
                self.wfile.write(json.dumps(response).encode())
                
                # Store data if it looks like vehicle detection
                if self.is_vehicle_data_from_post(json_data, post_data):
                    self.listener.received_data.append({
                        'timestamp': timestamp,
                        'method': 'POST',
                        'path': self.path,
                        'json_data': json_data,
                        'raw_data': post_data,
                        'client_ip': client_ip,
                        'data_type': 'vehicle_detection'
                    })
            
            def is_vehicle_data(self, query_params):
                """Check if GET parameters contain vehicle data"""
                vehicle_keywords = ['plate', 'number', 'license', 'vehicle', 'speed', 'direction', 'detection']
                for key, values in query_params.items():
                    if any(keyword in key.lower() for keyword in vehicle_keywords):
                        return True
                return False
            
            def is_vehicle_data_from_post(self, json_data, raw_data):
                """Check if POST data contains vehicle information"""
                if json_data:
                    vehicle_keywords = ['plate', 'number', 'license', 'vehicle', 'speed', 'direction', 'detection', 'confidence']
                    json_str = json.dumps(json_data).lower()
                    if any(keyword in json_str for keyword in vehicle_keywords):
                        return True
                
                # Check raw data for vehicle-related content
                if raw_data:
                    raw_str = raw_data.decode('utf-8', errors='ignore').lower()
                    vehicle_keywords = ['plate', 'number', 'license', 'vehicle', 'speed', 'direction', 'detection']
                    if any(keyword in raw_str for keyword in vehicle_keywords):
                        return True
                
                return False
        
        return CameraWebhookHandler
    
    def start_http_listener(self, port=8080):
        """Start HTTP server to receive camera data"""
        self.listener_port = port
        
        print(f"🚀 Starting HTTP listener on port {port}")
        print(f"📡 Camera will send data to: http://YOUR_IP:{port}/webhook")
        
        try:
            handler_class = self.create_webhook_handler()
            
            # Create handler with reference to listener instance
            def handler(*args, **kwargs):
                return handler_class(*args, listener_instance=self, **kwargs)
            
            self.server = HTTPServer(('', port), handler)
            self.server_thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            self.server_thread.start()
            
            print(f"✅ HTTP listener started on port {port}")
            print(f"📡 Waiting for camera data...")
            print(f"⏹️  Press Ctrl+C to stop")
            
            # Keep the main thread alive
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n⏹️  Stopping HTTP listener...")
                self.stop_listener()
                
        except Exception as e:
            print(f"❌ Failed to start HTTP listener: {e}")
    
    def stop_listener(self):
        """Stop the HTTP listener"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            print("🛑 HTTP listener stopped")
    
    def get_received_data(self):
        """Get all received data"""
        return self.received_data.copy()
    
    def clear_data(self):
        """Clear received data"""
        self.received_data.clear()
        print("🗑️  Cleared received data")
    
    def simulate_camera_data(self):
        """Simulate camera sending data to test the listener"""
        print(f"\n🧪 Testing listener with simulated camera data...")
        
        # Simulate GET request with vehicle data
        test_data = {
            'plate_number': 'ABC123',
            'confidence': 95.5,
            'timestamp': datetime.now().isoformat(),
            'speed': 45,
            'direction': 'north'
        }
        
        # Convert to query parameters
        params = urllib.parse.urlencode(test_data)
        
        try:
            response = requests.get(f"http://localhost:{self.listener_port}/webhook?{params}", timeout=5)
            print(f"✅ Simulated GET request sent (status: {response.status_code})")
        except Exception as e:
            print(f"❌ Simulated GET request failed: {e}")
        
        # Simulate POST request with vehicle data
        try:
            response = requests.post(
                f"http://localhost:{self.listener_port}/webhook",
                json=test_data,
                headers={'Content-Type': 'application/json'},
                timeout=5
            )
            print(f"✅ Simulated POST request sent (status: {response.status_code})")
        except Exception as e:
            print(f"❌ Simulated POST request failed: {e}")

def main():
    print("=== Camera HTTP Listener ===\n")
    
    camera_ip = "192.168.2.13"
    camera_port = 80
    
    listener = CameraHTTPListener(camera_ip, camera_port)
    
    # Test camera HTTP connection
    print("🔍 Step 1: Testing camera HTTP connection...")
    endpoints = listener.test_camera_http()
    
    if endpoints:
        print(f"\n✅ Found {len(endpoints)} accessible endpoints:")
        for endpoint in endpoints:
            print(f"  📡 {endpoint['endpoint']}: {endpoint['status']}")
    
    # Start HTTP listener
    print(f"\n🚀 Step 2: Starting HTTP listener...")
    
    # Get listener port
    listener_port = input(f"Enter listener port [8080]: ").strip()
    try:
        listener_port = int(listener_port) if listener_port else 8080
    except ValueError:
        listener_port = 8080
    
    print(f"\n📡 Instructions for camera configuration:")
    print(f"  📤 Camera should send data to: http://YOUR_IP:{listener_port}/webhook")
    print(f"  📤 Or any path like: http://YOUR_IP:{listener_port}/api/detection")
    print(f"  📤 Data format: JSON or URL parameters")
    
    # Test the listener
    test_input = input(f"\n🧪 Test listener with simulated data? (y/n): ")
    if test_input.lower() == 'y':
        # Start listener in background
        listener.server_thread = threading.Thread(
            target=listener.start_http_listener,
            args=(listener_port,),
            daemon=True
        )
        listener.server_thread.start()
        time.sleep(2)  # Give server time to start
        
        listener.simulate_camera_data()
        time.sleep(1)
        
        # Show received data
        data = listener.get_received_data()
        if data:
            print(f"\n📊 Received {len(data)} test data packets:")
            for i, item in enumerate(data):
                print(f"\n📦 Packet {i+1}:")
                print(f"  Time: {item['timestamp']}")
                print(f"  Method: {item['method']}")
                print(f"  Path: {item['path']}")
                if 'query_params' in item:
                    print(f"  Query Params: {item['query_params']}")
                if 'json_data' in item:
                    print(f"  JSON Data: {item['json_data']}")
        
        listener.stop_listener()
    else:
        # Start normal listener
        listener.start_http_listener(listener_port)
        
        # Show received data when stopped
        data = listener.get_received_data()
        if data:
            print(f"\n📊 Received {len(data)} data packets:")
            for i, item in enumerate(data):
                print(f"\n📦 Packet {i+1}:")
                print(f"  Time: {item['timestamp']}")
                print(f"  Method: {item['method']}")
                print(f"  Path: {item['path']}")
                if 'query_params' in item:
                    print(f"  Query Params: {item['query_params']}")
                if 'json_data' in item:
                    print(f"  JSON Data: {item['json_data']}")

if __name__ == "__main__":
    main()

