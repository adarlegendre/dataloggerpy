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
                print(f"\n📡 POST request received: {self.path}")
                
                if self.path == '/api/upark/capture' or self.path == '/NotificationInfo/TollgateInfo':
                    self.handle_camera_capture()
                else:
                    print(f"❌ Unknown endpoint: {self.path}")
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b'Not Found')
            
            def handle_camera_capture(self):
                """Handle camera capture data - following the C# flow"""
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
                        request_body = post_data.decode('utf-8')
                        
                        # Parse JSON
                        try:
                            json_data = json.loads(request_body)
                            print(f"📋 JSON data received:")
                            print(json.dumps(json_data, indent=2))
                            
                            # Extract data following the C# flow
                            device_id = None
                            plate_number = None
                            vehicle_type = None
                            picture_name = None
                            
                            # Extract device ID
                            if 'deviceId' in json_data:
                                device_id = json_data['deviceId']
                            elif 'params' in json_data and 'deviceId' in json_data['params']:
                                device_id = json_data['params']['deviceId']
                            
                            # Extract plate number (following the C# logic)
                            if 'params' in json_data and 'plateNo' in json_data['params']:
                                plate_number = json_data['params']['plateNo']
                                if plate_number:
                                    plate_number = str(plate_number).strip('{}')  # Remove curly braces
                            
                            # Extract vehicle type
                            if 'params' in json_data and 'vehicleType' in json_data['params']:
                                vehicle_type = json_data['params']['vehicleType']
                            
                            # Extract picture name
                            if 'params' in json_data and 'picInfo' in json_data['params']:
                                pic_info = json_data['params']['picInfo']
                                if pic_info and len(pic_info) > 0:
                                    picture_name = pic_info[0].get('url', '')
                            
                            # Extract other info
                            confidence = json_data['params'].get('confidence') if 'params' in json_data else None
                            pic_time = json_data['params'].get('picTime') if 'params' in json_data else None
                            
                            print(f"\n🚗 *** VEHICLE DETECTION DATA ***")
                            print(f"🚗 *** VEHICLE DETECTION DATA ***")
                            print(f"🚗 *** VEHICLE DETECTION DATA ***")
                            print(f"   Device ID: {device_id}")
                            print(f"   Plate Number: {plate_number}")
                            print(f"   Vehicle Type: {vehicle_type}")
                            print(f"   Confidence: {confidence}")
                            print(f"   Picture Time: {pic_time}")
                            print(f"   Picture Name: {picture_name}")
                            
                            # Process if we have a plate number (following C# logic)
                            if plate_number and plate_number.strip():
                                print("🚗 Calling processExitting...")
                                # Here you would call your Django processing function
                                # Task.Run(() => processExitting(serverUrl, plateNumber))
                                
                                # Store the detection
                                vehicle_info = {
                                    'device_id': device_id,
                                    'plate_number': plate_number,
                                    'vehicle_type': vehicle_type,
                                    'confidence': confidence,
                                    'pic_time': pic_time,
                                    'picture_name': picture_name
                                }
                                
                                self.listener.received_data.append({
                                    'timestamp': timestamp,
                                    'client_ip': client_ip,
                                    'path': self.path,
                                    'json_data': json_data,
                                    'vehicle_info': vehicle_info,
                                    'raw_data': post_data
                                })
                                
                                print(f"📊 Total detections: {len(self.listener.received_data)}")
                            else:
                                print("⚠️  No plate number found, skipping processing")
                            
                            # Show picture information if available
                            if picture_name:
                                print("📸 Picture Information:")
                                print(f"   Picture Name: {picture_name}")
                            
                        except json.JSONDecodeError as e:
                            print(f"❌ JSON decode error: {e}")
                            print(f"📄 Raw data: {request_body}")
                            
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
                    
                    # Send response back to camera (following C# response format)
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    
                    response_message = {"Result": True, "Message": "Success"}
                    json_response = json.dumps(response_message)
                    self.wfile.write(json_response.encode())
                    
                except Exception as e:
                    print(f"❌ Error handling camera capture: {e}")
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
