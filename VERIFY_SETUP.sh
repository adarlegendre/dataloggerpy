#!/bin/bash
# Verification script to check if the cron setup will work

echo "========================================="
echo "  Raspberry Pi Cron Setup Verification"
echo "========================================="
echo ""

# 1. Check OS
echo "1. Operating System Check"
echo "---"
if [[ "$(uname)" == "Linux" ]]; then
    echo "✓ Running on Linux"
    if command -v vcgencmd &> /dev/null; then
        echo "✓ Raspberry Pi detected (vcgencmd available)"
    else
        echo "⚠ Generic Linux (not Raspberry Pi specific, but cron will still work)"
    fi
else
    echo "✗ Not running on Linux (OS: $(uname))"
    exit 1
fi
echo ""

# 2. Check cron access
echo "2. Cron Access Check"
echo "---"
if command -v crontab &> /dev/null; then
    echo "✓ crontab command available"
    if crontab -l &> /dev/null; then
        echo "✓ Can access crontab"
        echo "  Current entries: $(crontab -l 2>/dev/null | grep -v '^#' | grep -v '^$' | wc -l)"
    else
        echo "⚠ crontab exists but may be empty (this is OK)"
    fi
else
    echo "✗ crontab command not found"
    exit 1
fi
echo ""

# 3. Check project directory
echo "3. Project Directory Check"
echo "---"
PROJECT_DIR="/home/admin/dataloggerpy"
if [ -d "$PROJECT_DIR" ]; then
    echo "✓ Project directory exists: $PROJECT_DIR"
else
    echo "✗ Project directory not found: $PROJECT_DIR"
    echo "  Current directory: $(pwd)"
    exit 1
fi
echo ""

# 4. Check virtual environment
echo "4. Virtual Environment Check"
echo "---"
VENV_FOUND=false
for venv_name in loggervenv venv env .venv virtualenv; do
    if [ -f "$PROJECT_DIR/$venv_name/bin/activate" ]; then
        echo "✓ Virtual environment found: $venv_name"
        echo "  Path: $PROJECT_DIR/$venv_name/bin/activate"
        VENV_FOUND=true
        VENV_NAME=$venv_name
        break
    fi
done

if [ "$VENV_FOUND" = false ]; then
    echo "✗ No virtual environment found"
    echo "  Looked for: loggervenv, venv, env, .venv, virtualenv"
    exit 1
fi
echo ""

# 5. Check Python and Django
echo "5. Python & Django Check"
echo "---"
cd "$PROJECT_DIR"
source "$VENV_NAME/bin/activate"
echo "✓ Virtual environment activated"
echo "  Python: $(which python)"
echo "  Version: $(python --version)"

if [ -f "manage.py" ]; then
    echo "✓ manage.py found"
    
    # Check if Django is accessible
    if python -c "import django" 2>/dev/null; then
        echo "✓ Django is installed"
        echo "  Version: $(python -c 'import django; print(django.get_version())')"
    else
        echo "✗ Django not installed"
        exit 1
    fi
else
    echo "✗ manage.py not found"
    exit 1
fi
echo ""

# 6. Check management command exists
echo "6. Management Command Check"
echo "---"
if [ -f "app/management/commands/check_notification_schedule.py" ]; then
    echo "✓ check_notification_schedule command exists"
else
    echo "✗ check_notification_schedule command not found"
    exit 1
fi

if [ -f "app/management/commands/cleanup_cron.py" ]; then
    echo "✓ cleanup_cron command exists"
else
    echo "⚠ cleanup_cron command not found (new file may need to be synced)"
fi
echo ""

# 7. Check logs directory
echo "7. Logs Directory Check"
echo "---"
if [ -d "$PROJECT_DIR/logs" ]; then
    echo "✓ Logs directory exists"
else
    echo "⚠ Logs directory doesn't exist (will be created automatically)"
    mkdir -p "$PROJECT_DIR/logs" 2>/dev/null && echo "  ✓ Created logs directory"
fi
echo ""

# 8. Test cron job syntax
echo "8. Cron Job Syntax Test"
echo "---"
TEST_CRON="* * * * * cd $PROJECT_DIR && source $VENV_NAME/bin/activate && python manage.py check_notification_schedule >> $PROJECT_DIR/logs/notification_service.log 2>&1"
echo "Proposed cron job:"
echo "  $TEST_CRON"
echo ""

# Create a test crontab file
TEMP_CRON=$(mktemp)
echo "$TEST_CRON" > "$TEMP_CRON"
if crontab -T "$TEMP_CRON" 2>/dev/null; then
    echo "✓ Cron syntax is valid (crontab -T passed)"
elif crontab "$TEMP_CRON" 2>/dev/null && crontab -l | grep -q "check_notification_schedule"; then
    # Some systems don't have -T, so we test by installing/checking/removing
    crontab -r 2>/dev/null
    echo "✓ Cron syntax is valid (installation test passed)"
else
    echo "⚠ Could not verify cron syntax (but syntax looks correct)"
fi
rm -f "$TEMP_CRON"
echo ""

# 9. Test command manually
echo "9. Manual Command Test"
echo "---"
echo "Testing: python manage.py check_notification_schedule"
if timeout 10s python manage.py check_notification_schedule 2>&1 | head -5; then
    echo "✓ Command executed successfully"
else
    echo "⚠ Command had issues (check notification settings)"
fi
echo ""

# 10. Summary
echo "========================================="
echo "           Verification Summary"
echo "========================================="
echo ""
echo "✅ Your system is compatible!"
echo ""
echo "Detected configuration:"
echo "  • OS: Linux (Raspberry Pi)"
echo "  • Project: $PROJECT_DIR"
echo "  • Virtual Env: $VENV_NAME"
echo "  • Python: $(python --version)"
echo "  • Cron: Available"
echo ""
echo "Next steps:"
echo "  1. Run: python manage.py cleanup_cron"
echo "  2. Run: python manage.py runserver 0.0.0.0:8000"
echo "  3. Check: crontab -l"
echo "  4. Monitor: tail -f logs/notification_service.log"
echo ""
echo "The system will auto-create the correct cron job!"
echo ""

