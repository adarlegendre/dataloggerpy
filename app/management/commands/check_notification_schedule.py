from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta, time
from app.models import NotificationSettings, EmailNotification, RadarDataFile
from app.utils.notification_utils import send_json_files, send_daily_summary_email
from app.utils.notification_logger import notification_logger
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
        # Start logging
        notification_logger.log_cron_check_start()
        
        # Get all notification settings
        settings_list = NotificationSettings.objects.all()
        
        if not settings_list.exists():
            notification_logger.log_error("No notification settings found")
            self.stdout.write(self.style.WARNING('No notification settings found'))
            notification_logger.log_cron_check_end()
            return
        
        for settings in settings_list:
            try:
                # Log settings being checked
                notification_logger.log_settings_check(settings)
                
                if self.should_send_notification(settings):
                    # Determine date range for the summary (previous day from 00:00 to 23:59:59)
                    now = timezone.now()
                    yesterday = (now - timedelta(days=1)).date()
                    start_date = datetime.combine(yesterday, time.min)
                    end_date = datetime.combine(yesterday, time.max)
                    
                    # Make them timezone-aware
                    start_date = timezone.make_aware(start_date) if timezone.is_naive(start_date) else start_date
                    end_date = timezone.make_aware(end_date) if timezone.is_naive(end_date) else end_date
                    
                    # Log email send attempt
                    notification_logger.log_email_send_attempt(settings.primary_email, 0)
                    self.stdout.write(
                        self.style.SUCCESS(f'Sending daily summary email for {start_date.date()} to {settings.primary_email}')
                    )
                    
                    # Send the daily summary email
                    success = send_daily_summary_email(
                        start_date,
                        end_date,
                        notification_settings=settings
                    )
                    
                    if success:
                        # Create and mark notification as sent
                        notification = EmailNotification.objects.create(
                            notification_settings=settings,
                            start_date=start_date,
                            end_date=end_date,
                            status='sent',
                            sent_at=timezone.now()
                        )
                        
                        # Log success
                        notification_logger.log_email_send_success(settings.primary_email, 0, notification.id)
                        self.stdout.write(
                            self.style.SUCCESS(f'Successfully sent daily summary notification {notification.id} for {settings.primary_email}')
                        )
                    else:
                        # Log failure
                        notification_logger.log_email_send_failure(settings.primary_email, "Email send function returned False or no data available")
                        self.stdout.write(
                            self.style.WARNING(f'Failed to send daily summary or no detection data available for {settings.primary_email}')
                        )
                else:
                    # Log why notification was not sent
                    now = timezone.now()
                    current_time = now.strftime('%H:%M')
                    current_day = now.strftime('%A')
                    
                    # Check each condition and log
                    if not settings.enable_notifications:
                        notification_logger.log_error("Notifications disabled")
                    elif settings.days_of_week and current_day not in settings.days_of_week.split(','):
                        notification_logger.log_day_check(current_day, settings.days_of_week, False)
                    elif settings.notification_times and current_time not in [t.strip() for t in settings.notification_times.split(',')]:
                        notification_logger.log_time_check(current_time, settings.notification_times, False)
                    else:
                        # Check frequency
                        last_notification = EmailNotification.objects.filter(
                            notification_settings=settings,
                            status='sent'
                        ).order_by('-sent_at').first()
                        
                        if last_notification:
                            time_since_last = now - last_notification.sent_at
                            if settings.frequency == 'hourly':
                                required_interval = timedelta(hours=1)
                            elif settings.frequency == 'daily':
                                required_interval = timedelta(days=1)
                            elif settings.frequency == 'weekly':
                                required_interval = timedelta(weeks=1)
                            elif settings.frequency == 'monthly':
                                required_interval = timedelta(days=30)
                            else:
                                required_interval = timedelta(seconds=0)
                            
                            notification_logger.log_frequency_check(settings.frequency, time_since_last, required_interval, False)
                        
            except Exception as e:
                notification_logger.log_error(str(e), f"Processing notifications for {settings.primary_email}")
                self.stdout.write(
                    self.style.ERROR(f'Error processing notifications for {settings.primary_email}: {str(e)}')
                )
        
        # End logging
        notification_logger.log_cron_check_end() 