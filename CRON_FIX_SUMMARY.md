# Cron Job Auto-Setup - Implementation Summary

## Problem Fixed

Your cron jobs weren't working because:
1. ❌ Using Windows path `venv/Scripts/python.exe` on Linux (should be `venv/bin/python`)
2. ❌ 100+ duplicate cron entries (causing resource waste)
3. ❌ Wrong command `send_json_reports` (should be `check_notification_schedule`)

## Solution Implemented

The system now **automatically** manages cron jobs every time you start the Django server.

### Files Modified

1. **`app/utils/system_utils.py`**
   - Fixed to use `cron_manager` instead of creating duplicates
   - Removes ALL old jobs before creating new one
   - Better error handling and logging

2. **`app/utils/cron_manager.py`**
   - Enhanced duplicate detection
   - Removes jobs by multiple keywords (catches all variations)
   - Better logging

3. **`app/apps.py`**
   - Improved startup logging
   - Only runs in main process (prevents duplicates)
   - Clear status messages

4. **`app/management/commands/cleanup_cron.py`** (NEW)
   - Manual cleanup command
   - Shows how many jobs will be removed
   - Option to reinstall after cleanup

### Helper Scripts Created

1. **`fix_crontab.sh`** - One-time cleanup script (legacy, not needed now)
2. **`diagnose_email_issue.sh`** - Full diagnostic tool
3. **`test_notification_manually.sh`** - Quick test script

### Documentation Created

1. **`AUTO_CRON_SETUP_README.md`** - Full documentation
2. **`QUICK_FIX_NOW.md`** - Immediate action steps
3. **`CRON_FIX_GUIDE.md`** - Troubleshooting guide
4. **`CRON_FIX_SUMMARY.md`** - This file

## How It Works Now

### Automatic Setup (Every Server Start)

```bash
python manage.py runserver 0.0.0.0:8000
```

On startup, the system:
1. ✅ Removes ALL existing notification cron jobs
2. ✅ Creates ONE new cron job with correct:
   - Linux paths (`venv/bin/python`)
   - Command (`check_notification_schedule`)
   - Schedule (runs every minute)
3. ✅ Logs everything clearly

### The Cron Job Created

```bash
# Radar Notification Service
# Configured on 2025-10-09 10:30:00
# Settings: your@email.com - daily
# Days: Monday,Sunday
# Times: 08:00
* * * * * cd /home/admin/dataloggerpy && source venv/bin/activate && python manage.py check_notification_schedule >> /home/admin/dataloggerpy/logs/notification_service.log 2>&1
```

This job:
- Runs every minute
- Checks if it's time to send email (based on your settings)
- Uses correct Linux virtual environment activation
- Logs to `logs/notification_service.log`

## Quick Start (On Your Raspberry Pi)

```bash
# 1. Clean up current mess
cd /home/admin/dataloggerpy
source venv/bin/activate
python manage.py cleanup_cron

# 2. Start server (auto-creates correct cron job)
python manage.py runserver 0.0.0.0:8000

# 3. Verify (in new terminal)
crontab -l  # Should show only 1 entry now

# 4. Monitor
tail -f logs/notification_service.log
```

## Benefits

✅ **Zero manual setup** - Just start the server  
✅ **Self-healing** - Every restart fixes cron jobs  
✅ **No duplicates** - Always cleaned first  
✅ **Correct paths** - Auto-detects OS  
✅ **Better logging** - Know what's happening  
✅ **Production ready** - Works with gunicorn/uwsgi  

## Email Schedule Logic

The cron job runs every minute, but emails only send when:

1. ✅ Current time matches `notification_times` (e.g., `08:00`)
2. ✅ Current day in `days_of_week` (if specified)
3. ✅ Enough time passed since last email (based on `frequency`)
4. ✅ Notifications enabled in settings

**Example:**
- Frequency: `daily`
- Times: `08:00,20:00`
- Days: `Monday,Friday`

**Result:** Emails at 08:00 and 20:00 on Mondays and Fridays only.

## Commands Available

```bash
# Automatic (recommended)
python manage.py runserver 0.0.0.0:8000  # Auto-creates cron job

# Manual cleanup
python manage.py cleanup_cron              # Remove all
python manage.py cleanup_cron --reinstall  # Remove and recreate

# Manual setup
python manage.py setup_cron_jobs           # Setup if not exists
python manage.py setup_cron_jobs --force   # Force recreate
python manage.py setup_cron_jobs --remove  # Remove all

# Testing
python manage.py test_summary_email         # Send test email
python manage.py test_summary_email --preview  # Preview JSON
python manage.py check_notification_schedule  # Run check manually

# Diagnosis
./diagnose_email_issue.sh  # Full diagnostic report
```

## Verification

### Check crontab:
```bash
crontab -l | grep -v "^#" | grep -v "^$"
```

Should show **exactly 1 line**.

### Check logs:
```bash
tail -f logs/notification_service.log
```

Should show activity every minute.

### Check settings:
```bash
python manage.py shell
>>> from app.models import NotificationSettings
>>> s = NotificationSettings.objects.first()
>>> print(f"Enabled: {s.enable_notifications}")
>>> print(f"Email: {s.primary_email}")
>>> print(f"Times: {s.notification_times}")
```

## Troubleshooting

### Still have duplicates after server restart?

The old duplicates should be auto-removed. If not:
```bash
python manage.py cleanup_cron --reinstall
```

### Emails not sending?

1. Check notification settings are enabled
2. Check SMTP configuration is correct
3. Verify current time matches schedule:
   ```bash
   ./diagnose_email_issue.sh
   ```
4. Test manually:
   ```bash
   python manage.py test_summary_email
   ```

### Cron job not created on startup?

Check server logs for errors. Make sure:
- You're on Linux (not Windows)
- Notification settings exist in database
- Notifications are enabled

## Production Deployment

For production (gunicorn/uwsgi/systemd):

1. Start your Django app normally
2. Cron jobs auto-configure on startup
3. Verify with `crontab -l`
4. Monitor `logs/notification_service.log`

No additional setup needed!

## What's Different From Before

### Before:
- Manual cron setup required
- Duplicates on each settings save
- Wrong paths on Linux
- Wrong command (send_json_reports)
- No cleanup of old jobs

### Now:
- ✅ Automatic on server start
- ✅ Duplicates prevented
- ✅ Correct Linux paths
- ✅ Correct command (check_notification_schedule)
- ✅ Auto-cleanup of old jobs
- ✅ Better logging
- ✅ Self-healing system

## Next Steps

1. ✅ Run `python manage.py cleanup_cron` to clean current mess
2. ✅ Restart server to auto-create correct cron job
3. ✅ Verify with `crontab -l`
4. ✅ Monitor `tail -f logs/notification_service.log`
5. ✅ Test with `python manage.py test_summary_email`

From now on, just start the server normally and cron jobs are handled automatically!

## Support

- Full docs: `AUTO_CRON_SETUP_README.md`
- Quick fix: `QUICK_FIX_NOW.md`
- Troubleshooting: `CRON_FIX_GUIDE.md`
- Diagnostic: `./diagnose_email_issue.sh`

