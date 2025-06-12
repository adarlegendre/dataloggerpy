from django.db import models
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
import re
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
        return f"Notification Settings for {self.primary_email}"

    def get_cc_emails_list(self):
        """Returns a list of CC email addresses"""
        if not self.cc_emails:
            return []
        return [email.strip() for email in self.cc_emails.split(',') if email.strip()]

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
    speed = models.FloatField(null=True, blank=True, help_text="Speed measurement in m/s")
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
