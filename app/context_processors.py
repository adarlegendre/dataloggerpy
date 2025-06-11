from .models import SystemSettings

def system_settings(request):
    settings = SystemSettings.get_settings()
    return {
        'settings': settings
    } 