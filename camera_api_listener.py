#!/usr/bin/env python3
"""
Camera API Listener - HTTP server to receive POST requests from camera at 192.168.2.13
Server runs at 192.168.2.101:5000 with authentication (admin/kObliha12@)
"""

import json
import threading
import time
import base64
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

class CameraAPIListener:
    def __init__(self, port=5000):
        self.port = port
        self.username = "admin"
        self.password = "kObliha12@"
        self.received_data = []
        self.server = None
        self.running = False
        
    def create_handler(self):
        """Create HTTP request handler for camera API"""
        
        class CameraAPIHandler(BaseHTTPRequestHandler):
            def __init__(self, *args, listener_instance=None, **kwargs):
                self.listener = listener_instance
                super().__init__(*args, **kwargs)
            
            def log_message(self, format, *args):
                pass  # Suppress default logging
            
            def check_auth(self):
                """Check HTTP Basic Authentication"""
                auth_header = self.headers.get('Authorization')
                if not auth_header or not auth_header.startswith('Basic '):
                    return False
                
                try:
                    encoded_credentials = auth_header[6:]
                    decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
                    username, password = decoded_credentials.split(':', 1)
                    return username == self.listener.username and password == self.listener.password
                except:
                    return False
            
            def send_auth_required(self):
                """Send 401 Unauthorized response"""
                self.send_response(401)
                self.send_header('WWW-Authenticate', 'Basic realm="Camera API"')
                self.end_headers()
                self.wfile.write(b'Authentication required')
            
            def do_POST(self):
                """Handle POST requests from camera"""
                print(f"\n{'='*70}")
                print(f"[POST] Request from {self.client_address[0]}: {self.path}")
                print(f"[TIME] {datetime.now()}")
                print(f"{'='*70}")
                
                # Log all headers
                print(f"[HEADERS]:")
                for header, value in self.headers.items():
                    print(f"  {header}: {value}")
                
                # Registration endpoint may not require auth initially
                if self.path == '/VIID/System/Register':
                    print(f"[TYPE] Camera registration request")
                    self.handle_camera_register()
                    return
                
                # Keepalive
                if 'Keepalive' in self.path or 'keepalive' in self.path:
                    print(f"[TYPE] Keepalive/Heartbeat request")
                    self.handle_keepalive()
                    return
                
                # Subscription
                if 'Subscribe' in self.path or 'subscribe' in self.path:
                    print(f"[TYPE] Subscription request")
                    self.handle_subscription()
                    return
                
                # Accept ALL OTHER POST requests and log them (no auth required for debugging)
                print(f"[TYPE] Unknown/Vehicle Data endpoint")
                self.handle_any_request()
                return
            
            def do_GET(self):
                """Handle GET requests"""
                print(f"\n{'='*70}")
                print(f"[GET] Request from {self.client_address[0]}: {self.path}")
                print(f"{'='*70}")
                
                if self.path == '/status':
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    
                    status = {
                        'status': 'running',
                        'detections_received': len(self.listener.received_data),
                        'server_time': datetime.now().isoformat()
                    }
                    
                    self.wfile.write(json.dumps(status, indent=2).encode())
                else:
                    # Log all GET requests too
                    print(f"[INFO] GET request to: {self.path}")
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'OK')
            
            def handle_camera_register(self):
                """Handle camera registration request"""
                try:
                    content_length = int(self.headers.get('Content-Length', 0))
                    print(f"[CONTENT-LENGTH] {content_length} bytes")
                    
                    if content_length > 0:
                        post_data = self.rfile.read(content_length)
                        request_body = post_data.decode('utf-8')
                        
                        # Log raw registration data
                        print(f"\n[RAW REGISTRATION DATA]")
                        print("=" * 60)
                        print(request_body)
                        print("=" * 60)
                        
                        try:
                            json_data = json.loads(request_body)
                            print(f"[REGISTER JSON]:")
                            print(json.dumps(json_data, indent=2))
                        except json.JSONDecodeError as e:
                            print(f"[ERROR] JSON decode error: {e}")
                    
                    # Send success response for registration
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = json.dumps({"ResultCode": 0, "Message": "Success"})
                    self.wfile.write(response.encode())
                    print(f"[REGISTER] Registration accepted")
                    
                except Exception as e:
                    print(f"[ERROR] Registration error: {e}")
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(f'Error: {str(e)}'.encode())
            
            def handle_keepalive(self):
                """Handle keepalive/heartbeat request"""
                try:
                    content_length = int(self.headers.get('Content-Length', 0))
                    if content_length > 0:
                        post_data = self.rfile.read(content_length)
                        print(f"[KEEPALIVE DATA] {post_data.decode('utf-8', errors='ignore')}")
                    
                    # Send success response
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = json.dumps({"ResultCode": 0, "Message": "Success"})
                    self.wfile.write(response.encode())
                    print(f"[KEEPALIVE] Acknowledged")
                except Exception as e:
                    print(f"[ERROR] Keepalive error: {e}")
                    self.send_response(200)
                    self.end_headers()
            
            def handle_subscription(self):
                """Handle subscription request"""
                try:
                    content_length = int(self.headers.get('Content-Length', 0))
                    if content_length > 0:
                        post_data = self.rfile.read(content_length)
                        request_body = post_data.decode('utf-8')
                        print(f"\n[SUBSCRIPTION DATA]")
                        print("=" * 60)
                        print(request_body)
                        print("=" * 60)
                    
                    # Send success response with subscription ID
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = json.dumps({
                        "ResultCode": 0, 
                        "Message": "Success",
                        "SubscribeID": "SUB_001"
                    })
                    self.wfile.write(response.encode())
                    print(f"[SUBSCRIPTION] Accepted")
                except Exception as e:
                    print(f"[ERROR] Subscription error: {e}")
                    self.send_response(200)
                    self.end_headers()
            
            def handle_any_request(self):
                """Handle any POST request and log everything"""
                try:
                    content_length = int(self.headers.get('Content-Length', 0))
                    print(f"[CONTENT-LENGTH] {content_length} bytes")
                    
                    if content_length > 0:
                        post_data = self.rfile.read(content_length)
                        request_body = post_data.decode('utf-8')
                        
                        # Log raw data from ANY endpoint
                        print(f"\n[RAW DATA FROM {self.path}]")
                        print("=" * 60)
                        print(request_body)
                        print("=" * 60)
                        
                        try:
                            json_data = json.loads(request_body)
                            print(f"[JSON PARSED]:")
                            print(json.dumps(json_data, indent=2))
                            
                            # Try to find plate number anywhere in the JSON
                            self.search_for_plate(json_data)
                            
                        except json.JSONDecodeError as e:
                            print(f"[WARNING] Not JSON format: {e}")
                    else:
                        print(f"[INFO] Empty request body")
                    
                    # Always send success response
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = json.dumps({"Result": True, "ResultCode": 0, "Message": "Success"})
                    self.wfile.write(response.encode())
                    print(f"[RESPONSE] Success sent")
                    
                except Exception as e:
                    print(f"[ERROR] {e}")
                    self.send_response(200)  # Still send 200 to keep camera happy
                    self.end_headers()
            
            def search_for_plate(self, data, path=""):
                """Recursively search for plate number in JSON"""
                if isinstance(data, dict):
                    for key, value in data.items():
                        if 'plate' in key.lower() or 'number' in key.lower():
                            print(f"[FOUND] {path}.{key} = {value}")
                        self.search_for_plate(value, f"{path}.{key}")
                elif isinstance(data, list):
                    for i, item in enumerate(data):
                        self.search_for_plate(item, f"{path}[{i}]")
        
        return CameraAPIHandler
    
    def start_server(self):
        """Start HTTP server to listen for camera data"""
        print(f"Starting Camera API Listener on port {self.port}...")
        print(f"Authentication: {self.username} / {self.password}")
        print(f"Endpoint: http://192.168.2.101:{self.port}/api/upark/capture")
        
        try:
            handler_class = self.create_handler()
            
            def handler(*args, **kwargs):
                return handler_class(*args, listener_instance=self, **kwargs)
            
            self.server = HTTPServer(('', self.port), handler)
            server_thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            server_thread.start()
            
            print(f"[OK] Server started on port {self.port}")
            print(f"[LISTEN] Waiting for camera POST requests...")
            print(f"[INFO] Press Ctrl+C to stop")
            print("=" * 60)
            print("\n[WAITING] Camera should now send vehicle detection data")
            print("[TIP] If no data arrives:")
            print("  1. Check camera web interface (http://192.168.2.13)")
            print("  2. Enable 'Upload to Platform' in settings")
            print("  3. Enable 'Upload Recognition Result' in ANPR settings")
            print("  4. Set trigger mode to 'Continuous' for testing")
            print("  5. See CAMERA_TROUBLESHOOTING.md for details")
            print("=" * 60)
            
            self.running = True
            
            # Monitor for data
            last_count = 0
            while self.running:
                time.sleep(10)
                current_count = len(self.received_data)
                if current_count != last_count:
                    print(f"[STATUS] {current_count} detections received")
                    last_count = current_count
                
        except Exception as e:
            print(f"[ERROR] Failed to start server: {e}")
    
    def stop_server(self):
        """Stop the HTTP server"""
        self.running = False
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            print("[STOP] Server stopped")
    
    def show_summary(self):
        """Show summary of received data"""
        print(f"\n[SUMMARY] Total detections: {len(self.received_data)}")
        
        if self.received_data:
            print(f"  First: {self.received_data[0]['timestamp']}")
            print(f"  Last: {self.received_data[-1]['timestamp']}")
            
            print(f"\n[DETECTIONS] Recent vehicles:")
            for i, data in enumerate(self.received_data[-5:]):
                info = data['vehicle_info']
                print(f"  {i+1}. {info['plate_number']} - {info['vehicle_type']} ({info['confidence']}%)")

def main():
    print("=== Camera API Listener ===\n")
    print("Camera (Client): 192.168.2.13")
    print("Server: 192.168.2.101:5000")
    print("Auth: admin / kObliha12@\n")
    
    port_input = input(f"Enter listener port [5000]: ").strip()
    port = int(port_input) if port_input else 5000
    
    listener = CameraAPIListener(port)
    
    try:
        listener.start_server()
    except KeyboardInterrupt:
        print("\n[STOP] Stopped by user")
    finally:
        listener.stop_server()
        listener.show_summary()

if __name__ == "__main__":
    main()
