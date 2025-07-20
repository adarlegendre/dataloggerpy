# 🚀 Automatic Cron Job Configuration for Radar Notifications

This system automatically configures Linux cron jobs based on notification settings in the web interface. The cron jobs are set up when the software starts and updated whenever notification settings are saved.

## 🎯 How It Works

### 1. **Automatic Setup on Startup**
- When the system boots, `startup_cron_setup.py` runs automatically
- Reads notification settings from the database
- Configures cron jobs based on the settings
- Logs all activity for monitoring

### 2. **Dynamic Updates**
- When notification settings are saved in the web interface
- The `NotificationSettings.save()` method automatically calls `setup_cron_job()`
- Cron jobs are updated to reflect the new settings
- If notifications are disabled, cron jobs are removed

### 3. **Smart Scheduling**
- Cron job runs every minute: `* * * * *`
- Django logic checks if notifications should be sent based on:
  - **Frequency**: hourly/daily/weekly/monthly
  - **Days of week**: Only send on specified days
  - **Notification times**: Only send at specified times
  - **Last notification**: Prevent duplicate sends

## 📁 Files Overview

### Core Components
- `app/utils/cron_manager.py` - Cron job management utility
- `app/management/commands/setup_cron_jobs.py` - Django management command
- `startup_cron_setup.py` - Startup script for automatic configuration
- `setup_automatic_notifications.sh` - Complete setup script for Linux

### Configuration Files
- `radar-notification.service` - Systemd service file
- `manual_cron_setup.sh` - Manual setup script (created by setup script)

## 🔧 Setup Instructions

### For Linux Systems

1. **Run the automatic setup script:**
   ```bash
   sudo chmod +x setup_automatic_notifications.sh
   sudo ./setup_automatic_notifications.sh
   ```

2. **The script will:**
   - Check Python and Django installation
   - Test cron access
   - Set up cron jobs based on current settings
   - Create systemd service for automatic startup
   - Configure log rotation
   - Create manual setup script

### Manual Setup (if needed)

1. **Set up cron jobs manually:**
   ```bash
   python manage.py setup_cron_jobs
   ```

2. **Check cron status:**
   ```bash
   crontab -l
   ```

3. **Monitor logs:**
   ```bash
   tail -f logs/notification_service.log
   ```

## 🖥️ Web Interface Integration

### Cron Status Display
The notification settings page shows:
- ✅ **Active**: Cron job is installed and running
- ⚠️ **Not Configured**: No cron job found
- 📋 **Cron Job Details**: Shows the actual cron command
- 📄 **Log File Location**: Path to notification logs

### Automatic Updates
- When you save notification settings, cron jobs are automatically updated
- If you disable notifications, cron jobs are automatically removed
- Status is refreshed in real-time

## 📊 Current Settings

Based on your current configuration:
- **Primary Email**: `adarzeph@gmail.com`
- **Frequency**: `daily`
- **Days**: `Monday, Sunday`
- **Times**: `Any time`
- **Status**: `Enabled`

## 🔍 Monitoring and Troubleshooting

### Check Cron Status
```bash
# View current cron jobs
crontab -l

# Check if radar notification job exists
crontab -l | grep "check_notification_schedule"
```

### Monitor Logs
```bash
# View notification service logs
tail -f logs/notification_service.log

# View systemd service logs
journalctl -u radar-notification.service -f
```

### Test Notification System
```bash
# Test the scheduling logic
python manage.py check_notification_schedule

# Send test email
python manage.py send_test_email
```

### Manual Cron Setup
```bash
# Run manual setup
./manual_cron_setup.sh

# Force reinstall cron jobs
python manage.py setup_cron_jobs --force
```

## 🚨 Troubleshooting

### Common Issues

1. **"No access to crontab"**
   - Ensure you're running as root: `sudo ./setup_automatic_notifications.sh`
   - Check if cron is installed: `sudo apt-get install cron` (Ubuntu/Debian)

2. **"Cron job not found"**
   - Configure notification settings in the web interface first
   - Run manual setup: `python manage.py setup_cron_jobs`

3. **"Notifications not sending"**
   - Check logs: `tail -f logs/notification_service.log`
   - Verify SMTP settings in the web interface
   - Test email sending manually

4. **"Systemd service failed"**
   - Check service status: `systemctl status radar-notification.service`
   - View logs: `journalctl -u radar-notification.service`

### Windows Systems
- Cron jobs are not available on Windows
- The system will show appropriate warnings
- Consider using Windows Task Scheduler as an alternative

## 📈 Benefits

### ✅ **Automatic Management**
- No manual cron configuration required
- Settings changes automatically update cron jobs
- System startup automatically configures notifications

### ✅ **Smart Scheduling**
- Respects all notification settings
- Prevents duplicate notifications
- Efficient resource usage

### ✅ **Comprehensive Logging**
- All activity is logged for monitoring
- Easy troubleshooting and debugging
- Log rotation prevents disk space issues

### ✅ **User-Friendly**
- Web interface shows cron status
- Clear feedback on configuration
- Easy to understand and manage

## 🔄 System Flow

```
System Boot → startup_cron_setup.py → Read Settings → Configure Cron
     ↓
Web Interface → Save Settings → NotificationSettings.save() → Update Cron
     ↓
Every Minute → Cron Job → check_notification_schedule → Send Email (if needed)
     ↓
Log Activity → notification_service.log → Monitor & Debug
```

## 🎉 Success Indicators

When everything is working correctly, you should see:

1. **In the web interface:**
   - ✅ "Cron job is active" status
   - Cron job details displayed
   - Log file location shown

2. **In the system:**
   - Cron job listed in `crontab -l`
   - Log file being updated regularly
   - Systemd service running

3. **In your email:**
   - Notifications arriving according to your schedule
   - JSON files attached as configured

The system is now fully automated and will handle all notification scheduling based on your web interface settings! 🚀 