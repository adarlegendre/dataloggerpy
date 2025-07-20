import os
import psutil
import subprocess
import platform
from datetime import datetime, timedelta
from django.utils import timezone
import logging
from ..models import SystemMetrics, NotificationSettings
from pathlib import Path
from crontab import CronTab
import threading
import time as pytime

logger = logging.getLogger(__name__)

def round_to_nearest_30_minutes(td):
    """Round a timedelta to the nearest 30 minutes."""
    total_seconds = int(td.total_seconds())
    minutes = total_seconds // 60
    rounded_minutes = round(minutes / 30) * 30
    return timedelta(minutes=rounded_minutes)

def get_cpu_temperature():
    """Get CPU temperature based on the operating system."""
    try:
        if platform.system() == 'Linux':
            # Try Raspberry Pi first
            try:
                temp = subprocess.check_output(['vcgencmd', 'measure_temp']).decode()
                return float(temp.replace('temp=', '').replace("'C", ''))
            except:
                # Try reading from thermal zone
                try:
                    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                        temp = float(f.read()) / 1000.0
                        return temp
                except:
                    pass
        elif platform.system() == 'Windows':
            # Windows doesn't have a direct way to get CPU temperature
            # You might need to use a third-party tool or WMI
            return None
        return None
    except Exception as e:
        logger.warning(f"Could not get CPU temperature: {str(e)}")
        return None

def get_system_info():
    """Get system information including disk, RAM, and temperature."""
    try:
        # Get disk usage
        disk = psutil.disk_usage('/')
        disk_total = disk.total / (1024 * 1024 * 1024)  # Convert to GB
        disk_used = disk.used / (1024 * 1024 * 1024)
        disk_free = disk.free / (1024 * 1024 * 1024)
        disk_percent = disk.percent

        # Get RAM usage
        memory = psutil.virtual_memory()
        ram_total = memory.total / (1024 * 1024 * 1024)  # Convert to GB
        ram_used = memory.used / (1024 * 1024 * 1024)
        ram_free = memory.available / (1024 * 1024 * 1024)
        ram_percent = memory.percent

        # Get CPU temperature
        cpu_temp = get_cpu_temperature()

        # Get system uptime and round to nearest 30 minutes
        uptime = datetime.fromtimestamp(psutil.boot_time())
        uptime_delta = datetime.now() - uptime
        rounded_uptime = round_to_nearest_30_minutes(uptime_delta)
        uptime_seconds = int(rounded_uptime.total_seconds())

        # Format uptime string
        days = uptime_seconds // (24 * 3600)
        hours = (uptime_seconds % (24 * 3600)) // 3600
        minutes = (uptime_seconds % 3600) // 60
        
        uptime_str = ""
        if days > 0:
            uptime_str += f"{days} days, "
        if hours > 0 or days > 0:
            uptime_str += f"{hours} hours, "
        uptime_str += f"{minutes} minutes"

        # Only save if 30 minutes have passed since last record
        try:
            now = timezone.now()
            last = SystemMetrics.objects.order_by('-timestamp').first()
            should_save = False
            if not last or (now - last.timestamp) >= timedelta(minutes=30):
                should_save = True

            if should_save:
                SystemMetrics.objects.create(
                    disk_used_percent=disk_percent,
                    ram_used_percent=ram_percent,
                    cpu_temperature=cpu_temp,
                    uptime_seconds=uptime_seconds
                )
                # Cleanup: remove records older than 7 days
                cutoff = now - timedelta(days=7)
                SystemMetrics.objects.filter(timestamp__lt=cutoff).delete()

            # Get historical metrics
            avg_metrics = SystemMetrics.get_average_metrics(hours=24)
        except Exception as e:
            logger.warning(f"Could not save system metrics: {str(e)}")
            avg_metrics = None

        return {
            'disk': {
                'total': round(disk_total, 2),
                'used': round(disk_used, 2),
                'free': round(disk_free, 2),
                'percent': disk_percent
            },
            'ram': {
                'total': round(ram_total, 2),
                'used': round(ram_used, 2),
                'free': round(ram_free, 2),
                'percent': ram_percent
            },
            'cpu_temp': cpu_temp,
            'uptime': uptime_str,
            'history': {
                'disk_avg': round(avg_metrics['disk_used_percent'], 1) if avg_metrics else None,
                'ram_avg': round(avg_metrics['ram_used_percent'], 1) if avg_metrics else None,
                'cpu_avg': round(avg_metrics['cpu_temperature'], 1) if avg_metrics and avg_metrics['cpu_temperature'] else None,
            }
        }
    except Exception as e:
        logger.error(f"Error in get_system_info: {str(e)}")
        raise  # Re-raise the exception to be handled by the view 

def get_cron_schedule(settings):
    """
    Generate cron schedule based on notification settings.
    
    Args:
        settings: NotificationSettings instance
    
    Returns:
        list: List of tuples (cron_schedule, description)
    """
    schedules = []
    
    # Parse notification times
    times = ['00:00']  # Default time if none specified
    if settings.notification_times:
        times = [t.strip() for t in settings.notification_times.split(',') if t.strip()]
    
    # Parse days of week
    days = []
    if settings.days_of_week:
        days = [d.strip() for d in settings.days_of_week.split(',') if d.strip()]
        # Convert day names to cron numbers (0=Sunday, 1=Monday, etc)
        day_map = {
            'Monday': '1', 'Tuesday': '2', 'Wednesday': '3', 'Thursday': '4',
            'Friday': '5', 'Saturday': '6', 'Sunday': '0'
        }
        days = [day_map[d] for d in days if d in day_map]
    
    # Generate schedules based on frequency
    for time in times:
        hour, minute = time.split(':')
        
        if settings.frequency == 'hourly':
            schedules.append((f'{minute} * * * *', f'Hourly at minute {minute}'))
            
        elif settings.frequency == 'daily':
            if days:
                # Specific days at specific times
                days_str = ','.join(days)
                schedules.append((f'{minute} {hour} * * {days_str}', 
                                f'Daily at {time} on specified days'))
            else:
                # Every day at specific times
                schedules.append((f'{minute} {hour} * * *', 
                                f'Daily at {time}'))
                
        elif settings.frequency == 'weekly':
            # Default to Monday if no days specified
            week_days = days if days else ['1']
            for day in week_days:
                schedules.append((f'{minute} {hour} * * {day}', 
                                f'Weekly on day {day} at {time}'))
                
        elif settings.frequency == 'monthly':
            # First day of month at specified times
            schedules.append((f'{minute} {hour} 1 * *', 
                            f'Monthly on day 1 at {time}'))
    
    return schedules

def setup_email_cron_jobs():
    """
    Set up cron jobs for email notifications.
    Removes existing jobs and creates new ones based on notification settings.
    """
    try:
        # Get notification settings
        settings = NotificationSettings.objects.first()
        if not settings:
            logger.warning("No notification settings found. Using default daily schedule.")
            settings = NotificationSettings(
                frequency='daily',
                enable_notifications=True
            )
        
        if not settings.enable_notifications:
            logger.info("Notifications are disabled in settings")
            return False
        
        # Get project directory
        project_dir = Path(__file__).resolve().parent.parent.parent
        
        # Get the Python interpreter path from the virtual environment
        venv_python = os.path.join(project_dir, 'venv', 'bin', 'python')
        if not os.path.exists(venv_python):
            # Try Windows path
            venv_python = os.path.join(project_dir, 'venv', 'Scripts', 'python.exe')
        
        if not os.path.exists(venv_python):
            logger.error("Virtual environment Python interpreter not found")
            return False

        # Create logs directory if it doesn't exist
        logs_dir = os.path.join(project_dir, 'logs')
        os.makedirs(logs_dir, exist_ok=True)
        
        # Check if we're on Windows
        if platform.system() == 'Windows':
            logger.info("Running on Windows - cron jobs will be handled by Windows Service")
            logger.info("Make sure the RadarNotificationService is installed and running")
            return True
        
        # Unix/Linux cron setup
        try:
            # Initialize crontab
            cron = CronTab(user=True)
            
            # Remove existing radar email jobs
            cron.remove_all(comment='radar_email_job')
            
            # Create the base command
            base_cmd = f'cd {project_dir} && {venv_python} manage.py send_json_reports >> {logs_dir}/email_reports.log 2>&1'
            
            # Get schedules based on notification settings
            schedules = get_cron_schedule(settings)
            
            # Add jobs for each schedule
            for schedule, description in schedules:
                job = cron.new(command=base_cmd, comment=f'radar_email_job - {description}')
                job.setall(schedule)
                logger.info(f"Created cron job: {description} ({schedule})")
            
            # Write the crontab
            cron.write()
            
            # Make log file writable
            log_file = os.path.join(logs_dir, 'email_reports.log')
            if not os.path.exists(log_file):
                with open(log_file, 'a'):
                    pass
            os.chmod(log_file, 0o666)
            
            logger.info(f"Email cron jobs set up successfully with {len(schedules)} schedule(s)")
            return True
            
        except Exception as e:
            logger.error(f"Failed to set up Unix cron jobs: {str(e)}")
            logger.info("Falling back to Windows Service approach")
            return True
        
    except Exception as e:
        logger.error(f"Failed to set up cron jobs: {str(e)}")
        return False 

def check_cron_status():
    """Thread function to check and report cron job status every minute"""
    while True:
        try:
            if platform.system() == 'Windows':
                print("\n=== Windows Service Status ===", flush=True)
                print("Email notifications are handled by RadarNotificationService", flush=True)
                print("Service runs every minute and calls check_notification_schedule", flush=True)
                print("Check notification_service.log for service status", flush=True)
                print("===========================\n", flush=True)
            else:
                cron = CronTab(user=True)
                email_jobs = [job for job in cron if 'radar_email_job' in str(job.comment)]
                
                print("\n=== Email Cron Jobs Status ===", flush=True)
                if not email_jobs:
                    print("No email cron jobs found", flush=True)
                else:
                    now = datetime.now()
                    for job in email_jobs:
                        schedule = job.slices
                        next_run = job.schedule(date_from=now).get_next()
                        print(f"Schedule: {schedule}", flush=True)
                        print(f"Next run in: {next_run} seconds", flush=True)
                print("===========================\n", flush=True)
            
        except Exception as e:
            print(f"Error checking cron status: {e}", flush=True)
        
        pytime.sleep(60)  # Wait for 1 minute

def start_status_monitor():
    """Start the status monitoring thread"""
    status_thread = threading.Thread(target=check_cron_status, daemon=True)
    status_thread.start()
    logger.info("Cron status monitoring thread started") 