from django.core.management.base import BaseCommand
from app.models import NotificationSettings
from app.utils.cron_manager import cron_manager

class Command(BaseCommand):
    help = 'Set up cron jobs based on notification settings'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force setup even if cron job already exists',
        )
        parser.add_argument(
            '--remove',
            action='store_true',
            help='Remove all notification cron jobs',
        )

    def handle(self, *args, **options):
        if options['remove']:
            self.stdout.write('Removing notification cron jobs...')
            success = cron_manager.remove_notification_cron()
            if success:
                self.stdout.write(
                    self.style.SUCCESS('Successfully removed notification cron jobs')
                )
            else:
                self.stdout.write(
                    self.style.ERROR('Failed to remove notification cron jobs')
                )
            return

        # Check if we have access to crontab
        if not cron_manager.test_cron_access():
            self.stdout.write(
                self.style.WARNING('No access to crontab. Make sure you have appropriate permissions.')
            )
            return

        # Get current cron status
        status = cron_manager.get_cron_status()
        
        if status['installed'] and not options['force']:
            self.stdout.write(
                self.style.WARNING('Notification cron job already installed. Use --force to reinstall.')
            )
            self.stdout.write(f"Current job: {status['cron_job']}")
            return

        # Get notification settings
        settings = NotificationSettings.objects.first()
        
        if not settings:
            self.stdout.write(
                self.style.WARNING('No notification settings found. Please configure notifications first.')
            )
            return

        if not settings.enable_notifications:
            self.stdout.write('Notifications are disabled, removing cron job...')
            success = cron_manager.remove_notification_cron()
            if success:
                self.stdout.write(
                    self.style.SUCCESS('Successfully removed notification cron job')
                )
            else:
                self.stdout.write(
                    self.style.ERROR('Failed to remove notification cron job')
                )
            return

        # Set up cron job
        self.stdout.write('Setting up notification cron job...')
        self.stdout.write(f"Settings: {settings.primary_email}")
        self.stdout.write(f"Frequency: {settings.frequency}")
        self.stdout.write(f"Days: {settings.days_of_week or 'All days'}")
        self.stdout.write(f"Times: {settings.notification_times or 'Any time'}")

        success = cron_manager.setup_notification_cron(settings)
        
        if success:
            self.stdout.write(
                self.style.SUCCESS('Successfully set up notification cron job')
            )
            
            # Show the new status
            new_status = cron_manager.get_cron_status()
            if new_status['installed']:
                self.stdout.write(f"Cron job: {new_status['cron_job']}")
                self.stdout.write(f"Log file: {new_status['log_file']}")
        else:
            self.stdout.write(
                self.style.ERROR('Failed to set up notification cron job')
            ) 