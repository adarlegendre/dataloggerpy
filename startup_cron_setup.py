#!/usr/bin/env python
"""
Startup script to automatically set up cron jobs based on notification settings
This should be run when the software starts to ensure cron jobs are properly configured.
"""
import os
import sys
import django

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.core.management import call_command
from app.models import NotificationSettings
from app.utils.cron_manager import cron_manager

def setup_cron_on_startup():
    """Set up cron jobs when the software starts"""
    print("🚀 Setting up cron jobs on startup...")
    
    # Check if we have access to crontab
    if not cron_manager.test_cron_access():
        print("⚠️  No access to crontab. Make sure you have appropriate permissions.")
        print("   You may need to run this script with sudo or as a user with crontab access.")
        return False
    
    # Get notification settings
    settings = NotificationSettings.objects.first()
    
    if not settings:
        print("⚠️  No notification settings found.")
        print("   Please configure notifications in the web interface first.")
        return False
    
    print(f"📧 Found notification settings for: {settings.primary_email}")
    print(f"📅 Frequency: {settings.frequency}")
    print(f"📅 Days: {settings.days_of_week or 'All days'}")
    print(f"⏰ Times: {settings.notification_times or 'Any time'}")
    print(f"🔧 Enabled: {settings.enable_notifications}")
    
    if not settings.enable_notifications:
        print("📧 Notifications are disabled, removing any existing cron jobs...")
        success = cron_manager.remove_notification_cron()
        if success:
            print("✅ Successfully removed notification cron jobs")
        else:
            print("❌ Failed to remove notification cron jobs")
        return success
    
    # Set up cron job
    print("🔧 Setting up notification cron job...")
    success = cron_manager.setup_notification_cron(settings)
    
    if success:
        print("✅ Successfully set up notification cron job")
        
        # Show the status
        status = cron_manager.get_cron_status()
        if status['installed']:
            print(f"📋 Cron job: {status['cron_job']}")
            print(f"📄 Log file: {status['log_file']}")
        
        print("\n🎯 The notification system is now configured to:")
        print(f"   • Run every minute to check if notifications should be sent")
        print(f"   • Send {settings.frequency} notifications to {settings.primary_email}")
        if settings.days_of_week:
            print(f"   • Only send on: {settings.days_of_week}")
        if settings.notification_times:
            print(f"   • Only send at: {settings.notification_times}")
        print(f"   • Log all activity to: {status['log_file']}")
        
    else:
        print("❌ Failed to set up notification cron job")
    
    return success

def check_cron_status():
    """Check the current status of cron jobs"""
    print("\n🔍 Checking cron job status...")
    
    status = cron_manager.get_cron_status()
    
    if status['installed']:
        print("✅ Notification cron job is installed")
        print(f"📋 Job: {status['cron_job']}")
        print(f"📄 Log: {status['log_file']}")
        
        # Check if log file exists
        if os.path.exists(status['log_file']):
            print("✅ Log file exists")
        else:
            print("⚠️  Log file does not exist yet")
    else:
        print("❌ No notification cron job found")
    
    return status['installed']

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Radar Notification System - Cron Setup")
    print("=" * 60)
    
    # Set up cron jobs
    success = setup_cron_on_startup()
    
    # Check status
    check_cron_status()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ Startup cron setup completed successfully!")
    else:
        print("❌ Startup cron setup encountered issues.")
        print("   Check the messages above for details.")
    print("=" * 60) 