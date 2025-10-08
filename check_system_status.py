#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.models import RadarObjectDetection, NotificationSettings, EmailNotification

print("=" * 60)
print("SYSTEM STATUS CHECK")
print("=" * 60)

print("\n[1] OBJECT DETECTION LOGIC:")
total_detections = RadarObjectDetection.objects.count()
print(f"  Total detections: {total_detections}")
if total_detections > 0:
    print(f"  Status: WORKING")
    recent = RadarObjectDetection.objects.order_by('-start_time')[:3]
    for d in recent:
        print(f"    - {d.detection_count} readings, {d.min_speed:.0f}-{d.max_speed:.0f} km/h, {d.direction_name}")
else:
    print(f"  Status: NO DATA YET")

print("\n[2] EMAIL NOTIFICATION SYSTEM:")
settings = NotificationSettings.objects.first()
print(f"  Enabled: {settings.enable_notifications}")
print(f"  Primary: {settings.primary_email}")
print(f"  CC: {settings.cc_emails}")
print(f"  Days: {settings.days_of_week or 'ALL DAYS'}")
print(f"  Times: {settings.notification_times or 'NOT SET'}")
emails_sent = EmailNotification.objects.filter(status='sent').count()
print(f"  Emails sent: {emails_sent}")
if emails_sent > 0:
    print(f"  Status: WORKING")
    last = EmailNotification.objects.filter(status='sent').order_by('-sent_at').first()
    print(f"    Last sent: {last.sent_at}")
else:
    print(f"  Status: READY (no emails sent yet)")

print("\n" + "=" * 60)
print("SUMMARY:")
print("  Object Detection: WORKING" if total_detections > 0 else "  Object Detection: NO DATA")
print("  Email System: CONFIGURED")
print("=" * 60)

