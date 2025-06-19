from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    
    def ready(self):
        """
        Run startup code when Django starts.
        Note: This may be called multiple times during startup
        """
        # Only run in main process
        import sys
        if 'runserver' not in sys.argv and 'uwsgi' not in sys.argv:
            return

        # Start radar data service
        try:
            from .services import RadarDataService
            service = RadarDataService()
            service.start_service()
            logger.info("Radar data service started")
        except Exception as e:
            logger.error(f"Failed to start radar data service: {str(e)}")

        # Setup cron jobs
        try:
            from .utils.system_utils import setup_email_cron_jobs
            setup_email_cron_jobs()
            logger.info("Email cron jobs setup completed")
        except Exception as e:
            logger.error(f"Failed to set up cron jobs during startup: {str(e)}")

        # Start cron status monitor
        try:
            from .utils.system_utils import start_status_monitor
            start_status_monitor()
        except Exception as e:
            logger.error(f"Failed to start cron status monitor: {str(e)}")
