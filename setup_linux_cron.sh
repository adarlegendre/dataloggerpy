#!/bin/bash

# Get the current directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create a temporary file for crontab
TEMP_CRON=$(mktemp)

# Backup existing crontab
crontab -l > "$TEMP_CRON" 2>/dev/null

# Remove any existing radar notification entries
sed -i '/# Radar Notification Service/,/^$/d' "$TEMP_CRON"

# Add comments for clarity
echo "# Radar Notification Service" >> "$TEMP_CRON"
echo "# Added on $(date)" >> "$TEMP_CRON"
echo "# Runs check_notification_schedule every minute to respect configured frequency, days, and times" >> "$TEMP_CRON"

# Add the cron job that runs every minute and lets Django handle the scheduling logic
echo "* * * * * cd $PROJECT_DIR && source venv/bin/activate && python manage.py check_notification_schedule >> logs/notification_service.log 2>&1" >> "$TEMP_CRON"

# Create logs directory if it doesn't exist
mkdir -p "$PROJECT_DIR/logs"

# Install the new crontab
crontab "$TEMP_CRON"

# Remove the temporary file
rm "$TEMP_CRON"

echo "✅ Linux cron job has been set up successfully!"
echo ""
echo "📋 What was configured:"
echo "   - Cron job runs every minute: * * * * *"
echo "   - Command: python manage.py check_notification_schedule"
echo "   - Log file: logs/notification_service.log"
echo ""
echo "🎯 How it works:"
echo "   - The cron job runs every minute"
echo "   - Django checks if notifications should be sent based on:"
echo "     • Frequency (hourly/daily/weekly/monthly)"
echo "     • Days of week (if configured)"
echo "     • Notification times (if configured)"
echo "     • Last notification sent"
echo ""
echo "📊 Current settings:"
echo "   - Primary Email: adarzeph@gmail.com"
echo "   - Frequency: daily"
echo "   - Days: Monday, Sunday"
echo "   - Times: Any time"
echo ""
echo "🔍 To monitor:"
echo "   - Check crontab: crontab -l"
echo "   - Monitor logs: tail -f logs/notification_service.log"
echo "   - Test manually: python manage.py check_notification_schedule"

# Make the log file writable
touch "$PROJECT_DIR/logs/notification_service.log"
chmod 666 "$PROJECT_DIR/logs/notification_service.log" 