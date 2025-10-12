#!/bin/bash
# Complete Linux Cron Job Diagnostic and Fix Script
# This script diagnoses and fixes all cron job issues for the radar notification system

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Project paths - auto-detect
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$SCRIPT_DIR"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Radar Cron Job - Complete Fix${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Function to print status
print_status() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✓${NC} $2"
    else
        echo -e "${RED}✗${NC} $2"
    fi
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# 1. Check we're on Linux
echo "1. Checking environment..."
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    print_warning "This script is for Linux systems only"
    echo "Current OS: $OSTYPE"
    exit 1
fi
print_status 0 "Running on Linux"

# 2. Check cron service
echo ""
echo "2. Checking cron service..."
if systemctl is-active --quiet cron 2>/dev/null || systemctl is-active --quiet crond 2>/dev/null; then
    print_status 0 "Cron service is running"
else
    print_warning "Cron service is not running"
    echo "Attempting to start cron service..."
    if sudo systemctl start cron 2>/dev/null || sudo systemctl start crond 2>/dev/null; then
        print_status 0 "Cron service started"
    else
        print_status 1 "Could not start cron service"
        echo "Please start it manually: sudo systemctl start cron"
    fi
fi

# 3. Check current crontab
echo ""
echo "3. Checking current crontab..."
CURRENT_CRONTAB=$(crontab -l 2>/dev/null)

if [ -z "$CURRENT_CRONTAB" ]; then
    print_info "No crontab entries found (clean slate)"
    RADAR_JOBS=0
else
    # Count radar-related jobs
    RADAR_JOBS=$(echo "$CURRENT_CRONTAB" | grep -E 'check_notification_schedule|send_json_reports|radar_email_job|notification_service\.log' | wc -l)
    
    if [ $RADAR_JOBS -eq 0 ]; then
        print_info "No radar notification jobs found"
    elif [ $RADAR_JOBS -eq 1 ]; then
        print_status 0 "Found 1 radar notification job"
    else
        print_warning "Found $RADAR_JOBS radar notification jobs (should be 1)"
        echo "  This indicates duplicate entries that need cleanup"
    fi
fi

# 4. Check for wrong paths (Windows paths on Linux)
echo ""
echo "4. Checking for incorrect paths..."
WINDOWS_PATHS=$(echo "$CURRENT_CRONTAB" | grep -E 'Scripts/python\.exe|\\\\' | wc -l)
if [ $WINDOWS_PATHS -gt 0 ]; then
    print_status 1 "Found $WINDOWS_PATHS entries with Windows paths!"
    echo "  These will NOT work on Linux"
else
    print_status 0 "No Windows paths found"
fi

# 5. Detect virtual environment
echo ""
echo "5. Detecting virtual environment..."
VENV_PATH=""
for venv_name in loggervenv venv env .venv virtualenv; do
    if [ -f "$PROJECT_DIR/$venv_name/bin/activate" ]; then
        VENV_PATH="$venv_name"
        print_status 0 "Found virtual environment: $venv_name"
        break
    fi
done

if [ -z "$VENV_PATH" ]; then
    print_status 1 "Could not find virtual environment!"
    echo "  Looked for: loggervenv, venv, env, .venv, virtualenv"
    echo "  Please ensure virtual environment is set up"
    exit 1
fi

# 6. Check if Django is accessible
echo ""
echo "6. Checking Django installation..."
cd "$PROJECT_DIR"
source "$VENV_PATH/bin/activate"

if python manage.py --version &>/dev/null; then
    DJANGO_VERSION=$(python manage.py --version)
    print_status 0 "Django is accessible (version: $DJANGO_VERSION)"
else
    print_status 1 "Django is not accessible"
    echo "  Make sure requirements are installed: pip install -r requirements.txt"
    exit 1
fi

# 7. Check notification settings
echo ""
echo "7. Checking notification settings..."
SETTINGS_CHECK=$(python manage.py shell -c "
from app.models import NotificationSettings
s = NotificationSettings.objects.first()
if s and s.enable_notifications:
    print(f'OK|{s.primary_email}|{s.frequency}|{s.notification_times or \"Any\"}')
elif s:
    print('DISABLED')
else:
    print('MISSING')
" 2>/dev/null)

if [[ "$SETTINGS_CHECK" == OK* ]]; then
    IFS='|' read -r status email freq times <<< "$SETTINGS_CHECK"
    print_status 0 "Notification settings found and enabled"
    echo "  Email: $email"
    echo "  Frequency: $freq"
    echo "  Times: $times"
elif [ "$SETTINGS_CHECK" == "DISABLED" ]; then
    print_warning "Notification settings exist but are DISABLED"
    echo "  Enable them in the Django admin interface"
    exit 0
elif [ "$SETTINGS_CHECK" == "MISSING" ]; then
    print_warning "No notification settings found"
    echo "  Configure settings in the Django admin interface first"
    exit 0
else
    print_warning "Could not check notification settings"
fi

# 8. Backup current crontab
echo ""
echo "8. Creating backup..."
if [ ! -z "$CURRENT_CRONTAB" ]; then
    BACKUP_FILE="$PROJECT_DIR/crontab_backup_$(date +%Y%m%d_%H%M%S).txt"
    echo "$CURRENT_CRONTAB" > "$BACKUP_FILE"
    print_status 0 "Backed up to: $BACKUP_FILE"
else
    print_info "No existing crontab to backup"
fi

# 9. Fix crontab using Django management command
echo ""
echo "9. Fixing cron jobs using Django..."
print_info "This will:"
echo "  - Remove ALL existing radar notification cron jobs"
echo "  - Create ONE new correct cron job"
echo "  - Use proper Linux paths"
echo ""

# Run the cleanup and reinstall
python manage.py cleanup_cron --reinstall

if [ $? -eq 0 ]; then
    print_status 0 "Cron jobs fixed successfully via Django"
else
    print_warning "Django command had issues, trying manual fix..."
    
    # Manual fix as fallback
    echo ""
    echo "10. Applying manual fix..."
    
    # Remove all radar-related cron jobs
    if [ ! -z "$CURRENT_CRONTAB" ]; then
        CLEANED_CRONTAB=$(echo "$CURRENT_CRONTAB" | grep -vE 'check_notification_schedule|send_json_reports|radar_email_job|notification_service\.log|Radar Notification Service')
    else
        CLEANED_CRONTAB=""
    fi
    
    # Create new cron job
    LOG_FILE="$PROJECT_DIR/logs/notification_service.log"
    mkdir -p "$PROJECT_DIR/logs"
    
    NEW_CRON_JOB="# Radar Notification Service
# Configured on $(date '+%Y-%m-%d %H:%M:%S')
# Virtual Environment: $VENV_PATH
* * * * * cd $PROJECT_DIR && source $VENV_PATH/bin/activate && python manage.py check_notification_schedule >> $LOG_FILE 2>&1
"
    
    # Install new crontab
    {
        echo "$CLEANED_CRONTAB"
        echo ""
        echo "$NEW_CRON_JOB"
    } | crontab -
    
    if [ $? -eq 0 ]; then
        print_status 0 "Manual fix applied successfully"
    else
        print_status 1 "Failed to install new crontab"
        exit 1
    fi
fi

# 11. Verify the fix
echo ""
echo "11. Verifying fix..."
NEW_CRONTAB=$(crontab -l 2>/dev/null)
NEW_RADAR_JOBS=$(echo "$NEW_CRONTAB" | grep -E 'check_notification_schedule' | wc -l)

if [ $NEW_RADAR_JOBS -eq 1 ]; then
    print_status 0 "Exactly 1 radar notification job installed"
    echo ""
    echo "Installed cron job:"
    echo "$NEW_CRONTAB" | grep -A 5 "Radar Notification Service"
elif [ $NEW_RADAR_JOBS -eq 0 ]; then
    print_warning "No radar notification jobs found after fix"
    echo "The cron job may not have been created"
else
    print_warning "Still have $NEW_RADAR_JOBS radar jobs (should be 1)"
fi

# 12. Test the command manually
echo ""
echo "12. Testing command manually..."
echo "Running: python manage.py check_notification_schedule"
echo "---"
python manage.py check_notification_schedule
TEST_RESULT=$?
echo "---"

if [ $TEST_RESULT -eq 0 ]; then
    print_status 0 "Command runs successfully"
else
    print_warning "Command exited with code: $TEST_RESULT"
fi

# 13. Check log file
echo ""
echo "13. Checking log file..."
LOG_FILE="$PROJECT_DIR/logs/notification_service.log"
if [ -f "$LOG_FILE" ]; then
    print_status 0 "Log file exists: $LOG_FILE"
    LOG_SIZE=$(stat -f%z "$LOG_FILE" 2>/dev/null || stat -c%s "$LOG_FILE" 2>/dev/null)
    echo "  Size: $LOG_SIZE bytes"
    
    if [ $LOG_SIZE -gt 0 ]; then
        echo ""
        echo "  Last 5 lines:"
        tail -5 "$LOG_FILE" | sed 's/^/  | /'
    fi
else
    print_info "Log file will be created when cron job runs"
fi

# Final summary
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Fix Complete - Summary${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

if [ $NEW_RADAR_JOBS -eq 1 ]; then
    echo -e "${GREEN}✓ SUCCESS${NC}"
    echo "  Your cron job is now properly configured!"
    echo ""
    echo "What happens now:"
    echo "  1. Cron runs every minute: * * * * *"
    echo "  2. Checks if it's time to send email"
    echo "  3. Sends email based on your schedule"
    echo "  4. Logs to: $LOG_FILE"
    echo ""
    echo "Monitor activity:"
    echo "  tail -f $LOG_FILE"
    echo ""
    echo "View crontab:"
    echo "  crontab -l"
    echo ""
    echo "Test email manually:"
    echo "  cd $PROJECT_DIR"
    echo "  source $VENV_PATH/bin/activate"
    echo "  python manage.py test_summary_email"
else
    echo -e "${YELLOW}⚠ PARTIAL SUCCESS${NC}"
    echo "  The fix was applied but verification shows issues."
    echo "  Please check the output above for details."
    echo ""
    echo "Manual verification:"
    echo "  crontab -l | grep check_notification_schedule"
    echo ""
    echo "Manual fix:"
    echo "  python manage.py setup_cron_jobs --force"
fi

echo ""
echo -e "${BLUE}========================================${NC}"
echo ""

deactivate 2>/dev/null

