from django.core.management.base import BaseCommand
from app.utils.notification_utils import create_notification_for_today

class Command(BaseCommand):
    help = 'Creates a daily notification for radar detections'

    def handle(self, *args, **options):
        try:
            notification = create_notification_for_today()
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created notification {notification.id} for today')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to create notification: {str(e)}')
            ) 