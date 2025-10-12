#!/bin/bash
# Email Notification Troubleshooting Script
# Run this to diagnose why emails aren't sending

cd /home/admin/dataloggerpy
source loggervenv/bin/activate

echo "========================================"
echo "  Email Notification Diagnostic"
echo "========================================"
echo ""

# 1. Check current time
echo "1. CURRENT TIME CHECK"
echo "---"
echo "Server time: $(date '+%Y-%m-%d %H:%M:%S %A')"
echo "Current hour:minute: $(date '+%H:%M')"
echo ""

# 2. Check notification settings
echo "2. NOTIFICATION SETTINGS"
echo "---"
python manage.py shell << 'EOF'
from app.models import NotificationSettings
from django.utils import timezone

try:
    settings = NotificationSettings.objects.first()
    if settings:
        print(f"✓ Settings found")
        print(f"  Enabled: {settings.enable_notifications}")
        print(f"  Email: {settings.primary_email}")
        print(f"  Frequency: {settings.frequency}")
        print(f"  Times: {settings.notification_times}")
        print(f"  Days: {settings.days_of_week}")
        print(f"  SMTP Server: {settings.smtp_server}:{settings.smtp_port}")
        print(f"  SMTP User: {settings.smtp_username}")
        print(f"  SMTP TLS: {settings.smtp_use_tls}")
        
        if not settings.enable_notifications:
            print("\n⚠ WARNING: Notifications are DISABLED!")
            print("  Enable them in Django admin")
        
        if not settings.primary_email:
            print("\n⚠ WARNING: No primary email configured!")
        
        if not settings.smtp_server or not settings.smtp_username:
            print("\n⚠ WARNING: SMTP settings incomplete!")
            print("  Configure SMTP in Django admin")
            
    else:
        print("✗ No notification settings found!")
        print("  Create settings in Django admin first")
except Exception as e:
    print(f"✗ Error checking settings: {e}")
EOF

echo ""

# 3. Check last notification sent
echo "3. LAST NOTIFICATIONS SENT"
echo "---"
python manage.py shell << 'EOF'
from app.models import EmailNotification
from django.utils import timezone
from datetime import timedelta

try:
    recent = EmailNotification.objects.filter(status='sent').order_by('-sent_at')[:5]
    if recent:
        print(f"Found {recent.count()} recent notifications:")
        for notif in recent:
            print(f"  - {notif.sent_at.strftime('%Y-%m-%d %H:%M:%S')} → {notif.recipient}")
    else:
        print("⚠ No notifications have been sent yet")
        
    # Check pending/failed
    pending = EmailNotification.objects.filter(status='pending').count()
    failed = EmailNotification.objects.filter(status='failed').count()
    
    if pending > 0:
        print(f"\n{pending} pending notifications")
    if failed > 0:
        print(f"{failed} failed notifications")
        last_failed = EmailNotification.objects.filter(status='failed').order_by('-created_at').first()
        if last_failed:
            print(f"  Last failure: {last_failed.error_message}")
            
except Exception as e:
    print(f"✗ Error checking notifications: {e}")
EOF

echo ""

# 4. Check detection data availability
echo "4. DETECTION DATA AVAILABILITY"
echo "---"
python manage.py shell << 'EOF'
from app.models import Detection, RadarObjectDetection
from django.utils import timezone
from datetime import timedelta

try:
    # Check Detection model
    total_detections = Detection.objects.count()
    print(f"Total detections (Detection model): {total_detections}")
    
    if total_detections > 0:
        latest = Detection.objects.order_by('-start_time').first()
        print(f"  Latest: {latest.start_time}")
    
    # Check RadarObjectDetection model
    total_radar = RadarObjectDetection.objects.count()
    print(f"Total detections (RadarObjectDetection): {total_radar}")
    
    if total_radar > 0:
        latest_radar = RadarObjectDetection.objects.order_by('-start_time').first()
        print(f"  Latest: {latest_radar.start_time}")
    
    # Check today's data
    today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_detections = Detection.objects.filter(start_time__gte=today_start).count()
    today_radar = RadarObjectDetection.objects.filter(start_time__gte=today_start).count()
    
    print(f"\nToday's detections:")
    print(f"  Detection: {today_detections}")
    print(f"  RadarObjectDetection: {today_radar}")
    
    if today_detections == 0 and today_radar == 0:
        print("\n⚠ WARNING: No detections today!")
        print("  Emails may not send if there's no data to report")
        
except Exception as e:
    print(f"✗ Error checking detections: {e}")
EOF

echo ""

# 5. Check cron job log
echo "5. CRON JOB LOG (Last 20 lines)"
echo "---"
if [ -f "logs/notification_service.log" ]; then
    tail -20 logs/notification_service.log
else
    echo "✗ Log file not found: logs/notification_service.log"
    echo "  This means the cron job hasn't run yet!"
fi

echo ""

# 6. Check cron service
echo "6. CRON SERVICE STATUS"
echo "---"
if systemctl is-active --quiet cron 2>/dev/null; then
    echo "✓ Cron service is running"
elif systemctl is-active --quiet crond 2>/dev/null; then
    echo "✓ Cron service (crond) is running"
else
    echo "✗ Cron service is NOT running!"
    echo "  Start it: sudo systemctl start cron"
fi

echo ""

# 7. Test the command manually
echo "7. MANUAL TEST (Running check_notification_schedule now)"
echo "---"
python manage.py check_notification_schedule
echo ""

# 8. Test SMTP connection
echo "8. SMTP CONNECTION TEST"
echo "---"
python manage.py shell << 'EOF'
from app.models import NotificationSettings
import smtplib
from email.mime.text import MIMEText

try:
    settings = NotificationSettings.objects.first()
    if settings and settings.smtp_server:
        print(f"Testing connection to {settings.smtp_server}:{settings.smtp_port}...")
        
        try:
            if settings.smtp_use_tls:
                server = smtplib.SMTP(settings.smtp_server, settings.smtp_port, timeout=10)
                server.starttls()
            else:
                server = smtplib.SMTP(settings.smtp_server, settings.smtp_port, timeout=10)
            
            if settings.smtp_username and settings.smtp_password:
                server.login(settings.smtp_username, settings.smtp_password)
                print("✓ SMTP authentication successful!")
            else:
                print("⚠ No SMTP credentials configured")
            
            server.quit()
            print("✓ SMTP connection successful!")
            
        except smtplib.SMTPAuthenticationError:
            print("✗ SMTP authentication failed!")
            print("  Check your username and password")
        except smtplib.SMTPException as e:
            print(f"✗ SMTP error: {e}")
        except Exception as e:
            print(f"✗ Connection error: {e}")
    else:
        print("⚠ No SMTP settings configured")
except Exception as e:
    print(f"✗ Error testing SMTP: {e}")
EOF

echo ""
echo "========================================"
echo "  Diagnostic Complete"
echo "========================================"
echo ""
echo "NEXT STEPS:"
echo "1. Review the output above for any ✗ or ⚠ warnings"
echo "2. Check that notifications are enabled"
echo "3. Verify SMTP settings are correct"
echo "4. Monitor: tail -f logs/notification_service.log"
echo "5. Force send test: python manage.py test_summary_email"
echo ""

deactivate

