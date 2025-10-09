from django.core.management.base import BaseCommand
from app.utils.cron_manager import cron_manager
import platform


class Command(BaseCommand):
    help = 'Clean up ALL radar notification cron jobs and optionally reinstall'

    def add_arguments(self, parser):
        parser.add_argument(
            '--reinstall',
            action='store_true',
            help='Reinstall cron job after cleanup',
        )

    def handle(self, *args, **options):
        self.stdout.write('=' * 60)
        self.stdout.write('Radar Notification Cron Job Cleanup')
        self.stdout.write('=' * 60)
        self.stdout.write('')

        if platform.system() == 'Windows':
            self.stdout.write(
                self.style.WARNING('This command is for Linux/Unix systems only.')
            )
            self.stdout.write('On Windows, use Windows Task Scheduler or the notification service.')
            return

        # Show current cron jobs
        current_crontab = cron_manager.get_current_crontab()
        radar_lines = [line for line in current_crontab.split('\n') 
                      if any(keyword in line for keyword in [
                          'send_json_reports',
                          'check_notification_schedule',
                          'radar_email_job',
                          'email_reports.log',
                          'notification_service.log'
                      ])]
        
        if radar_lines:
            self.stdout.write(self.style.WARNING(f'Found {len(radar_lines)} radar notification cron entries:'))
            for line in radar_lines[:5]:  # Show first 5
                self.stdout.write(f'  {line.strip()}')
            if len(radar_lines) > 5:
                self.stdout.write(f'  ... and {len(radar_lines) - 5} more')
            self.stdout.write('')
        else:
            self.stdout.write(self.style.SUCCESS('No radar notification cron jobs found'))
            return

        # Clean up
        self.stdout.write('Removing all radar notification cron jobs...')
        success = cron_manager.remove_notification_cron()

        if success:
            self.stdout.write(
                self.style.SUCCESS(f'✓ Successfully removed {len(radar_lines)} cron job(s)')
            )
        else:
            self.stdout.write(
                self.style.ERROR('✗ Failed to remove cron jobs')
            )
            return

        # Reinstall if requested
        if options['reinstall']:
            self.stdout.write('')
            self.stdout.write('Reinstalling cron job from notification settings...')
            
            from app.models import NotificationSettings
            settings = NotificationSettings.objects.first()
            
            if not settings:
                self.stdout.write(
                    self.style.WARNING('No notification settings found. Cannot reinstall.')
                )
                return
            
            if not settings.enable_notifications:
                self.stdout.write(
                    self.style.WARNING('Notifications are disabled in settings.')
                )
                return
            
            success = cron_manager.setup_notification_cron(settings)
            
            if success:
                self.stdout.write(
                    self.style.SUCCESS('✓ Successfully reinstalled cron job')
                )
                status = cron_manager.get_cron_status()
                if status['installed']:
                    self.stdout.write(f"Cron job: {status['cron_job']}")
                    self.stdout.write(f"Log file: {status['log_file']}")
            else:
                self.stdout.write(
                    self.style.ERROR('✗ Failed to reinstall cron job')
                )

        self.stdout.write('')
        self.stdout.write('=' * 60)
        self.stdout.write('Cleanup Complete')
        self.stdout.write('=' * 60)

