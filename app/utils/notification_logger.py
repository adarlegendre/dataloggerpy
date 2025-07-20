import logging
import os
from datetime import datetime
from django.conf import settings
from django.utils import timezone

class NotificationLogger:
    """Comprehensive logging for notification system"""
    
    def __init__(self):
        # Create logs directory if it doesn't exist
        logs_dir = os.path.join(settings.BASE_DIR, 'logs')
        os.makedirs(logs_dir, exist_ok=True)
        
        # Set up file handler for notification logs
        log_file = os.path.join(logs_dir, 'notification_service.log')
        
        # Create logger
        self.logger = logging.getLogger('notification_service')
        self.logger.setLevel(logging.INFO)
        
        # Prevent duplicate handlers
        if not self.logger.handlers:
            # File handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.INFO)
            
            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            
            # Handle Windows console encoding issues
            import sys
            if sys.platform.startswith('win'):
                # Use simple text format for Windows console
                console_formatter = logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )
                console_handler.setFormatter(console_formatter)
            else:
                console_handler.setFormatter(formatter)
            
            # Create formatter
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)
            
            # Add handlers
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)
    
    def log_cron_check_start(self):
        """Log when cron check starts"""
        self.logger.info("Cron check started - checking notification schedule")
    
    def log_cron_check_end(self):
        """Log when cron check ends"""
        self.logger.info("Cron check completed")
    
    def log_settings_check(self, settings):
        """Log notification settings check"""
        self.logger.info(f"Checking settings for: {settings.primary_email}")
        self.logger.info(f"   Frequency: {settings.frequency}")
        self.logger.info(f"   Days: {settings.days_of_week or 'All days'}")
        self.logger.info(f"   Times: {settings.notification_times or 'Any time'}")
        self.logger.info(f"   Enabled: {settings.enable_notifications}")
    
    def log_day_check(self, current_day, allowed_days, passed):
        """Log day of week check"""
        if passed:
            self.logger.info(f"Day check passed: {current_day} is in allowed days {allowed_days}")
        else:
            self.logger.info(f"Day check failed: {current_day} is not in allowed days {allowed_days}")
    
    def log_time_check(self, current_time, allowed_times, passed):
        """Log time check"""
        if passed:
            self.logger.info(f"Time check passed: {current_time} is in allowed times {allowed_times}")
        else:
            self.logger.info(f"Time check failed: {current_time} is not in allowed times {allowed_times}")
    
    def log_frequency_check(self, frequency, time_since_last, required_interval, passed):
        """Log frequency check"""
        if passed:
            self.logger.info(f"Frequency check passed: {time_since_last} >= {required_interval} ({frequency})")
        else:
            self.logger.info(f"Frequency check failed: {time_since_last} < {required_interval} ({frequency})")
    
    def log_file_check(self, file_count):
        """Log file availability check"""
        if file_count > 0:
            self.logger.info(f"File check passed: {file_count} unsent files found")
        else:
            self.logger.info(f"File check failed: No unsent files found")
    
    def log_email_send_attempt(self, recipient, file_count):
        """Log email send attempt"""
        self.logger.info(f"Attempting to send email to {recipient} with {file_count} files")
    
    def log_email_send_success(self, recipient, file_count, notification_id):
        """Log successful email send"""
        self.logger.info(f"Email sent successfully to {recipient}")
        self.logger.info(f"   Files sent: {file_count}")
        self.logger.info(f"   Notification ID: {notification_id}")
    
    def log_email_send_failure(self, recipient, error):
        """Log email send failure"""
        self.logger.error(f"Failed to send email to {recipient}: {error}")
    
    def log_cron_setup(self, action, success, details=None):
        """Log cron setup actions"""
        if success:
            self.logger.info(f"Cron {action} successful")
        else:
            self.logger.error(f"Cron {action} failed")
        
        if details:
            self.logger.info(f"   Details: {details}")
    
    def log_settings_save(self, settings, cron_updated):
        """Log when settings are saved"""
        self.logger.info(f"Notification settings saved for {settings.primary_email}")
        if cron_updated:
            self.logger.info("   Cron jobs updated automatically")
        else:
            self.logger.warning("   Cron jobs not updated (check permissions)")
    
    def log_test_email(self, recipient, success, error=None):
        """Log test email attempts"""
        if success:
            self.logger.info(f"Test email sent successfully to {recipient}")
        else:
            self.logger.error(f"Test email failed for {recipient}: {error}")
    
    def log_system_startup(self):
        """Log system startup"""
        self.logger.info("Radar Notification System starting up")
        self.logger.info(f"   Time: {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.logger.info(f"   Base directory: {settings.BASE_DIR}")
    
    def log_error(self, error, context=None):
        """Log general errors"""
        self.logger.error(f"Error: {error}")
        if context:
            self.logger.error(f"   Context: {context}")

# Global logger instance
notification_logger = NotificationLogger() 