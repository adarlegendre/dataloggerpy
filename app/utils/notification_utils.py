import json
import os
from datetime import datetime, time, timedelta
from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models import Count, Q
from django.utils import timezone
from ..models import EmailNotification, RadarObjectDetection, NotificationSettings, RadarDataFile, RadarConfig

def generate_json_report(detections):
    """Generate a JSON report from radar detections"""
    data = []
    for detection in detections:
        data.append({
            'id': detection.id,
            'radar': detection.radar.name,
            'start_time': detection.start_time.isoformat(),
            'end_time': detection.end_time.isoformat(),
            'min_range': detection.min_range,
            'max_range': detection.max_range,
            'avg_range': detection.avg_range,
            'min_speed': detection.min_speed,
            'max_speed': detection.max_speed,
            'avg_speed': detection.avg_speed,
            'detection_count': detection.detection_count,
            'anpr_detected': detection.anpr_detected,
            'license_plate': detection.license_plate,
        })
    
    return json.dumps(data, indent=2)

def send_notification_email(notification):
    """Send email notification with radar detection reports"""
    try:
        settings = notification.notification_settings
        detections = notification.get_detections()
        
        if not detections.exists():
            notification.status = 'failed'
            notification.error_message = "No detections found for the specified period"
            notification.save()
            return False
        
        # Generate JSON report
        json_data = generate_json_report(detections)
        
        # Create email
        subject = f"Radar Detection Report - {notification.start_date.strftime('%Y-%m-%d')} to {notification.end_date.strftime('%Y-%m-%d')}"
        
        # Create email message with custom connection
        email = EmailMessage(
            subject=subject,
            body=f"Please find attached the radar detection report for the period {notification.start_date} to {notification.end_date}.",
            from_email=settings.smtp_username,
            to=[settings.primary_email],
            cc=settings.get_cc_emails_list(),
            connection=settings.get_email_connection(),
        )
        
        # Attach JSON report
        email.attach('radar_detections.json', json_data, 'application/json')
        
        # Send email
        email.send()
        
        # Update notification status
        notification.status = 'sent'
        notification.sent_at = datetime.now()
        notification.save()
        
        # Mark detections as email sent
        detections.update(email_sent=True)
        
        return True
        
    except Exception as e:
        notification.status = 'failed'
        notification.error_message = str(e)
        notification.save()
        return False

def process_pending_notifications():
    """Process all pending email notifications"""
    pending_notifications = EmailNotification.objects.filter(status='pending')
    
    for notification in pending_notifications:
        send_notification_email(notification)

def create_notification(start_date, end_date, notification_settings=None):
    """
    Create a new email notification for radar detections.
    
    Args:
        start_date (datetime): Start date of the detection period
        end_date (datetime): End date of the detection period
        notification_settings (NotificationSettings, optional): Notification settings to use.
            If not provided, will use the first available settings.
    
    Returns:
        EmailNotification: The created notification instance
    """
    if notification_settings is None:
        notification_settings = NotificationSettings.objects.first()
        if not notification_settings:
            raise ValueError("No notification settings found. Please configure notification settings first.")
    
    notification = EmailNotification.objects.create(
        notification_settings=notification_settings,
        start_date=start_date,
        end_date=end_date,
        status='pending'
    )
    
    return notification

def create_notification_for_today():
    """
    Create a notification for today's detections.
    
    Returns:
        EmailNotification: The created notification instance
    """
    today = datetime.now().date()
    start_date = datetime.combine(today, time.min)
    end_date = datetime.combine(today, time.max)
    
    return create_notification(start_date, end_date)

def create_notification_for_date_range(start_date, end_date):
    """
    Create a notification for a specific date range.
    
    Args:
        start_date (date): Start date
        end_date (date): End date
    
    Returns:
        EmailNotification: The created notification instance
    """
    start_datetime = datetime.combine(start_date, time.min)
    end_datetime = datetime.combine(end_date, time.max)
    
    return create_notification(start_datetime, end_datetime)

def generate_daily_summary_report(start_date, end_date):
    """
    Generate a daily summary report of radar detections grouped by radar and direction.
    
    Args:
        start_date (datetime): Start date/time for the report
        end_date (datetime): End date/time for the report
    
    Returns:
        list: List of radar summary dictionaries
    """
    summary_data = []
    
    # Get all active radars
    radars = RadarConfig.objects.filter(is_active=True)
    
    for radar in radars:
        # Get all detections for this radar in the date range
        detections = RadarObjectDetection.objects.filter(
            radar=radar,
            start_time__gte=start_date,
            start_time__lt=end_date
        )
        
        total_detections = detections.count()
        
        # Skip radar if no detections
        if total_detections == 0:
            continue
        
        # Count ANPR detections
        anpr_detections = detections.filter(anpr_detected=True).count()
        
        # Get the most recent detection datetime for this radar
        latest_detection = detections.order_by('-start_time').first()
        detection_datetime = latest_detection.start_time.isoformat() if latest_detection else start_date.isoformat()
        
        # Build direction statistics
        directions = []
        
        # Direction: Positive
        if radar.direction_id_positive and radar.direction_positive_name:
            positive_detections = detections.filter(
                Q(direction_name=radar.direction_positive_name) | Q(direction_name__isnull=True)
            )
            positive_count = positive_detections.count()
            positive_anpr = positive_detections.filter(anpr_detected=True).count()
            
            if positive_count > 0:
                directions.append({
                    "id": radar.direction_id_positive,
                    "name": radar.direction_positive_name,
                    "detections": positive_count,
                    "detections_ANPR": positive_anpr
                })
        
        # Direction: Negative
        if radar.direction_id_negative and radar.direction_negative_name:
            negative_detections = detections.filter(direction_name=radar.direction_negative_name)
            negative_count = negative_detections.count()
            negative_anpr = negative_detections.filter(anpr_detected=True).count()
            
            if negative_count > 0:
                directions.append({
                    "id": radar.direction_id_negative,
                    "name": radar.direction_negative_name,
                    "detections": negative_count,
                    "detections_ANPR": negative_anpr
                })
        
        # Build radar summary
        radar_summary = {
            "IMR_AD": radar.imr_ad or "",
            "name": radar.name,
            "route": radar.route or "",
            "datetime": detection_datetime,
            "lat": radar.latitude if radar.latitude else 0.0,
            "lon": radar.longitude if radar.longitude else 0.0,
            "detections": total_detections,
            "detections_ANPR": anpr_detections,
            "directions": directions
        }
        
        summary_data.append(radar_summary)
    
    return summary_data


def send_daily_summary_email(start_date, end_date, notification_settings=None):
    """
    Send a daily summary email with aggregated detection data.
    
    Args:
        start_date (datetime): Start date/time for the report
        end_date (datetime): End date/time for the report
        notification_settings (NotificationSettings, optional): Notification settings to use.
            If not provided, will use the first available settings.
    
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    try:
        if notification_settings is None:
            notification_settings = NotificationSettings.objects.first()
            if not notification_settings:
                raise ValueError("No notification settings found. Please configure notification settings first.")
        
        # Generate summary report
        summary_data = generate_daily_summary_report(start_date, end_date)
        
        if not summary_data:
            print("No detection data available for the specified period")
            return False
        
        # Convert to JSON
        json_data = json.dumps(summary_data, indent=2)
        
        # Create email subject with date
        date_str = start_date.strftime('%Y-%m-%d')
        subject = f"Daily Radar Detection Summary - {date_str}"
        
        # Create email body
        total_detections = sum(radar['detections'] for radar in summary_data)
        total_anpr = sum(radar['detections_ANPR'] for radar in summary_data)
        body = f"""Daily Radar Detection Summary Report

Date: {date_str}
Report Period: {start_date.strftime('%Y-%m-%d %H:%M')} to {end_date.strftime('%Y-%m-%d %H:%M')}

Summary:
- Total Radars with Detections: {len(summary_data)}
- Total Detections: {total_detections}
- Total ANPR Detections: {total_anpr}

Please find the detailed detection data attached as JSON.
"""
        
        # Create email message with custom connection
        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=notification_settings.smtp_username,
            to=[notification_settings.primary_email],
            cc=notification_settings.get_cc_emails_list(),
            connection=notification_settings.get_email_connection(),
        )
        
        # Attach JSON report
        filename = f"radar_summary_{date_str}.json"
        email.attach(filename, json_data, 'application/json')
        
        # Send email
        email.send()
        
        print(f"Daily summary email sent successfully to {notification_settings.primary_email}")
        return True
        
    except Exception as e:
        print(f"Error sending daily summary email: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def send_json_files(json_file_paths, subject=None, body=None, notification_settings=None):
    """
    Send JSON files via email.
    
    Args:
        json_file_paths (list): List of paths to JSON files to send
        subject (str, optional): Email subject. Defaults to "JSON Data Files"
        body (str, optional): Email body text. Defaults to a generic message
        notification_settings (NotificationSettings, optional): Notification settings to use.
            If not provided, will use the first available settings.
    
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    try:
        if notification_settings is None:
            notification_settings = NotificationSettings.objects.first()
            if not notification_settings:
                raise ValueError("No notification settings found. Please configure notification settings first.")
        
        # Set default subject and body if not provided
        if subject is None:
            subject = "JSON Data Files"
        if body is None:
            body = "Please find attached the JSON data files."
        
        # Create email message with custom connection
        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=notification_settings.smtp_username,
            to=[notification_settings.primary_email],
            cc=notification_settings.get_cc_emails_list(),
            connection=notification_settings.get_email_connection(),
        )
        
        # Get RadarDataFile objects for the files
        data_files = []
        
        # Attach JSON files and collect RadarDataFile objects
        for file_path in json_file_paths:
            try:
                with open(file_path, 'r') as f:
                    json_content = f.read()
                    filename = os.path.basename(file_path)
                    email.attach(filename, json_content, 'application/json')
                    
                    # Find the corresponding RadarDataFile object
                    data_file = RadarDataFile.objects.filter(file_path=file_path).first()
                    if data_file:
                        data_files.append(data_file)
            except Exception as e:
                raise ValueError(f"Error reading JSON file {file_path}: {str(e)}")
        
        # Send email
        email.send()
        
        # Mark files as sent
        for data_file in data_files:
            data_file.email_sent = True
            data_file.save()
            
        return True
        
    except Exception as e:
        print(f"Error sending JSON files via email: {str(e)}")
        return False 