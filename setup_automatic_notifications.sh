#!/bin/bash

# Radar Notification System - Automatic Setup Script
# This script sets up automatic cron job configuration for the notification system

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get the project directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}🚀 Radar Notification System - Automatic Setup${NC}"
echo -e "${BLUE}==============================================${NC}"
echo ""

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if running as root
if [[ $EUID -eq 0 ]]; then
    print_warning "Running as root. This is required for cron setup."
else
    print_error "This script must be run as root to set up cron jobs."
    print_info "Please run: sudo $0"
    exit 1
fi

# Check if Python and Django are available
print_info "Checking Python and Django installation..."

if ! command -v python3 &> /dev/null; then
    print_error "Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "$PROJECT_DIR/venv" ]; then
    print_error "Virtual environment not found at $PROJECT_DIR/venv"
    print_info "Please create a virtual environment first:"
    print_info "  python3 -m venv venv"
    print_info "  source venv/bin/activate"
    print_info "  pip install -r requirements.txt"
    exit 1
fi

print_status "Python and virtual environment found"

# Create logs directory
print_info "Creating logs directory..."
mkdir -p "$PROJECT_DIR/logs"
chmod 755 "$PROJECT_DIR/logs"
print_status "Logs directory created"

# Test Django setup
print_info "Testing Django setup..."
cd "$PROJECT_DIR"
source venv/bin/activate

# Test if Django can be imported
if ! python3 -c "import django; print('Django version:', django.get_version())" 2>/dev/null; then
    print_error "Django is not properly installed in the virtual environment."
    exit 1
fi

print_status "Django is properly installed"

# Test cron access
print_info "Testing cron access..."
if ! crontab -l &>/dev/null; then
    print_error "Cannot access crontab. Please ensure cron is installed and running."
    print_info "On Ubuntu/Debian: sudo apt-get install cron"
    print_info "On CentOS/RHEL: sudo yum install cronie"
    exit 1
fi

print_status "Cron access confirmed"

# Run the startup script
print_info "Setting up notification cron jobs..."
if python3 startup_cron_setup.py; then
    print_status "Cron jobs configured successfully"
else
    print_error "Failed to configure cron jobs"
    exit 1
fi

# Create systemd service file
print_info "Creating systemd service for automatic startup..."

SERVICE_FILE="/etc/systemd/system/radar-notification.service"
SERVICE_CONTENT="[Unit]
Description=Radar Notification System
After=network.target
Wants=network.target

[Service]
Type=oneshot
User=root
WorkingDirectory=$PROJECT_DIR
ExecStart=$PROJECT_DIR/venv/bin/python $PROJECT_DIR/startup_cron_setup.py
RemainAfterExit=yes
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target"

echo "$SERVICE_CONTENT" | sudo tee "$SERVICE_FILE" > /dev/null

# Enable and start the service
print_info "Enabling systemd service..."
systemctl daemon-reload
systemctl enable radar-notification.service
systemctl start radar-notification.service

if systemctl is-active --quiet radar-notification.service; then
    print_status "Systemd service enabled and started"
else
    print_warning "Systemd service failed to start, but cron jobs should still work"
fi

# Set up log rotation
print_info "Setting up log rotation..."
LOG_ROTATE_FILE="/etc/logrotate.d/radar-notification"
LOG_ROTATE_CONTENT="$PROJECT_DIR/logs/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    create 644 root root
}"

echo "$LOG_ROTATE_CONTENT" | sudo tee "$LOG_ROTATE_FILE" > /dev/null
print_status "Log rotation configured"

# Create a manual setup script
print_info "Creating manual setup script..."
MANUAL_SCRIPT="$PROJECT_DIR/manual_cron_setup.sh"
cat > "$MANUAL_SCRIPT" << 'EOF'
#!/bin/bash
# Manual cron setup script for radar notifications

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"
source venv/bin/activate

echo "Setting up cron jobs manually..."
python3 startup_cron_setup.py

echo "Current cron jobs:"
crontab -l | grep -A 5 -B 5 "Radar Notification Service" || echo "No radar notification cron jobs found"
EOF

chmod +x "$MANUAL_SCRIPT"
print_status "Manual setup script created: $MANUAL_SCRIPT"

# Final status check
print_info "Performing final status check..."

# Check if cron job is installed
if crontab -l 2>/dev/null | grep -q "check_notification_schedule"; then
    print_status "Cron job is installed and active"
else
    print_warning "Cron job not found. You may need to configure notification settings first."
fi

# Show current cron jobs
echo ""
print_info "Current cron jobs:"
crontab -l 2>/dev/null | grep -A 5 -B 5 "Radar Notification Service" || echo "No radar notification cron jobs found"

echo ""
print_status "Setup completed successfully!"
echo ""
print_info "What was configured:"
echo "  • Cron job that runs every minute to check notification schedule"
echo "  • Systemd service for automatic startup"
echo "  • Log rotation for notification logs"
echo "  • Manual setup script for troubleshooting"
echo ""
print_info "Next steps:"
echo "  1. Configure notification settings in the web interface"
echo "  2. Test the notification system"
echo "  3. Monitor logs at: $PROJECT_DIR/logs/notification_service.log"
echo ""
print_info "Useful commands:"
echo "  • Check cron status: crontab -l"
echo "  • View logs: tail -f $PROJECT_DIR/logs/notification_service.log"
echo "  • Manual setup: $MANUAL_SCRIPT"
echo "  • Service status: systemctl status radar-notification.service"
echo ""
print_info "The system will now automatically:"
echo "  • Set up cron jobs when the system starts"
echo "  • Configure cron jobs when notification settings are saved"
echo "  • Remove cron jobs when notifications are disabled"
echo "  • Log all activity for monitoring" 