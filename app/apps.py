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
        import os
        
        # Check if this is the main process (not a reload or worker)
        if 'runserver' not in sys.argv and 'uwsgi' not in sys.argv and 'gunicorn' not in sys.argv:
            return
        
        # Prevent running multiple times during development reload
        if os.environ.get('RUN_MAIN') != 'true' and 'runserver' in sys.argv:
            return

        logger.info("=" * 60)
        logger.info("Radar Data Logger - Server Startup")
        logger.info("=" * 60)

        # Start radar data service
        try:
            from .services import RadarDataService
            service = RadarDataService()
            service.start_service()
            logger.info("✓ Radar data service started")
        except Exception as e:
            logger.error(f"✗ Failed to start radar data service: {str(e)}")

        # Setup cron jobs (this clears ALL old jobs and creates a fresh one)
        try:
            from .utils.system_utils import setup_email_cron_jobs
            import platform
            
            if platform.system() != 'Windows':
                logger.info("Configuring Linux cron jobs for email notifications...")
                success = setup_email_cron_jobs()
                if success:
                    logger.info("✓ Email notification cron job configured")
                    logger.info("  Cron job runs every minute and checks schedule")
                    logger.info("  Emails sent based on notification settings")
                else:
                    logger.warning("⚠ Email cron job not configured")
                    logger.warning("  Possible reasons:")
                    logger.warning("  - Notification settings not found in database")
                    logger.warning("  - Notifications are disabled")
                    logger.warning("  Configure in Django admin: /admin/app/notificationsettings/")
            else:
                logger.info("Running on Windows - use Windows Task Scheduler for notifications")
                logger.info("  Run: .\\setup_notification_scheduler.ps1")
        except Exception as e:
            logger.error(f"✗ Failed to set up cron jobs during startup: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())

        # Start cron status monitor
        try:
            from .utils.system_utils import start_status_monitor
            start_status_monitor()
            logger.info("✓ Cron status monitor started")
        except Exception as e:
            logger.error(f"✗ Failed to start cron status monitor: {str(e)}")
        
        logger.info("=" * 60)
