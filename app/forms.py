from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SystemSettings, TCPIPConfig, TimeConfig, FTPConfig, RadarConfig, NotificationSettings, User

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
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'gateway': forms.TextInput(attrs={'class': 'form-control'}),
            'subnet_mask': forms.TextInput(attrs={'class': 'form-control'}),
            'dns': forms.TextInput(attrs={'class': 'form-control'}),
            'timeout': forms.NumberInput(attrs={'class': 'form-control'})
        }

class TimeForm(forms.ModelForm):
    class Meta:
        model = TimeConfig
        fields = ['timezone', 'date_format', 'time_format']
        widgets = {
            'timezone': forms.Select(attrs={'class': 'form-select'}),
            'date_format': forms.Select(attrs={'class': 'form-select'}),
            'time_format': forms.Select(attrs={'class': 'form-select'})
        }

class FTPForm(forms.ModelForm):
    class Meta:
        model = FTPConfig
        fields = ['server', 'port', 'username', 'password', 'remote_directory']
        widgets = {
            'server': forms.TextInput(attrs={'class': 'form-control'}),
            'port': forms.NumberInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'remote_directory': forms.TextInput(attrs={'class': 'form-control'})
        }

class RadarForm(forms.ModelForm):
    class Meta:
        model = RadarConfig
        fields = ['name', 'port', 'baud_rate', 'data_bits', 'parity', 'stop_bits', 
                 'update_interval', 'file_save_interval', 'data_storage_path', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'port': forms.TextInput(attrs={'class': 'form-control'}),
            'baud_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'data_bits': forms.NumberInput(attrs={'class': 'form-control'}),
            'parity': forms.Select(attrs={'class': 'form-control'}),
            'stop_bits': forms.NumberInput(attrs={'class': 'form-control'}),
            'update_interval': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '50',
                'max': '1000',
                'step': '10'
            }),
            'file_save_interval': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '60',
                'step': '1'
            }),
            'data_storage_path': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter path for data storage'
            }),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

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
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Days of the Week',
        help_text='Select days to send notifications.'
    )
    notification_times = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 08:00,14:00'}),
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
        widgets = {
            'primary_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'frequency': forms.Select(attrs={'class': 'form-select'}),
            'cc_emails': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter multiple email addresses separated by commas'
            }),
            'smtp_server': forms.TextInput(attrs={'class': 'form-control'}),
            'smtp_port': forms.NumberInput(attrs={'class': 'form-control'}),
            'smtp_username': forms.TextInput(attrs={'class': 'form-control'}),
            'smtp_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'enable_notifications': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'use_tls': forms.CheckboxInput(attrs={'class': 'form-check-input'})
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
                    except Exception:
                        raise forms.ValidationError(f"Invalid time format: {t}. Use HH:MM.")
        return times

    def clean_days_of_week(self):
        days = self.cleaned_data.get('days_of_week', [])
        return ','.join(days) if days else ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If instance exists, populate days_of_week as a list
        if self.instance and self.instance.days_of_week:
            self.initial['days_of_week'] = [d.strip() for d in self.instance.days_of_week.split(',') if d.strip()]

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
                           widget=forms.Select(attrs={'class': 'form-control'})) 