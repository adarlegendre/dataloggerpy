from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta, time
from app.models import NotificationSettings
from app.utils.notification_utils import send_daily_summary_email, generate_daily_summary_report
import json


class Command(BaseCommand):
    help = 'Test the daily summary email functionality'

    def add_arguments(self, parser):
        parser.add_argument(
            '--date',
            type=str,
            help='Date to generate summary for (YYYY-MM-DD). Defaults to yesterday.',
        )
        parser.add_argument(
            '--preview',
            action='store_true',
            help='Preview the JSON data without sending email',
        )

    def handle(self, *args, **options):
        self.stdout.write('Testing Daily Summary Email Functionality')
        self.stdout.write('=' * 60)
        
        # Get notification settings
        settings = NotificationSettings.objects.first()
        if not settings:
            self.stdout.write(
                self.style.ERROR('No notification settings found. Please configure notification settings first.')
            )
            return
        
        self.stdout.write(
            self.style.SUCCESS(f'✓ Found notification settings for: {settings.primary_email}')
        )
        
        # Determine date range
        if options['date']:
            try:
                target_date = datetime.strptime(options['date'], '%Y-%m-%d').date()
            except ValueError:
                self.stdout.write(
                    self.style.ERROR('Invalid date format. Use YYYY-MM-DD')
                )
                return
        else:
            # Default to yesterday
            target_date = (timezone.now() - timedelta(days=1)).date()
        
        start_date = datetime.combine(target_date, time.min)
        end_date = datetime.combine(target_date, time.max)
        
        # Make them timezone-aware
        start_date = timezone.make_aware(start_date) if timezone.is_naive(start_date) else start_date
        end_date = timezone.make_aware(end_date) if timezone.is_naive(end_date) else end_date
        
        self.stdout.write(
            self.style.SUCCESS(f'✓ Date range: {start_date.date()} (00:00 to 23:59:59)')
        )
        
        # Generate summary report
        self.stdout.write('\nGenerating summary report...')
        summary_data = generate_daily_summary_report(start_date, end_date)
        
        if not summary_data:
            self.stdout.write(
                self.style.WARNING('⚠ No detection data found for the specified period')
            )
            return
        
        self.stdout.write(
            self.style.SUCCESS(f'✓ Found data for {len(summary_data)} radar(s)')
        )
        
        # Display summary statistics
        total_detections = sum(radar['detections'] for radar in summary_data)
        total_anpr = sum(radar['detections_ANPR'] for radar in summary_data)
        
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write('SUMMARY STATISTICS')
        self.stdout.write('=' * 60)
        self.stdout.write(f'Total Radars:          {len(summary_data)}')
        self.stdout.write(f'Total Detections:      {total_detections}')
        self.stdout.write(f'Total ANPR Detections: {total_anpr}')
        
        # Display per-radar breakdown
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write('PER-RADAR BREAKDOWN')
        self.stdout.write('=' * 60)
        
        for radar in summary_data:
            self.stdout.write(f"\nRadar: {radar['name']}")
            self.stdout.write(f"  IMR_AD: {radar['IMR_AD']}")
            self.stdout.write(f"  Route: {radar['route']}")
            self.stdout.write(f"  Location: ({radar['lat']}, {radar['lon']})")
            self.stdout.write(f"  Detections: {radar['detections']}")
            self.stdout.write(f"  ANPR Detections: {radar['detections_ANPR']}")
            
            if radar['directions']:
                self.stdout.write(f"  Directions:")
                for direction in radar['directions']:
                    self.stdout.write(f"    - {direction['name']} ({direction['id']})")
                    self.stdout.write(f"      Detections: {direction['detections']}")
                    self.stdout.write(f"      ANPR: {direction['detections_ANPR']}")
        
        # Preview JSON
        if options['preview']:
            self.stdout.write('\n' + '=' * 60)
            self.stdout.write('JSON PREVIEW')
            self.stdout.write('=' * 60)
            json_data = json.dumps(summary_data, indent=2)
            self.stdout.write(json_data)
            return
        
        # Send email
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write('SENDING EMAIL')
        self.stdout.write('=' * 60)
        self.stdout.write(f'To: {settings.primary_email}')
        
        cc_emails = settings.get_cc_emails_list()
        if cc_emails:
            self.stdout.write(f'CC: {", ".join(cc_emails)}')
        
        self.stdout.write('\nSending email...')
        
        success = send_daily_summary_email(
            start_date,
            end_date,
            notification_settings=settings
        )
        
        if success:
            self.stdout.write(
                self.style.SUCCESS('\n✓ Email sent successfully!')
            )
        else:
            self.stdout.write(
                self.style.ERROR('\n✗ Failed to send email')
            )

