#!/usr/bin/env python3
"""
Continuous Display Data Sender - Sends display data continuously to port 80
"""

import sys
import os
import time
import socket
import threading
import signal
import logging
from datetime import datetime

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.services import build_cp5200_protocol, get_effect_code, get_alignment_code, get_color_code
from app.models import DisplayConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('continuous_display.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ContinuousDisplaySender:
    def __init__(self, target_ip='192.168.1.222', target_port=80, interval=5):
        """
        Initialize the continuous display sender
        
        Args:
            target_ip (str): Target IP address (default: localhost)
            target_port (int): Target port (default: 80)
            interval (int): Interval between sends in seconds (default: 5)
        """
        self.target_ip = target_ip
        self.target_port = target_port
        self.interval = interval
        self.running = False
        self.socket = None
        self.display_config = None
        self.message_counter = 0
        
    def setup_display_config(self):
        """Setup display configuration from database or create default"""
        try:
            # Try to get configuration from database
            self.display_config = DisplayConfig.objects.first()
            if not self.display_config:
                logger.warning("No display configuration found in database, using defaults")
                # Create a default configuration
                self.display_config = DisplayConfig(
                    ip_address='192.168.1.222',
                    port=self.target_port,
                    font_size=16,
                    effect_type='draw',
                    justify='center',
                    color='red',
                    test_message='ABC 1234'
                )
        except Exception as e:
            logger.error(f"Error setting up display config: {e}")
            # Create a minimal default config
            self.display_config = DisplayConfig(
                ip_address=self.target_ip,
                port=self.target_port,
                font_size=16,
                effect_type='draw',
                justify='center',
                color='red',
                                    test_message='ABC 1234'
            )
    
    def create_czech_license_plate(self):
        """Create a Czech license plate with timestamp and counter"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.message_counter += 1
        
        # Czech license plate format: ABC 1234 (3 letters + space + 4 digits)
        import random
        import string
        
        # Generate random letters (A-Z)
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        
        # Generate random digits (0-9)
        digits = ''.join(random.choices(string.digits, k=4))
        
        # Format: ABC 1234
        license_plate = f"{letters} {digits}"
        
        return license_plate
    
    def send_display_data(self, message):
        """Send display data to the target port"""
        try:
            # Build protocol data
            protocol_data = build_cp5200_protocol(message, self.display_config)
            
            # Create socket and send data
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(10)  # 10 second timeout
                sock.connect((self.target_ip, self.target_port))
                sock.sendall(protocol_data)
                
                logger.info(f"Sent to {self.target_ip}:{self.target_port} - Message: '{message}'")
                logger.debug(f"Protocol data: {protocol_data.hex()}")
                
        except socket.timeout:
            logger.warning(f"Timeout connecting to {self.target_ip}:{self.target_port}")
        except ConnectionRefusedError:
            logger.warning(f"Connection refused to {self.target_ip}:{self.target_port}")
        except Exception as e:
            logger.error(f"Error sending display data: {e}")
    
    def start_continuous_sending(self):
        """Start continuous sending of display data"""
        logger.info(f"Starting continuous display sender to {self.target_ip}:{self.target_port}")
        logger.info(f"Interval: {self.interval} seconds")
        
        self.running = True
        
        while self.running:
            try:
                # Create Czech license plate
                message = self.create_czech_license_plate()
                
                # Send the message
                self.send_display_data(message)
                
                # Wait for next interval
                time.sleep(self.interval)
                
            except KeyboardInterrupt:
                logger.info("Received keyboard interrupt, stopping...")
                break
            except Exception as e:
                logger.error(f"Error in continuous sending loop: {e}")
                time.sleep(1)  # Brief pause before retrying
        
        logger.info("Continuous display sender stopped")
    
    def stop(self):
        """Stop the continuous sending"""
        self.running = False
        logger.info("Stopping continuous display sender...")

def signal_handler(signum, frame):
    """Handle system signals for graceful shutdown"""
    logger.info(f"Received signal {signum}, shutting down...")
    if hasattr(signal_handler, 'sender'):
        signal_handler.sender.stop()
    sys.exit(0)

def main():
    """Main function to run the continuous display sender"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Continuous Display Data Sender')
    parser.add_argument('--ip', default='192.168.1.222', help='Target IP address (default: 192.168.1.222)')
    parser.add_argument('--port', type=int, default=80, help='Target port (default: 80)')
    parser.add_argument('--interval', type=int, default=5, help='Interval between sends in seconds (default: 5)')
    parser.add_argument('--test', action='store_true', help='Run a single test send instead of continuous')
    
    args = parser.parse_args()
    
    # Create sender instance
    sender = ContinuousDisplaySender(
        target_ip=args.ip,
        target_port=args.port,
        interval=args.interval
    )
    
    # Setup display configuration
    sender.setup_display_config()
    
    # Setup signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal_handler.sender = sender
    
    if args.test:
        # Run a single test
        logger.info("Running single test send...")
        test_message = sender.create_czech_license_plate()
        sender.send_display_data(test_message)
        logger.info("Test completed")
    else:
        # Start continuous sending
        sender.start_continuous_sending()

if __name__ == "__main__":
    main() 