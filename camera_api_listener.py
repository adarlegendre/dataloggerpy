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
                print(f"\n[POST] Request from {self.client_address[0]}: {self.path}")
                
                # Check authentication
                if not self.check_auth():
                    print(f"[AUTH FAILED] {self.client_address[0]}")
                    self.send_auth_required()
                    return
                
                print(f"[AUTH OK]")
                
                if self.path in ['/api/upark/capture', '/NotificationInfo/TollgateInfo']:
                    self.handle_camera_capture()
                else:
                    print(f"[ERROR] Unknown endpoint: {self.path}")
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b'Not Found')
            
            def handle_camera_capture(self):
                """Handle camera capture data"""
                try:
                    content_length = int(self.headers.get('Content-Length', 0))
                    print(f"[CONTENT-LENGTH] {content_length} bytes")
                    
                    if content_length > 0:
                        post_data = self.rfile.read(content_length)
                        request_body = post_data.decode('utf-8')
                        
                        # Log raw data BEFORE processing
                        print(f"\n[RAW DATA RECEIVED]")
                        print("=" * 60)
                        print(request_body)
                        print("=" * 60)
                        
                        try:
                            json_data = json.loads(request_body)
                            print(f"[JSON] Data received:")
                            print(json.dumps(json_data, indent=2))
                            
                            # Extract data
                            device_id = json_data.get('deviceId')
                            params = json_data.get('params', {})
                            
                            plate_number = params.get('plateNo', '')
                            if plate_number:
                                plate_number = str(plate_number).strip('{}')  # Remove curly braces
                            
                            vehicle_type = params.get('vehicleType')
                            confidence = params.get('confidence')
                            pic_time = params.get('picTime')
                            
                            pic_info = params.get('picInfo', [])
                            picture_name = pic_info[0].get('url', '') if pic_info else ''
                            
                            print(f"\n*** VEHICLE DETECTION ***")
                            print(f"   Device ID: {device_id}")
                            print(f"   Plate Number: {plate_number}")
                            print(f"   Vehicle Type: {vehicle_type}")
                            print(f"   Confidence: {confidence}")
                            print(f"   Picture Time: {pic_time}")
                            print(f"   Picture Name: {picture_name}")
                            
                            # Process if plate number exists
                            if plate_number and plate_number.strip():
                                vehicle_info = {
                                    'device_id': device_id,
                                    'plate_number': plate_number,
                                    'vehicle_type': vehicle_type,
                                    'confidence': confidence,
                                    'pic_time': pic_time,
                                    'picture_name': picture_name
                                }
                                
                                self.listener.received_data.append({
                                    'timestamp': datetime.now(),
                                    'client_ip': self.client_address[0],
                                    'vehicle_info': vehicle_info,
                                    'json_data': json_data
                                })
                                
                                print(f"[STORED] Total detections: {len(self.listener.received_data)}")
                            else:
                                print("[WARNING] No plate number found")
                            
                        except json.JSONDecodeError as e:
                            print(f"[ERROR] JSON decode error: {e}")
                    else:
                        print("[WARNING] No content received")
                    
                    # Send success response
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = json.dumps({"Result": True, "Message": "Success"})
                    self.wfile.write(response.encode())
                    
                except Exception as e:
                    print(f"[ERROR] {e}")
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(f'Error: {str(e)}'.encode())
            
            def do_GET(self):
                """Handle GET requests"""
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
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b'Not Found')
        
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
