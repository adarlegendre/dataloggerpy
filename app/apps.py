from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    
    def ready(self):
        """Initialize the radar data service when Django starts"""
        try:
            from .services import RadarDataService
            service = RadarDataService()
            service.start_service()
            logger.info("Radar data service started")
        except Exception as e:
            logger.error(f"Failed to start radar data service: {str(e)}")
