#!/usr/bin/env python
"""
Test script to verify email functionality
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.models import NotificationSettings
from django.core.mail import EmailMessage

def test_email_connection():
    """Test if email connection can be created"""
    try:
        # Get notification settings
        settings = NotificationSettings.objects.first()
        if not settings:
            print("❌ No notification settings found in database")
            return False
        
        print(f"✅ Found notification settings for: {settings.primary_email}")
        print(f"   SMTP Server: {settings.smtp_server}:{settings.smtp_port}")
        print(f"   Username: {settings.smtp_username}")
        print(f"   Use TLS: {settings.use_tls}")
        
        # Test connection creation
        connection = settings.get_email_connection()
        print("✅ Email connection created successfully")
        
        # Test email message creation (without sending)
        email = EmailMessage(
            subject='Test Email Connection',
            body='This is a test email to verify connection setup.',
            from_email=settings.smtp_username,
            to=[settings.primary_email],
            connection=connection,
        )
        print("✅ Email message created successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing email connection: {str(e)}")
        return False

def test_email_sending():
    """Test actual email sending (optional)"""
    try:
        settings = NotificationSettings.objects.first()
        if not settings:
            print("❌ No notification settings found")
            return False
        
        # Ask user if they want to send a test email
        response = input("\nDo you want to send a test email? (y/n): ").lower().strip()
        if response != 'y':
            print("Skipping email sending test")
            return True
        
        email = EmailMessage(
            subject='Test Email from Datalogger',
            body='This is a test email to confirm your SMTP settings are working correctly.',
            from_email=settings.smtp_username,
            to=[settings.primary_email],
            cc=settings.get_cc_emails_list(),
            connection=settings.get_email_connection(),
        )
        
        email.send()
        print("✅ Test email sent successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error sending test email: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing Email Functionality")
    print("=" * 40)
    
    # Test connection
    if test_email_connection():
        print("\n✅ Email connection test passed")
        
        # Test sending (optional)
        test_email_sending()
    else:
        print("\n❌ Email connection test failed")
        sys.exit(1) 