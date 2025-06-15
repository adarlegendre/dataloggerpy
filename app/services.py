import threading
import time
import json
import serial
from django.apps import apps
from queue import Queue
import logging
import os
from datetime import datetime
from collections import deque

logger = logging.getLogger(__name__)

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
            radar = RadarConfig.objects.get(id=radar_id)
            
            # Create directory if it doesn't exist
            save_dir = os.path.join(radar.data_storage_path)
            os.makedirs(save_dir, exist_ok=True)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"radar_{radar.name}_{timestamp}.json"
            filepath = os.path.join(save_dir, filename)
            
            # Extract only timestamp and raw data from the data
            simplified_data = []
            for data_point in self.data_cache[radar_id]:
                # Convert timestamp to datetime string
                dt = datetime.fromtimestamp(data_point['timestamp'])
                formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # Format: YYYY-MM-DD HH:MM:SS.mmm
                simplified_data.append({
                    'timestamp': formatted_time,
                    'raw_data': data_point['raw_data']
                })
            
            # Save simplified data to file
            with open(filepath, 'w') as f:
                json.dump(simplified_data, f, indent=2)
            
            # Get file size
            file_size = os.path.getsize(filepath)
            record_count = len(simplified_data)
            
            # Create RadarDataFile record
            RadarDataFile.objects.create(
                radar=radar,
                filename=filename,
                file_path=filepath,
                record_count=record_count,
                file_size=file_size
            )
            
            logger.info(f"Saved {record_count} readings to {filepath}")
            # Clear the cache after saving
            self.data_cache[radar_id].clear()
            
        except Exception as e:
            logger.error(f"Error saving data to file for radar {radar_id}: {str(e)}")
    
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
                    bytesize=radar.data_bits,
                    parity=radar.parity,
                    stopbits=radar.stop_bits,
                    timeout=1
                ) as ser:
                    logger.info(f"Successfully connected to radar {radar.id} on {radar.port}")
                    
                    # Send connection success message
                    success_message = {
                        'timestamp': int(time.time()),
                        'display_text': f"Connected to radar on port {radar.port}",
                        'connection_status': 'connected'
                    }
                    data_queue.put(success_message)
                    
                    while not stop_event.is_set():
                        if ser.in_waiting:
                            try:
                                # Log waiting bytes
                                logger.debug(f"Data waiting: {ser.in_waiting} bytes")
                                
                                data = ser.readline().strip()
                                if data:
                                    # Log raw data received
                                    logger.debug(f"Raw data received: {data}")
                                    
                                    # Process the data
                                    try:
                                        # Decode the data
                                        decoded_data = data.decode('utf-8', errors='replace')
                                        logger.debug(f"Processing data: {decoded_data}")
                                        
                                        # Parse the data (assuming format *+XXX.X,YYY)
                                        if decoded_data.startswith('*'):
                                            # Extract range and speed
                                            parts = decoded_data[1:].split(',')
                                            if len(parts) == 2:
                                                range_val = float(parts[0])
                                                speed_val = float(parts[1])
                                                logger.debug(f"Parsed values - Range: {range_val}, Speed: {speed_val}")
                                                
                                                # Format the data for display
                                                display_data = {
                                                    'status': 'success',
                                                    'range': range_val,
                                                    'speed': speed_val,
                                                    'timestamp': time.time(),
                                                    'connection_status': 'connected',
                                                    'raw_data': decoded_data,
                                                    'display_text': f"[CONNECTED] Range: {range_val}m, Speed: {speed_val}mm/s"
                                                }
                                                
                                                # Log the queued data
                                                logger.debug(f"Data queued: {display_data}")
                                                data_queue.put(display_data)
                                            else:
                                                logger.warning(f"Invalid data format: {decoded_data}")
                                        else:
                                            logger.warning(f"Invalid data prefix: {decoded_data}")
                                    except ValueError as e:
                                        logger.error(f"Error parsing data: {str(e)}")
                                        error_data = {
                                            'timestamp': int(time.time()),
                                            'display_text': f"Error parsing data: {str(e)}",
                                            'connection_status': 'error'
                                        }
                                        data_queue.put(error_data)
                            except Exception as e:
                                error_msg = f"Error reading data: {str(e)}"
                                logger.error(f"Error reading from radar {radar.id}: {error_msg}")
                                error_data = {
                                    'timestamp': int(time.time()),
                                    'display_text': error_msg,
                                    'connection_status': 'error'
                                }
                                data_queue.put(error_data)
                        time.sleep(radar.update_interval / 1000.0)  # Convert to seconds
                    
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