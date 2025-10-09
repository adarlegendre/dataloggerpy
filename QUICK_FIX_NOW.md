# Quick Fix - Run This Now

## On Your Raspberry Pi

Follow these steps to fix the cron job issue immediately:

### Step 1: Stop the server (if running)
```bash
# Press Ctrl+C if server is running
```

### Step 2: Clean up the current mess
```bash
cd /home/admin/dataloggerpy
source loggervenv/bin/activate
python manage.py cleanup_cron
```

This will remove all 100+ duplicate cron entries.

### Step 3: Start the server
```bash
python manage.py runserver 0.0.0.0:8000
```

**Watch the startup logs** - you should see:
```
============================================================
Radar Data Logger - Server Startup
============================================================
✓ Radar data service started
Setting up email notification cron jobs...
✓ Email cron jobs configured
Cron job: * * * * * cd /home/admin/dataloggerpy && ...
✓ Cron status monitor started
============================================================
```

### Step 4: Verify the cron job (in a new terminal)
```bash
crontab -l
```

You should now see **ONLY ONE** entry instead of 100+.

### Step 5: Monitor the log
```bash
tail -f /home/admin/dataloggerpy/logs/notification_service.log
```

You should see activity every minute.

## That's It!

From now on, **every time you start the server**, it will:
- Clean up any old/duplicate cron jobs
- Create one fresh, correct cron job
- Use the right Linux paths

## Test Email Sending

```bash
# Test immediately (sends test email now)
python manage.py test_summary_email

# Preview what would be sent (no email)
python manage.py test_summary_email --preview
```

## What Changed?

The system now automatically manages cron jobs on server startup. You never need to manually set them up again!

See `AUTO_CRON_SETUP_README.md` for full details.

