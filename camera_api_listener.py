#!/usr/bin/env python3
"""
Camera API Listener - HTTP server to receive POST requests from camera at /api/upark/capture
"""

import json
import threading
import time
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class CameraAPIListener:
    def __init__(self, port=5195):
        self.port = port
        self.received_data = []
        self.server = None
        self.server_thread = None
        self.running = False
        
    def create_handler(self):
        """Create HTTP request handler for camera API"""
        
        class CameraAPIHandler(BaseHTTPRequestHandler):
            def __init__(self, *args, listener_instance=None, **kwargs):
                self.listener = listener_instance
                super().__init__(*args, **kwargs)
            
            def log_message(self, format, *args):
                # Suppress default logging
                pass
            
            def do_POST(self):
                """Handle POST requests from camera"""
                if self.path == '/api/upark/capture':
                    self.handle_camera_capture()
                else:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b'Not Found')
            
            def handle_camera_capture(self):
                """Handle camera capture data"""
                try:
                    timestamp = datetime.now()
                    client_ip = self.client_address[0]
                    
                    print(f"\n📡 POST request from {client_ip} at {timestamp}")
                    print(f"📋 Path: {self.path}")
                    print(f"📄 Content-Type: {self.headers.get('Content-Type', 'unknown')}")
                    
                    # Get content length
                    content_length = int(self.headers.get('Content-Length', 0))
                    print(f"📦 Content-Length: {content_length}")
                    
                    if content_length > 0:
                        # Read POST data
                        post_data = self.rfile.read(content_length)
                        
                        # Try to parse as JSON
                        try:
                            json_data = json.loads(post_data.decode('utf-8'))
                            print(f"📋 JSON data received:")
                            print(json.dumps(json_data, indent=2))
                            
                            # Extract vehicle information
                            vehicle_info = self.extract_vehicle_info(json_data)
                            
                            if vehicle_info:
                                print(f"\n🚗 *** VEHICLE DETECTION DATA ***")
                                print(f"🚗 *** VEHICLE DETECTION DATA ***")
                                print(f"🚗 *** VEHICLE DETECTION DATA ***")
                                for key, value in vehicle_info.items():
                                    print(f"   {key}: {value}")
                                
                                # Store in listener
                                self.listener.received_data.append({
                                    'timestamp': timestamp,
                                    'client_ip': client_ip,
                                    'path': self.path,
                                    'json_data': json_data,
                                    'vehicle_info': vehicle_info,
                                    'raw_data': post_data
                                })
                                
                                print(f"📊 Total detections: {len(self.listener.received_data)}")
                            
                        except json.JSONDecodeError as e:
                            print(f"❌ JSON decode error: {e}")
                            print(f"📄 Raw data: {post_data.decode('utf-8', errors='ignore')}")
                            
                            # Store raw data anyway
                            self.listener.received_data.append({
                                'timestamp': timestamp,
                                'client_ip': client_ip,
                                'path': self.path,
                                'json_data': None,
                                'vehicle_info': None,
                                'raw_data': post_data,
                                'error': str(e)
                            })
                    else:
                        print("📦 No content received")
                    
                    # Send response back to camera
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    
                    response = {
                        'status': 'success',
                        'message': 'Vehicle detection data received',
                        'timestamp': timestamp.isoformat(),
                        'server': 'Django Integration Server'
                    }
                    
                    self.wfile.write(json.dumps(response).encode())
                    
                except Exception as e:
                    print(f"❌ Error handling camera capture: {e}")
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(f'Error: {str(e)}'.encode())
            
            def extract_vehicle_info(self, json_data):
                """Extract vehicle information from JSON"""
                vehicle_info = {}
                
                # Common field mappings for vehicle detection
                field_mappings = {
                    'plate_number': ['plate_number', 'plateNumber', 'license_plate', 'licensePlate', 'plate', 'number_plate', 'numberPlate'],
                    'confidence': ['confidence', 'score', 'accuracy', 'detection_confidence'],
                    'timestamp': ['timestamp', 'time', 'datetime', 'capture_time'],
                    'speed': ['speed', 'velocity', 'vehicle_speed'],
                    'direction': ['direction', 'bearing', 'vehicle_direction'],
                    'location': ['location', 'position', 'coordinates', 'gps'],
                    'vehicle_type': ['vehicle_type', 'vehicleType', 'type', 'class'],
                    'color': ['color', 'vehicle_color', 'vehicleColor'],
                    'make': ['make', 'brand', 'manufacturer'],
                    'model': ['model', 'vehicle_model'],
                    'image_url': ['image_url', 'imageUrl', 'image', 'photo', 'picture'],
                    'camera_id': ['camera_id', 'cameraId', 'device_id', 'deviceId']
                }
                
                def extract_nested_value(obj, keys):
                    """Extract value from nested object using key list"""
                    for key in keys:
                        if key in obj:
                            return obj[key]
                    return None
                
                # Extract fields
                for field, possible_keys in field_mappings.items():
                    value = extract_nested_value(json_data, possible_keys)
                    if value is not None:
                        vehicle_info[field] = value
                
                return vehicle_info if vehicle_info else None
            
            def do_GET(self):
                """Handle GET requests"""
                if self.path == '/status':
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    
                    status = {
                        'status': 'running',
                        'detections_received': len(self.listener.received_data),
                        'server_time': datetime.now().isoformat(),
                        'endpoints': ['/api/upark/capture']
                    }
                    
                    self.wfile.write(json.dumps(status, indent=2).encode())
                else:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b'Not Found')
        
        return CameraAPIHandler
    
    def start_server(self):
        """Start HTTP server to listen for camera data"""
        print(f"🚀 Starting Camera API Listener...")
        print(f"📡 Port: {self.port}")
        print(f"📋 Endpoint: http://YOUR_IP:{self.port}/api/upark/capture")
        print(f"📋 Status: http://localhost:{self.port}/status")
        
        try:
            handler_class = self.create_handler()
            
            # Create handler with reference to listener instance
            def handler(*args, **kwargs):
                return handler_class(*args, listener_instance=self, **kwargs)
            
            self.server = HTTPServer(('', self.port), handler)
            self.server_thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            self.server_thread.start()
            
            print(f"✅ HTTP server started on port {self.port}")
            print(f"📡 Waiting for camera POST requests...")
            print(f"⏹️  Press Ctrl+C to stop")
            print("=" * 60)
            
            self.running = True
            
            # Monitor for data
            last_count = 0
            while self.running:
                time.sleep(10)
                
                current_count = len(self.received_data)
                if current_count != last_count:
                    print(f"📊 Status: {current_count} detections received")
                    last_count = current_count
                
        except Exception as e:
            print(f"❌ Failed to start server: {e}")
    
    def stop_server(self):
        """Stop the HTTP server"""
        self.running = False
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            print("🛑 HTTP server stopped")
    
    def get_received_data(self):
        """Get all received data"""
        return self.received_data.copy()
    
    def show_summary(self):
        """Show summary of received data"""
        print(f"\n📊 Camera API Summary:")
        print(f"  Total detections: {len(self.received_data)}")
        
        if self.received_data:
            print(f"  First detection: {self.received_data[0]['timestamp']}")
            print(f"  Last detection: {self.received_data[-1]['timestamp']}")
            
            # Show recent detections
            print(f"\n🚗 Recent Vehicle Detections:")
            for i, data in enumerate(self.received_data[-5:]):  # Last 5
                print(f"\n  Detection {i+1}:")
                print(f"    Time: {data['timestamp']}")
                print(f"    Client: {data['client_ip']}")
                if data['vehicle_info']:
                    for key, value in data['vehicle_info'].items():
                        print(f"    {key}: {value}")
                else:
                    print(f"    Raw data: {data.get('raw_data', b'').decode('utf-8', errors='ignore')[:100]}...")

def main():
    print("=== Camera API Listener ===\n")
    
    print("📷 Camera Configuration:")
    print("  IP: 192.168.2.13")
    print("  Port: 5000")
    print("  Endpoint: /api/upark/capture")
    print("  Method: POST")
    print("  Format: JSON")
    
    # Get listener port
    port_input = input(f"\nEnter listener port [5195]: ").strip()
    try:
        port = int(port_input) if port_input else 5195
    except ValueError:
        port = 5195
    
    print(f"\n📋 Camera should send data to: http://YOUR_IP:{port}/api/upark/capture")
    print(f"📋 You can check status at: http://localhost:{port}/status")
    
    listener = CameraAPIListener(port)
    
    try:
        listener.start_server()
    except KeyboardInterrupt:
        print("\n⏹️  Stopped by user")
    finally:
        listener.stop_server()
        listener.show_summary()
        
        # Show results
        data = listener.get_received_data()
        if data:
            print(f"\n🎉 Successfully received {len(data)} vehicle detections!")
            print("📋 This data is ready for Django integration")
        else:
            print(f"\n📊 No vehicle detections received")
            print("💡 Make sure the camera is configured to send data to the correct endpoint")

if __name__ == "__main__":
    main()
