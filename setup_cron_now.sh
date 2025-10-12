#!/bin/bash
# Quick cron job setup script for Linux
# Run this on your Linux/Raspberry Pi system

set -e

echo "=========================================="
echo "  Quick Cron Job Setup"
echo "=========================================="
echo ""

# Get the directory where script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Find virtual environment (loggervenv checked first for this project)
VENV_PATH=""
for venv_name in loggervenv venv env .venv virtualenv; do
    if [ -f "$venv_name/bin/activate" ]; then
        VENV_PATH="$venv_name"
        echo "✓ Found virtual environment: $venv_name"
        break
    fi
done

if [ -z "$VENV_PATH" ]; then
    echo "✗ Error: No virtual environment found!"
    echo "  Please create one first: python3 -m venv venv"
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_PATH/bin/activate"

# Check Django
if ! python manage.py --version &>/dev/null; then
    echo "✗ Error: Django not accessible"
    echo "  Install requirements: pip install -r requirements.txt"
    exit 1
fi

echo "✓ Django is accessible"
echo ""

# Run the Django command to clean up and reinstall cron
echo "Setting up cron jobs..."
echo "This will:"
echo "  1. Remove all existing radar notification cron jobs"
echo "  2. Create ONE new correct cron job"
echo ""

python manage.py cleanup_cron --reinstall

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "  Setup Complete!"
    echo "=========================================="
    echo ""
    echo "Verify:"
    echo "  crontab -l"
    echo ""
    echo "Monitor logs:"
    echo "  tail -f $SCRIPT_DIR/logs/notification_service.log"
    echo ""
    echo "Test email:"
    echo "  python manage.py test_summary_email"
    echo ""
else
    echo ""
    echo "✗ Setup failed. Trying alternative method..."
    echo ""
    
    # Alternative: use setup_cron_jobs command
    python manage.py setup_cron_jobs --force
    
    if [ $? -eq 0 ]; then
        echo "✓ Setup successful using alternative method"
    else
        echo "✗ Both methods failed."
        echo "  Please check:"
        echo "  1. Notification settings exist in Django admin"
        echo "  2. Notifications are enabled"
        echo "  3. cron service is running: sudo systemctl status cron"
    fi
fi

deactivate

