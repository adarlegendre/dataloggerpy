import threading
import time
import json
import serial
from django.apps import apps
from queue import Queue
import logging
import os
from datetime import datetime, timezone
from collections import deque
from django.utils import timezone
from app.shared_state import recent_anpr_events
import socket

logger = logging.getLogger(__name__)

def send_to_display(plate, ip='192.168.1.222', port=8080):
    # Placeholder: build the message according to your display protocol
    # For now, just send the plate as plain text
    message = plate.encode('utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(message)

def test_send_to_display():
    """Test sending a sample plate to the C-Power5200 display board."""
    sample_plate = "1A2 3456"
    print(f"Sending test plate '{sample_plate}' to display...")
    send_to_display(sample_plate)
    print("Test message sent.")

class RadarDataService:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(RadarDataService, cls).__new__(cls)
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
        self.test_data = [
            {'range': -33.2, 'speed': 2},
            {'range': -33.2, 'speed': 0},
            {'range': -33.2, 'speed': 0},
            {'range': -33.2, 'speed': 0},
            {'range': 15.8, 'speed': 2},
            {'range': 15.3, 'speed': 11},
            {'range': 15.4, 'speed': 0},
            {'range': 16.4, 'speed': 6},
            {'range': 16.6, 'speed': 0},
            {'range': 16.6, 'speed': 0},
            {'range': 16.6, 'speed': 0},
            {'range': 16.6, 'speed': 0}
        ]
        logger.info("RadarDataService initialized")
    
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
        """Start the radar data service"""
        logger.info("Starting radar data service")
        RadarConfig = apps.get_model('app', 'RadarConfig')
        radars = RadarConfig.objects.filter(is_active=True)
        
        logger.info(f"Found {len(radars)} active radars")
        for radar in radars:
            logger.info(f"Starting radar {radar.id} ({radar.name}) on port {radar.port}")
            self.start_radar_stream(radar)
    
    def stop_service(self):
        """Stop the radar data service"""
        logger.info("Stopping radar data service")
        for radar_id in list(self.stop_events.keys()):
            logger.info(f"Stopping radar {radar_id}")
            self.stop_radar_stream(radar_id)
    
    def start_radar_stream(self, radar):
        """Start streaming data for a specific radar"""
        radar_id = radar.id
        if radar_id in self.radar_threads and self.radar_threads[radar_id].is_alive():
            logger.warning(f"Radar {radar_id} stream already running")
            return
            
        logger.info(f"Initializing data structures for radar {radar_id}")
        self.data_queues[radar_id] = Queue()
        self.stop_events[radar_id] = threading.Event()
        self.data_cache[radar_id] = []  # Removed maxlen limit
        self.last_save_time[radar_id] = time.time()
        
        thread = threading.Thread(
            target=self._stream_radar_data,
            args=(radar, self.data_queues[radar_id], self.stop_events[radar_id]),
            daemon=True
        )
        thread.start()
        self.radar_threads[radar_id] = thread
        logger.info(f"Started streaming thread for radar {radar_id}")
    
    def stop_radar_stream(self, radar_id):
        """Stop streaming data for a specific radar"""
        if radar_id in self.stop_events:
            logger.info(f"Stopping radar {radar_id} stream")
            self.stop_events[radar_id].set()
            
            if radar_id in self.radar_threads:
                logger.debug(f"Waiting for radar {radar_id} thread to finish")
                self.radar_threads[radar_id].join(timeout=5.0)
            
            # Save any remaining data before stopping
            if radar_id in self.data_cache and self.data_cache[radar_id]:
                logger.info(f"Saving remaining data for radar {radar_id}")
                self._save_data_to_file(radar_id)
            
            # Clean up resources
            logger.debug(f"Cleaning up resources for radar {radar_id}")
            del self.stop_events[radar_id]
            del self.radar_threads[radar_id]
            del self.data_queues[radar_id]
            del self.data_cache[radar_id]
            del self.last_save_time[radar_id]
            logger.info(f"Successfully stopped radar {radar_id} stream")
    
    def get_latest_data(self, radar_id):
        """Get the latest data for a specific radar"""
        if radar_id in self.data_queues:
            try:
                data = self.data_queues[radar_id].get_nowait()
                logger.debug(f"Retrieved latest data for radar {radar_id}")
                return data
            except:
                logger.debug(f"No new data available for radar {radar_id}")
                return None
        logger.warning(f"No data queue found for radar {radar_id}")
        return None

    def _save_data_to_file(self, radar_id):
        """Save cached data to file"""
        try:
            RadarConfig = apps.get_model('app', 'RadarConfig')
            RadarDataFile = apps.get_model('app', 'RadarDataFile')
            RadarObjectDetection = apps.get_model('app', 'RadarObjectDetection')
            radar = RadarConfig.objects.get(id=radar_id)
            
            # Create a copy of the cache to work with
            data_to_process = self.data_cache[radar_id].copy()
            
            # Only proceed if we have data
            if not data_to_process:
                logger.info(f"No data to process for radar {radar_id}")
                return
            
            # Process and save data in a single pass
            object_detections = []
            current_detection = []
            last_was_zero = True
            detection_count = 0
            total_readings = 0
            
            # First pass: count detections and process data
            for i, data_point in enumerate(data_to_process):
                try:
                    if data_point['raw_data'].startswith(('*+', '*-', '*?')):
                        parts = data_point['raw_data'][1:].split(',')
                        if len(parts) == 2:
                            range_val = float(parts[0])
                            speed_val = float(parts[1])
                            
                            # If we have a non-zero reading
                            if range_val != 0 or speed_val != 0:
                                current_detection.append(data_point)
                                last_was_zero = False
                            # If we have a zero reading and we were tracking a detection
                            elif current_detection and not last_was_zero:
                                # Count the detection
                                detection_count += 1
                                total_readings += len(current_detection)
                                logger.debug(f"Counted detection #{detection_count} with {len(current_detection)} readings")
                                current_detection = []
                                last_was_zero = True
                            
                            # Process the last detection if this is the last data point
                            if i == len(data_to_process) - 1 and current_detection and not last_was_zero:
                                detection_count += 1
                                total_readings += len(current_detection)
                                logger.debug(f"Counted final detection #{detection_count} with {len(current_detection)} readings")
                except (ValueError, IndexError) as e:
                    logger.warning(f"Error processing data point: {str(e)}")
                    continue
            
            # Only create file if we have detections
            if detection_count > 0:
                # Create directory if it doesn't exist
                save_dir = os.path.join(radar.data_storage_path)
                os.makedirs(save_dir, exist_ok=True)
                logger.debug(f"Ensuring save directory exists: {save_dir}")
                
                # Generate filename with timestamp
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"radar_{radar.name}_{timestamp}.json"
                filepath = os.path.join(save_dir, filename)
                logger.debug(f"Preparing to save data to file: {filepath}")
                
                # Reset for second pass
                current_detection = []
                last_was_zero = True
                detection_count = 0
                
                # Open file for writing
                logger.debug(f"Opening file for writing: {filepath}")
                with open(filepath, 'w') as f:
                    f.write('[\n')  # Start JSON array
                    
                    for i, data_point in enumerate(data_to_process):
                        try:
                            if data_point['raw_data'].startswith(('*+', '*-', '*?')):
                                parts = data_point['raw_data'][1:].split(',')
                                if len(parts) == 2:
                                    range_val = float(parts[0])
                                    speed_val = float(parts[1])
                                    
                                    # If we have a non-zero reading
                                    if range_val != 0 or speed_val != 0:
                                        current_detection.append(data_point)
                                        last_was_zero = False
                                    # If we have a zero reading and we were tracking a detection
                                    elif current_detection and not last_was_zero:
                                        # Process and save the current detection
                                        if self._process_and_save_detection(current_detection, f, detection_count + 1, radar):
                                            detection_count += 1
                                            logger.debug(f"Processed detection #{detection_count}")
                                        current_detection = []
                                        last_was_zero = True
                                    
                                    # Process the last detection if this is the last data point
                                    if i == len(data_to_process) - 1 and current_detection and not last_was_zero:
                                        if self._process_and_save_detection(current_detection, f, detection_count + 1, radar):
                                            detection_count += 1
                                            logger.debug(f"Processed final detection #{detection_count}")
                        except (ValueError, IndexError) as e:
                            logger.warning(f"Error processing data point: {str(e)}")
                            continue
                    
                    f.write('\n]')  # End JSON array
                
                # Get file size
                file_size = os.path.getsize(filepath)
                logger.debug(f"File size: {file_size} bytes")
                
                # Create RadarDataFile record
                data_file = RadarDataFile.objects.create(
                    radar=radar,
                    filename=filename,
                    file_path=filepath,
                    record_count=total_readings,
                    file_size=file_size
                )
                logger.debug(f"Created RadarDataFile record with ID: {data_file.id}")
                
                logger.info(f"Saved {detection_count} object detections ({total_readings} total readings) to {filepath}")
                
                # Clear the cache only after successful save
                self.data_cache[radar_id].clear()
                logger.debug(f"Cleared data cache for radar {radar_id}")
            else:
                logger.warning(f"No valid detections found to save for radar {radar_id}")
                
                # Clear the cache even when no detections
                self.data_cache[radar_id].clear()
                logger.debug(f"Cleared data cache for radar {radar_id}")
            
        except Exception as e:
            logger.error(f"Error saving data to file for radar {radar_id}: {str(e)}")
            # Don't clear cache on error to prevent data loss
            raise

    def _process_and_save_detection(self, detection, file_handle, detection_number, radar):
        """Process a single detection and save it to file and database"""
        try:
            # Calculate statistics in a single pass
            ranges = []
            speeds = []
            formatted_data = []
            start_time = timezone.make_aware(datetime.fromtimestamp(detection[0]['timestamp']))
            end_time = timezone.make_aware(datetime.fromtimestamp(detection[-1]['timestamp']))
            
            # Add detection header
            if detection_number > 1:
                file_handle.write(',\n')
            file_handle.write('  [\n')
            file_handle.write(f'    {{"comment": "Object Detection #{detection_number} - Start Time: {start_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}"}},\n')
            
            # Process each reading
            direction_counts = {'positive': 0, 'negative': 0, 'unknown': 0}
            for i, data_point in enumerate(detection):
                # Parse prefix and range/speed
                prefix = data_point['raw_data'][:2]
                parts = data_point['raw_data'][2:].split(',')
                range_val = float(parts[0])
                speed_val = float(parts[1])
                
                # Determine direction name from prefix
                if prefix == '*+':
                    direction_name = radar.direction_positive_name
                    direction_counts['positive'] += 1
                elif prefix == '*-':
                    direction_name = radar.direction_negative_name
                    direction_counts['negative'] += 1
                else:
                    direction_name = 'Unknown'
                    direction_counts['unknown'] += 1
                
                ranges.append(range_val)
                speeds.append(speed_val)
                
                # Format timestamp
                dt = timezone.make_aware(datetime.fromtimestamp(data_point['timestamp']))
                formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                
                # Write to file
                if i > 0:
                    file_handle.write(',\n')
                file_handle.write(f'    {{"timestamp": "{formatted_time}", "raw_data": "{data_point["raw_data"]}", "direction_name": "{direction_name}"}}')
                
                formatted_data.append({
                    'timestamp': formatted_time,
                    'raw_data': data_point['raw_data'],
                    'direction_name': direction_name
                })
            
            # Calculate statistics
            min_range = min(ranges)
            max_range = max(ranges)
            avg_range = sum(ranges) / len(ranges)
            min_speed = min(speeds)
            max_speed = max(speeds)
            avg_speed = sum(speeds) / len(speeds)
            
            # Add detection summary
            duration = (end_time - start_time).total_seconds()
            file_handle.write(f',\n    {{"comment": "Object Detection #{detection_number} - End Time: {end_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}, ')
            file_handle.write(f'Duration: {duration:.1f}s, Readings: {len(detection)}, ')
            file_handle.write(f'Range: {min_range:.1f}-{max_range:.1f}m (avg: {avg_range:.1f}m), ')
            file_handle.write(f'Speed: {min_speed:.1f}-{max_speed:.1f}km/h (avg: {avg_speed:.1f}km/h)"}}\n')
            file_handle.write('  ]')
            
            # Determine majority direction for the detection
            if direction_counts['negative'] > direction_counts['positive'] and direction_counts['negative'] > direction_counts['unknown']:
                detection_direction_name = radar.direction_negative_name
            elif direction_counts['positive'] > direction_counts['unknown']:
                detection_direction_name = radar.direction_positive_name
            else:
                detection_direction_name = 'Unknown'
            
            # Save to database
            RadarObjectDetection = apps.get_model('app', 'RadarObjectDetection')
            now = datetime.now()
            recent_anpr = next((e for e in reversed(recent_anpr_events)
                               if e['timestamp'] and abs((now - e['timestamp']).total_seconds()) < 2), None)

            RadarObjectDetection.objects.create(
                radar=radar,
                start_time=start_time,
                end_time=end_time,
                min_range=min_range,
                max_range=max_range,
                avg_range=avg_range,
                min_speed=min_speed,
                max_speed=max_speed,
                avg_speed=avg_speed,
                detection_count=len(detection),
                raw_data=formatted_data,
                direction_name=detection_direction_name,
                anpr_detected=bool(recent_anpr and recent_anpr['plate']),
                license_plate=recent_anpr['plate'] if recent_anpr else None,
                anpr_timestamp=recent_anpr['timestamp'] if recent_anpr else None,
                anpr_device_id=recent_anpr['device_id'] if recent_anpr else None,
                anpr_confidence=recent_anpr['confidence'] if recent_anpr else None,
                anpr_image_url=recent_anpr['image_url'] if recent_anpr else None,
                anpr_record_id=recent_anpr['record_id'] if recent_anpr else None,
            )

            if recent_anpr and recent_anpr['plate']:
                send_to_display(recent_anpr['plate'])
            
            return True
            
        except Exception as e:
            logger.error(f"Error processing detection: {str(e)}")
            return False

    def set_test_mode(self, enabled):
        """Enable or disable test mode"""
        with self._lock:
            self.test_mode = enabled
            self.test_data_index = 0  # Reset test data index when toggling
            logger.info(f"Test mode {'enabled' if enabled else 'disabled'}")
            return self.test_mode

    def get_test_mode(self):
        """Get current test mode state"""
        with self._lock:
            return self.test_mode

    def _get_test_data(self):
        """Get next test data point"""
        with self._lock:
            if not self.test_data:
                return {'range': 0, 'speed': 0}
            
            data = self.test_data[self.test_data_index]
            self.test_data_index = (self.test_data_index + 1) % len(self.test_data)
            return data

    def _stream_radar_data(self, radar, data_queue, stop_event):
        """Background thread function for streaming radar data"""
        logger.info(f"Starting data stream for radar {radar.id} on port {radar.port}")
        
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
                                    
                                    # Process the data if it starts with *+, *-, or *?
                                    if decoded_data.startswith(("*+", "*-", "*?")):
                                        try:
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

                                                # Update last valid data time
                                                last_valid_data_time = time.time()

                                                # Format the data for display
                                                display_data = {
                                                    'status': 'success',
                                                    'range': range_val,
                                                    'speed': speed_val,
                                                    'timestamp': time.time(),
                                                    'connection_status': 'connected',
                                                    'raw_data': decoded_data,
                                                    'display_text': f"[CONNECTED] Range: {range_val}m, Speed: {speed_val}km/h",
                                                    'direction_name': direction_name,  # Save direction name directly
                                                    'direction_prefix': prefix         # Save prefix for reference
                                                }

                                                data_queue.put(display_data)

                                                # Add to data cache for periodic file saving
                                                if radar.id in self.data_cache:
                                                    self.data_cache[radar.id].append(display_data)

                                                # Handle zero and non-zero readings
                                                if range_val == 0 and speed_val == 0:
                                                    consecutive_zeros += 1
                                                    # If we have enough consecutive zeros and we were tracking a detection
                                                    if consecutive_zeros >= max_consecutive_zeros and current_detection:
                                                        # Save the current detection if it has any non-zero values
                                                        has_non_zero = any(
                                                            float(p['raw_data'][2:].split(',')[0]) != 0 or 
                                                            float(p['raw_data'][2:].split(',')[1]) != 0 
                                                            for p in current_detection
                                                        )
                                                        if has_non_zero:
                                                            # Save detection to database
                                                            self._save_detection(radar, current_detection)
                                                        current_detection = []
                                                        last_was_zero = True
                                                else:
                                                    # Reset consecutive zeros counter
                                                    consecutive_zeros = 0
                                                    # Add to current detection
                                                    current_detection.append(display_data)
                                                    last_was_zero = False
                                                    
                                        except ValueError as e:
                                            logger.debug(f"Invalid numeric values in data: {decoded_data}, error: {str(e)}")
                                            continue
                                        except Exception as e:
                                            logger.error(f"Error processing data point: {str(e)}")
                                            continue
                                except Exception as e:
                                    logger.error(f"Error reading data line: {str(e)}")
                                    continue
                            
                            # Small sleep to prevent CPU spinning
                            time.sleep(0.001)
                        except Exception as e:
                            error_msg = f"Error reading data: {str(e)}"
                            logger.error(f"Error reading from radar {radar.id}: {error_msg}")
                            error_data = {
                                'timestamp': int(time.time()),
                                'display_text': error_msg,
                                'connection_status': 'error'
                            }
                            data_queue.put(error_data)
                            break  # Break on error to allow reconnection
                    
                    logger.info(f"Stop event received for radar {radar.id}")
                    
            except serial.SerialException as e:
                connection_attempts += 1
                error_msg = f"Serial connection error: {str(e)}"
                logger.error(f"Connection error for radar {radar.id}: {error_msg}")
                
                # Send error message to serial terminal
                error_data = {
                    'timestamp': int(time.time()),
                    'display_text': error_msg,
                    'connection_status': 'error'
                }
                data_queue.put(error_data)
                
                if connection_attempts < max_connection_attempts:
                    retry_msg = f"Retrying connection in {connection_retry_delay} seconds... (Attempt {connection_attempts}/{max_connection_attempts})"
                    logger.info(retry_msg)
                    retry_data = {
                        'timestamp': int(time.time()),
                        'display_text': retry_msg,
                        'connection_status': 'retrying'
                    }
                    data_queue.put(retry_data)
                    time.sleep(connection_retry_delay)
                else:
                    final_error = f"Failed to connect after {max_connection_attempts} attempts"
                    logger.error(final_error)
                    final_error_data = {
                        'timestamp': int(time.time()),
                        'display_text': final_error,
                        'connection_status': 'disconnected'
                    }
                    data_queue.put(final_error_data)
                    break
                    
            except Exception as e:
                error_msg = f"Unexpected error: {str(e)}"
                logger.error(f"Unexpected error in radar {radar.id} stream: {error_msg}")
                error_data = {
                    'timestamp': int(time.time()),
                    'display_text': error_msg,
                    'connection_status': 'error'
                }
                data_queue.put(error_data)
                break
                
        if connection_attempts >= max_connection_attempts:
            logger.error(f"Maximum connection attempts reached for radar {radar.id}")
            final_error_data = {
                'timestamp': int(time.time()),
                'display_text': "Connection failed - maximum attempts reached",
                'connection_status': 'disconnected'
            }
            data_queue.put(final_error_data)
        
        logger.info(f"Closing data stream for radar {radar.id}")
        # Send final disconnect message
        disconnect_data = {
            'timestamp': int(time.time()),
            'display_text': "Connection closed",
            'connection_status': 'disconnected'
        }
        data_queue.put(disconnect_data)

    def _save_detection(self, radar, detection_data):
        """Save a single object detection to the database"""
        try:
            RadarObjectDetection = apps.get_model('app', 'RadarObjectDetection')
            
            # Calculate statistics for the detection
            ranges = []
            speeds = []
            formatted_data = []
            
            direction_counts = {'positive': 0, 'negative': 0, 'unknown': 0}
            for data_point in detection_data:
                # Parse prefix and range/speed
                prefix = data_point['raw_data'][:2]
                parts = data_point['raw_data'][2:].split(',')
                range_val = float(parts[0])
                speed_val = float(parts[1])
                # Determine direction name from prefix
                if prefix == '*+':
                    direction_name = radar.direction_positive_name
                    direction_counts['positive'] += 1
                elif prefix == '*-':
                    direction_name = radar.direction_negative_name
                    direction_counts['negative'] += 1
                else:
                    direction_name = 'Unknown'
                    direction_counts['unknown'] += 1
                ranges.append(range_val)
                speeds.append(speed_val)
                # Convert timestamp to datetime string
                dt = datetime.fromtimestamp(data_point['timestamp'])
                dt = timezone.make_aware(dt)
                formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                formatted_data.append({
                    'timestamp': formatted_time,
                    'raw_data': data_point['raw_data'],
                    'direction_name': direction_name
                })
            # Create detection record
            start_time = datetime.fromtimestamp(detection_data[0]['timestamp'])
            start_time = timezone.make_aware(start_time)
            end_time = datetime.fromtimestamp(detection_data[-1]['timestamp'])
            end_time = timezone.make_aware(end_time)
            # Determine majority direction for the detection
            if direction_counts['negative'] > direction_counts['positive'] and direction_counts['negative'] > direction_counts['unknown']:
                detection_direction_name = radar.direction_negative_name
            elif direction_counts['positive'] > direction_counts['unknown']:
                detection_direction_name = radar.direction_positive_name
            else:
                detection_direction_name = 'Unknown'
            RadarObjectDetection.objects.create(
                radar=radar,
                start_time=start_time,
                end_time=end_time,
                min_range=min(ranges),
                max_range=max(ranges),
                avg_range=sum(ranges) / len(ranges),
                min_speed=min(speeds),
                max_speed=max(speeds),
                avg_speed=sum(speeds) / len(speeds),
                detection_count=len(detection_data),
                raw_data=formatted_data,
                direction_name=detection_direction_name
            )
            logger.info(f"Saved object detection for radar {radar.id} with {len(detection_data)} readings")
        except Exception as e:
            logger.error(f"Error saving object detection for radar {radar.id}: {str(e)}")