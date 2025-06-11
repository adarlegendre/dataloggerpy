from django import forms
from .models import SystemSettings

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