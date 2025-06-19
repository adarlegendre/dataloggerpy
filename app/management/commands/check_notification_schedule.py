from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from app.models import NotificationSettings, EmailNotification, RadarDataFile
from app.utils.notification_utils import send_json_files
import os

class Command(BaseCommand):
    help = 'Check notification schedule and send emails based on configured settings'

    def should_send_notification(self, settings):
        """Check if notification should be sent based on frequency and schedule"""
        now = timezone.now()
        current_time = now.strftime('%H:%M')
        current_day = now.strftime('%A')

        # Check if notifications are enabled
        if not settings.enable_notifications:
            return False

        # Check if current day is in scheduled days (if specified)
        if settings.days_of_week and current_day not in settings.days_of_week.split(','):
            return False

        # Check if current time matches any scheduled time (if specified)
        if settings.notification_times:
            scheduled_times = [t.strip() for t in settings.notification_times.split(',')]
            if current_time not in scheduled_times:
                return False

        # Check frequency-based conditions
        last_notification = EmailNotification.objects.filter(
            notification_settings=settings,
            status='sent'
        ).order_by('-sent_at').first()

        if not last_notification:
            return True

        last_sent = last_notification.sent_at
        time_since_last = now - last_sent

        if settings.frequency == 'hourly':
            return time_since_last >= timedelta(hours=1)
        elif settings.frequency == 'daily':
            return time_since_last >= timedelta(days=1)
        elif settings.frequency == 'weekly':
            return time_since_last >= timedelta(weeks=1)
        elif settings.frequency == 'monthly':
            # Approximate month as 30 days
            return time_since_last >= timedelta(days=30)

        return False

    def get_json_files_since_last_notification(self, settings):
        """Get unsent JSON files created since last notification"""
        last_notification = EmailNotification.objects.filter(
            notification_settings=settings,
            status='sent'
        ).order_by('-sent_at').first()

        # Get unsent files from the database
        unsent_files = RadarDataFile.objects.filter(
            email_sent=False,
            is_valid=True
        ).order_by('timestamp')

        # If there was a previous notification, only get files created after it
        if last_notification:
            unsent_files = unsent_files.filter(timestamp__gt=last_notification.sent_at)

        # Return the file paths
        return [file.file_path for file in unsent_files]

    def handle(self, *args, **options):
        self.stdout.write('Checking notification schedule...')
        
        # Get all notification settings
        settings_list = NotificationSettings.objects.all()
        
        for settings in settings_list:
            try:
                if self.should_send_notification(settings):
                    # Get JSON files to send
                    json_files = self.get_json_files_since_last_notification(settings)
                    
                    if json_files:
                        # Send the email
                        success = send_json_files(
                            json_files,
                            subject=f"Radar Data Files - {timezone.now().strftime('%Y-%m-%d %H:%M')}",
                            body=f"Please find attached the radar data files collected since the last notification.",
                            notification_settings=settings
                        )
                        
                        if success:
                            # Create and mark notification as sent
                            notification = EmailNotification.objects.create(
                                notification_settings=settings,
                                start_date=timezone.now() - timedelta(days=1),
                                end_date=timezone.now(),
                                status='sent',
                                sent_at=timezone.now()
                            )
                            self.stdout.write(
                                self.style.SUCCESS(f'Successfully sent notification {notification.id} for {settings.primary_email}')
                            )
                        else:
                            self.stdout.write(
                                self.style.ERROR(f'Failed to send notification for {settings.primary_email}')
                            )
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'No new JSON files to send for {settings.primary_email}')
                        )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error processing notifications for {settings.primary_email}: {str(e)}')
                ) 