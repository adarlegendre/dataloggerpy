#!/usr/bin/env python3
"""
Test script for radar integration
Tests the new A+XXX format reader without requiring actual hardware
"""

import time
import random
from modified_serial_reader import ModifiedSerialReader
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MockSerialReader:
    """
    Mock serial reader that simulates radar data for testing
    """
    
    def __init__(self, port: str = '/dev/ttyAMA0', baudrate: int = 9600, timeout: float = 0.01):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.running = False
        self.data_queue = []
        self.reader_thread = None
        
        # Statistics
        self.total_readings = 0
        self.valid_readings = 0
        self.zero_readings = 0
        self.last_speed = 0
        self.last_direction = None
        
        # Detection tracking
        self.current_detection = []
        self.last_was_zero = True
        self.consecutive_zeros = 0
        self.max_consecutive_zeros = 10
        
        # Mock data patterns
        self.mock_data_patterns = [
            # Vehicle approaching (positive direction)
            "A+000", "A+000", "A+000",  # No vehicle
            "A+045", "A+047", "A+049", "A+051", "A+053", "A+055",  # Vehicle approaching
            "A+057", "A+059", "A+061", "A+063", "A+065", "A+067",  # Vehicle getting closer
            "A+069", "A+069", "A+069", "A+069", "A+069", "A+069",  # Vehicle at closest point
            "A+067", "A+065", "A+063", "A+061", "A+059", "A+057",  # Vehicle moving away
            "A+055", "A+053", "A+051", "A+049", "A+047", "A+045",  # Vehicle moving away
            "A+000", "A+000", "A+000",  # No vehicle
            
            # Vehicle approaching (negative direction)
            "A-000", "A-000", "A-000",  # No vehicle
            "A-042", "A-044", "A-046", "A-048", "A-050", "A-052",  # Vehicle approaching
            "A-054", "A-056", "A-058", "A-060", "A-062", "A-064",  # Vehicle getting closer
            "A-066", "A-066", "A-066", "A-066", "A-066", "A-066",  # Vehicle at closest point
            "A-064", "A-062", "A-060", "A-058", "A-056", "A-054",  # Vehicle moving away
            "A-052", "A-050", "A-048", "A-046", "A-044", "A-042",  # Vehicle moving away
            "A-000", "A-000", "A-000",  # No vehicle
        ]
        
        self.current_pattern_index = 0
    
    def connect(self) -> bool:
        """Mock connection - always succeeds"""
        logger.info(f"Mock connected to radar on {self.port} at {self.baudrate} baud")
        return True
    
    def disconnect(self):
        """Mock disconnect"""
        logger.info("Mock disconnected from radar")
    
    def parse_radar_data(self, data: str) -> dict:
        """
        Parse radar data in A+XXX/A-XXX format
        
        Args:
            data: Raw string data
            
        Returns:
            Dictionary with parsed data or None if invalid
        """
        try:
            # Check if it's the expected format (A+XXX or A-XXX)
            if len(data) == 5 and data.startswith('A') and data[1] in '+-':
                direction_sign = data[1]  # + or -
                speed_str = data[2:]      # XXX (3 digits)
                
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
                    'raw_data': data,
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
        """Mock background thread for reading serial data"""
        logger.info("Starting mock serial reader thread")
        
        while self.running:
            try:
                # Get next data from pattern
                if self.current_pattern_index < len(self.mock_data_patterns):
                    data = self.mock_data_patterns[self.current_pattern_index]
                    self.current_pattern_index += 1
                else:
                    # Loop back to beginning
                    self.current_pattern_index = 0
                    data = self.mock_data_patterns[self.current_pattern_index]
                    self.current_pattern_index += 1
                
                # Parse the data
                parsed_data = self.parse_radar_data(data)
                if parsed_data:
                    # Only process non-zero readings or when transitioning from non-zero to zero
                    if parsed_data['vehicle_present'] or self.last_speed != 0:
                        self._process_reading(parsed_data)
                
                # Simulate real-time data
                time.sleep(0.1)  # 100ms between readings
                
            except Exception as e:
                logger.error(f"Error in mock reader thread: {e}")
                break
        
        logger.info("Mock serial reader thread stopped")
    
    def _process_reading(self, reading: dict):
        """
        Process a radar reading and handle detection logic
        
        Args:
            reading: Parsed radar reading
        """
        # Add to data queue
        self.data_queue.append(reading)
        logger.debug(f"Received: {reading['raw_data']} -> {reading['display_text']}")
        
        # Handle detection logic
        if reading['vehicle_present']:
            self.current_detection.append(reading)
            self.last_was_zero = False
            self.consecutive_zeros = 0
        else:
            # If we have a zero reading and we were tracking a detection
            if self.current_detection and not self.last_was_zero:
                # Count the detection
                detection_count = len(self.current_detection)
                logger.info(f"Completed detection with {detection_count} readings")
                
                # You can add detection processing logic here
                # For example, save to database, send notifications, etc.
                
                self.current_detection = []
                self.last_was_zero = True
    
    def start_reading(self) -> bool:
        """Start reading from the mock serial port"""
        if not self.connect():
            return False
        
        self.running = True
        self.reader_thread = threading.Thread(target=self._reader_thread, daemon=True)
        self.reader_thread.start()
        
        logger.info("Started reading mock radar data")
        return True
    
    def stop_reading(self):
        """Stop reading from the mock serial port"""
        self.running = False
        
        if self.reader_thread:
            self.reader_thread.join(timeout=2)
        
        self.disconnect()
        logger.info("Stopped reading mock radar data")
    
    def get_data(self, timeout: float = 0.1) -> dict:
        """
        Get the next available data point
        
        Args:
            timeout: Maximum time to wait for data
            
        Returns:
            Parsed radar data or None if no data available
        """
        if self.data_queue:
            return self.data_queue.pop(0)
        return None
    
    def get_statistics(self) -> dict:
        """Get reading statistics"""
        return {
            'total_readings': self.total_readings,
            'valid_readings': self.valid_readings,
            'zero_readings': self.zero_readings,
            'last_speed': self.last_speed,
            'last_direction': self.last_direction,
            'queue_size': len(self.data_queue)
        }
    
    def __enter__(self):
        """Context manager entry"""
        self.start_reading()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.stop_reading()


def test_mock_radar_reader():
    """Test function for the mock radar reader"""
    print("Testing Mock Radar Reader...")
    print("This simulates radar data without requiring actual hardware")
    print("Press Ctrl+C to stop")
    
    try:
        with MockSerialReader() as reader:
            while True:
                data = reader.get_data(timeout=1.0)
                if data:
                    print(f"Received: {data['raw_data']} -> {data['display_text']}")
                    
                    # Print statistics every 50 readings
                    if reader.total_readings % 50 == 0:
                        stats = reader.get_statistics()
                        print(f"Stats: {stats}")
                else:
                    print("No data received...")
                    
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"Error: {e}")


def test_real_radar_reader():
    """Test function for the real radar reader"""
    print("Testing Real Radar Reader...")
    print("This requires actual radar hardware connected to /dev/ttyAMA0")
    print("Press Ctrl+C to stop")
    
    try:
        with ModifiedSerialReader() as reader:
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
    print("Radar Integration Test")
    print("=====================")
    print("1. Test with mock data (no hardware required)")
    print("2. Test with real hardware (requires radar connected)")
    print("3. Test detection logic only")
    
    choice = input("Enter choice (1, 2, or 3): ").strip()
    
    if choice == "1":
        test_mock_radar_reader()
    elif choice == "2":
        test_real_radar_reader()
    elif choice == "3":
        # Test detection logic with sample data
        print("Testing detection logic with sample data...")
        sample_data = [
            "A+000", "A+000", "A+000",  # No vehicle
            "A+045", "A+047", "A+049", "A+051", "A+053", "A+055",  # Vehicle approaching
            "A+057", "A+059", "A+061", "A+063", "A+065", "A+067",  # Vehicle getting closer
            "A+069", "A+069", "A+069", "A+069", "A+069", "A+069",  # Vehicle at closest point
            "A+067", "A+065", "A+063", "A+061", "A+059", "A+057",  # Vehicle moving away
            "A+055", "A+053", "A+051", "A+049", "A+047", "A+045",  # Vehicle moving away
            "A+000", "A+000", "A+000",  # No vehicle
        ]
        
        reader = MockSerialReader()
        reader.connect()
        
        for data in sample_data:
            parsed = reader.parse_radar_data(data)
            if parsed:
                reader._process_reading(parsed)
                print(f"Processed: {parsed['raw_data']} -> {parsed['display_text']}")
        
        stats = reader.get_statistics()
        print(f"Final stats: {stats}")
        
    else:
        print("Invalid choice. Running mock test...")
        test_mock_radar_reader()
