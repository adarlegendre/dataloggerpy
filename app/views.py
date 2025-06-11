from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import SystemSettingsForm, TCPIPSettingsForm, TimeSettingsForm, FTPSettingsForm, RadarConfigForm
from .models import SystemSettings, TCPIPConfig, TimeConfig, FTPConfig, RadarConfig

# Create your views here.

@login_required
def home(request):
    settings = SystemSettings.get_settings()
    return render(request, 'home.html', {'settings': settings})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def settings(request):
    settings = SystemSettings.get_settings()
    if request.method == 'POST':
        form = SystemSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings updated successfully!')
            return redirect('settings')
    else:
        form = SystemSettingsForm(instance=settings)
    
    return render(request, 'settings.html', {
        'form': form,
        'settings': settings
    })

@login_required
def config_view(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'tcp':
            form = TCPIPSettingsForm(request.POST)
            if form.is_valid():
                config = form.save(commit=False)
                config.save()
                messages.success(request, 'TCP/IP settings saved successfully!')
                return redirect('config')
            else:
                messages.error(request, 'Please correct the errors in the TCP/IP settings.')
        elif form_type == 'time':
            form = TimeSettingsForm(request.POST)
            if form.is_valid():
                config = form.save(commit=False)
                config.save()
                messages.success(request, 'Time settings saved successfully!')
                return redirect('config')
            else:
                messages.error(request, 'Please correct the errors in the time settings.')
        elif form_type == 'ftp':
            form = FTPSettingsForm(request.POST)
            if form.is_valid():
                config = form.save(commit=False)
                config.save()
                messages.success(request, 'FTP settings saved successfully!')
                return redirect('config')
            else:
                messages.error(request, 'Please correct the errors in the FTP settings.')
        elif form_type == 'radar':
            form = RadarConfigForm(request.POST)
            if form.is_valid():
                try:
                    # Create a new radar configuration
                    radar_config = form.save()
                    messages.success(request, f'Radar configuration "{radar_config.name}" added successfully!')
                except Exception as e:
                    messages.error(request, f'Error saving radar configuration: {str(e)}')
                return redirect('config')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'Error in {field}: {error}')
    
    # Get the latest configuration for each type
    tcp_config = TCPIPConfig.objects.first()
    time_config = TimeConfig.objects.first()
    ftp_config = FTPConfig.objects.first()
    
    # Get all radar configurations, ordered by creation date
    radar_configs = RadarConfig.objects.all().order_by('-created_at')
    
    # Initialize forms with existing data
    tcp_form = TCPIPSettingsForm(instance=tcp_config)
    time_form = TimeSettingsForm(instance=time_config)
    ftp_form = FTPSettingsForm(instance=ftp_config)
    radar_form = RadarConfigForm()
    
    context = {
        'tcp_form': tcp_form,
        'time_form': time_form,
        'ftp_form': ftp_form,
        'radar_form': radar_form,
        'radar_configs': radar_configs,
    }
    
    return render(request, 'app/config.html', context)
