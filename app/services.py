import threading
import time
import json
import serial
from django.apps import apps
from queue import Queue
import logging

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
        logger.info("RadarDataService initialized")
    
    def start_service(self):
        """Start the radar data service"""
        logger.info("Starting radar data service")
        RadarConfig = apps.get_model('app', 'RadarConfig')
        radars = RadarConfig.objects.filter(is_active=True)
        
        for radar in radars:
            self.start_radar_stream(radar)
    
    def stop_service(self):
        """Stop the radar data service"""
        logger.info("Stopping radar data service")
        for radar_id in list(self.stop_events.keys()):
            self.stop_radar_stream(radar_id)
    
    def start_radar_stream(self, radar):
        """Start streaming data for a specific radar"""
        radar_id = radar.id
        if radar_id in self.radar_threads and self.radar_threads[radar_id].is_alive():
            logger.info(f"Radar {radar_id} stream already running")
            return
            
        self.data_queues[radar_id] = Queue()
        self.stop_events[radar_id] = threading.Event()
        
        thread = threading.Thread(
            target=self._stream_radar_data,
            args=(radar, self.data_queues[radar_id], self.stop_events[radar_id]),
            daemon=True
        )
        thread.start()
        self.radar_threads[radar_id] = thread
        logger.info(f"Started streaming for radar {radar_id}")
    
    def stop_radar_stream(self, radar_id):
        """Stop streaming data for a specific radar"""
        if radar_id in self.stop_events:
            self.stop_events[radar_id].set()
            if radar_id in self.radar_threads:
                self.radar_threads[radar_id].join(timeout=5.0)
            del self.stop_events[radar_id]
            del self.radar_threads[radar_id]
            del self.data_queues[radar_id]
            logger.info(f"Stopped streaming for radar {radar_id}")
    
    def get_latest_data(self, radar_id):
        """Get the latest data for a specific radar"""
        if radar_id in self.data_queues:
            try:
                return self.data_queues[radar_id].get_nowait()
            except:
                return None
        return None
    
    def _stream_radar_data(self, radar, data_queue, stop_event):
        """Background thread function for streaming radar data"""
        logger.info(f"Starting data stream for radar {radar.id} on port {radar.port}")
        
        while not stop_event.is_set():
            try:
                with serial.Serial(
                    port=radar.port,
                    baudrate=radar.baud_rate,
                    bytesize=radar.data_bits,
                    parity=radar.parity,
                    stopbits=radar.stop_bits,
                    timeout=0.1
                ) as ser:
                    while not stop_event.is_set():
                        if ser.in_waiting:
                            try:
                                data = ser.readline().decode('utf-8').strip()
                                logger.debug(f"Raw data from radar {radar.id}: {data}")
                                
                                try:
                                    parsed_data = json.loads(data)
                                    data_queue.put({
                                        'status': 'success',
                                        'range': parsed_data.get('range'),
                                        'speed': parsed_data.get('speed'),
                                        'direction': parsed_data.get('direction'),
                                        'timestamp': time.time(),
                                        'connection_status': 'connected'
                                    })
                                except json.JSONDecodeError:
                                    data_queue.put({
                                        'status': 'success',
                                        'raw_data': data,
                                        'timestamp': time.time(),
                                        'connection_status': 'connected'
                                    })
                            except Exception as e:
                                logger.error(f"Error reading data from radar {radar.id}: {str(e)}")
                                data_queue.put({
                                    'status': 'error',
                                    'message': f'Error reading data: {str(e)}',
                                    'connection_status': 'error'
                                })
                        time.sleep(radar.update_interval / 1000.0)  # Convert ms to seconds
                        
            except serial.SerialException as e:
                logger.error(f"Serial port error for radar {radar.id}: {str(e)}")
                data_queue.put({
                    'status': 'error',
                    'message': f'Serial port error: {str(e)}',
                    'connection_status': 'disconnected'
                })
                time.sleep(5)  # Wait before retrying connection
                
            except Exception as e:
                logger.error(f"Unexpected error for radar {radar.id}: {str(e)}")
                data_queue.put({
                    'status': 'error',
                    'message': f'Unexpected error: {str(e)}',
                    'connection_status': 'error'
                })
                time.sleep(5)  # Wait before retrying