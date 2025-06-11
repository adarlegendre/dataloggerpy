from django import forms
from .models import SystemSettings, TCPIPConfig, TimeConfig, FTPConfig, RadarConfig

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

class TCPIPSettingsForm(forms.ModelForm):
    class Meta:
        model = TCPIPConfig
        fields = ['ip_address', 'gateway', 'subnet_mask', 'dns', 'timeout']
        widgets = {
            'ip_address': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 220px;'}),
            'gateway': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 220px;'}),
            'subnet_mask': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 220px;'}),
            'dns': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 220px;'}),
            'timeout': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 120px;'}),
        }

class TimeSettingsForm(forms.ModelForm):
    class Meta:
        model = TimeConfig
        fields = ['timezone', 'date_format', 'time_format']
        widgets = {
            'timezone': forms.Select(attrs={'class': 'form-select form-select-sm', 'style': 'max-width: 220px;'}),
            'date_format': forms.Select(attrs={'class': 'form-select form-select-sm', 'style': 'max-width: 220px;'}),
            'time_format': forms.Select(attrs={'class': 'form-select form-select-sm', 'style': 'max-width: 220px;'}),
        }

class FTPSettingsForm(forms.ModelForm):
    class Meta:
        model = FTPConfig
        fields = ['server', 'port', 'username', 'password', 'remote_directory']
        widgets = {
            'server': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 220px;'}),
            'port': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 120px;'}),
            'username': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 180px;'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 180px;'}),
            'remote_directory': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 180px;'}),
        }

class RadarConfigForm(forms.ModelForm):
    class Meta:
        model = RadarConfig
        fields = ['name', 'port', 'baud_rate', 'data_bits', 'parity', 'stop_bits', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 220px;'}),
            'port': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 220px;'}),
            'baud_rate': forms.Select(attrs={'class': 'form-select form-select-sm', 'style': 'max-width: 220px;'}),
            'data_bits': forms.Select(attrs={'class': 'form-select form-select-sm', 'style': 'max-width: 220px;'}),
            'parity': forms.Select(attrs={'class': 'form-select form-select-sm', 'style': 'max-width: 220px;'}),
            'stop_bits': forms.Select(attrs={'class': 'form-select form-select-sm', 'style': 'max-width: 220px;'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        } 