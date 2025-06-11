from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import SystemSettingsForm, TCPIPForm, TimeForm, FTPForm, RadarForm, NotificationForm
from .models import SystemSettings, TCPIPConfig, TimeConfig, FTPConfig, RadarConfig, NotificationSettings

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
def config(request):
    # Get or create notification settings
    notification_settings, created = NotificationSettings.objects.get_or_create(
        pk=1,  # We'll use a single instance for notification settings
        defaults={
            'primary_email': '',
            'frequency': 'daily',
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'use_tls': True
        }
    )

    # Initialize forms
    tcp_form = TCPIPForm(instance=TCPIPConfig.objects.first())
    time_form = TimeForm(instance=TimeConfig.objects.first())
    ftp_form = FTPForm(instance=FTPConfig.objects.first())
    radar_form = RadarForm()
    notification_form = NotificationForm(instance=notification_settings)

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'tcp':
            tcp_form = TCPIPForm(request.POST, instance=TCPIPConfig.objects.first())
            if tcp_form.is_valid():
                tcp_form.save()
                messages.success(request, 'TCP/IP settings updated successfully.')
                return redirect('config')
        elif form_type == 'time':
            time_form = TimeForm(request.POST, instance=TimeConfig.objects.first())
            if time_form.is_valid():
                time_form.save()
                messages.success(request, 'Time settings updated successfully.')
                return redirect('config')
        elif form_type == 'ftp':
            ftp_form = FTPForm(request.POST, instance=FTPConfig.objects.first())
            if ftp_form.is_valid():
                ftp_form.save()
                messages.success(request, 'FTP settings updated successfully.')
                return redirect('config')
        elif form_type == 'radar':
            radar_form = RadarForm(request.POST)
            if radar_form.is_valid():
                radar_form.save()
                messages.success(request, 'Radar configuration added successfully.')
                return redirect('config')
        elif form_type == 'notification':
            notification_form = NotificationForm(request.POST, instance=notification_settings)
            if notification_form.is_valid():
                notification_form.save()
                messages.success(request, 'Notification settings updated successfully.')
                return redirect('config')

    context = {
        'tcp_form': tcp_form,
        'time_form': time_form,
        'ftp_form': ftp_form,
        'radar_form': radar_form,
        'notification_form': notification_form,
        'radar_configs': RadarConfig.objects.all().order_by('-created_at'),
    }
    
    return render(request, 'app/config.html', context)

@login_required
def edit_radar(request, radar_id):
    radar = get_object_or_404(RadarConfig, id=radar_id)
    if request.method == 'POST':
        form = RadarForm(request.POST, instance=radar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Radar configuration updated successfully.')
            return redirect('config')
    else:
        form = RadarForm(instance=radar)
    
    return render(request, 'app/edit_radar.html', {
        'form': form,
        'radar': radar
    })

@login_required
def delete_radar(request, radar_id):
    radar = get_object_or_404(RadarConfig, id=radar_id)
    if request.method == 'POST':
        radar_name = radar.name
        radar.delete()
        messages.success(request, f'Radar configuration "{radar_name}" deleted successfully.')
    return redirect('config')
