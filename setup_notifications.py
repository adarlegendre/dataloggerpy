#!/usr/bin/env python
"""
Cross-platform notification setup script
Automatically detects the platform and sets up the appropriate scheduling method
"""

import os
import sys
import platform
import subprocess
from pathlib import Path

def setup_windows():
    """Set up Windows notification system"""
    print("🔧 Setting up Windows notification system...")
    
    # Check if PowerShell script exists
    ps_script = Path(__file__).parent / "setup_windows_tasks.ps1"
    if ps_script.exists():
        print("📋 Found Windows Task Scheduler setup script")
        print("💡 To set up Windows Task Scheduler, run as Administrator:")
        print(f"   powershell -ExecutionPolicy Bypass -File {ps_script}")
        print()
    
    # Check if Windows Service is available
    service_file = Path(__file__).parent / "notification_service.py"
    if service_file.exists():
        print("🔧 Found Windows Service implementation")
        print("💡 To install the Windows Service, run as Administrator:")
        print(f"   python {service_file} install")
        print(f"   python {service_file} start")
        print()
    
    print("✅ Windows notification system setup information provided")
    print("📝 Choose one of the following methods:")
    print("   1. Windows Task Scheduler (recommended for development)")
    print("   2. Windows Service (recommended for production)")
    print()

def setup_unix():
    """Set up Unix/Linux notification system"""
    print("🔧 Setting up Unix/Linux notification system...")
    
    # Check if bash script exists
    bash_script = Path(__file__).parent / "setup_cron.sh"
    if bash_script.exists():
        print("📋 Found Unix cron setup script")
        print("💡 To set up cron jobs, run:")
        print(f"   chmod +x {bash_script}")
        print(f"   {bash_script}")
        print()
    
    # Try to set up cron jobs directly
    try:
        print("🔧 Attempting to set up cron jobs directly...")
        # Import Django settings
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
        
        import django
        django.setup()
        
        from app.utils.system_utils import setup_email_cron_jobs
        
        if setup_email_cron_jobs():
            print("✅ Cron jobs set up successfully!")
        else:
            print("⚠️  Cron jobs setup failed, but you can still use the bash script")
    except Exception as e:
        print(f"⚠️  Could not set up cron jobs directly: {e}")
        print("💡 Use the bash script instead")
    
    print()

def check_dependencies():
    """Check if required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8+ is required")
        return False
    
    print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Check Django
    try:
        import django
        print(f"✅ Django {django.get_version()}")
    except ImportError:
        print("❌ Django not found")
        return False
    
    # Check python-crontab (for Unix systems)
    if platform.system() != 'Windows':
        try:
            import crontab
            print("✅ python-crontab available")
        except ImportError:
            print("⚠️  python-crontab not found (will use bash script)")
    
    # Check pywin32 (for Windows systems)
    if platform.system() == 'Windows':
        try:
            import win32serviceutil
            print("✅ pywin32 available")
        except ImportError:
            print("⚠️  pywin32 not found (Windows Service not available)")
    
    print()
    return True

def check_notification_settings():
    """Check if notification settings are configured"""
    print("🔍 Checking notification settings...")
    
    try:
        # Import Django settings
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
        
        import django
        django.setup()
        
        from app.models import NotificationSettings
        
        settings = NotificationSettings.objects.first()
        if settings:
            print(f"✅ Notification settings found for: {settings.primary_email}")
            print(f"   Frequency: {settings.frequency}")
            print(f"   SMTP Server: {settings.smtp_server}")
            print(f"   Enabled: {settings.enable_notifications}")
        else:
            print("⚠️  No notification settings found")
            print("💡 Configure notification settings in the Django admin or web interface")
        
    except Exception as e:
        print(f"⚠️  Could not check notification settings: {e}")
    
    print()

def main():
    """Main setup function"""
    print("🚀 Radar Notification System Setup")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Setup failed due to missing dependencies")
        sys.exit(1)
    
    # Check notification settings
    check_notification_settings()
    
    # Detect platform and set up accordingly
    system = platform.system()
    print(f"🖥️  Detected platform: {system}")
    
    if system == 'Windows':
        setup_windows()
    else:
        setup_unix()
    
    print("🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("   1. Configure notification settings in the web interface")
    print("   2. Set up the scheduling method for your platform")
    print("   3. Test the email functionality")
    print("\n📚 For more information, check the README.md file")

if __name__ == "__main__":
    main() 