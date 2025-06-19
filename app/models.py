from django.db import models
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
import re
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.core.paginator import Paginator
import logging

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('manager', 'Manager'),
        ('operator', 'Operator'),
        ('viewer', 'Viewer'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Fix reverse accessor conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class SystemSettings(models.Model):
    system_name = models.CharField(max_length=100, default="Secure Login")
    login_title = models.CharField(max_length=100, default="Welcome Back")
    primary_color = models.CharField(max_length=7, default="#1a237e")
    secondary_color = models.CharField(max_length=7, default="#283593")
    accent_color = models.CharField(max_length=7, default="#3949ab")
    text_color = models.CharField(max_length=7, default="#2b2d42")
    background_color = models.CharField(max_length=7, default="#f8f9fa")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "System Settings"
        verbose_name_plural = "System Settings"

    def __str__(self):
        return f"Settings (Last updated: {self.updated_at})"

    @classmethod
    def get_settings(cls):
        settings = cls.objects.first()
        if not settings:
            settings = cls.objects.create()
        return settings

class TCPIPConfig(models.Model):
    ip_address = models.GenericIPAddressField(default='192.168.1.100')
    gateway = models.GenericIPAddressField(default='192.168.1.1')
    subnet_mask = models.GenericIPAddressField(default='255.255.255.0')
    dns = models.GenericIPAddressField(default='8.8.8.8')
    timeout = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'TCP/IP Configuration'
        verbose_name_plural = 'TCP/IP Configurations'

    def __str__(self):
        return f"TCP/IP Config - {self.ip_address}"

class TimeConfig(models.Model):
    TIMEZONE_CHOICES = [
        ('UTC', 'UTC'),
        ('EST', 'EST'),
        ('PST', 'PST'),
    ]
    DATE_FORMAT_CHOICES = [
        ('YYYY-MM-DD', 'YYYY-MM-DD'),
        ('DD-MM-YYYY', 'DD-MM-YYYY'),
        ('MM-DD-YYYY', 'MM-DD-YYYY'),
    ]
    TIME_FORMAT_CHOICES = [
        ('24h', '24-hour'),
        ('12h', '12-hour'),
    ]

    timezone = models.CharField(max_length=10, choices=TIMEZONE_CHOICES, default='UTC')
    date_format = models.CharField(max_length=10, choices=DATE_FORMAT_CHOICES, default='YYYY-MM-DD')
    time_format = models.CharField(max_length=3, choices=TIME_FORMAT_CHOICES, default='24h')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Time Configuration'
        verbose_name_plural = 'Time Configurations'

    def __str__(self):
        return f"Time Config - {self.timezone}"

class FTPConfig(models.Model):
    server = models.CharField(max_length=255, default='ftp.example.com')
    port = models.IntegerField(default=21)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    remote_directory = models.CharField(max_length=255, default='/uploads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'FTP Configuration'
        verbose_name_plural = 'FTP Configurations'

    def __str__(self):
        return f"FTP Config - {self.server}"

    def save(self, *args, **kwargs):
        # You might want to encrypt the password before saving
        # This is a simple example - use proper encryption in production
        if self.password and not self.password.startswith('encrypted:'):
            self.password = f"encrypted:{self.password}"
        super().save(*args, **kwargs)

class RadarConfig(models.Model):
    name = models.CharField(max_length=100, help_text="Name to identify this radar")
    port = models.CharField(max_length=50, help_text="Serial port (e.g., COM1, /dev/ttyUSB0)", unique=True)
    baud_rate = models.IntegerField(
        choices=[
            (9600, '9600'),
            (19200, '19200'),
            (38400, '38400'),
            (57600, '57600'),
            (115200, '115200'),
        ],
        default=9600
    )
    data_bits = models.IntegerField(
        choices=[
            (7, '7'),
            (8, '8'),
        ],
        default=8
    )
    parity = models.CharField(
        max_length=1,
        choices=[
            ('N', 'None'),
            ('E', 'Even'),
            ('O', 'Odd'),
        ],
        default='N'
    )
    stop_bits = models.IntegerField(
        choices=[
            (1, '1'),
            (2, '2'),
        ],
        default=1
    )
    update_interval = models.IntegerField(
        default=100,
        help_text="Update interval in milliseconds (min: 50ms, max: 1000ms)"
    )
    file_save_interval = models.IntegerField(
        default=5,
        help_text="Interval for saving data to files in minutes (min: 1min, max: 60min)"
    )
    data_storage_path = models.CharField(
        max_length=255,
        default='data',
        help_text="Path to store radar data files"
    )
    is_active = models.BooleanField(default=True)
    direction_positive_name = models.CharField(
        max_length=100,
        default='Towards Village',
        help_text="Name for the positive direction"
    )
    direction_negative_name = models.CharField(
        max_length=100,
        default='Towards Town',
        help_text="Name for the negative direction"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def direction_name(self):
        # Default to positive direction name for display
        return self.direction_positive_name

    class Meta:
        verbose_name = 'Radar Configuration'
        verbose_name_plural = 'Radar Configurations'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_radar_name')
        ]

    def clean(self):
        if self.update_interval < 50:
            raise ValidationError({'update_interval': 'Update interval cannot be less than 50ms'})
        if self.update_interval > 1000:
            raise ValidationError({'update_interval': 'Update interval cannot be more than 1000ms'})

    def __str__(self):
        return f"{self.name} ({self.port})"

    def save(self, *args, **kwargs):
        # Check if is_active has changed
        if self.pk:
            old_instance = RadarConfig.objects.get(pk=self.pk)
            is_active_changed = old_instance.is_active != self.is_active
        else:
            is_active_changed = True

        super().save(*args, **kwargs)
        
        # Update summary stats if active status changed
        if is_active_changed:
            SummaryStats.update_stats()

class NotificationSettings(models.Model):
    FREQUENCY_CHOICES = [
        ('hourly', 'Hourly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    primary_email = models.EmailField(
        validators=[EmailValidator()],
        help_text="Primary email address for notifications"
    )
    frequency = models.CharField(
        max_length=10,
        choices=FREQUENCY_CHOICES,
        default='daily',
        help_text="How often to send notifications"
    )
    cc_emails = models.TextField(
        blank=True,
        help_text="Comma-separated list of CC email addresses"
    )
    smtp_server = models.CharField(
        max_length=255,
        help_text="SMTP server address"
    )
    smtp_port = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(65535)],
        default=587,
        help_text="SMTP server port"
    )
    smtp_username = models.CharField(
        max_length=255,
        help_text="SMTP username"
    )
    smtp_password = models.CharField(
        max_length=255,
        help_text="SMTP password"
    )
    enable_notifications = models.BooleanField(
        default=True,
        help_text="Enable/disable email notifications"
    )
    use_tls = models.BooleanField(
        default=True,
        help_text="Use TLS for SMTP connection"
    )
    days_of_week = models.CharField(
        max_length=100,
        blank=True,
        help_text="Comma-separated days of the week (e.g., Monday,Tuesday,Friday)"
    )
    notification_times = models.CharField(
        max_length=100,
        blank=True,
        help_text="Comma-separated times in HH:MM format (e.g., 08:00,14:00)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Notification Settings"
        verbose_name_plural = "Notification Settings"

    def clean(self):
        super().clean()
        if self.cc_emails:
            emails = [email.strip() for email in self.cc_emails.split(',')]
            email_validator = EmailValidator()
            for email in emails:
                if email:  # Skip empty strings
                    try:
                        email_validator(email)
                    except:
                        raise ValidationError(f"Invalid email address in CC list: {email}")

    def __str__(self):
        return f"Notification Settings - {self.primary_email}"

    def get_cc_emails_list(self):
        """Returns a list of CC email addresses"""
        if not self.cc_emails:
            return []
        return [email.strip() for email in self.cc_emails.split(',') if email.strip()]

class ANPRConfig(models.Model):
    radar = models.ForeignKey(
        RadarConfig,
        on_delete=models.CASCADE,
        related_name='anpr_configs',
        null=True,
        blank=True,
        help_text="Associated radar for this ANPR configuration"
    )
    ip_address = models.GenericIPAddressField(
        default='192.168.1.200',
        help_text="IP address of the ANPR server"
    )
    port = models.IntegerField(
        default=8080,
        validators=[MinValueValidator(1), MaxValueValidator(65535)],
        help_text="Port number for ANPR server communication"
    )
    polling_interval = models.IntegerField(
        default=1000,
        validators=[MinValueValidator(100), MaxValueValidator(5000)],
        help_text="Interval between ANPR readings in milliseconds"
    )
    timeout = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(30)],
        help_text="Connection timeout in seconds"
    )
    endpoint = models.CharField(
        max_length=255,
        default='/api/plate',
        help_text="API endpoint for ANPR data"
    )
    api_key = models.CharField(
        max_length=255,
        blank=True,
        help_text="API key for authentication (if required)"
    )
    enable_continuous_reading = models.BooleanField(
        default=True,
        help_text="Enable continuous reading mode"
    )
    enable_logging = models.BooleanField(
        default=True,
        help_text="Enable ANPR logging"
    )
    log_path = models.CharField(
        max_length=255,
        default='logs/anpr',
        help_text="Path where ANPR logs will be stored"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ANPR Configuration'
        verbose_name_plural = 'ANPR Configurations'

    def __str__(self):
        return f"ANPR Config - {self.ip_address}:{self.port}"

    def clean(self):
        if self.polling_interval < 100:
            raise ValidationError({'polling_interval': 'Polling interval cannot be less than 100ms'})
        if self.polling_interval > 5000:
            raise ValidationError({'polling_interval': 'Polling interval cannot be more than 5000ms'})

class SystemMetrics(models.Model):
    """Model to store historical system metrics."""
    timestamp = models.DateTimeField(auto_now_add=True)
    disk_used_percent = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Disk usage percentage"
    )
    ram_used_percent = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="RAM usage percentage"
    )
    cpu_temperature = models.FloatField(
        null=True,
        blank=True,
        help_text="CPU temperature in Celsius"
    )
    uptime_seconds = models.IntegerField(
        help_text="System uptime in seconds"
    )

    class Meta:
        verbose_name = 'System Metric'
        verbose_name_plural = 'System Metrics'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['timestamp']),
        ]

    def __str__(self):
        return f"System Metrics at {self.timestamp}"

    @classmethod
    def get_latest_metrics(cls):
        """Get the most recent system metrics."""
        return cls.objects.order_by('-timestamp').first()

    @classmethod
    def get_metrics_history(cls, hours=24):
        """Get system metrics for the last specified hours."""
        cutoff_time = timezone.now() - timezone.timedelta(hours=hours)
        return cls.objects.filter(timestamp__gte=cutoff_time).order_by('timestamp')

    @classmethod
    def get_average_metrics(cls, hours=24):
        """Calculate average metrics for the last specified hours."""
        metrics = cls.get_metrics_history(hours)
        if not metrics:
            return None

        return {
            'disk_used_percent': metrics.aggregate(models.Avg('disk_used_percent'))['disk_used_percent__avg'],
            'ram_used_percent': metrics.aggregate(models.Avg('ram_used_percent'))['ram_used_percent__avg'],
            'cpu_temperature': metrics.aggregate(models.Avg('cpu_temperature'))['cpu_temperature__avg'],
        }

class RadarData(models.Model):
    radar = models.ForeignKey(RadarConfig, on_delete=models.CASCADE, related_name='data')
    timestamp = models.DateTimeField(auto_now_add=True)
    range = models.FloatField(null=True, blank=True, help_text="Range measurement in meters")
    speed = models.FloatField(null=True, blank=True, help_text="Speed measurement in km/h")
    direction = models.FloatField(null=True, blank=True, help_text="Direction in degrees")
    raw_data = models.TextField(null=True, blank=True, help_text="Raw data if parsing failed")
    status = models.CharField(max_length=20, default='success', help_text="Status of the reading")
    connection_status = models.CharField(max_length=20, default='connected', help_text="Connection status")

    class Meta:
        verbose_name = 'Radar Data'
        verbose_name_plural = 'Radar Data'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['radar', 'timestamp']),
        ]

    def __str__(self):
        return f"{self.radar.name} - {self.timestamp}"

class RadarDataFile(models.Model):
    radar = models.ForeignKey(RadarConfig, on_delete=models.CASCADE, related_name='data_files')
    filename = models.CharField(max_length=255, help_text="Name of the saved file")
    file_path = models.CharField(max_length=512, help_text="Full path to the saved file")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="When the file was saved")
    record_count = models.IntegerField(help_text="Number of records in the file")
    file_size = models.BigIntegerField(help_text="Size of the file in bytes")
    is_valid = models.BooleanField(default=True, help_text="Whether the file is valid and complete")

    class Meta:
        verbose_name = 'Radar Data File'
        verbose_name_plural = 'Radar Data Files'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['radar', 'timestamp']),
        ]

    def __str__(self):
        return f"{self.radar.name} - {self.filename} ({self.timestamp})"

class SystemInfo(models.Model):
    """Model to store system information history"""
    disk_usage = models.FloatField()
    ram_usage = models.FloatField()
    cpu_temp = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'System Info'
        verbose_name_plural = 'System Info'

    def __str__(self):
        return f"System Info at {self.timestamp}"

class RadarObjectDetection(models.Model):
    """Model to store radar object detections"""
    radar = models.ForeignKey(RadarConfig, on_delete=models.CASCADE, related_name='object_detections')
    start_time = models.DateTimeField(help_text="When the object was first detected")
    end_time = models.DateTimeField(help_text="When the object was last detected")
    min_range = models.FloatField(help_text="Minimum range during detection (meters)")
    max_range = models.FloatField(help_text="Maximum range during detection (meters)")
    avg_range = models.FloatField(help_text="Average range during detection (meters)")
    min_speed = models.FloatField(help_text="Minimum speed during detection (km/h)")
    max_speed = models.FloatField(help_text="Maximum speed during detection (km/h)")
    avg_speed = models.FloatField(help_text="Average speed during detection (km/h)")
    detection_count = models.IntegerField(help_text="Number of readings in this detection")
    raw_data = models.JSONField(help_text="All raw readings for this detection")
    anpr_detected = models.BooleanField(default=False, help_text="Whether a license plate was detected")
    license_plate = models.CharField(max_length=20, null=True, blank=True, help_text="Detected license plate number")
    email_sent = models.BooleanField(default=False, help_text="Whether notification email has been sent")
    created_at = models.DateTimeField(auto_now_add=True)
    direction_name = models.CharField(max_length=100, null=True, blank=True, help_text="Direction name for this detection")

    class Meta:
        verbose_name = 'Radar Object Detection'
        verbose_name_plural = 'Radar Object Detections'
        ordering = ['-start_time']
        indexes = [
            models.Index(fields=['radar', 'start_time']),
            models.Index(fields=['radar', 'end_time']),
        ]

    def __str__(self):
        return f"{self.radar.name} - Object {self.start_time} to {self.end_time}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        # Update summary stats when a new detection is added
        if is_new:
            SummaryStats.update_stats()

    @property
    def duration(self):
        """Calculate the duration of the detection in seconds"""
        return (self.end_time - self.start_time).total_seconds()

    @classmethod
    def get_paginated_detections(cls, radar_id, page=1, per_page=10):
        """
        Get paginated detections for a specific radar.
        
        Args:
            radar_id (int): The ID of the radar
            page (int): The page number (1-based)
            per_page (int): Number of items per page
            
        Returns:
            tuple: (paginator, page_obj) where:
                - paginator is a Django Paginator object
                - page_obj is the current page of detections
        """
        detections = cls.objects.filter(radar_id=radar_id).order_by('-start_time')
        paginator = Paginator(detections, per_page)
        page_obj = paginator.get_page(page)
        
        return paginator, page_obj

class EmailNotification(models.Model):
    """Model to track email notifications for radar detections"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
    ]

    notification_settings = models.ForeignKey(NotificationSettings, on_delete=models.CASCADE)
    start_date = models.DateTimeField(help_text="Start date of the detection period")
    end_date = models.DateTimeField(help_text="End date of the detection period")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    error_message = models.TextField(blank=True, null=True, help_text="Error message if sending failed")
    sent_at = models.DateTimeField(null=True, blank=True, help_text="When the email was sent")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Email Notification'
        verbose_name_plural = 'Email Notifications'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', 'created_at'], name='email_notif_status_created_idx'),
        ]

    def __str__(self):
        return f"Notification {self.id} - {self.status} ({self.start_date} to {self.end_date})"

    def get_detections(self):
        """Get all detections for this notification period"""
        return RadarObjectDetection.objects.filter(
            start_time__gte=self.start_date,
            end_time__lte=self.end_date
        ).order_by('start_time')

class SummaryStats(models.Model):
    """Model to store summary statistics for the dashboard"""
    total_objects = models.IntegerField(default=0, help_text="Total number of objects detected")
    active_radars = models.IntegerField(default=0, help_text="Number of active radars")
    last_detection = models.DateTimeField(null=True, blank=True, help_text="Time of the last detection")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Summary Statistics'
        verbose_name_plural = 'Summary Statistics'
        ordering = ['-timestamp']

    def __str__(self):
        return f"Summary Stats at {self.timestamp}"

    @classmethod
    def get_latest_stats(cls):
        """Get the most recent summary statistics."""
        try:
            return cls.objects.order_by('-timestamp').first()
        except Exception as e:
            logger.error(f"Error getting latest stats: {str(e)}")
            return None

    @classmethod
    def update_stats(cls):
        """Update summary statistics based on current data."""
        from django.db.models import Count, Max
        from django.utils import timezone
        from django.db import transaction

        logger = logging.getLogger(__name__)

        try:
            with transaction.atomic():
                # Get total objects detected
                total_objects = RadarObjectDetection.objects.count()

                # Get number of active radars
                active_radars = RadarConfig.objects.filter(is_active=True).count()

                # Get time of last detection
                last_detection = RadarObjectDetection.objects.aggregate(
                    last_detection=Max('end_time')
                )['last_detection']

                # Create new stats entry
                stats = cls.objects.create(
                    total_objects=total_objects,
                    active_radars=active_radars,
                    last_detection=last_detection
                )

                # Clean up old stats (keep only last 1000 entries)
                # Get IDs of records to keep
                keep_ids = cls.objects.order_by('-timestamp')[:1000].values_list('id', flat=True)
                # Delete all records except those we want to keep
                cls.objects.exclude(id__in=keep_ids).delete()

                return stats
        except Exception as e:
            logger.error(f"Error updating summary stats: {str(e)}")
            # Return the last valid stats if available
            return cls.get_latest_stats()
