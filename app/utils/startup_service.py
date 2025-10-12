"""
Startup service module for radar data collection status
"""
import logging
from django.utils import timezone

logger = logging.getLogger(__name__)


def get_radar_service_status():
    """
    Get the status of the radar data collection service.
    Returns a dictionary with service status information.
    """
    try:
        from app.services import RadarDataService
        
        service = RadarDataService()
        
        # Count active radar threads
        active_radars = len([t for t in service.radar_threads.values() if t and t.is_alive()])
        active_threads = len(service.radar_threads)
        
        return {
            'started': active_radars > 0,
            'radar_service': 'running' if active_radars > 0 else 'stopped',
            'active_radars': active_radars,
            'active_threads': active_threads,
            'last_check': timezone.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Error getting radar service status: {str(e)}")
        return {
            'started': False,
            'radar_service': 'error',
            'active_radars': 0,
            'active_threads': 0,
            'last_check': timezone.now().isoformat(),
            'error': str(e)
        }


def initialize_radar_data_collection():
    """
    Initialize radar data collection service.
    This is called during Django startup.
    """
    try:
        from app.services import RadarDataService
        
        logger.info("Initializing radar data collection service...")
        service = RadarDataService()
        service.start_service()
        logger.info("Radar data collection service initialized")
        return True
    except Exception as e:
        logger.error(f"Failed to initialize radar data collection: {str(e)}")
        return False


class StartupService:
    """
    Service for managing radar data collection startup and lifecycle.
    """
    
    def __init__(self):
        self.service = None
        
    def start_radar_data_collection(self):
        """Start the radar data collection service"""
        try:
            from app.services import RadarDataService
            
            if not self.service:
                self.service = RadarDataService()
            
            self.service.start_service()
            logger.info("Radar data collection started")
            return True
        except Exception as e:
            logger.error(f"Failed to start radar data collection: {str(e)}")
            return False
    
    def stop_radar_data_collection(self):
        """Stop the radar data collection service"""
        try:
            if self.service:
                self.service.stop_service()
                logger.info("Radar data collection stopped")
            return True
        except Exception as e:
            logger.error(f"Failed to stop radar data collection: {str(e)}")
            return False
    
    def get_status(self):
        """Get the current status"""
        return get_radar_service_status()


# Global instance
startup_service = StartupService()

