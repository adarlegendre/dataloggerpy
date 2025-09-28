#!/usr/bin/env python3
"""
Enhanced Serial Radar Reader
Handles A+XXX/A-XXX format speed data from radar sensors
Integrates with existing Django radar logging system
"""

import serial
import time
import threading
import queue
from typing import Optional, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SerialRadarReader:
    """
    Serial radar reader that handles A+XXX/A-XXX format data
    """
    
    def __init__(self, port: str = '/dev/ttyAMA0', baudrate: int = 9600, timeout: float = 0.01):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser: Optional[serial.Serial] = None
        self.buffer = b''
        self.running = False
        self.data_queue = queue.Queue()
        self.reader_thread: Optional[threading.Thread] = None
        
        # Statistics
        self.total_readings = 0
        self.valid_readings = 0
        self.zero_readings = 0
        self.last_speed = 0
        self.last_direction = None
        
    def connect(self) -> bool:
        """Connect to the serial port"""
        try:
            self.ser = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            logger.info(f"Connected to radar on {self.port} at {self.baudrate} baud")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to {self.port}: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from the serial port"""
        if self.ser and self.ser.is_open:
            self.ser.close()
            logger.info("Disconnected from radar")
    
    def parse_radar_data(self, data: bytes) -> Optional[Dict[str, Any]]:
        """
        Parse radar data in A+XXX/A-XXX format
        
        Args:
            data: Raw bytes from serial port
            
        Returns:
            Dictionary with parsed data or None if invalid
        """
        try:
            # Decode the data
            decoded = data.decode('utf-8', errors='ignore').strip()
            
            # Check if it's the expected format (A+XXX or A-XXX)
            if len(decoded) == 5 and decoded.startswith('A') and decoded[1] in '+-':
                direction_sign = decoded[1]  # + or -
                speed_str = decoded[2:]      # XXX (3 digits)
                
                # Parse speed value
                speed = int(speed_str)
                
                # Determine direction
                direction = "Towards Village" if direction_sign == '+' else "Towards Town"
                
                # Determine if vehicle is present
                vehicle_present = speed != 0
                
                # Update statistics
                self.total_readings += 1
                if vehicle_present:
                    self.valid_readings += 1
                else:
                    self.zero_readings += 1
                
                # Store last values
                self.last_speed = speed
                self.last_direction = direction
                
                return {
                    'raw_data': decoded,
                    'speed': speed,
                    'direction': direction,
                    'direction_sign': direction_sign,
                    'vehicle_present': vehicle_present,
                    'timestamp': time.time(),
                    'display_text': f"[{direction}] Speed: {speed}km/h" if vehicle_present else f"[{direction}] No vehicle (0km/h)"
                }
                
        except (ValueError, IndexError) as e:
            logger.warning(f"Failed to parse radar data '{data}': {e}")
            
        return None
    
    def _reader_thread(self):
        """Background thread for reading serial data"""
        logger.info("Starting serial reader thread")
        
        while self.running and self.ser and self.ser.is_open:
            try:
                # Read data in chunks
                data = self.ser.read(32)
                if data:
                    self.buffer += data
                    
                    # Process complete messages (5 bytes each: A+XXX or A-XXX)
                    while len(self.buffer) >= 5:
                        chunk = self.buffer[:5]
                        self.buffer = self.buffer[5:]
                        
                        # Parse the data
                        parsed_data = self.parse_radar_data(chunk)
                        if parsed_data:
                            # Only process non-zero readings or when transitioning from non-zero to zero
                            if parsed_data['vehicle_present'] or self.last_speed != 0:
                                self.data_queue.put(parsed_data)
                                logger.debug(f"Received: {parsed_data['raw_data']} -> {parsed_data['display_text']}")
                
                # Small sleep to prevent excessive CPU usage
                time.sleep(0.001)
                
            except Exception as e:
                logger.error(f"Error in reader thread: {e}")
                break
        
        logger.info("Serial reader thread stopped")
    
    def start_reading(self) -> bool:
        """Start reading from the serial port"""
        if not self.connect():
            return False
        
        self.running = True
        self.reader_thread = threading.Thread(target=self._reader_thread, daemon=True)
        self.reader_thread.start()
        
        logger.info("Started reading radar data")
        return True
    
    def stop_reading(self):
        """Stop reading from the serial port"""
        self.running = False
        
        if self.reader_thread:
            self.reader_thread.join(timeout=2)
        
        self.disconnect()
        logger.info("Stopped reading radar data")
    
    def get_data(self, timeout: float = 0.1) -> Optional[Dict[str, Any]]:
        """
        Get the next available data point
        
        Args:
            timeout: Maximum time to wait for data
            
        Returns:
            Parsed radar data or None if no data available
        """
        try:
            return self.data_queue.get(timeout=timeout)
        except queue.Empty:
            return None
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get reading statistics"""
        return {
            'total_readings': self.total_readings,
            'valid_readings': self.valid_readings,
            'zero_readings': self.zero_readings,
            'last_speed': self.last_speed,
            'last_direction': self.last_direction,
            'queue_size': self.data_queue.qsize()
        }
    
    def __enter__(self):
        """Context manager entry"""
        self.start_reading()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.stop_reading()


def test_radar_reader():
    """Test function for the radar reader"""
    print("Testing Serial Radar Reader...")
    print("Press Ctrl+C to stop")
    
    try:
        with SerialRadarReader() as reader:
            while True:
                data = reader.get_data(timeout=1.0)
                if data:
                    print(f"Received: {data['raw_data']} -> {data['display_text']}")
                    
                    # Print statistics every 100 readings
                    if reader.total_readings % 100 == 0:
                        stats = reader.get_statistics()
                        print(f"Stats: {stats}")
                else:
                    print("No data received...")
                    
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_radar_reader()
