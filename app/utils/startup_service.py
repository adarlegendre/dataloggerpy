import threading
import time
import logging
from django.apps import apps
from django.utils import timezone
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class StartupService:
    """Service to handle automatic startup of radar data collection"""
    
    def __init__(self):
        self.radar_service = None
        self.startup_completed = False
        self.startup_lock = threading.Lock()
    
    def start_radar_data_collection(self):
        """Start radar data collection service"""
        with self.startup_lock:
            if self.startup_completed:
                logger.info("Radar data collection already started")
                return
            
            try:
                logger.info("Starting radar data collection service...")
                
                # Import and start the radar data service
                from ..services import RadarDataService
                self.radar_service = RadarDataService()
                
                # Start the service
                self.radar_service.start_service()
                
                # Log active radars
                RadarConfig = apps.get_model('app', 'RadarConfig')
                active_radars = RadarConfig.objects.filter(is_active=True)
                
                logger.info(f"Radar data collection started successfully")
                logger.info(f"Active radars: {len(active_radars)}")
                
                for radar in active_radars:
                    logger.info(f"  - Radar {radar.id}: {radar.name} on {radar.port}")
                
                self.startup_completed = True
                
                # Start monitoring thread
                self._start_monitoring_thread()
                
            except Exception as e:
                logger.error(f"Failed to start radar data collection: {str(e)}")
                raise
    
    def _start_monitoring_thread(self):
        """Start a background thread to monitor radar service health"""
        def monitor_radar_service():
            while self.startup_completed:
                try:
                    # Check if radar threads are still running
                    if self.radar_service:
                        active_threads = 0
                        for radar_id, thread in self.radar_service.radar_threads.items():
                            if thread.is_alive():
                                active_threads += 1
                            else:
                                logger.warning(f"Radar {radar_id} thread is not alive, restarting...")
                                # Restart the radar
                                self._restart_radar(radar_id)
                        
                        if active_threads > 0:
                            logger.debug(f"Radar service monitoring: {active_threads} active threads")
                    
                    # Sleep for 30 seconds before next check
                    time.sleep(30)
                    
                except Exception as e:
                    logger.error(f"Error in radar service monitoring: {str(e)}")
                    time.sleep(30)
        
        monitor_thread = threading.Thread(target=monitor_radar_service, daemon=True)
        monitor_thread.start()
        logger.info("Radar service monitoring thread started")
    
    def _restart_radar(self, radar_id):
        """Restart a specific radar"""
        try:
            RadarConfig = apps.get_model('app', 'RadarConfig')
            radar = RadarConfig.objects.get(id=radar_id, is_active=True)
            
            logger.info(f"Restarting radar {radar_id} ({radar.name})")
            
            # Stop the current stream
            self.radar_service.stop_radar_stream(radar_id)
            
            # Wait a moment
            time.sleep(2)
            
            # Start the stream again
            self.radar_service.start_radar_stream(radar)
            
            logger.info(f"Radar {radar_id} restarted successfully")
            
        except Exception as e:
            logger.error(f"Failed to restart radar {radar_id}: {str(e)}")
    
    def stop_radar_data_collection(self):
        """Stop radar data collection service"""
        try:
            if self.radar_service:
                logger.info("Stopping radar data collection service...")
                self.radar_service.stop_service()
                self.startup_completed = False
                logger.info("Radar data collection service stopped")
        except Exception as e:
            logger.error(f"Error stopping radar data collection: {str(e)}")
    
    def get_service_status(self):
        """Get the current status of the radar data collection service"""
        status = {
            'started': self.startup_completed,
            'radar_service': None,
            'active_radars': 0,
            'active_threads': 0,
            'last_check': timezone.now().isoformat()
        }
        
        if self.radar_service:
            status['radar_service'] = 'active'
            status['active_threads'] = len([
                thread for thread in self.radar_service.radar_threads.values() 
                if thread.is_alive()
            ])
            
            # Count active radars
            try:
                RadarConfig = apps.get_model('app', 'RadarConfig')
                active_radars = RadarConfig.objects.filter(is_active=True)
                status['active_radars'] = len(active_radars)
            except Exception as e:
                logger.error(f"Error getting active radars count: {str(e)}")
        
        return status

# Global startup service instance
startup_service = StartupService()

def initialize_radar_data_collection():
    """Initialize radar data collection on system startup"""
    try:
        logger.info("Initializing radar data collection...")
        startup_service.start_radar_data_collection()
        logger.info("Radar data collection initialization completed")
        return True
    except Exception as e:
        logger.error(f"Failed to initialize radar data collection: {str(e)}")
        return False

def get_radar_service_status():
    """Get the status of the radar data collection service"""
    return startup_service.get_service_status() 