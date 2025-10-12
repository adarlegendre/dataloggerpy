# Cron Job Fix - Quick Start

## On Your Linux/Raspberry Pi System

### Option 1: Automatic Fix Script (Recommended)

```bash
cd /home/admin/dataloggerpy  # or your project path
chmod +x fix_linux_cron_complete.sh
./fix_linux_cron_complete.sh
```

✅ Done! The script fixes everything automatically.

---

### Option 2: Using Django Commands

```bash
cd /home/admin/dataloggerpy
source venv/bin/activate  # or loggervenv/bin/activate
python manage.py cleanup_cron --reinstall
```

---

### Option 3: Restart Django Server

```bash
cd /home/admin/dataloggerpy
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

Cron jobs auto-fix on startup!

---

## Verify It Worked

```bash
# Check crontab (should show 1 entry)
crontab -l | grep check_notification_schedule

# Monitor logs
tail -f /home/admin/dataloggerpy/logs/notification_service.log

# Test email manually
cd /home/admin/dataloggerpy
source venv/bin/activate
python manage.py test_summary_email
```

---

## Common Issues

### "No virtual environment found"
```bash
# Find your venv
ls -la | grep -E "venv|loggervenv|env"

# Then use that name when activating
source YOUR_VENV_NAME/bin/activate
```

### "Notifications disabled"
1. Go to Django admin: `http://your-ip:8000/admin`
2. Open "Notification Settings"
3. Enable notifications ✓
4. Save

### "Cron service not running"
```bash
sudo systemctl start cron
sudo systemctl enable cron
```

---

## What Gets Installed

```bash
# Radar Notification Service
# Runs every minute, checks schedule, sends emails when time matches
* * * * * cd /home/admin/dataloggerpy && source venv/bin/activate && python manage.py check_notification_schedule >> /home/admin/dataloggerpy/logs/notification_service.log 2>&1
```

---

## Need More Help?

See detailed guides:
- `LINUX_CRON_FIX_README.md` - Complete fix guide
- `AUTO_CRON_SETUP_README.md` - How auto-setup works
- Run: `./diagnose_email_issue.sh` - Full diagnostic

