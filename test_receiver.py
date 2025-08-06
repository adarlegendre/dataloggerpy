#!/usr/bin/env python3
"""
Test Receiver - Simple HTTP server to receive display data on port 80
"""

import socket
import threading
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TestReceiver:
    def __init__(self, host='0.0.0.0', port=80):
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        self.received_data = []
        
    def start_server(self):
        """Start the test receiver server"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            
            logger.info(f"Test receiver started on {self.host}:{self.port}")
            logger.info("Waiting for connections...")
            
            self.running = True
            
            while self.running:
                try:
                    client_socket, address = self.server_socket.accept()
                    logger.info(f"Connection from {address}")
                    
                    # Handle client in separate thread
                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_socket, address)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                    
                except Exception as e:
                    if self.running:
                        logger.error(f"Error accepting connection: {e}")
                        
        except Exception as e:
            logger.error(f"Error starting server: {e}")
        finally:
            if self.server_socket:
                self.server_socket.close()
    
    def handle_client(self, client_socket, address):
        """Handle individual client connection"""
        try:
            # Receive data
            data = client_socket.recv(1024)
            if data:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Store received data
                self.received_data.append({
                    'timestamp': timestamp,
                    'address': address,
                    'data': data,
                    'hex_data': data.hex(),
                    'length': len(data)
                })
                
                # Log the received data
                logger.info(f"Received from {address}:")
                logger.info(f"  Length: {len(data)} bytes")
                logger.info(f"  Hex: {data.hex()}")
                
                # Try to decode as text (for debugging)
                try:
                    text_data = data.decode('ascii', errors='ignore')
                    logger.info(f"  Text: {repr(text_data)}")
                except:
                    logger.info("  Text: (binary data)")
                
                # Send simple response
                response = b"HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n"
                client_socket.send(response)
                
        except Exception as e:
            logger.error(f"Error handling client {address}: {e}")
        finally:
            client_socket.close()
    
    def stop(self):
        """Stop the server"""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        logger.info("Test receiver stopped")
    
    def get_received_data(self):
        """Get list of received data"""
        return self.received_data.copy()
    
    def print_summary(self):
        """Print summary of received data"""
        logger.info(f"Total received packets: {len(self.received_data)}")
        for i, packet in enumerate(self.received_data[-10:], 1):  # Show last 10
            logger.info(f"  {i}. {packet['timestamp']} - {packet['length']} bytes from {packet['address']}")

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Test Receiver for Display Data')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=80, help='Port to listen on (default: 80)')
    
    args = parser.parse_args()
    
    # Check if port 80 requires admin privileges
    if args.port == 80:
        logger.warning("Port 80 may require administrator privileges on some systems")
        logger.warning("If you get permission denied, try running with sudo or use a different port")
    
    receiver = TestReceiver(host=args.host, port=args.port)
    
    try:
        receiver.start_server()
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt, shutting down...")
        receiver.stop()
    except Exception as e:
        logger.error(f"Error: {e}")
        receiver.stop()

if __name__ == "__main__":
    main() 