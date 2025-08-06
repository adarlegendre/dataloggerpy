from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SystemSettings, TCPIPConfig, TimeConfig, FTPConfig, DisplayConfig, RadarConfig, NotificationSettings, User, ANPRConfig
import ipaddress
from django.db.models import Q

COLOR_PRESETS = {
    'navy': {
        'name': 'Navy Blue',
        'primary': '#1a237e',
        'secondary': '#283593',
        'accent': '#3949ab',
        'text': '#333333',
        'background': '#f5f5f5'
    },
    'forest': {
        'name': 'Forest Green',
        'primary': '#1b5e20',
        'secondary': '#2e7d32',
        'accent': '#388e3c',
        'text': '#333333',
        'background': '#f5f5f5'
    },
    'burgundy': {
        'name': 'Burgundy',
        'primary': '#880e4f',
        'secondary': '#ad1457',
        'accent': '#c2185b',
        'text': '#333333',
        'background': '#f5f5f5'
    },
    'midnight': {
        'name': 'Midnight',
        'primary': '#000051',
        'secondary': '#1a237e',
        'accent': '#283593',
        'text': '#ffffff',
        'background': '#121212'
    },
    'ocean': {
        'name': 'Ocean',
        'primary': '#006064',
        'secondary': '#00838f',
        'accent': '#0097a7',
        'text': '#333333',
        'background': '#f5f5f5'
    }
}

class SystemSettingsForm(forms.ModelForm):
    color_preset = forms.ChoiceField(
        choices=[(key, value['name']) for key, value in COLOR_PRESETS.items()],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = SystemSettings
        fields = ['system_name', 'login_title', 'primary_color', 'secondary_color', 
                 'accent_color', 'text_color', 'background_color']
        widgets = {
            'primary_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
            'secondary_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
            'accent_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
            'text_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
            'background_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['color_preset'].widget.attrs.update({
            'onchange': 'applyColorPreset(this.value)'
        })

class TCPIPForm(forms.ModelForm):
    class Meta:
        model = TCPIPConfig
        fields = ['ip_address', 'gateway', 'subnet_mask', 'dns', 'timeout']
        widgets = {
            'ip_address': forms.TextInput(attrs={'class': 'form-control', 'id': 'tcp-ip_address'}),
            'gateway': forms.TextInput(attrs={'class': 'form-control', 'id': 'tcp-gateway'}),
            'subnet_mask': forms.TextInput(attrs={'class': 'form-control', 'id': 'tcp-subnet_mask'}),
            'dns': forms.TextInput(attrs={'class': 'form-control', 'id': 'tcp-dns'}),
            'timeout': forms.NumberInput(attrs={'class': 'form-control', 'id': 'tcp-timeout'})
        }

class TimeForm(forms.ModelForm):
    class Meta:
        model = TimeConfig
        fields = ['timezone', 'date_format', 'time_format']
        widgets = {
            'timezone': forms.Select(attrs={'class': 'form-select', 'id': 'time-timezone'}),
            'date_format': forms.Select(attrs={'class': 'form-select', 'id': 'time-date_format'}),
            'time_format': forms.Select(attrs={'class': 'form-select', 'id': 'time-time_format'})
        }

class FTPForm(forms.ModelForm):
    class Meta:
        model = FTPConfig
        fields = ['server', 'port', 'username', 'password', 'remote_directory']
        widgets = {
            'server': forms.TextInput(attrs={'class': 'form-control', 'id': 'ftp-server'}),
            'port': forms.NumberInput(attrs={'class': 'form-control', 'id': 'ftp-port'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'ftp-username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'ftp-password'}),
            'remote_directory': forms.TextInput(attrs={'class': 'form-control', 'id': 'ftp-remote_directory'})
        }

class DisplayForm(forms.ModelForm):
    class Meta:
        model = DisplayConfig
        fields = ['ip_address', 'port', 'font_size', 'effect_type', 'justify', 'color', 'test_message']
        widgets = {
            'ip_address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'display-ip_address',
                'placeholder': 'e.g., 192.168.1.222'
            }),
            'port': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'display-port',
                'min': '1',
                'max': '65535'
            }),
            'font_size': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'display-font_size',
                'min': '8',
                'max': '72'
            }),
            'effect_type': forms.Select(attrs={
                'class': 'form-select',
                'id': 'display-effect_type'
            }),
            'justify': forms.Select(attrs={
                'class': 'form-select',
                'id': 'display-justify'
            }),
            'color': forms.Select(attrs={
                'class': 'form-select',
                'id': 'display-color'
            }),
            'test_message': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'display-test_message',
                'placeholder': 'Enter test message'
            })
        }

class RadarForm(forms.ModelForm):
    anpr_config = forms.ModelChoiceField(
        queryset=ANPRConfig.objects.filter(radar__isnull=True),
        required=False,
        empty_label="No ANPR",
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text="Select ANPR configuration for this radar"
    )

    class Meta:
        model = RadarConfig
        fields = ['name', 'imr_ad', 'port', 'baud_rate', 'data_bits', 'parity', 'stop_bits', 
                 'update_interval', 'file_save_interval', 'data_storage_path', 'is_active', 
                 'direction_positive_name', 'direction_negative_name', 'direction_id_positive', 'direction_id_negative']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'radar-name'}),
            'imr_ad': forms.TextInput(attrs={'class': 'form-control', 'id': 'radar-imr_ad', 'placeholder': 'e.g., IMR_KD-BEKO'}),
            'port': forms.TextInput(attrs={'class': 'form-control', 'id': 'radar-port'}),
            'baud_rate': forms.NumberInput(attrs={'class': 'form-control', 'id': 'radar-baud_rate'}),
            'data_bits': forms.NumberInput(attrs={'class': 'form-control', 'id': 'radar-data_bits'}),
            'parity': forms.Select(attrs={'class': 'form-control', 'id': 'radar-parity'}),
            'stop_bits': forms.NumberInput(attrs={'class': 'form-control', 'id': 'radar-stop_bits'}),
            'update_interval': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'radar-update_interval',
                'min': '50',
                'max': '1000',
                'step': '10'
            }),
            'file_save_interval': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'radar-file_save_interval',
                'min': '1',
                'max': '60',
                'step': '1'
            }),
            'data_storage_path': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'radar-data_storage_path',
                'placeholder': 'Enter path for data storage'
            }),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'radar-is_active'}),
            'direction_positive_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'radar-direction_positive_name', 'placeholder': "e.g. Towards Village"}),
            'direction_negative_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'radar-direction_negative_name', 'placeholder': "e.g. Towards Town"}),
            'direction_id_positive': forms.TextInput(attrs={'class': 'form-control', 'id': 'radar-direction_id_positive', 'placeholder': "e.g., IMR_KD-BE"}),
            'direction_id_negative': forms.TextInput(attrs={'class': 'form-control', 'id': 'radar-direction_id_negative', 'placeholder': "e.g., IMR_KD-KO"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Include the current ANPR config in the queryset
            self.fields['anpr_config'].queryset = ANPRConfig.objects.filter(
                Q(radar__isnull=True) | Q(radar=self.instance)
            )
            # Set the initial value
            try:
                self.fields['anpr_config'].initial = self.instance.anpr_configs.first()
            except:
                pass

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        port = cleaned_data.get('port')
        instance = getattr(self, 'instance', None)

        # Validate name
        if name:
            # Check for duplicate name
            name_exists = RadarConfig.objects.filter(name=name)
            if instance and instance.pk:
                name_exists = name_exists.exclude(pk=instance.pk)
            if name_exists.exists():
                existing_radar = name_exists.first()
                self.add_error('name', f'Radar name "{name}" is already in use by another radar (Port: {existing_radar.port}). Please choose a different name.')

        # Validate port
        if port:
            # Check for duplicate port
            port_exists = RadarConfig.objects.filter(port=port)
            if instance and instance.pk:
                port_exists = port_exists.exclude(pk=instance.pk)
            if port_exists.exists():
                existing_radar = port_exists.first()
                self.add_error('port', f'Port "{port}" is already in use by radar "{existing_radar.name}". Please choose a different port.')

            # Validate port format
            if not port.startswith(('COM', '/dev/tty')):
                self.add_error('port', 'Port must start with "COM" (Windows) or "/dev/tty" (Linux)')
            elif port.startswith('COM') and not port[3:].isdigit():
                self.add_error('port', 'Windows COM port must be followed by a number (e.g., COM1, COM2)')
            elif port.startswith('/dev/tty') and not port[8:].isalnum():
                self.add_error('port', 'Linux port must be followed by alphanumeric characters (e.g., /dev/ttyUSB0)')

        return cleaned_data

class NotificationForm(forms.ModelForm):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    days_of_week = forms.MultipleChoiceField(
        choices=DAYS_OF_WEEK,
        widget=forms.CheckboxSelectMultiple(attrs={'id': 'notification-days_of_week'}),
        required=False,
        label='Days of the Week',
        help_text='Select days to send notifications.'
    )
    notification_times = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'notification-notification_times', 'placeholder': 'e.g., 08:00,14:00'}),
        label='Notification Times',
        help_text='Enter one or more times in HH:MM format, separated by commas.'
    )
    class Meta:
        model = NotificationSettings
        fields = [
            'primary_email',
            'frequency',
            'cc_emails',
            'smtp_server',
            'smtp_port',
            'smtp_username',
            'smtp_password',
            'enable_notifications',
            'use_tls',
            'days_of_week',
            'notification_times',
        ]
        help_texts = {
            'smtp_password': 'Leave empty to keep the current password unchanged.',
        }
        widgets = {
            'primary_email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'notification-primary_email'}),
            'frequency': forms.Select(attrs={'class': 'form-select', 'id': 'notification-frequency'}),
            'cc_emails': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'notification-cc_emails',
                'rows': 3,
                'placeholder': 'Enter multiple email addresses separated by commas'
            }),
            'smtp_server': forms.TextInput(attrs={'class': 'form-control', 'id': 'notification-smtp_server'}),
            'smtp_port': forms.NumberInput(attrs={'class': 'form-control', 'id': 'notification-smtp_port'}),
            'smtp_username': forms.TextInput(attrs={'class': 'form-control', 'id': 'notification-smtp_username'}),
            'smtp_password': forms.PasswordInput(attrs={
                'class': 'form-control', 
                'id': 'notification-smtp_password',
                'placeholder': 'Enter password to change'
            }),
            'enable_notifications': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'notification-enable_notifications'}),
            'use_tls': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'notification-use_tls'})
        }

    def clean_cc_emails(self):
        cc_emails = self.cleaned_data.get('cc_emails', '')
        if cc_emails:
            emails = [email.strip() for email in cc_emails.split(',')]
            email_validator = forms.EmailField()
            for email in emails:
                if email:  # Skip empty strings
                    try:
                        email_validator.clean(email)
                    except forms.ValidationError:
                        raise forms.ValidationError(f"Invalid email address in CC list: {email}")
        return cc_emails

    def clean_notification_times(self):
        times = self.cleaned_data.get('notification_times', '')
        if times:
            for t in times.split(','):
                t = t.strip()
                if t:
                    try:
                        hour, minute = map(int, t.split(':'))
                        if not (0 <= hour < 24 and 0 <= minute < 60):
                            raise ValueError
                    except ValueError:
                        raise forms.ValidationError(
                            "Invalid time format. Please use HH:MM format (e.g., 08:00, 14:30)"
                        )
        return times

    def clean_days_of_week(self):
        days = self.cleaned_data.get('days_of_week', [])
        return ','.join(days) if days else ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If instance exists, populate days_of_week as a list
        if self.instance and self.instance.days_of_week:
            self.initial['days_of_week'] = [d.strip() for d in self.instance.days_of_week.split(',') if d.strip()]
        
        # Set a placeholder for password field if instance exists and has a password
        if self.instance and self.instance.pk and self.instance.smtp_password:
            self.fields['smtp_password'].widget.attrs['placeholder'] = '••••••••'
            # Don't set initial value for password field to keep it empty
            # This way the field shows as empty but user knows there's a password saved
        
        # Make password field not required when updating an existing instance
        if self.instance and self.instance.pk:
            self.fields['smtp_password'].required = False
            # Ensure password field is always empty in the form (for security)
            if 'smtp_password' in self.initial:
                del self.initial['smtp_password']

    def save(self, commit=True):
        """Custom save method to handle password field properly"""
        instance = super().save(commit=False)
        
        # Get fresh instance from database if we have a pk
        if self.instance and self.instance.pk:
            try:
                fresh_instance = NotificationSettings.objects.get(pk=self.instance.pk)
            except NotificationSettings.DoesNotExist:
                fresh_instance = None
        else:
            fresh_instance = None
        
        # Only update password if a new one was provided
        if self.cleaned_data.get('smtp_password'):
            instance.smtp_password = self.cleaned_data['smtp_password']
        # If no password provided and this is an update, keep the existing password
        elif fresh_instance and fresh_instance.smtp_password:
            instance.smtp_password = fresh_instance.smtp_password
        elif self.instance and self.instance.pk and self.instance.smtp_password:
            instance.smtp_password = self.instance.smtp_password
        
        if commit:
            instance.save()
        return instance

class ANPRForm(forms.ModelForm):
    class Meta:
        model = ANPRConfig
        fields = [
            'ip_address',
            'port',
            'polling_interval',
            'timeout',
            'endpoint',
            'api_key',
            'enable_continuous_reading',
            'enable_logging',
            'log_path',
            'matching_window_seconds'
        ]
        widgets = {
            'ip_address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'anpr-ip_address',
                'placeholder': 'e.g., 192.168.1.200'
            }),
            'port': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'anpr-port',
                'min': '1',
                'max': '65535'
            }),
            'polling_interval': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'anpr-polling_interval',
                'min': '100',
                'max': '5000',
                'step': '100'
            }),
            'timeout': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'anpr-timeout',
                'min': '1',
                'max': '30'
            }),
            'endpoint': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'anpr-endpoint',
                'placeholder': 'e.g., /api/plate'
            }),
            'api_key': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'anpr-api_key',
                'placeholder': 'Enter API key if required'
            }),
            'enable_continuous_reading': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'anpr-enable_continuous_reading'
            }),
            'enable_logging': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'anpr-enable_logging'
            }),
            'log_path': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'anpr-log_path',
                'placeholder': 'e.g., logs/anpr'
            }),
            'matching_window_seconds': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'anpr-matching_window_seconds',
                'min': '1',
                'max': '10',
                'step': '1'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        ip_address = cleaned_data.get('ip_address')
        port = cleaned_data.get('port')
        polling_interval = cleaned_data.get('polling_interval')
        timeout = cleaned_data.get('timeout')
        matching_window_seconds = cleaned_data.get('matching_window_seconds')

        # Validate IP address format
        if ip_address:
            try:
                ipaddress.ip_address(ip_address)
            except ValueError:
                self.add_error('ip_address', 'Invalid IP address format')

        # Validate port range
        if port and (port < 1 or port > 65535):
            self.add_error('port', 'Port must be between 1 and 65535')

        # Validate polling interval
        if polling_interval and (polling_interval < 100 or polling_interval > 5000):
            self.add_error('polling_interval', 'Polling interval must be between 100ms and 5000ms')

        # Validate timeout
        if timeout and (timeout < 1 or timeout > 30):
            self.add_error('timeout', 'Timeout must be between 1 and 30 seconds')

        # Validate matching window seconds
        if matching_window_seconds and (matching_window_seconds < 1 or matching_window_seconds > 10):
            self.add_error('matching_window_seconds', 'Matching window must be between 1 and 10 seconds')

        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'department', 'is_active']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['is_active']:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('password'):
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserSearchForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Search users...'
    }))
    role = forms.ChoiceField(required=False, choices=[('', 'All Roles')] + User.ROLE_CHOICES,
                            widget=forms.Select(attrs={'class': 'form-select'}))

 