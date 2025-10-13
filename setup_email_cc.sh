#!/bin/bash
# Setup CC email for notifications

cd /home/admin/dataloggerpy
source loggervenv/bin/activate

echo "========================================"
echo "  Setup Email CC (Carbon Copy)"
echo "========================================"
echo ""

echo "Current notification settings:"
echo ""

python manage.py shell << 'EOF'
from app.models import NotificationSettings

settings = NotificationSettings.objects.first()
if settings:
    print(f"Primary Email: {settings.primary_email}")
    print(f"Current CC: {settings.cc_emails or 'Not set'}")
    print("")
    
    # Check if CC emails field already has email addresses
    if settings.cc_emails:
        print(f"✓ CC emails already configured: {settings.cc_emails}")
        print("  No changes needed.")
        print("")
        print("To modify CC emails, go to Django admin:")
        print("  http://your-ip:8000/admin/app/notificationsettings/")
    else:
        print("⚠ No CC emails configured")
        print("")
        print("To add CC emails, you can either:")
        print("  1. Update in Django admin: http://your-ip:8000/admin/app/notificationsettings/")
        print("  2. Or update now via shell (enter full email addresses)")
        print("")
        print("Example CC emails format: email1@domain.com, email2@domain.com")
    
    # Show current settings
    print("\nCurrent Email Settings:")
    print(f"  To: {settings.primary_email}")
    print(f"  CC: {settings.cc_emails}")
else:
    print("✗ No notification settings found")
    print("  Create settings in Django admin first")
EOF

echo ""
echo "========================================"
echo "  CC Setup Complete"
echo "========================================"
echo ""

deactivate

