#!/bin/bash

# Get the current directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create a temporary file for crontab
TEMP_CRON=$(mktemp)

# Backup existing crontab
crontab -l > "$TEMP_CRON" 2>/dev/null

# Add comments for clarity
echo "# Radar JSON Data Email Notifications" >> "$TEMP_CRON"
echo "# Added on $(date)" >> "$TEMP_CRON"

# Add the cron jobs for different frequencies
# Hourly job (runs at minute 0 of every hour)
echo "0 * * * * cd $PROJECT_DIR && source venv/bin/activate && python manage.py send_json_reports >> logs/email_reports.log 2>&1" >> "$TEMP_CRON"

# Daily job (runs at 00:00)
echo "0 0 * * * cd $PROJECT_DIR && source venv/bin/activate && python manage.py send_json_reports >> logs/email_reports.log 2>&1" >> "$TEMP_CRON"

# Weekly job (runs at 00:00 on Monday)
echo "0 0 * * 1 cd $PROJECT_DIR && source venv/bin/activate && python manage.py send_json_reports >> logs/email_reports.log 2>&1" >> "$TEMP_CRON"

# Monthly job (runs at 00:00 on the 1st of each month)
echo "0 0 1 * * cd $PROJECT_DIR && source venv/bin/activate && python manage.py send_json_reports >> logs/email_reports.log 2>&1" >> "$TEMP_CRON"

# Create logs directory if it doesn't exist
mkdir -p "$PROJECT_DIR/logs"

# Install the new crontab
crontab "$TEMP_CRON"

# Remove the temporary file
rm "$TEMP_CRON"

echo "Cron jobs have been set up successfully!"
echo "Check logs/email_reports.log for the output of the scheduled tasks."

# Make the log file writable
touch "$PROJECT_DIR/logs/email_reports.log"
chmod 666 "$PROJECT_DIR/logs/email_reports.log" 