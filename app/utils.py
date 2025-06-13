import os
import psutil
import subprocess
from datetime import datetime, timedelta
from .models import SystemMetrics
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

def round_to_nearest_30_minutes(td):
    """Round a timedelta to the nearest 30 minutes."""
    total_seconds = int(td.total_seconds())
    minutes = total_seconds // 60
    rounded_minutes = round(minutes / 30) * 30
    return timedelta(minutes=rounded_minutes)

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

        # Get CPU temperature for Raspberry Pi
        try:
            temp = subprocess.check_output(['vcgencmd', 'measure_temp']).decode()
            cpu_temp = float(temp.replace('temp=', '').replace("'C", ''))
        except Exception as e:
            logger.warning(f"Could not get CPU temperature: {str(e)}")
            cpu_temp = None

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