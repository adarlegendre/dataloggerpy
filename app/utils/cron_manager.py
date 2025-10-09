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
        """
        Remove ALL existing radar notification cron jobs.
        This includes:
        - Jobs with our comment marker
        - Jobs calling send_json_reports
        - Jobs calling check_notification_schedule
        - Jobs with radar_email_job comment
        """
        lines = crontab_content.split('\n')
        filtered_lines = []
        skip_until_empty = False
        
        # Keywords that indicate a radar notification job
        radar_keywords = [
            'send_json_reports',
            'check_notification_schedule',
            'radar_email_job',
            'email_reports.log',
            'notification_service.log',
            'loggervenv',  # User's actual venv name
            'dataloggerpy',  # Project path
            self.cron_comment
        ]
        
        for line in lines:
            # Skip comment blocks for radar jobs
            if self.cron_comment in line:
                skip_until_empty = True
                continue
            elif skip_until_empty and line.strip() == '':
                skip_until_empty = False
                continue
            elif skip_until_empty:
                continue
            # Skip any line containing radar keywords (catches all the duplicates)
            elif any(keyword in line for keyword in radar_keywords):
                logger.debug(f"Removing duplicate cron job: {line.strip()}")
                continue
            else:
                filtered_lines.append(line)
        
        return '\n'.join(filtered_lines)
    
    def setup_notification_cron(self, notification_settings):
        """
        Set up cron job based on notification settings.
        ALWAYS cleans ALL existing radar cron jobs first, then creates a fresh one.
        """
        # STEP 1: ALWAYS remove ALL existing radar cron jobs first
        logger.info("Step 1: Cleaning up ALL existing radar notification cron jobs...")
        current_crontab = self.get_current_crontab()
        
        # Count how many entries will be removed
        radar_lines = [line for line in current_crontab.split('\n') 
                      if any(keyword in line for keyword in [
                          'send_json_reports',
                          'check_notification_schedule',
                          'radar_email_job',
                          'email_reports.log',
                          'notification_service.log',
                          'loggervenv',
                          'dataloggerpy'
                      ])]
        
        if radar_lines:
            logger.info(f"Found {len(radar_lines)} existing radar cron entries to remove")
        else:
            logger.info("No existing radar cron entries found (clean slate)")
        
        # Remove all existing radar cron jobs
        cleaned_crontab = self.remove_radar_cron_jobs(current_crontab)
        
        # STEP 2: Check if we should create a new one
        if not notification_settings.enable_notifications:
            logger.info("Notifications disabled - only cleanup performed, no new job created")
            return self.install_crontab(cleaned_crontab)
        
        # Create logs directory if it doesn't exist
        logs_dir = os.path.dirname(self.log_file)
        os.makedirs(logs_dir, exist_ok=True)
        
        # STEP 3: Detect virtual environment path
        logger.info("Step 2: Detecting virtual environment...")
        venv_path = None
        possible_venv_names = ['loggervenv', 'venv', 'env', '.venv', 'virtualenv']
        for venv_name in possible_venv_names:
            test_path = os.path.join(self.project_dir, venv_name, 'bin', 'activate')
            if os.path.exists(test_path):
                venv_path = venv_name
                logger.info(f"✓ Detected virtual environment: {venv_name}")
                break
        
        if not venv_path:
            logger.error("✗ Could not find virtual environment directory!")
            logger.error(f"  Looked for: {', '.join(possible_venv_names)}")
            logger.error("  Aborting cron setup")
            return False
        
        # STEP 4: Create new crontab content
        logger.info("Step 3: Creating new cron job entry...")
        new_crontab = cleaned_crontab.rstrip() + '\n\n'
        new_crontab += f"{self.cron_comment}\n"
        new_crontab += f"# Configured on {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        new_crontab += f"# Settings: {notification_settings.primary_email} - {notification_settings.frequency}\n"
        new_crontab += f"# Days: {notification_settings.days_of_week or 'All days'}\n"
        new_crontab += f"# Times: {notification_settings.notification_times or 'Any time'}\n"
        new_crontab += f"# Virtual Environment: {venv_path}\n"
        
        # Add the cron job that runs every minute
        cron_job = f"* * * * * cd {self.project_dir} && "
        cron_job += f"source {venv_path}/bin/activate && "
        cron_job += f"python manage.py check_notification_schedule >> {self.log_file} 2>&1"
        
        new_crontab += cron_job + '\n'
        
        logger.info(f"  Cron schedule: Every minute (* * * * *)")
        logger.info(f"  Virtual env: {venv_path}")
        logger.info(f"  Log file: {self.log_file}")
        
        # STEP 5: Install the new crontab
        logger.info("Step 4: Installing new crontab...")
        success = self.install_crontab(new_crontab)
        
        if success:
            logger.info("=" * 60)
            logger.info("✓ CRON JOB SETUP SUCCESSFUL")
            logger.info("=" * 60)
            if radar_lines:
                logger.info(f"  Removed: {len(radar_lines)} old cron entries")
            logger.info(f"  Created: 1 new cron entry")
            logger.info(f"  Email: {notification_settings.primary_email}")
            logger.info(f"  Virtual Env: {venv_path}")
            logger.info(f"  Schedule: Checks every minute")
            logger.info(f"  Sends when: {notification_settings.notification_times or 'Any time'}")
            logger.info("=" * 60)
            
            # Log with notification logger if available
            try:
                from app.utils.notification_logger import notification_logger
                notification_logger.log_cron_setup("setup", True, f"Email: {notification_settings.primary_email}")
            except:
                pass
            return True
        else:
            logger.error("=" * 60)
            logger.error("✗ CRON JOB SETUP FAILED")
            logger.error("=" * 60)
            logger.error("Failed to install new crontab")
            
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