# What Happens When You Restart Django

## Your Setup
- **OS:** Linux
- **Virtual Environment:** `loggervenv`
- **Project Path:** (auto-detected from Django BASE_DIR)

## When You Restart the Application

### Automatic Actions on Startup

When you run:
```bash
cd /path/to/your/project
source loggervenv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

The system will automatically:

1. ✅ **Detect your virtual environment** - `loggervenv` (checked first!)
2. ✅ **Remove ALL old/broken cron jobs** - Cleans up duplicates and wrong paths
3. ✅ **Create ONE correct cron job** - Using proper Linux paths
4. ✅ **Start status monitor** - Shows cron job status every 60 seconds

### What You'll See in the Startup Log

```
============================================================
Radar Data Logger - Server Startup
============================================================
✓ Radar data service started
Configuring Linux cron jobs for email notifications...
Setting up notification cron job for your@email.com
Schedule: daily, Days: All, Times: 08:00
Step 1: Cleaning up ALL existing radar notification cron jobs...
Found X existing radar cron entries to remove
Step 2: Detecting virtual environment...
✓ Detected virtual environment: loggervenv
Step 3: Creating new cron job entry...
  Cron schedule: Every minute (* * * * *)
  Virtual env: loggervenv
  Log file: /path/to/project/logs/notification_service.log
Step 4: Installing new crontab...
============================================================
✓ CRON JOB SETUP SUCCESSFUL
============================================================
  Removed: X old cron entries
  Created: 1 new cron entry
  Email: your@email.com
  Virtual Env: loggervenv
  Schedule: Checks every minute
  Sends when: 08:00
============================================================
✓ Email notification cron job configured
  Cron job runs every minute and checks schedule
  Emails sent based on notification settings
Cron job: * * * * * cd /path/to/project && source loggervenv/bin/activate && python manage.py check_notification_schedule >> /path/to/project/logs/notification_service.log 2>&1
Log file: /path/to/project/logs/notification_service.log
✓ Cron status monitor started
============================================================
```

### The Cron Job That Gets Created

```bash
# Radar Notification Service
# Configured on 2025-10-12 08:30:00
# Settings: your@email.com - daily
# Days: All days
# Times: 08:00
# Virtual Environment: loggervenv
* * * * * cd /path/to/project && source loggervenv/bin/activate && python manage.py check_notification_schedule >> /path/to/project/logs/notification_service.log 2>&1
```

### Status Monitor Output (Every 60 Seconds)

**Before Fix:**
```
=== Email Cron Jobs Status ===
No email cron jobs found
===========================
```

**After Fix (what you'll see):**
```
=== Email Cron Jobs Status ===
✓ Cron job installed
Schedule: Every minute (* * * * *)
Command: check_notification_schedule
Log file: /path/to/project/logs/notification_service.log
Next run in: ~42 seconds
===========================
```

## Verification After Restart

### 1. Check Crontab
```bash
crontab -l
```

You should see **exactly 1** entry with `loggervenv/bin/activate`.

### 2. Monitor Logs
```bash
tail -f /path/to/project/logs/notification_service.log
```

Should show activity every minute.

### 3. Verify Virtual Environment Detection
Look in startup logs for:
```
✓ Detected virtual environment: loggervenv
```

## If Notifications Don't Work

### Issue 1: No notification settings
**Symptoms:**
```
⚠ Email cron job not configured
  Possible reasons:
  - Notification settings not found in database
```

**Fix:**
1. Go to Django admin: `http://your-ip:8000/admin`
2. Navigate to: App → Notification Settings
3. Create/edit settings
4. Enable notifications ✓
5. Set email and schedule
6. Save
7. Restart Django application

### Issue 2: Notifications disabled
**Symptoms:**
```
Notifications are disabled in settings. Removing cron jobs.
```

**Fix:**
1. Django admin → Notification Settings
2. Check "Enable notifications" ✓
3. Save
4. Restart Django application

### Issue 3: Can't access crontab
**Symptoms:**
```
✗ Cannot access crontab. Make sure cron is installed and accessible.
```

**Fix:**
```bash
# Check cron service
sudo systemctl status cron

# If not running, start it
sudo systemctl start cron
sudo systemctl enable cron
```

## Files Modified/Created

### Files Modified (Already in Codebase)
1. **`app/apps.py`** - Enhanced startup logging
2. **`app/utils/system_utils.py`** - Fixed status monitor detection
3. **`app/utils/cron_manager.py`** - Added cron access check

### Files Created (Already in Codebase)
1. **`app/utils/startup_service.py`** - Fixes missing module error

### Documentation Created
1. **`FIX_CRON_NOW.md`** - Quick fix guide
2. **`LINUX_CRON_FIX_README.md`** - Complete documentation
3. **`CRON_QUICK_START.md`** - One-page reference
4. **`fix_linux_cron_complete.sh`** - Diagnostic script
5. **`setup_cron_now.sh`** - Quick setup script
6. **`RESTART_SUMMARY.md`** - This file

## What Gets Fixed Automatically

✅ **Duplicate cron jobs** - All removed, only 1 created  
✅ **Wrong paths** - `Scripts/python.exe` → `loggervenv/bin/python`  
✅ **Wrong command** - `send_json_reports` → `check_notification_schedule`  
✅ **Missing venv detection** - Finds `loggervenv` first  
✅ **Status monitor** - Now properly detects installed cron jobs  
✅ **Missing module** - `startup_service.py` created  

## Testing After Restart

### Test 1: Send Test Email (Ignores Schedule)
```bash
cd /path/to/project
source loggervenv/bin/activate
python manage.py test_summary_email
```

### Test 2: Check Schedule Logic
```bash
python manage.py check_notification_schedule
```

This runs the same command that cron executes.

### Test 3: Preview Email Content
```bash
python manage.py test_summary_email --preview
```

Shows JSON without sending.

## Expected Behavior

### Cron Job Execution
- **Runs:** Every minute (* * * * *)
- **Checks:** If current time matches notification schedule
- **Sends email when:**
  - ✅ Time matches `notification_times` (e.g., "08:00")
  - ✅ Day matches `days_of_week` (if specified)
  - ✅ Enough time passed since last email (based on frequency)
  - ✅ Notifications are enabled

### Example Schedule
**Settings:**
- Frequency: `daily`
- Times: `08:00,20:00`
- Days: `Monday,Friday`

**Result:** Emails at 08:00 and 20:00 on Mondays and Fridays only.

## Summary

Simply restart your Django application:

```bash
cd /path/to/your/project
source loggervenv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

Everything will be fixed automatically:
- ✅ Cron jobs cleaned up
- ✅ `loggervenv` detected
- ✅ Correct cron job installed
- ✅ Status monitor working
- ✅ Missing module error fixed

**No manual steps needed!** Just restart and verify.

