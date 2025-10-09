# Cron Job Email Notification Fix Guide

## Problems Found

Your cron jobs aren't working because of three critical issues:

### 1. Wrong Python Path (Windows vs Linux)
- **Current (Wrong)**: `/home/admin/dataloggerpy/venv/Scripts/python.exe`
- **Should be**: `/home/admin/dataloggerpy/venv/bin/python`

The path `Scripts/python.exe` is Windows format. On Linux/Raspberry Pi, it's `bin/python`.

### 2. Massive Duplicate Entries
Your crontab has 100+ duplicate entries of the same jobs, which can cause:
- Resource waste (multiple instances running)
- Log file confusion
- Cron daemon performance issues

### 3. Most Entries Use Wrong Format
Most entries won't work because they use the Windows Python path.

## The Fix

I've created two scripts for you:

### 1. `fix_crontab.sh` - Cleans and fixes your crontab
This script:
- Backs up your current crontab
- Removes all duplicates
- Installs a clean, working cron entry
- Uses correct Linux paths

### 2. `test_notification_manually.sh` - Tests the system
This script:
- Checks your notification settings
- Runs the notification command manually
- Shows recent log entries

## Step-by-Step Instructions

### On your Raspberry Pi, run:

```bash
# 1. Make scripts executable
chmod +x fix_crontab.sh test_notification_manually.sh

# 2. Fix the crontab
./fix_crontab.sh

# 3. Test the notification system
./test_notification_manually.sh
```

## What the Fixed Crontab Looks Like

After running `fix_crontab.sh`, you'll have ONE clean entry:

```bash
* * * * * cd /home/admin/dataloggerpy && source venv/bin/activate && python manage.py check_notification_schedule >> /home/admin/dataloggerpy/logs/notification_service.log 2>&1
```

This runs every minute and:
- Changes to your project directory
- Activates the Python virtual environment
- Runs the notification check command
- Logs output to `logs/notification_service.log`

## Verifying It Works

### Check cron is running:
```bash
# View current crontab
crontab -l

# Check if cron service is active
sudo systemctl status cron
```

### Monitor the log file:
```bash
# Watch log file in real-time
tail -f /home/admin/dataloggerpy/logs/notification_service.log

# View last 50 lines
tail -50 /home/admin/dataloggerpy/logs/notification_service.log
```

### Test sending immediately:
```bash
cd /home/admin/dataloggerpy
source venv/bin/activate
python manage.py test_summary_email
```

## Understanding the Schedule

The cron job runs **every minute**, but emails are only sent when:

1. ✅ Current time matches your configured notification time
2. ✅ Current day is in your allowed days (if specified)
3. ✅ Enough time has passed since last notification (based on frequency)
4. ✅ Notifications are enabled in settings

### Example Configuration:
- **Frequency**: Daily
- **Time**: 08:00
- **Days**: Monday, Friday

**Result**: Email sent every Monday and Friday at 08:00 AM

## Troubleshooting

### Emails still not sending?

1. **Check notification settings in Django admin:**
   ```bash
   python manage.py shell
   >>> from app.models import NotificationSettings
   >>> settings = NotificationSettings.objects.first()
   >>> print(f"Enabled: {settings.enable_notifications}")
   >>> print(f"Email: {settings.primary_email}")
   >>> print(f"Times: {settings.notification_times}")
   >>> print(f"Days: {settings.days_of_week}")
   ```

2. **Check SMTP settings are correct:**
   - SMTP server and port
   - Username and password
   - TLS/SSL settings

3. **Test email sending manually:**
   ```bash
   python manage.py test_summary_email --preview
   ```

4. **Check cron logs:**
   ```bash
   grep CRON /var/log/syslog | tail -20
   ```

5. **Verify timezone:**
   Your server time should match your expected notification time.
   ```bash
   date
   timedatectl  # Shows timezone info
   ```

### Common Issues

**Issue**: "No data to send"
- **Fix**: Make sure you have radar detections in the database for the previous day

**Issue**: "SMTP authentication failed"
- **Fix**: Check your email password and SMTP settings

**Issue**: "Permission denied"
- **Fix**: Ensure log directory exists and is writable:
  ```bash
  mkdir -p /home/admin/dataloggerpy/logs
  chmod 755 /home/admin/dataloggerpy/logs
  ```

## Manual Testing Commands

```bash
# Test notification check (doesn't send unless it's the right time)
python manage.py check_notification_schedule

# Force send test email (sends regardless of schedule)
python manage.py test_summary_email

# Preview what would be sent without sending
python manage.py test_summary_email --preview

# Test with specific date
python manage.py test_summary_email --date 2025-10-08
```

## Restoring from Backup

If something goes wrong, restore your old crontab:

```bash
# List backups
ls -la crontab_backup_*.txt

# Restore a specific backup
crontab crontab_backup_YYYYMMDD_HHMMSS.txt
```

## Next Steps

After running the fix script:

1. ✅ Wait 1-2 minutes
2. ✅ Check the log file for activity
3. ✅ Verify your notification settings are correct
4. ✅ Test manually if needed
5. ✅ Wait for the scheduled time to see if emails are sent

## Need Help?

Check these files for more information:
- `DAILY_SUMMARY_EMAIL_README.md` - Full email system documentation
- `logs/notification_service.log` - Current activity log
- `/var/log/syslog` - System cron logs

