# Automatic Cron Job Setup

## Overview

The system now **automatically** cleans and sets up cron jobs every time you start the Django server. No manual setup required!

## How It Works

When you run `python manage.py runserver` (or deploy with gunicorn/uwsgi), the system:

1. ✅ **Removes ALL old cron jobs** - Cleans up any duplicates or outdated entries
2. ✅ **Creates ONE fresh cron job** - Based on your current notification settings
3. ✅ **Uses correct paths** - Automatically detects Linux vs Windows and uses proper paths
4. ✅ **Logs everything** - Shows what it's doing in the server logs

## What Gets Cleaned Up

The system removes:
- All duplicate `send_json_reports` entries
- All duplicate `check_notification_schedule` entries  
- Any cron jobs with `radar_email_job` comment
- Any cron jobs logging to `email_reports.log` or `notification_service.log`

## What Gets Created

**ONE** cron job that:
- Runs every minute: `* * * * *`
- Checks if it's time to send emails based on your settings
- Uses the correct command: `python manage.py check_notification_schedule`
- Logs to: `logs/notification_service.log`

## Server Startup

When you start the server, you'll see:

```
============================================================
Radar Data Logger - Server Startup
============================================================
✓ Radar data service started
Setting up email notification cron jobs...
Setting up notification cron job for your@email.com
Schedule: daily, Days: Monday,Sunday, Times: 08:00
✓ Email cron jobs configured
Cron job: * * * * * cd /home/admin/dataloggerpy && source venv/bin/activate && python manage.py check_notification_schedule >> /home/admin/dataloggerpy/logs/notification_service.log 2>&1
Log file: /home/admin/dataloggerpy/logs/notification_service.log
✓ Cron status monitor started
============================================================
```

## Manual Commands

### Clean up cron jobs manually:
```bash
python manage.py cleanup_cron
```

### Clean up and reinstall:
```bash
python manage.py cleanup_cron --reinstall
```

### Setup cron jobs manually:
```bash
python manage.py setup_cron_jobs --force
```

### Remove all cron jobs:
```bash
python manage.py setup_cron_jobs --remove
```

## Verify It's Working

### 1. Check the crontab:
```bash
crontab -l
```

You should see **ONE** entry like:
```bash
# Radar Notification Service
# Configured on 2025-10-09 10:30:00
# Settings: your@email.com - daily
# Days: Monday,Sunday
# Times: 08:00
* * * * * cd /home/admin/dataloggerpy && source venv/bin/activate && python manage.py check_notification_schedule >> /home/admin/dataloggerpy/logs/notification_service.log 2>&1
```

### 2. Monitor the log file:
```bash
tail -f logs/notification_service.log
```

Every minute you should see entries checking the schedule.

### 3. Check notification settings:
Make sure in your Django admin or web interface:
- ✅ Email notifications are **enabled**
- ✅ SMTP settings are configured
- ✅ Notification times are set (e.g., `08:00`)
- ✅ Days of week are set (if you want specific days)

## Troubleshooting

### No cron job created?

Check if:
1. You're on Linux (not Windows)
2. Notification settings exist in the database
3. Notifications are enabled in settings
4. Server logs show any errors

### Cron job not running?

```bash
# Check if cron service is running
sudo systemctl status cron

# Check system cron logs
grep CRON /var/log/syslog | tail -20

# Test the command manually
cd /home/admin/dataloggerpy
source venv/bin/activate
python manage.py check_notification_schedule
```

### Still have duplicates?

Restart the server:
```bash
# Stop the server (Ctrl+C)
# Start it again
python manage.py runserver 0.0.0.0:8000
```

Or manually clean:
```bash
python manage.py cleanup_cron --reinstall
```

## How Scheduling Works

The cron job runs **every minute**, but emails are only sent when:

1. ✅ Current time matches `notification_times` (e.g., `08:00`)
2. ✅ Current day matches `days_of_week` (if specified)
3. ✅ Enough time passed since last email (based on `frequency`)
4. ✅ Notifications are enabled

### Example Settings:

**Configuration:**
- Frequency: `daily`
- Times: `08:00,20:00`
- Days: `Monday,Friday`

**Result:** Emails sent on Monday and Friday at 08:00 and 20:00

## Key Changes Made

### 1. Fixed `app/utils/system_utils.py`
- Now uses `cron_manager` instead of creating duplicates
- Properly removes old jobs before creating new ones

### 2. Enhanced `app/utils/cron_manager.py`
- Better duplicate detection and removal
- Catches all variations of notification cron jobs

### 3. Updated `app/apps.py`
- Better logging on startup
- Only runs in main process (no duplicates)
- Clear status messages

### 4. New command: `cleanup_cron`
- Manually clean up all notification cron jobs
- Option to reinstall after cleanup

## Benefits

✅ **No manual setup** - Just start the server  
✅ **No duplicates** - Always cleaned on startup  
✅ **Correct paths** - Auto-detects OS and uses right Python path  
✅ **Self-healing** - Every server restart fixes the cron jobs  
✅ **Easy debugging** - Clear logs show what's happening  

## For Deployment

When deploying to production:

1. Start your Django application (gunicorn/uwsgi)
2. Cron jobs are automatically configured
3. Check logs to verify setup
4. Monitor `logs/notification_service.log` for activity

That's it! The system handles everything automatically.

## Need Help?

Check these logs:
- Django server logs (console output)
- `logs/notification_service.log` - Cron job activity
- `/var/log/syslog` - System cron logs

Run diagnostic:
```bash
./diagnose_email_issue.sh
```

