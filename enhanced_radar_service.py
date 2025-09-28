#!/usr/bin/env python3
"""
Enhanced Radar Service with A+XXX/A-XXX format support
Integrates with existing Django radar logging system
"""

import serial
import time
import threading
import queue
import logging
from typing import Optional, Dict, Any, List
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class RadarReading:
    """Data class for radar readings"""
    raw_data: str
    speed: int
    direction: str
    direction_sign: str
    vehicle_present: bool
    timestamp: float
    display_text: str

class EnhancedRadarReader:
    """
    Enhanced radar reader that supports both old (*+XXX,YYY) and new (A+XXX) formats
    """
    
    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 0.01):
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
        
        # Detection tracking for new format
        self.current_detection = []
        self.last_was_zero = True
        self.consecutive_zeros = 0
        self.max_consecutive_zeros = 10
        
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
    
    def parse_radar_data(self, data: bytes) -> Optional[RadarReading]:
        """
        Parse radar data supporting both formats:
        - Old format: *+XXX,YYY or *-XXX,YYY (range,speed)
        - New format: A+XXX or A-XXX (speed only)
        
        Args:
            data: Raw bytes from serial port
            
        Returns:
            RadarReading object or None if invalid
        """
        try:
            # Decode the data
            decoded = data.decode('utf-8', errors='ignore').strip()
            
            # Check for new format (A+XXX or A-XXX)
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
                
                return RadarReading(
                    raw_data=decoded,
                    speed=speed,
                    direction=direction,
                    direction_sign=direction_sign,
                    vehicle_present=vehicle_present,
                    timestamp=time.time(),
                    display_text=f"[{direction}] Speed: {speed}km/h" if vehicle_present else f"[{direction}] No vehicle (0km/h)"
                )
            
            # Check for old format (*+XXX,YYY or *-XXX,YYY)
            elif decoded.startswith(("*+", "*-", "*?")):
                # Get the prefix and remove it
                prefix = decoded[:2]  # *+ or *- or *?
                data_without_prefix = decoded[2:]
                # Split by comma
                parts = data_without_prefix.split(',')
                if len(parts) == 2:
                    range_val = float(parts[0])
                    speed_val = float(parts[1])
                    
                    # Determine direction name based on prefix
                    if prefix == '*+':
                        direction = "Towards Village"
                        direction_sign = '+'
                    elif prefix == '*-':
                        direction = "Towards Town"
                        direction_sign = '-'
                    else:  # '*?'
                        direction = "Unknown"
                        direction_sign = '?'
                    
                    # Update statistics
                    self.total_readings += 1
                    if range_val != 0 or speed_val != 0:
                        self.valid_readings += 1
                    else:
                        self.zero_readings += 1
                    
                    # Store last values
                    self.last_speed = speed_val
                    self.last_direction = direction
                    
                    vehicle_present = range_val != 0 or speed_val != 0
                    
                    return RadarReading(
                        raw_data=decoded,
                        speed=speed_val,
                        direction=direction,
                        direction_sign=direction_sign,
                        vehicle_present=vehicle_present,
                        timestamp=time.time(),
                        display_text=f"[{direction}] Range: {range_val}m, Speed: {speed_val}km/h" if vehicle_present else f"[{direction}] No vehicle (0km/h)"
                    )
                
        except (ValueError, IndexError) as e:
            logger.warning(f"Failed to parse radar data '{data}': {e}")
            
        return None
    
    def _reader_thread(self):
        """Background thread for reading serial data"""
        logger.info("Starting enhanced serial reader thread")
        
        while self.running and self.ser and self.ser.is_open:
            try:
                # Read data in chunks
                data = self.ser.read(32)
                if data:
                    self.buffer += data
                    
                    # Process complete messages
                    # For new format: 5 bytes each (A+XXX or A-XXX)
                    # For old format: variable length lines
                    
                    # Try to process fixed-size messages first (new format)
                    while len(self.buffer) >= 5:
                        chunk = self.buffer[:5]
                        
                        # Check if it's new format
                        try:
                            test_decode = chunk.decode('utf-8', errors='ignore')
                            if len(test_decode) == 5 and test_decode.startswith('A') and test_decode[1] in '+-':
                                self.buffer = self.buffer[5:]
                                parsed_data = self.parse_radar_data(chunk)
                                if parsed_data:
                                    self._process_reading(parsed_data)
                                continue
                        except:
                            pass
                        
                        # If not new format, break and try line-based reading
                        break
                    
                    # Process line-based messages (old format)
                    while b'\n' in self.buffer or b'\r' in self.buffer:
                        # Find line ending
                        line_end = -1
                        if b'\n' in self.buffer:
                            line_end = self.buffer.find(b'\n')
                        elif b'\r' in self.buffer:
                            line_end = self.buffer.find(b'\r')
                        
                        if line_end >= 0:
                            line = self.buffer[:line_end]
                            self.buffer = self.buffer[line_end + 1:]
                            
                            # Skip empty lines
                            if line.strip():
                                parsed_data = self.parse_radar_data(line.strip())
                                if parsed_data:
                                    self._process_reading(parsed_data)
                
                # Small sleep to prevent excessive CPU usage
                time.sleep(0.001)
                
            except Exception as e:
                logger.error(f"Error in reader thread: {e}")
                break
        
        logger.info("Enhanced serial reader thread stopped")
    
    def _process_reading(self, reading: RadarReading):
        """
        Process a radar reading and handle detection logic
        
        Args:
            reading: Parsed radar reading
        """
        # Only process non-zero readings or when transitioning from non-zero to zero
        if reading.vehicle_present or self.last_speed != 0:
            self.data_queue.put(reading)
            logger.debug(f"Received: {reading.raw_data} -> {reading.display_text}")
        
        # Handle detection logic for new format
        if reading.vehicle_present:
            self.current_detection.append(reading)
            self.last_was_zero = False
            self.consecutive_zeros = 0
        else:
            # If we have a zero reading and we were tracking a detection
            if self.current_detection and not self.last_was_zero:
                # Count the detection
                detection_count = len(self.current_detection)
                logger.debug(f"Completed detection with {detection_count} readings")
                
                # You can add detection processing logic here
                # For example, save to database, send notifications, etc.
                
                self.current_detection = []
                self.last_was_zero = True
    
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
    
    def get_data(self, timeout: float = 0.1) -> Optional[RadarReading]:
        """
        Get the next available data point
        
        Args:
            timeout: Maximum time to wait for data
            
        Returns:
            RadarReading object or None if no data available
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


def test_enhanced_radar_reader():
    """Test function for the enhanced radar reader"""
    print("Testing Enhanced Radar Reader...")
    print("Supports both A+XXX format (new) and *+XXX,YYY format (old)")
    print("Press Ctrl+C to stop")
    
    try:
        with EnhancedRadarReader('/dev/ttyAMA0') as reader:
            while True:
                data = reader.get_data(timeout=1.0)
                if data:
                    print(f"Received: {data.raw_data} -> {data.display_text}")
                    
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
    test_enhanced_radar_reader()
