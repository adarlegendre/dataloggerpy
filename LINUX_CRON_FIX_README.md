# Linux Cron Job Fix - Quick Guide

## Problem
Your cron jobs are not working on your Linux/Raspberry Pi system.

## Quick Fix

Run this on your Linux system:

```bash
cd /path/to/dataloggerpy
chmod +x fix_linux_cron_complete.sh
./fix_linux_cron_complete.sh
```

This script will:
- ✓ Check your environment
- ✓ Detect and fix wrong paths
- ✓ Remove duplicate cron jobs
- ✓ Create ONE correct cron job
- ✓ Verify everything works

## What the Script Does

### 1. Environment Check
- Verifies you're on Linux
- Checks cron service is running
- Finds your virtual environment

### 2. Diagnosis
- Counts existing cron jobs
- Detects Windows paths (Scripts/python.exe)
- Checks notification settings

### 3. Backup
- Saves your current crontab to a backup file
- Located at: `crontab_backup_YYYYMMDD_HHMMSS.txt`

### 4. Fix
- Removes ALL existing radar notification cron jobs
- Creates ONE new correct cron job with:
  - Correct Linux paths (`venv/bin/python`)
  - Correct command (`check_notification_schedule`)
  - Proper virtual environment activation

### 5. Verification
- Tests the command manually
- Checks log file
- Shows you the installed cron job

## The Correct Cron Job

After fixing, you'll have ONE cron entry like this:

```bash
# Radar Notification Service
# Configured on 2025-10-12 10:30:00
# Virtual Environment: venv
* * * * * cd /home/admin/dataloggerpy && source venv/bin/activate && python manage.py check_notification_schedule >> /home/admin/dataloggerpy/logs/notification_service.log 2>&1
```

This runs every minute and checks if it's time to send emails based on your settings.

## Alternative Methods

### Method 1: Using Django Commands (Recommended)

```bash
cd /path/to/dataloggerpy
source venv/bin/activate  # or loggervenv/bin/activate

# Clean up and reinstall
python manage.py cleanup_cron --reinstall

# Or force setup
python manage.py setup_cron_jobs --force
```

### Method 2: Restart Django Server

The system automatically fixes cron jobs when Django starts:

```bash
cd /path/to/dataloggerpy
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

Watch for startup messages like:
```
============================================================
Radar Data Logger - Server Startup
============================================================
✓ Radar data service started
Setting up email notification cron jobs...
✓ Email cron jobs configured
✓ Cron status monitor started
============================================================
```

## Verification

### 1. Check Crontab
```bash
crontab -l
```

Should show **exactly 1** radar notification entry.

### 2. Check Log File
```bash
tail -f /path/to/dataloggerpy/logs/notification_service.log
```

Should show activity every minute.

### 3. Check Cron Service
```bash
sudo systemctl status cron
```

Should be "active (running)".

### 4. Check System Logs
```bash
grep CRON /var/log/syslog | tail -20
```

Should show cron executing your job every minute.

## Common Issues

### Issue 1: "No virtual environment found"

**Fix:**
```bash
cd /path/to/dataloggerpy
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Issue 2: "Notifications are disabled"

**Fix:** Enable notifications in Django admin:
1. Go to `http://your-server:8000/admin`
2. Navigate to Notification Settings
3. Check "Enable notifications"
4. Save

### Issue 3: "Cron service not running"

**Fix:**
```bash
sudo systemctl start cron
sudo systemctl enable cron  # Start on boot
```

### Issue 4: "Permission denied on log file"

**Fix:**
```bash
cd /path/to/dataloggerpy
mkdir -p logs
chmod 755 logs
touch logs/notification_service.log
chmod 644 logs/notification_service.log
```

### Issue 5: Still have duplicates after fix

**Fix:**
```bash
# Manually clear crontab
crontab -r  # Removes ALL cron jobs (be careful!)

# Or edit manually
crontab -e  # Remove duplicate lines manually

# Then reinstall
cd /path/to/dataloggerpy
source venv/bin/activate
python manage.py setup_cron_jobs --force
```

## Testing

### Test Without Waiting

Send a test email immediately (ignores schedule):

```bash
cd /path/to/dataloggerpy
source venv/bin/activate
python manage.py test_summary_email
```

### Preview Email Content

See what would be sent without actually sending:

```bash
python manage.py test_summary_email --preview
```

### Check Schedule

See if current time matches your configured schedule:

```bash
python manage.py check_notification_schedule
```

## Understanding the Schedule

The cron job runs **every minute** (`* * * * *`), but emails are only sent when:

1. ✅ Current time matches `notification_times` (e.g., "08:00")
2. ✅ Current day matches `days_of_week` (if specified)
3. ✅ Enough time passed since last email (based on `frequency`)
4. ✅ Notifications are enabled in settings

### Example

**Settings:**
- Frequency: `daily`
- Times: `08:00,20:00`
- Days: `Monday,Friday`

**Result:** Emails sent at 08:00 and 20:00 on Mondays and Fridays only.

## Automatic Maintenance

The system is **self-healing**:

- ✓ Every Django server restart fixes cron jobs automatically
- ✓ Duplicate jobs are removed on startup
- ✓ Wrong paths are corrected on startup
- ✓ No manual maintenance needed

Just restart your Django application and cron jobs will be fixed.

## Monitoring

### Real-time Log Monitoring

```bash
tail -f /path/to/dataloggerpy/logs/notification_service.log
```

### Check Last 50 Lines

```bash
tail -50 /path/to/dataloggerpy/logs/notification_service.log
```

### Search for Errors

```bash
grep -i error /path/to/dataloggerpy/logs/notification_service.log
```

### Watch for "Sending email" Messages

```bash
grep "Sending email" /path/to/dataloggerpy/logs/notification_service.log
```

## Diagnostic Tools

### Full Diagnostic Report

```bash
cd /path/to/dataloggerpy
chmod +x diagnose_email_issue.sh
./diagnose_email_issue.sh
```

This checks:
- Environment setup
- Notification settings
- Recent notifications sent
- Detection data availability
- Crontab status
- Log file activity
- Manual command test

### Quick Status Check

```bash
cd /path/to/dataloggerpy
source venv/bin/activate
python -c "
from app.utils.cron_manager import cron_manager
status = cron_manager.get_cron_status()
print(f\"Installed: {status['installed']}\")
if status['installed']:
    print(f\"Job: {status['cron_job']}\")
    print(f\"Log: {status['log_file']}\")
"
```

## File Locations

- **Cron job log:** `/path/to/dataloggerpy/logs/notification_service.log`
- **Crontab backup:** `/path/to/dataloggerpy/crontab_backup_*.txt`
- **Fix script:** `/path/to/dataloggerpy/fix_linux_cron_complete.sh`
- **Diagnostic script:** `/path/to/dataloggerpy/diagnose_email_issue.sh`

## Help & Support

If issues persist:

1. Run the diagnostic script: `./diagnose_email_issue.sh`
2. Check all verification steps above
3. Review log files for errors
4. Ensure notification settings are correct
5. Test email sending manually

## Related Documentation

- `AUTO_CRON_SETUP_README.md` - Automatic cron setup details
- `CRON_FIX_GUIDE.md` - Original fix guide
- `CRON_FIX_SUMMARY.md` - Summary of changes
- `DAILY_SUMMARY_EMAIL_README.md` - Email system documentation

## Windows Users

If you're on Windows, cron doesn't exist. Use instead:

```powershell
# In PowerShell as Administrator
.\setup_notification_scheduler.ps1
```

This uses Windows Task Scheduler instead of cron.

