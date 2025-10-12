# Fix Your Cron Jobs Now - Linux

## The Problem

You're seeing: **"No email cron jobs found"**

This means your cron jobs are not set up, so email notifications won't be sent.

## Quick Fix (5 Minutes)

### On Your Linux System:

```bash
# 1. Navigate to your project
cd /home/admin/dataloggerpy  # or your actual path

# 2. Make script executable
chmod +x setup_cron_now.sh

# 3. Run the setup script
./setup_cron_now.sh
```

That's it! The script will automatically:
- ✅ Find your virtual environment
- ✅ Remove any broken cron jobs
- ✅ Create ONE correct cron job
- ✅ Show you the result

---

## Alternative Methods

### Method 1: Using Django Commands Directly

```bash
cd /home/admin/dataloggerpy
source venv/bin/activate  # or loggervenv/bin/activate

# Clean up and reinstall
python manage.py cleanup_cron --reinstall
```

### Method 2: Restart Django Server

The system auto-fixes cron jobs on startup:

```bash
cd /home/admin/dataloggerpy
source venv/bin/activate

# Stop current server (Ctrl+C if running)

# Start server (this auto-fixes cron jobs)
python manage.py runserver 0.0.0.0:8000
```

Watch for these messages in the startup log:
```
============================================================
Radar Data Logger - Server Startup
============================================================
✓ Radar data service started
Setting up email notification cron jobs...
✓ Email cron jobs configured
============================================================
```

---

## Verify It Worked

### 1. Check Crontab

```bash
crontab -l
```

You should see **exactly 1** radar notification entry like:

```bash
# Radar Notification Service
# Configured on 2025-10-12 08:30:00
# Virtual Environment: venv
* * * * * cd /home/admin/dataloggerpy && source venv/bin/activate && python manage.py check_notification_schedule >> /home/admin/dataloggerpy/logs/notification_service.log 2>&1
```

### 2. Monitor Logs

Wait 1-2 minutes, then:

```bash
tail -f /home/admin/dataloggerpy/logs/notification_service.log
```

You should see entries every minute checking the schedule.

### 3. Test Email Manually

```bash
cd /home/admin/dataloggerpy
source venv/bin/activate
python manage.py test_summary_email
```

This sends a test email immediately (ignores schedule).

---

## Still Showing "No email cron jobs found"?

### Check 1: Notification Settings

```bash
cd /home/admin/dataloggerpy
source venv/bin/activate

python manage.py shell
```

Then in the Python shell:

```python
from app.models import NotificationSettings
s = NotificationSettings.objects.first()
if s:
    print(f"Enabled: {s.enable_notifications}")
    print(f"Email: {s.primary_email}")
else:
    print("No settings found - configure in Django admin first!")
```

Exit with `exit()`.

**If notifications are disabled or missing:**
1. Go to Django admin: `http://your-ip:8000/admin`
2. Navigate to "Notification Settings"
3. Enable notifications ✓
4. Set your email and schedule
5. Save
6. Run `./setup_cron_now.sh` again

### Check 2: Cron Service

```bash
sudo systemctl status cron
```

Should show "active (running)". If not:

```bash
sudo systemctl start cron
sudo systemctl enable cron  # Start on boot
```

### Check 3: Virtual Environment

Make sure your virtual environment exists:

```bash
cd /home/admin/dataloggerpy
ls -la | grep -E "venv|loggervenv"
```

If not found, create one:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## The Status Monitor Message

The message you're seeing:

```
=== Email Cron Jobs Status ===
No email cron jobs found
===========================
```

This is from the **status monitor** that runs every 60 seconds. It's looking for a cron job with the comment `radar_email_job`. 

After running the fix, this will change to:

```
=== Email Cron Jobs Status ===
Schedule: * * * * *
Next run in: 45 seconds
===========================
```

---

## Fixed the "startup_service" Error

I also fixed this error you were seeing:

```
Error getting radar service status: No module named 'app.utils.startup_service'
```

This was caused by a missing file. I've created `app/utils/startup_service.py` which provides radar service status information.

After you pull the latest code, this error will disappear.

---

## What You Should See After Fix

### In Crontab (`crontab -l`):
```bash
# Radar Notification Service
# Configured on 2025-10-12 08:30:00
* * * * * cd /home/admin/dataloggerpy && source venv/bin/activate && python manage.py check_notification_schedule >> /home/admin/dataloggerpy/logs/notification_service.log 2>&1
```

### In Status Monitor (every 60 seconds):
```
=== Email Cron Jobs Status ===
Schedule: * * * * *
Next run in: 23 seconds
===========================
```

### In Logs (`tail -f logs/notification_service.log`):
```
[2025-10-12 08:30:01] Checking notification schedule...
[2025-10-12 08:30:01] Current time: 08:30
[2025-10-12 08:30:01] Not time to send yet
[2025-10-12 08:31:01] Checking notification schedule...
...
```

---

## Understanding the Schedule

The cron job runs **every minute**, but emails are only sent when:

1. ✅ Current time matches your configured `notification_times` (e.g., "08:00")
2. ✅ Current day matches your `days_of_week` (if specified)
3. ✅ Enough time has passed since last email (based on `frequency`)
4. ✅ Notifications are enabled

### Example:
- **Frequency:** `daily`
- **Times:** `08:00,20:00`
- **Days:** `Monday,Friday`

**Result:** Emails sent at 08:00 and 20:00 on Mondays and Fridays only.

---

## Need More Help?

### Run Full Diagnostic:

```bash
cd /home/admin/dataloggerpy
chmod +x fix_linux_cron_complete.sh
./fix_linux_cron_complete.sh
```

This comprehensive script checks everything and fixes all issues.

### Check Documentation:

- `CRON_QUICK_START.md` - Quick reference
- `LINUX_CRON_FIX_README.md` - Complete guide
- `AUTO_CRON_SETUP_README.md` - How auto-setup works

---

## Summary

Run this on your Linux system:

```bash
cd /home/admin/dataloggerpy
chmod +x setup_cron_now.sh
./setup_cron_now.sh
```

Then verify:

```bash
# Check crontab
crontab -l

# Monitor logs (wait 1-2 minutes)
tail -f logs/notification_service.log

# Test email
python manage.py test_summary_email
```

You're done! 🎉

