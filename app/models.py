from django.db import models
from django.db.models import Max
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

class DisplayConfig(models.Model):
    """Model for CP5200 VMS Display Settings"""
    ip_address = models.GenericIPAddressField(
        default='192.168.1.222',
        help_text="IP address of the display device"
    )
    port = models.IntegerField(
        default=8080,
        validators=[MinValueValidator(1), MaxValueValidator(65535)],
        help_text="Port number for display communication"
    )
    font_size = models.IntegerField(
        default=16,
        validators=[MinValueValidator(8), MaxValueValidator(72)],
        help_text="Font size for display text"
    )
    effect_type = models.CharField(
        max_length=20,
        default='draw',
        choices=[
            ('draw', 'Draw'),
            ('scroll', 'Scroll'),
            ('flash', 'Flash'),
            ('fade', 'Fade'),
        ],
        help_text="Visual effect for text display"
    )
    justify = models.CharField(
        max_length=10,
        default='right',
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
        ],
        help_text="Text alignment on display"
    )
    color = models.CharField(
        max_length=20,
        default='white',
        choices=[
            ('white', 'White'),
            ('red', 'Red'),
            ('green', 'Green'),
            ('yellow', 'Yellow'),
            ('blue', 'Blue'),
            ('orange', 'Orange'),
            ('purple', 'Purple'),
        ],
        help_text="Text color for display"
    )
    test_message = models.CharField(
        max_length=255,
        blank=True,
        help_text="Test message for display testing"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Display Configuration'
        verbose_name_plural = 'Display Configurations'

    def __str__(self):
        return f"Display Config - {self.ip_address}:{self.port}"

class RadarConfig(models.Model):
    name = models.CharField(max_length=100, help_text="Name to identify this radar")
    imr_ad = models.CharField(max_length=50, blank=True, null=True, help_text="IMR_AD identifier (e.g., IMR_KD-BEKO)")
    route = models.CharField(max_length=255, blank=True, null=True, help_text="Route identifier")
    latitude = models.FloatField(blank=True, null=True, help_text="Latitude coordinate")
    longitude = models.FloatField(blank=True, null=True, help_text="Longitude coordinate")
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
    direction_id_positive = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Positive direction ID (e.g., IMR_KD-BE)"
    )
    direction_id_negative = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Negative direction ID (e.g., IMR_KD-KO)"
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
    
    def save(self, *args, **kwargs):
        """Override save to automatically manage cron jobs"""
        # Call the parent save method first
        super().save(*args, **kwargs)
        
        # Set up or remove cron job based on settings
        cron_updated = False
        if self.enable_notifications:
            cron_updated = self.setup_cron_job()
        else:
            cron_updated = self.remove_cron_job()
        
        # Log the settings save
        try:
            from app.utils.notification_logger import notification_logger
            notification_logger.log_settings_save(self, cron_updated)
        except Exception as e:
            # Don't let logging errors break the save
            pass

    def get_cc_emails_list(self):
        """Returns a list of CC email addresses"""
        if not self.cc_emails:
            return []
        return [email.strip() for email in self.cc_emails.split(',') if email.strip()]

    def get_email_connection(self):
        """Returns a configured email connection using the stored SMTP settings"""
        from django.core.mail import get_connection
        
        return get_connection(
            host=self.smtp_server,
            port=self.smtp_port,
            username=self.smtp_username,
            password=self.smtp_password,
            use_tls=self.use_tls,
            fail_silently=False
        )
    
    def setup_cron_job(self):
        """Set up cron job for this notification configuration"""
        try:
            from app.utils.cron_manager import cron_manager
            return cron_manager.setup_notification_cron(self)
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Failed to setup cron job: {e}")
            return False
    
    def remove_cron_job(self):
        """Remove cron job for this notification configuration"""
        try:
            from app.utils.cron_manager import cron_manager
            return cron_manager.remove_notification_cron()
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Failed to remove cron job: {e}")
            return False

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
    matching_window_seconds = models.IntegerField(
        default=2,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Time window (seconds) to match ANPR to radar detections"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    protocol = models.CharField(
        max_length=10,
        default='http',
        choices=[('http', 'HTTP'), ('https', 'HTTPS')],
        help_text="Protocol to use for ANPR camera callback URL"
    )

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
    email_sent = models.BooleanField(default=False, help_text="Whether this file has been sent via email")

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
    license_plate = models.CharField(max_length=20, null=True, blank=True, help_text="Detected license plate number")  # plateNo
    anpr_timestamp = models.DateTimeField(null=True, blank=True, help_text="Timestamp of ANPR event (picTime)")
    anpr_device_id = models.CharField(max_length=32, null=True, blank=True, help_text="Device ID of ANPR camera")
    anpr_confidence = models.IntegerField(null=True, blank=True, help_text="Confidence of ANPR detection")
    anpr_image_url = models.URLField(null=True, blank=True, help_text="URL of ANPR image")
    anpr_record_id = models.CharField(max_length=64, null=True, blank=True, help_text="Record ID of ANPR event")
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

class CameraConfig(models.Model):
    """Model to store camera configuration for vehicle detection"""
    name = models.CharField(max_length=100, help_text="Camera name")
    ip_address = models.GenericIPAddressField(help_text="Camera IP address")
    port = models.IntegerField(default=5000, help_text="Camera port")
    username = models.CharField(max_length=50, default="admin", help_text="Camera username")
    password = models.CharField(max_length=100, help_text="Camera password")
    protocol = models.CharField(max_length=20, default="VIID_2017", help_text="Protocol version")
    is_active = models.BooleanField(default=True, help_text="Is camera active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Camera Configuration'
        verbose_name_plural = 'Camera Configurations'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.ip_address}:{self.port})"

class CameraDetection(models.Model):
    """Model to store camera vehicle detection data"""
    camera = models.ForeignKey(CameraConfig, on_delete=models.CASCADE, related_name='detections')
    plate_number = models.CharField(max_length=20, help_text="License plate number")
    confidence = models.FloatField(help_text="Detection confidence (0-100)")
    speed = models.FloatField(null=True, blank=True, help_text="Vehicle speed in km/h")
    direction = models.CharField(max_length=50, blank=True, help_text="Vehicle direction")
    vehicle_type = models.CharField(max_length=50, default="Motor Vehicle", help_text="Type of vehicle")
    timestamp = models.DateTimeField(help_text="Detection timestamp")
    raw_data = models.TextField(blank=True, help_text="Raw detection data")
    data_format = models.CharField(max_length=20, default="unknown", help_text="Data format (xml, json, text)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Camera Detection'
        verbose_name_plural = 'Camera Detections'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['camera', 'timestamp']),
            models.Index(fields=['plate_number']),
        ]

    def __str__(self):
        return f"{self.plate_number} - {self.camera.name} ({self.timestamp})"

class SummaryStats(models.Model):
    """Model to store summary statistics for the dashboard"""
    total_objects = models.IntegerField(default=0, help_text="Total number of objects detected")
    active_radars = models.IntegerField(default=0, help_text="Number of active radars")
    active_cameras = models.IntegerField(default=0, help_text="Number of active cameras")
    last_detection = models.DateTimeField(null=True, blank=True, help_text="Time of the last detection")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Summary Statistics'
        verbose_name_plural = 'Summary Statistics'
        ordering = ['-timestamp']

    def __str__(self):
        return f"Summary Stats - {self.timestamp}"

    @classmethod
    def get_latest_stats(cls):
        """Get the latest summary statistics"""
        return cls.objects.first()

    @classmethod
    def update_stats(cls):
        """Update summary statistics"""
        total_objects = RadarObjectDetection.objects.count()
        active_radars = RadarConfig.objects.filter(is_active=True).count()
        active_cameras = CameraConfig.objects.filter(is_active=True).count()
        
        # Get last detection from radar or camera
        last_radar_detection = RadarObjectDetection.objects.aggregate(
            last=Max('start_time')
        )['last']
        last_camera_detection = CameraDetection.objects.aggregate(
            last=Max('timestamp')
        )['last']
        
        # Use the most recent detection
        last_detection = None
        if last_radar_detection and last_camera_detection:
            last_detection = max(last_radar_detection, last_camera_detection)
        elif last_radar_detection:
            last_detection = last_radar_detection
        elif last_camera_detection:
            last_detection = last_camera_detection

        stats, created = cls.objects.get_or_create(
            pk=1,
            defaults={
                'total_objects': total_objects,
                'active_radars': active_radars,
                'active_cameras': active_cameras,
                'last_detection': last_detection
            }
        )
        
        if not created:
            stats.total_objects = total_objects
            stats.active_radars = active_radars
            stats.active_cameras = active_cameras
            stats.last_detection = last_detection
            stats.save()
        
        return stats


