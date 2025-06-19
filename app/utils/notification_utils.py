import json
import os
from datetime import datetime, time
from django.conf import settings
from django.core.mail import EmailMessage
from ..models import EmailNotification, RadarObjectDetection, NotificationSettings, RadarDataFile

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
        
        # Create email message
        email = EmailMessage(
            subject=subject,
            body=f"Please find attached the radar detection report for the period {notification.start_date} to {notification.end_date}.",
            from_email=settings.smtp_username,
            to=[settings.primary_email],
            cc=settings.get_cc_emails_list(),
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
        
        # Create email message
        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=notification_settings.smtp_username,
            to=[notification_settings.primary_email],
            cc=notification_settings.get_cc_emails_list(),
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