"""
Camera Service - Django service to integrate camera vehicle detection data
"""

import threading
import time
import json
import logging
from datetime import datetime
from django.apps import apps
from django.utils import timezone

logger = logging.getLogger(__name__)

class CameraDataService:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(CameraDataService, cls).__new__(cls)
                cls._instance._initialized = False
            return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        self._initialized = True
        self.running = False
        self.camera_threads = {}
        self.data_queues = {}
        self.stop_events = {}
        self.last_detection_time = {}
        
        logger.info("CameraDataService initialized")
    
    def start_service(self):
        """Start the camera data service"""
        logger.info("Starting camera data service")
        
        # Get camera configurations
        CameraConfig = apps.get_model('app', 'CameraConfig')
        cameras = CameraConfig.objects.filter(is_active=True)
        
        if not cameras.exists():
            logger.warning("No active cameras found")
            return
        
        for camera in cameras:
            logger.info(f"Starting camera: {camera.name}")
            self.start_camera_stream(camera)
    
    def stop_service(self):
        """Stop the camera data service"""
        logger.info("Stopping camera data service")
        for camera_id in list(self.stop_events.keys()):
            self.stop_camera_stream(camera_id)
    
    def start_camera_stream(self, camera):
        """Start streaming data for a specific camera"""
        camera_id = camera.id
        if camera_id in self.camera_threads and self.camera_threads[camera_id].is_alive():
            logger.warning(f"Camera {camera_id} stream already running")
            return
        
        logger.info(f"Starting camera stream for {camera.name} (ID: {camera_id})")
        self.data_queues[camera_id] = []
        self.stop_events[camera_id] = threading.Event()
        self.last_detection_time[camera_id] = time.time()
        
        thread = threading.Thread(
            target=self._stream_camera_data,
            args=(camera, self.data_queues[camera_id], self.stop_events[camera_id]),
            daemon=True
        )
        thread.start()
        self.camera_threads[camera_id] = thread
        logger.info(f"Started camera streaming thread for {camera.name}")
    
    def stop_camera_stream(self, camera_id):
        """Stop streaming data for a specific camera"""
        if camera_id in self.stop_events:
            self.stop_events[camera_id].set()
        
        if camera_id in self.camera_threads:
            thread = self.camera_threads[camera_id]
            if thread.is_alive():
                thread.join(timeout=5)
            del self.camera_threads[camera_id]
        
        if camera_id in self.data_queues:
            del self.data_queues[camera_id]
        
        if camera_id in self.stop_events:
            del self.stop_events[camera_id]
        
        logger.info(f"Stopped camera stream for ID: {camera_id}")
    
    def _stream_camera_data(self, camera, data_queue, stop_event):
        """Background thread function for streaming camera data"""
        logger.info(f"Starting camera data stream for {camera.name}")
        
        try:
            # Import here to avoid circular imports
            from .viid_camera_listener import VIIDCameraListener
            
            # Create VIID listener
            listener = VIIDCameraListener(
                camera_ip=camera.ip_address,
                camera_port=camera.port,
                username=camera.username,
                password=camera.password
            )
            
            # Connect to camera
            if not listener.connect_to_camera():
                logger.error(f"Failed to connect to camera {camera.name}")
                return
            
            # Listen for data
            while not stop_event.is_set():
                try:
                    # Check for new vehicle detections
                    vehicle_data = listener.get_vehicle_data()
                    
                    if vehicle_data:
                        # Process new detections
                        for detection in vehicle_data:
                            self._process_vehicle_detection(camera, detection, data_queue)
                    
                    time.sleep(1)  # Check every second
                    
                except Exception as e:
                    logger.error(f"Error in camera data stream: {e}")
                    time.sleep(5)
            
        except Exception as e:
            logger.error(f"Failed to start camera data stream: {e}")
        finally:
            if hasattr(listener, 'socket') and listener.socket:
                listener.socket.close()
            logger.info(f"Camera data stream ended for {camera.name}")
    
    def _process_vehicle_detection(self, camera, detection_data, data_queue):
        """Process vehicle detection data from camera"""
        try:
            vehicle_data = detection_data.get('vehicle_data', {})
            timestamp = detection_data.get('timestamp', timezone.now())
            
            # Extract vehicle information
            plate_number = vehicle_data.get('plate_number', '')
            confidence = float(vehicle_data.get('confidence', 0))
            speed = float(vehicle_data.get('speed', 0)) if vehicle_data.get('speed') else None
            direction = vehicle_data.get('direction', '')
            vehicle_type = vehicle_data.get('vehicle_type', 'Motor Vehicle')
            
            # Only process if we have a plate number and good confidence
            if plate_number and confidence > 50:
                logger.info(f"Processing vehicle detection: {plate_number} (confidence: {confidence}%)")
                
                # Create camera detection record
                self._save_camera_detection(camera, {
                    'plate_number': plate_number,
                    'confidence': confidence,
                    'speed': speed,
                    'direction': direction,
                    'vehicle_type': vehicle_type,
                    'timestamp': timestamp,
                    'raw_data': detection_data.get('raw_message', ''),
                    'format': detection_data.get('format', 'unknown')
                })
                
                # Add to data queue for real-time display
                display_data = {
                    'timestamp': int(timestamp.timestamp()),
                    'plate_number': plate_number,
                    'confidence': confidence,
                    'speed': speed,
                    'direction': direction,
                    'vehicle_type': vehicle_type,
                    'source': 'camera',
                    'camera_name': camera.name
                }
                
                data_queue.append(display_data)
                
                # Keep only last 100 items in queue
                if len(data_queue) > 100:
                    data_queue.pop(0)
                
        except Exception as e:
            logger.error(f"Error processing vehicle detection: {e}")
    
    def _save_camera_detection(self, camera, detection_data):
        """Save camera detection to database"""
        try:
            CameraDetection = apps.get_model('app', 'CameraDetection')
            
            CameraDetection.objects.create(
                camera=camera,
                plate_number=detection_data['plate_number'],
                confidence=detection_data['confidence'],
                speed=detection_data['speed'],
                direction=detection_data['direction'],
                vehicle_type=detection_data['vehicle_type'],
                timestamp=detection_data['timestamp'],
                raw_data=detection_data['raw_data'],
                data_format=detection_data['format']
            )
            
            logger.info(f"Saved camera detection: {detection_data['plate_number']}")
            
        except Exception as e:
            logger.error(f"Error saving camera detection: {e}")
    
    def get_camera_data(self, camera_id, limit=50):
        """Get recent camera data for a specific camera"""
        if camera_id in self.data_queues:
            return self.data_queues[camera_id][-limit:]
        return []
    
    def get_all_camera_data(self, limit=100):
        """Get recent camera data from all cameras"""
        all_data = []
        for camera_id, data_queue in self.data_queues.items():
            all_data.extend(data_queue[-limit:])
        
        # Sort by timestamp
        all_data.sort(key=lambda x: x.get('timestamp', 0), reverse=True)
        return all_data[:limit]

# Global instance
camera_service = CameraDataService()

