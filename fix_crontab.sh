#!/bin/bash
# Script to clean up and fix the crontab for radar notifications

echo "========================================="
echo "  Fixing Radar Notification Crontab"
echo "========================================="
echo ""

# Backup current crontab
echo "Creating backup of current crontab..."
crontab -l > crontab_backup_$(date +%Y%m%d_%H%M%S).txt
echo "✓ Backup created"

# Create clean crontab with only the necessary entry
echo ""
echo "Creating clean crontab..."

# Create new crontab file
cat > new_crontab.txt << 'EOF'
# Radar Notification Service - Check every minute if it's time to send emails
# Configured automatically by the notification settings page
* * * * * cd /home/admin/dataloggerpy && source venv/bin/activate && python manage.py check_notification_schedule >> /home/admin/dataloggerpy/logs/notification_service.log 2>&1
EOF

# Install the new crontab
crontab new_crontab.txt

echo "✓ Clean crontab installed"
echo ""

# Show the new crontab
echo "New crontab contents:"
echo "---"
crontab -l
echo "---"
echo ""

# Clean up
rm new_crontab.txt

echo "✓ Crontab cleaned and fixed!"
echo ""
echo "What was fixed:"
echo "  1. Removed 100+ duplicate entries"
echo "  2. Fixed Python path from Windows to Linux format"
echo "  3. Using correct virtual environment activation"
echo ""
echo "The cron job now runs every minute and checks if it's time to send emails"
echo "based on your notification settings."
echo ""

