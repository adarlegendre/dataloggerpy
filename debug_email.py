#!/usr/bin/env python
"""
Detailed email debugging script
"""
import os
import sys
import django
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.models import NotificationSettings

def test_email_delivery():
    """Test email delivery with detailed logging"""
    print("🔍 Email Delivery Debug Test")
    print("=" * 50)
    
    # Get notification settings
    settings = NotificationSettings.objects.first()
    if not settings:
        print("❌ No notification settings found")
        return
    
    print(f"📧 Primary Email: {settings.primary_email}")
    print(f"📧 SMTP Server: {settings.smtp_server}:{settings.smtp_port}")
    print(f"📧 SMTP Username: {settings.smtp_username}")
    print(f"📧 Use TLS: {settings.use_tls}")
    print()
    
    # Test SMTP connection
    print("🔌 Testing SMTP Connection...")
    try:
        if settings.use_tls:
            server = smtplib.SMTP(settings.smtp_server, settings.smtp_port)
            server.starttls()
        else:
            server = smtplib.SMTP(settings.smtp_server, settings.smtp_port)
        
        print("✅ SMTP connection established")
        
        # Login
        print("🔐 Attempting login...")
        server.login(settings.smtp_username, settings.smtp_password)
        print("✅ SMTP login successful")
        
        # Create test email
        msg = MIMEMultipart()
        msg['From'] = settings.smtp_username
        msg['To'] = settings.primary_email
        msg['Subject'] = "🔍 Email Delivery Test - Datalogger"
        
        body = f"""
        This is a test email to verify email delivery.
        
        Test Details:
        - From: {settings.smtp_username}
        - To: {settings.primary_email}
        - SMTP Server: {settings.smtp_server}:{settings.smtp_port}
        - TLS: {settings.use_tls}
        - Timestamp: {django.utils.timezone.now()}
        
        If you receive this email, the email system is working correctly.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        print("📤 Sending test email...")
        text = msg.as_string()
        server.sendmail(settings.smtp_username, settings.primary_email, text)
        print("✅ Email sent successfully!")
        print(f"📧 From: {settings.smtp_username}")
        print(f"📧 To: {settings.primary_email}")
        print(f"📧 Subject: {msg['Subject']}")
        print(f"📧 Body: {body[:100]}{'...' if len(body) > 100 else ''}")
        
        server.quit()
        
        print("\n📋 Troubleshooting Steps:")
        print("1. Check your email inbox at:", settings.primary_email)
        print("2. Check SPAM/JUNK folder")
        print("3. Check Gmail's 'All Mail' folder")
        print("4. Check Gmail's 'Promotions' tab")
        print("5. Verify the email address is correct")
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ SMTP Authentication Error: {e}")
        print("💡 This usually means the app password is incorrect")
    except smtplib.SMTPRecipientsRefused as e:
        print(f"❌ Recipient Refused: {e}")
        print("💡 The email address might be invalid")
    except smtplib.SMTPServerDisconnected as e:
        print(f"❌ Server Disconnected: {e}")
        print("💡 Check your internet connection")
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"💡 Error type: {type(e).__name__}")

def check_gmail_settings():
    """Provide Gmail-specific troubleshooting tips"""
    print("\n📧 Gmail-Specific Troubleshooting:")
    print("=" * 40)
    print("1. Check if 2-Factor Authentication is enabled")
    print("2. Verify you're using an App Password (not your regular password)")
    print("3. Check Gmail's 'Less secure app access' settings")
    print("4. Look in Gmail's 'All Mail' folder")
    print("5. Check Gmail's 'Promotions' tab")
    print("6. Add the sender to your contacts")
    print("7. Check Gmail's filters and forwarding settings")

if __name__ == "__main__":
    test_email_delivery()
    check_gmail_settings() 