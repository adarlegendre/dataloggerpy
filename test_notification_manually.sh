#!/bin/bash
# Script to manually test the notification system

cd /home/admin/dataloggerpy
source venv/bin/activate

echo "========================================="
echo "  Testing Notification System"
echo "========================================="
echo ""

echo "1. Checking notification settings..."
python manage.py shell << EOF
from app.models import NotificationSettings
settings = NotificationSettings.objects.first()
if settings:
    print(f"✓ Email: {settings.primary_email}")
    print(f"✓ Frequency: {settings.frequency}")
    print(f"✓ Days: {settings.days_of_week or 'All days'}")
    print(f"✓ Times: {settings.notification_times or 'Any time'}")
    print(f"✓ Enabled: {settings.enable_notifications}")
else:
    print("✗ No notification settings found!")
EOF

echo ""
echo "2. Running notification check command..."
python manage.py check_notification_schedule

echo ""
echo "3. Checking recent log entries..."
if [ -f logs/notification_service.log ]; then
    echo "Last 20 lines of notification log:"
    tail -20 logs/notification_service.log
else
    echo "✗ Log file not found at logs/notification_service.log"
fi

echo ""
echo "========================================="
echo "  Test Complete"
echo "========================================="

