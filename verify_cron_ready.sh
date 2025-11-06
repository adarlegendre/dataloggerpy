#!/bin/bash
# Verify cron jobs are ready to work

cd /home/admin/dataloggerpy
source loggervenv/bin/activate

echo "========================================"
echo "  Cron Job Readiness Check"
echo "========================================"
echo ""

# 1. Check crontab
echo "1. CRONTAB CHECK"
echo "---"
CRON_ENTRY=$(crontab -l 2>/dev/null | grep "check_notification_schedule")
if [ -n "$CRON_ENTRY" ]; then
    echo "✓ Cron job found in crontab:"
    echo "  $CRON_ENTRY"
else
    echo "✗ No cron job found!"
    echo "  Run: python manage.py setup_cron_jobs --force"
    exit 1
fi
echo ""

# 2. Check cron service
echo "2. CRON SERVICE"
echo "---"
if systemctl is-active --quiet cron 2>/dev/null; then
    echo "✓ Cron service is running"
elif systemctl is-active --quiet crond 2>/dev/null; then
    echo "✓ Cron service (crond) is running"
else
    echo "✗ Cron service is NOT running"
    echo "  Start it: sudo systemctl start cron"
    exit 1
fi
echo ""

# 3. Check notification settings
echo "3. NOTIFICATION SETTINGS"
echo "---"
python manage.py shell << 'EOF'
from app.models import NotificationSettings

settings = NotificationSettings.objects.first()
if settings:
    if settings.enable_notifications:
        print(f"✓ Notifications enabled")
        print(f"  To: {settings.primary_email}")
        print(f"  CC: {settings.cc_emails or 'None'}")
        print(f"  Times: {settings.notification_times}")
        print(f"  Days: {settings.days_of_week or 'All days'}")
        print(f"  Frequency: {settings.frequency}")
    else:
        print("✗ Notifications are DISABLED")
        print("  Enable in Django admin")
        exit(1)
else:
    print("✗ No notification settings found")
    exit(1)
EOF

if [ $? -ne 0 ]; then
    echo ""
    echo "Fix notification settings first!"
    exit 1
fi
echo ""

# 4. Test the cron command manually
echo "4. TEST CRON COMMAND"
echo "---"
echo "Running: python manage.py check_notification_schedule"
python manage.py check_notification_schedule
COMMAND_RESULT=$?
echo ""
if [ $COMMAND_RESULT -eq 0 ]; then
    echo "✓ Command runs successfully"
else
    echo "✗ Command failed with exit code: $COMMAND_RESULT"
    exit 1
fi
echo ""

# 5. Check log file
echo "5. LOG FILE"
echo "---"
if [ -f "logs/notification_service.log" ]; then
    echo "✓ Log file exists: logs/notification_service.log"
    LOG_SIZE=$(stat -c%s "logs/notification_service.log" 2>/dev/null || stat -f%z "logs/notification_service.log" 2>/dev/null)
    echo "  Size: $LOG_SIZE bytes"
    if [ $LOG_SIZE -gt 0 ]; then
        echo ""
        echo "  Last 3 lines:"
        tail -3 logs/notification_service.log | sed 's/^/  | /'
    fi
else
    echo "⚠ Log file doesn't exist yet"
    echo "  Will be created when cron runs"
fi
echo ""

# 6. Show when emails will be sent
echo "6. EMAIL SCHEDULE"
echo "---"
python manage.py shell << 'EOF'
from app.models import NotificationSettings
from django.utils import timezone

settings = NotificationSettings.objects.first()
if settings and settings.enable_notifications:
    times = [t.strip() for t in settings.notification_times.split(',')]
    days = settings.days_of_week.split(',') if settings.days_of_week else ['All days']
    
    print(f"Emails will be sent:")
    print(f"  Frequency: {settings.frequency}")
    print(f"  Times: {', '.join(times)}")
    print(f"  Days: {', '.join(days)}")
    print("")
    
    # Show current time
    now = timezone.now()
    current_time = now.strftime('%H:%M')
    current_day = now.strftime('%A')
    
    print(f"Current server time: {now.strftime('%Y-%m-%d %H:%M:%S %A')}")
    print(f"  Time: {current_time}")
    print(f"  Day: {current_day}")
    print("")
    
    # Check if current time matches
    time_matches = current_time in times
    day_matches = not settings.days_of_week or current_day in days
    
    if time_matches and day_matches:
        print("🎯 RIGHT NOW is a scheduled time! Email should send on next cron run (within 1 minute)")
    else:
        # Find next scheduled time
        from datetime import datetime, timedelta
        
        next_times = []
        for scheduled_time in times:
            hour, minute = map(int, scheduled_time.split(':'))
            next_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            
            # If time has passed today, schedule for tomorrow
            if next_time <= now:
                next_time += timedelta(days=1)
            
            next_times.append(next_time)
        
        # Get earliest next time
        next_send = min(next_times)
        time_until = next_send - now
        
        hours = int(time_until.total_seconds() // 3600)
        minutes = int((time_until.total_seconds() % 3600) // 60)
        
        print(f"⏰ Next email will send at: {next_send.strftime('%Y-%m-%d %H:%M')} ({next_send.strftime('%A')})")
        print(f"   Time until next email: {hours}h {minutes}m")
EOF
echo ""

# 7. Final summary
echo "========================================"
echo "  READINESS SUMMARY"
echo "========================================"
echo ""
echo "✓ Cron job is installed in crontab"
echo "✓ Cron service is running"
echo "✓ Notification settings are configured"
echo "✓ Check command runs successfully"
echo "✓ Test email works (you confirmed)"
echo ""
echo "🎉 Everything is ready!"
echo ""
echo "WHAT HAPPENS NEXT:"
echo "1. Cron runs every minute (* * * * *)"
echo "2. Executes: python manage.py check_notification_schedule"
echo "3. Checks if current time matches your schedule"
echo "4. If match: sends email with detection data"
echo "5. If no match: does nothing (waits for next minute)"
echo ""
echo "MONITORING:"
echo "  Watch logs: tail -f logs/notification_service.log"
echo "  Check cron: crontab -l"
echo "  Force send: python manage.py test_summary_email --date \$(date +%Y-%m-%d)"
echo ""

deactivate

