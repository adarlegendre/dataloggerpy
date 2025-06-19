from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import NotificationSettings
from app.utils.notification_utils import send_json_files
import os
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Send JSON files based on notification settings'

    def handle(self, *args, **options):
        try:
            # Get notification settings
            settings = NotificationSettings.objects.first()
            if not settings or not settings.enable_notifications:
                self.stdout.write('Notifications are not configured or disabled')
                return

            # Get current time
            now = timezone.now()
            
            # Get JSON files from the last period based on frequency
            data_dir = 'data'  # Your JSON files directory
            if not os.path.exists(data_dir):
                self.stdout.write(f'Data directory {data_dir} does not exist')
                return

            # Calculate the time window based on frequency
            if settings.frequency == 'hourly':
                time_window = timedelta(hours=1)
            elif settings.frequency == 'daily':
                time_window = timedelta(days=1)
            elif settings.frequency == 'weekly':
                time_window = timedelta(weeks=1)
            else:  # monthly
                time_window = timedelta(days=30)

            # Get files modified within the time window
            cutoff_time = now - time_window
            json_files = []
            
            for filename in os.listdir(data_dir):
                if filename.endswith('.json'):
                    file_path = os.path.join(data_dir, filename)
                    file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                    if file_mtime > cutoff_time:
                        json_files.append(file_path)

            if not json_files:
                self.stdout.write('No new JSON files to send')
                return

            # Check if we should send based on days of week
            if settings.days_of_week:
                allowed_days = [day.strip() for day in settings.days_of_week.split(',')]
                current_day = now.strftime('%A')
                if current_day not in allowed_days:
                    self.stdout.write(f'Not configured to send on {current_day}')
                    return

            # Check if we should send based on notification times
            if settings.notification_times:
                allowed_times = [time.strip() for time in settings.notification_times.split(',')]
                current_time = now.strftime('%H:%M')
                if not any(current_time.startswith(allowed_time) for allowed_time in allowed_times):
                    self.stdout.write(f'Not configured to send at {current_time}')
                    return

            # Send the files
            success = send_json_files(
                json_files,
                subject=f"Radar JSON Data - {now.strftime('%Y-%m-%d %H:%M')}",
                body=f"Please find attached the radar JSON data files from the last {settings.frequency} period."
            )

            if success:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully sent {len(json_files)} JSON files')
                )
            else:
                self.stdout.write(
                    self.style.ERROR('Failed to send JSON files')
                )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error sending JSON files: {str(e)}')
            ) 