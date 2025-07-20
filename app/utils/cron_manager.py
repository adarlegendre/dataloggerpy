import os
import subprocess
import tempfile
import logging
from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)

class CronManager:
    """Manages Linux cron jobs for notification scheduling"""
    
    def __init__(self):
        self.project_dir = settings.BASE_DIR
        self.cron_comment = "# Radar Notification Service"
        self.log_file = os.path.join(self.project_dir, 'logs', 'notification_service.log')
    
    def get_current_crontab(self):
        """Get the current crontab content"""
        try:
            result = subprocess.run(
                ['crontab', '-l'],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                return result.stdout
            else:
                return ""
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError) as e:
            logger.error(f"Error getting current crontab: {e}")
            return ""
    
    def install_crontab(self, crontab_content):
        """Install a new crontab"""
        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(crontab_content)
                temp_file_path = temp_file.name
            
            # Install the crontab
            result = subprocess.run(
                ['crontab', temp_file_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            # Clean up temporary file
            os.unlink(temp_file_path)
            
            if result.returncode == 0:
                logger.info("Crontab installed successfully")
                return True
            else:
                logger.error(f"Failed to install crontab: {result.stderr}")
                return False
                
        except Exception as e:
            logger.error(f"Error installing crontab: {e}")
            return False
    
    def remove_radar_cron_jobs(self, crontab_content):
        """Remove existing radar notification cron jobs"""
        lines = crontab_content.split('\n')
        filtered_lines = []
        skip_until_empty = False
        
        for line in lines:
            if self.cron_comment in line:
                skip_until_empty = True
                continue
            elif skip_until_empty and line.strip() == '':
                skip_until_empty = False
                continue
            elif skip_until_empty:
                continue
            else:
                filtered_lines.append(line)
        
        return '\n'.join(filtered_lines)
    
    def setup_notification_cron(self, notification_settings):
        """Set up cron job based on notification settings"""
        if not notification_settings.enable_notifications:
            logger.info("Notifications disabled, removing cron job")
            return self.remove_notification_cron()
        
        # Get current crontab
        current_crontab = self.get_current_crontab()
        
        # Remove existing radar cron jobs
        cleaned_crontab = self.remove_radar_cron_jobs(current_crontab)
        
        # Create logs directory if it doesn't exist
        logs_dir = os.path.dirname(self.log_file)
        os.makedirs(logs_dir, exist_ok=True)
        
        # Create new crontab content
        new_crontab = cleaned_crontab.rstrip() + '\n\n'
        new_crontab += f"{self.cron_comment}\n"
        new_crontab += f"# Configured on {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        new_crontab += f"# Settings: {notification_settings.primary_email} - {notification_settings.frequency}\n"
        new_crontab += f"# Days: {notification_settings.days_of_week or 'All days'}\n"
        new_crontab += f"# Times: {notification_settings.notification_times or 'Any time'}\n"
        
        # Add the cron job that runs every minute
        cron_job = f"* * * * * cd {self.project_dir} && "
        cron_job += f"source venv/bin/activate && "
        cron_job += f"python manage.py check_notification_schedule >> {self.log_file} 2>&1"
        
        new_crontab += cron_job + '\n'
        
        # Install the new crontab
        success = self.install_crontab(new_crontab)
        
        if success:
            logger.info(f"Notification cron job configured for {notification_settings.primary_email}")
            # Log with notification logger if available
            try:
                from app.utils.notification_logger import notification_logger
                notification_logger.log_cron_setup("setup", True, f"Email: {notification_settings.primary_email}")
            except:
                pass
            return True
        else:
            logger.error("Failed to configure notification cron job")
            # Log with notification logger if available
            try:
                from app.utils.notification_logger import notification_logger
                notification_logger.log_cron_setup("setup", False, f"Email: {notification_settings.primary_email}")
            except:
                pass
            return False
    
    def remove_notification_cron(self):
        """Remove notification cron job"""
        current_crontab = self.get_current_crontab()
        cleaned_crontab = self.remove_radar_cron_jobs(current_crontab)
        
        if cleaned_crontab != current_crontab:
            success = self.install_crontab(cleaned_crontab)
            if success:
                logger.info("Notification cron job removed")
                return True
            else:
                logger.error("Failed to remove notification cron job")
                return False
        else:
            logger.info("No notification cron job found to remove")
            return True
    
    def get_cron_status(self):
        """Get the status of the notification cron job"""
        current_crontab = self.get_current_crontab()
        
        if self.cron_comment in current_crontab:
            # Extract the cron job line
            lines = current_crontab.split('\n')
            for line in lines:
                if line.strip() and not line.startswith('#') and 'check_notification_schedule' in line:
                    return {
                        'installed': True,
                        'cron_job': line.strip(),
                        'log_file': self.log_file
                    }
        
        return {
            'installed': False,
            'cron_job': None,
            'log_file': self.log_file
        }
    
    def test_cron_access(self):
        """Test if we have access to crontab"""
        import platform
        
        # Check if we're on a Unix-like system
        if platform.system() not in ['Linux', 'Darwin', 'FreeBSD']:
            logger.info(f"Cron not available on {platform.system()}")
            return False
            
        try:
            result = subprocess.run(
                ['crontab', '-l'],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except Exception as e:
            logger.error(f"Cron access test failed: {e}")
            return False

# Global instance
cron_manager = CronManager() 