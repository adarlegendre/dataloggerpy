#!/usr/bin/env python3
"""
Enhanced Radar Data Service with A+XXX format support
This is a drop-in replacement for the existing RadarDataService
"""

import serial
import time
import threading
import queue
import logging
import json
from django.apps import apps
from pathlib import Path

logger = logging.getLogger(__name__)

class EnhancedRadarDataService:
    """
    Enhanced radar data service that supports both old (*+XXX,YYY) and new (A+XXX) formats
    """
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(EnhancedRadarDataService, cls).__new__(cls)
                cls._instance._initialized = False
            return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        self._initialized = True
        self.radar_threads = {}
        self.data_queues = {}
        self.stop_events = {}
        self.data_cache = {}  # Cache for storing radar data
        self.last_save_time = {}  # Track last save time for each radar
        self.test_mode = False  # Flag for test mode
        self.test_data_index = 0  # Index for cycling through test data
        
        # Enhanced test data for both formats
        self.test_data = [
            # Old format test data
            {'raw_data': '*+15.8,2', 'range': 15.8, 'speed': 2, 'format': 'old'},
            {'raw_data': '*+15.3,11', 'range': 15.3, 'speed': 11, 'format': 'old'},
            {'raw_data': '*+0,0', 'range': 0, 'speed': 0, 'format': 'old'},
            
            # New format test data
            {'raw_data': 'A+044', 'range': None, 'speed': 44, 'format': 'new'},
            {'raw_data': 'A+047', 'range': None, 'speed': 47, 'format': 'new'},
            {'raw_data': 'A+000', 'range': None, 'speed': 0, 'format': 'new'},
            {'raw_data': 'A-042', 'range': None, 'speed': 42, 'format': 'new'},
            {'raw_data': 'A-000', 'range': None, 'speed': 0, 'format': 'new'},
        ]
        
        logger.info("Enhanced RadarDataService initialized with A+XXX format support")
    
    def check_serial_ports(self):
        """Check available serial ports and their status"""
        import serial.tools.list_ports
        ports = serial.tools.list_ports.comports()
        port_info = []
        logger.info("Checking available serial ports...")
        
        for port in ports:
            try:
                logger.debug(f"Attempting to open port {port.device}")
                with serial.Serial(port.device, timeout=0.1) as ser:
                    port_info.append({
                        'device': port.device,
                        'description': port.description,
                        'hwid': port.hwid,
                        'status': 'available'
                    })
                    logger.info(f"Port {port.device} is available")
            except serial.SerialException as e:
                port_info.append({
                    'device': port.device,
                    'description': port.description,
                    'hwid': port.hwid,
                    'status': 'in_use'
                })
                logger.warning(f"Port {port.device} is in use or unavailable: {str(e)}")
        
        logger.info(f"Found {len(ports)} serial ports: {[p['device'] for p in port_info]}")
        return port_info

    def start_service(self):
        """Start the enhanced radar data service"""
        logger.info("Starting enhanced radar data service with A+XXX format support")
        RadarConfig = apps.get_model('app', 'RadarConfig')
        radars = RadarConfig.objects.filter(is_active=True)
        
        logger.info(f"Found {len(radars)} active radars")
        for radar in radars:
            logger.info(f"Starting radar {radar.id} ({radar.name}) on port {radar.port}")
            self.start_radar_stream(radar)
    
    def stop_service(self):
        """Stop the radar data service"""
        logger.info("Stopping enhanced radar data service")
        for radar_id in list(self.stop_events.keys()):
            logger.info(f"Stopping radar {radar_id}")
            self.stop_radar_stream(radar_id)
    
    def start_radar_stream(self, radar):
        """Start streaming data for a specific radar"""
        if radar.id in self.radar_threads:
            logger.warning(f"Radar {radar.id} is already running")
            return
        
        # Create stop event and data queue
        stop_event = threading.Event()
        data_queue = queue.Queue()
        
        self.stop_events[radar.id] = stop_event
        self.data_queues[radar.id] = data_queue
        self.data_cache[radar.id] = []
        self.last_save_time[radar.id] = time.time()
        
        # Start background thread
        thread = threading.Thread(
            target=self._stream_radar_data,
            args=(radar, data_queue, stop_event),
            daemon=True
        )
        thread.start()
        
        self.radar_threads[radar.id] = thread
        logger.info(f"Started radar stream for {radar.id}")
    
    def stop_radar_stream(self, radar_id):
        """Stop streaming data for a specific radar"""
        if radar_id in self.stop_events:
            self.stop_events[radar_id].set()
            
        if radar_id in self.radar_threads:
            thread = self.radar_threads[radar_id]
            thread.join(timeout=5)
            del self.radar_threads[radar_id]
            
        if radar_id in self.stop_events:
            del self.stop_events[radar_id]
        if radar_id in self.data_queues:
            del self.data_queues[radar_id]
        if radar_id in self.data_cache:
            del self.data_cache[radar_id]
        if radar_id in self.last_save_time:
            del self.last_save_time[radar_id]
            
        logger.info(f"Stopped radar stream for {radar_id}")
    
    def get_radar_data(self, radar_id, timeout=1.0):
        """Get the latest data for a specific radar"""
        if radar_id in self.data_queues:
            try:
                return self.data_queues[radar_id].get(timeout=timeout)
            except queue.Empty:
                return None
        return None
    
    def get_service_status(self):
        """Get the status of all radar streams"""
        status = {}
        for radar_id in self.radar_threads:
            thread = self.radar_threads[radar_id]
            status[radar_id] = {
                'running': thread.is_alive(),
                'queue_size': self.data_queues[radar_id].qsize() if radar_id in self.data_queues else 0,
                'cache_size': len(self.data_cache[radar_id]) if radar_id in self.data_cache else 0
            }
        return status

    def _parse_radar_data(self, decoded_data: str, radar):
        """
        Parse radar data supporting both formats:
        - Old format: *+XXX,YYY or *-XXX,YYY (range,speed)
        - New format: A+XXX or A-XXX (speed only)
        
        Args:
            decoded_data: Decoded string from serial port
            radar: RadarConfig object
            
        Returns:
            Dictionary with parsed data or None if invalid
        """
        try:
            # Check for new format (A+XXX or A-XXX)
            if len(decoded_data) == 5 and decoded_data.startswith('A') and decoded_data[1] in '+-':
                direction_sign = decoded_data[1]  # + or -
                speed_str = decoded_data[2:]      # XXX (3 digits)
                
                # Parse speed value
                speed = int(speed_str)
                
                # Determine direction name based on sign
                if direction_sign == '+':
                    direction_name = radar.direction_positive_name
                else:
                    direction_name = radar.direction_negative_name
                
                # Determine if vehicle is present
                vehicle_present = speed != 0
                
                return {
                    'status': 'success',
                    'range': None,  # No range data in new format
                    'speed': speed,
                    'timestamp': time.time(),
                    'connection_status': 'connected',
                    'raw_data': decoded_data,
                    'display_text': f"[{direction_name}] Speed: {speed}km/h" if vehicle_present else f"[{direction_name}] No vehicle (0km/h)",
                    'direction_name': direction_name,
                    'direction_prefix': direction_sign,
                    'format': 'new',
                    'vehicle_present': vehicle_present
                }
            
            # Check for old format (*+XXX,YYY or *-XXX,YYY)
            elif decoded_data.startswith(("*+", "*-", "*?")):
                # Get the prefix and remove it
                prefix = decoded_data[:2]  # *+ or *- or *?
                data_without_prefix = decoded_data[2:]
                # Split by comma
                parts = data_without_prefix.split(',')
                if len(parts) == 2:
                    range_val = float(parts[0])
                    speed_val = float(parts[1])
                    
                    # Determine direction name based on prefix
                    if prefix == '*+':
                        direction_name = radar.direction_positive_name
                    elif prefix == '*-':
                        direction_name = radar.direction_negative_name
                    else:  # '*?'
                        direction_name = 'Unknown'
                    
                    vehicle_present = range_val != 0 or speed_val != 0
                    
                    return {
                        'status': 'success',
                        'range': range_val,
                        'speed': speed_val,
                        'timestamp': time.time(),
                        'connection_status': 'connected',
                        'raw_data': decoded_data,
                        'display_text': f"[{direction_name}] Range: {range_val}m, Speed: {speed_val}km/h" if vehicle_present else f"[{direction_name}] No vehicle (0km/h)",
                        'direction_name': direction_name,
                        'direction_prefix': prefix,
                        'format': 'old',
                        'vehicle_present': vehicle_present
                    }
                
        except (ValueError, IndexError) as e:
            logger.warning(f"Failed to parse radar data '{decoded_data}': {e}")
            
        return None

    def _stream_radar_data(self, radar, data_queue, stop_event):
        """Enhanced background thread function for streaming radar data"""
        logger.info(f"Starting enhanced data stream for radar {radar.id} on port {radar.port}")
        
        # Log radar configuration
        config_info = {
            'port': radar.port,
            'baud_rate': radar.baud_rate,
            'data_bits': radar.data_bits,
            'parity': radar.parity,
            'stop_bits': radar.stop_bits,
            'update_interval': radar.update_interval,
            'file_save_interval': radar.file_save_interval
        }
        logger.info(f"Radar {radar.id} configuration: {config_info}")

        connection_attempts = 0
        max_connection_attempts = 3
        connection_retry_delay = 5  # seconds
        current_detection = []
        last_was_zero = True
        last_save_time = time.time()
        last_valid_data_time = time.time()
        data_timeout = 10  # seconds without valid data before reconnecting

        while not stop_event.is_set() and connection_attempts < max_connection_attempts:
            try:
                logger.info(f"Attempting to connect to radar {radar.id} on {radar.port} (Attempt {connection_attempts + 1}/{max_connection_attempts})")
                
                # Create error message for serial terminal
                error_message = {
                    'timestamp': int(time.time()),
                    'display_text': f"Connecting to radar on port {radar.port}...",
                    'connection_status': 'connecting'
                }
                data_queue.put(error_message)
                
                with serial.Serial(
                    port=radar.port,
                    baudrate=radar.baud_rate,
                    timeout=1.0  # Simplified timeout configuration
                ) as ser:
                    logger.info(f"Successfully connected to radar {radar.id} on {radar.port}")
                    
                    # Give some time for the serial connection to initialize
                    time.sleep(2)
                    
                    # Send connection success message
                    success_message = {
                        'timestamp': int(time.time()),
                        'display_text': f"Connected to radar on port {radar.port}",
                        'connection_status': 'connected'
                    }
                    data_queue.put(success_message)
                    
                    # Initialize tracking variables
                    consecutive_zeros = 0
                    max_consecutive_zeros = 10  # Threshold for considering a detection complete
                    
                    while not stop_event.is_set():
                        try:
                            # Check if it's time to save data to file
                            current_time = time.time()
                            if current_time - last_save_time >= radar.file_save_interval * 60:
                                logger.info(f"Saving data to file for radar {radar.id} after {radar.file_save_interval} minutes")
                                if radar.id in self.data_cache and self.data_cache[radar.id]:
                                    self._save_data_to_file(radar.id)
                                    last_save_time = current_time
                                    logger.info(f"Successfully saved data file for radar {radar.id}")
                                else:
                                    logger.info(f"No data to save for radar {radar.id}")
                            
                            # Check for data timeout
                            if current_time - last_valid_data_time > data_timeout:
                                logger.warning(f"No valid data received for {data_timeout} seconds, reconnecting...")
                                break
                            
                            # Read data line by line
                            if ser.in_waiting > 0:
                                try:
                                    # Read a complete line
                                    data = ser.readline().strip()
                                    
                                    # Skip empty lines or carriage returns
                                    if not data or data == b'\r':
                                        continue
                                        
                                    # Decode the data
                                    decoded_data = data.decode('utf-8', errors='replace').strip("b'")
                                    
                                    # Parse the data using enhanced parser
                                    parsed_data = self._parse_radar_data(decoded_data, radar)
                                    
                                    if parsed_data:
                                        # Update last valid data time
                                        last_valid_data_time = time.time()
                                        
                                        # Add to data queue
                                        data_queue.put(parsed_data)
                                        
                                        # Add to data cache for periodic file saving
                                        if radar.id in self.data_cache:
                                            self.data_cache[radar.id].append(parsed_data)
                                        
                                        # Handle zero and non-zero readings
                                        if parsed_data['vehicle_present']:
                                            current_detection.append(parsed_data)
                                            last_was_zero = False
                                            consecutive_zeros = 0
                                        else:
                                            consecutive_zeros += 1
                                            # If we have enough consecutive zeros and we were tracking a detection
                                            if consecutive_zeros >= max_consecutive_zeros and current_detection:
                                                # Save the current detection if it has any non-zero values
                                                has_non_zero = any(point['vehicle_present'] for point in current_detection)
                                                if has_non_zero:
                                                    logger.info(f"Completed detection with {len(current_detection)} readings for radar {radar.id}")
                                                    
                                                    # Save detection to database
                                                    self._save_detection_to_database(radar, current_detection)
                                                
                                                current_detection = []
                                                last_was_zero = True
                                        
                                        # Log the received data
                                        logger.debug(f"Radar {radar.id}: {parsed_data['raw_data']} -> {parsed_data['display_text']}")
                                        
                                except Exception as e:
                                    logger.error(f"Error processing data from radar {radar.id}: {str(e)}")
                                    continue
                            else:
                                # Small sleep when no data is available
                                time.sleep(0.01)
                                
                        except Exception as e:
                            logger.error(f"Error in radar {radar.id} data processing loop: {str(e)}")
                            break
                    
                    # If we exit the inner loop, close the connection
                    logger.info(f"Closing connection to radar {radar.id}")
                    
            except Exception as e:
                logger.error(f"Error connecting to radar {radar.id}: {str(e)}")
                connection_attempts += 1
                if connection_attempts < max_connection_attempts:
                    logger.info(f"Retrying connection to radar {radar.id} in {connection_retry_delay} seconds...")
                    time.sleep(connection_retry_delay)
                else:
                    logger.error(f"Failed to connect to radar {radar.id} after {max_connection_attempts} attempts")
                    break
        
        logger.info(f"Stopped data stream for radar {radar.id}")
    
    def _save_detection_to_database(self, radar, detection_data):
        """Save detection data to database"""
        try:
            RadarData = apps.get_model('app', 'RadarData')
            
            # Save each data point in the detection
            for data_point in detection_data:
                radar_data = RadarData(
                    radar=radar,
                    range=data_point.get('range'),
                    speed=data_point['speed'],
                    direction=None,  # Direction is in direction_name
                    raw_data=data_point['raw_data'],
                    status='success',
                    connection_status='connected'
                )
                radar_data.save()
            
            logger.info(f"Saved {len(detection_data)} data points to database for radar {radar.id}")
            
        except Exception as e:
            logger.error(f"Error saving detection to database: {str(e)}")
    
    def _save_data_to_file(self, radar_id):
        """Save cached data to file"""
        try:
            if radar_id not in self.data_cache or not self.data_cache[radar_id]:
                return
            
            RadarConfig = apps.get_model('app', 'RadarConfig')
            radar = RadarConfig.objects.get(id=radar_id)
            
            # Create data directory if it doesn't exist
            data_dir = Path(radar.data_storage_path)
            data_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate filename with timestamp
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"radar_{radar.name}_{timestamp}.json"
            filepath = data_dir / filename
            
            # Process and save data
            data_to_process = self.data_cache[radar_id].copy()
            self.data_cache[radar_id] = []  # Clear cache
            
            # Save data to file
            with open(filepath, 'w') as f:
                json.dump(data_to_process, f, indent=2, default=str)
            
            logger.info(f"Saved {len(data_to_process)} data points to file: {filepath}")
            
        except Exception as e:
            logger.error(f"Error saving data to file for radar {radar_id}: {str(e)}")


# Create a singleton instance
enhanced_service = EnhancedRadarDataService()
