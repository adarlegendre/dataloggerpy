#!/bin/bash
# Check which dates have detection data available

cd /home/admin/dataloggerpy
source loggervenv/bin/activate

echo "========================================"
echo "  Detection Data Availability Report"
echo "========================================"
echo ""

python manage.py shell << 'EOF'
from app.models import Detection, RadarObjectDetection, NotificationSettings
from django.utils import timezone
from django.db.models import Count, Min, Max
from datetime import datetime, timedelta

print("1. CURRENT EMAIL SETTINGS")
print("-" * 40)
settings = NotificationSettings.objects.first()
if settings:
    print(f"To: {settings.primary_email}")
    print(f"CC: {settings.cc_emails or 'Not configured'}")
else:
    print("⚠ No notification settings found")

print("\n2. DETECTION DATA BY DATE")
print("-" * 40)

# Check Detection model
detections_by_date = Detection.objects.extra(
    select={'date': 'DATE(start_time)'}
).values('date').annotate(
    count=Count('id')
).order_by('-date')[:14]  # Last 14 days

if detections_by_date:
    print("\nDetection Model (Last 14 days):")
    for entry in detections_by_date:
        date_str = entry['date'].strftime('%Y-%m-%d %A') if hasattr(entry['date'], 'strftime') else str(entry['date'])
        print(f"  {date_str}: {entry['count']} detections")
else:
    print("\n⚠ No detections found in Detection model")

# Check RadarObjectDetection model
radar_by_date = RadarObjectDetection.objects.extra(
    select={'date': 'DATE(start_time)'}
).values('date').annotate(
    count=Count('id')
).order_by('-date')[:14]  # Last 14 days

if radar_by_date:
    print("\nRadarObjectDetection Model (Last 14 days):")
    for entry in radar_by_date:
        date_str = entry['date'].strftime('%Y-%m-%d %A') if hasattr(entry['date'], 'strftime') else str(entry['date'])
        print(f"  {date_str}: {entry['count']} detections")
else:
    print("\n⚠ No detections found in RadarObjectDetection model")

# Get date range
print("\n3. DATA RANGE SUMMARY")
print("-" * 40)

first_detection = Detection.objects.order_by('start_time').first()
last_detection = Detection.objects.order_by('-start_time').first()

if first_detection and last_detection:
    print(f"First detection: {first_detection.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Last detection:  {last_detection.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total detections: {Detection.objects.count()}")
else:
    print("⚠ No detection data available")

first_radar = RadarObjectDetection.objects.order_by('start_time').first()
last_radar = RadarObjectDetection.objects.order_by('-start_time').first()

if first_radar and last_radar:
    print(f"\nRadar First: {first_radar.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Radar Last:  {last_radar.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total radar detections: {RadarObjectDetection.objects.count()}")

# Suggest a test date
print("\n4. SUGGESTED TEST DATES")
print("-" * 40)

if last_detection:
    test_date = last_detection.start_time.date()
    print(f"✓ Test with this date (has data): {test_date}")
    print(f"  Command: python manage.py test_summary_email --date {test_date}")
elif last_radar:
    test_date = last_radar.start_time.date()
    print(f"✓ Test with this date (has data): {test_date}")
    print(f"  Command: python manage.py test_summary_email --date {test_date}")
else:
    print("⚠ No detection data available for testing")
    print("  Create some test detections first or wait for real data")

EOF

echo ""
echo "========================================"
echo "  Report Complete"
echo "========================================"
echo ""

deactivate

