from django.core.management.base import BaseCommand
from app.utils.notification_utils import process_pending_notifications

class Command(BaseCommand):
    help = 'Process pending email notifications for radar detections'

    def handle(self, *args, **options):
        self.stdout.write('Processing pending notifications...')
        process_pending_notifications()
        self.stdout.write(self.style.SUCCESS('Successfully processed notifications')) 