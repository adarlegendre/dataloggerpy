#!/bin/bash
# Comprehensive diagnostic script for email notification issues

cd /home/admin/dataloggerpy
source venv/bin/activate

echo "========================================="
echo "  Email Notification Diagnostic Report"
echo "========================================="
echo ""

# 1. Check Python and Django
echo "1. ENVIRONMENT CHECK"
echo "---"
which python
python --version
echo ""

# 2. Check notification settings
echo "2. NOTIFICATION SETTINGS"
echo "---"
python manage.py shell << 'EOF'
from app.models import NotificationSettings
from django.utils import timezone

settings = NotificationSettings.objects.first()
if settings:
    print(f"Primary Email: {settings.primary_email}")
    print(f"Frequency: {settings.frequency}")
    print(f"Days of Week: {settings.days_of_week or 'All days'}")
    print(f"Notification Times: {settings.notification_times or 'Any time'}")
    print(f"Enabled: {settings.enable_notifications}")
    print(f"SMTP Server: {settings.smtp_server}:{settings.smtp_port}")
    print(f"SMTP User: {settings.smtp_username}")
    print(f"SMTP TLS: {settings.smtp_use_tls}")
    
    # Current time info
    now = timezone.now()
    print(f"\nCurrent server time: {now.strftime('%Y-%m-%d %H:%M:%S %A')}")
    print(f"Current day: {now.strftime('%A')}")
    print(f"Current time: {now.strftime('%H:%M')}")
    
    # Check if current time matches schedule
    current_time = now.strftime('%H:%M')
    current_day = now.strftime('%A')
    
    print("\n--- SCHEDULE CHECK ---")
    if settings.days_of_week:
        days_match = current_day in settings.days_of_week.split(',')
        print(f"Day matches: {days_match} (Current: {current_day}, Allowed: {settings.days_of_week})")
    else:
        print("Day matches: True (All days allowed)")
    
    if settings.notification_times:
        times = [t.strip() for t in settings.notification_times.split(',')]
        time_match = current_time in times
        print(f"Time matches: {time_match} (Current: {current_time}, Scheduled: {', '.join(times)})")
    else:
        print("Time matches: True (All times allowed)")
        
else:
    print("ERROR: No notification settings found!")
    print("Please configure notification settings in Django admin or web interface.")
EOF

echo ""

# 3. Check last notifications sent
echo "3. LAST NOTIFICATIONS SENT"
echo "---"
python manage.py shell << 'EOF'
from app.models import EmailNotification
from django.utils import timezone

recent = EmailNotification.objects.filter(status='sent').order_by('-sent_at')[:5]
if recent:
    print(f"Found {recent.count()} recent notifications:")
    for notif in recent:
        print(f"  - ID {notif.id}: {notif.sent_at} ({notif.start_date.date()})")
else:
    print("No notifications have been sent yet.")
EOF

echo ""

# 4. Check for detections data
echo "4. DETECTION DATA AVAILABILITY"
echo "---"
python manage.py shell << 'EOF'
from app.models import Detection
from django.utils import timezone
from datetime import timedelta

now = timezone.now()
yesterday = now - timedelta(days=1)

total = Detection.objects.count()
yesterday_count = Detection.objects.filter(start_time__gte=yesterday.replace(hour=0, minute=0, second=0), start_time__lte=yesterday.replace(hour=23, minute=59, second=59)).count()

print(f"Total detections in database: {total}")
print(f"Detections from yesterday: {yesterday_count}")

if yesterday_count == 0:
    print("\nWARNING: No detections from yesterday!")
    print("This might be why no email is being sent.")
EOF

echo ""

# 5. Check crontab
echo "5. CRONTAB STATUS"
echo "---"
crontab -l | grep -v "^#" | grep -v "^$" | head -5
echo ""
echo "Total cron entries: $(crontab -l | grep -v '^#' | grep -v '^$' | wc -l)"
echo ""

# 6. Check cron service
echo "6. CRON SERVICE STATUS"
echo "---"
sudo systemctl is-active cron && echo "✓ Cron service is running" || echo "✗ Cron service is NOT running!"
echo ""

# 7. Check log file
echo "7. RECENT LOG ACTIVITY"
echo "---"
if [ -f logs/notification_service.log ]; then
    echo "Last 15 lines of notification log:"
    tail -15 logs/notification_service.log
else
    echo "✗ Log file not found: logs/notification_service.log"
    echo "This means the cron job has never run!"
fi

echo ""

# 8. Test command manually
echo "8. MANUAL COMMAND TEST"
echo "---"
echo "Running: python manage.py check_notification_schedule"
python manage.py check_notification_schedule
echo ""

echo "========================================="
echo "  Diagnostic Complete"
echo "========================================="
echo ""
echo "NEXT STEPS:"
echo "  1. Review the settings above"
echo "  2. Ensure current time matches your scheduled times"
echo "  3. Check that detections exist in the database"
echo "  4. Run: ./fix_crontab.sh (if cron entries look wrong)"
echo "  5. Monitor: tail -f logs/notification_service.log"
echo ""

