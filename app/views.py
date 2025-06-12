from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from .forms import SystemSettingsForm, TCPIPForm, TimeForm, FTPForm, RadarForm, NotificationForm, UserForm, UserSearchForm
from .models import SystemSettings, TCPIPConfig, TimeConfig, FTPConfig, RadarConfig, NotificationSettings, User, RadarDataFile, SystemInfo
from .utils import get_system_info
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import Permission
import serial
import time
import json
from django.db.models import Q
from functools import wraps
from .services import RadarDataService
import logging
import os
import threading
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

# Global variable to store latest system info
latest_system_info = None
system_info_lock = threading.Lock()

def update_system_info_thread():
    """Background thread to update system info every minute without saving"""
    while True:
        try:
            # Get system info without saving
            info = get_system_info()
            
            # Update global variable with thread safety
            with system_info_lock:
                global latest_system_info
                latest_system_info = info
                
            # Sleep for 1 minute
            time.sleep(60)
        except Exception as e:
            print(f"Error in system info update thread: {e}")
            time.sleep(60)  # Still sleep on error to prevent tight loop

# Start the background thread when the application starts
system_info_thread = threading.Thread(target=update_system_info_thread, daemon=True)
system_info_thread.start()

def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Create your views here.

@login_required
def home(request):
    """Home view showing system status and radar configurations."""
    # Get system information
    system_info = get_system_info()
    
    # Get all radar configurations with their data files
    radars = RadarConfig.objects.all().order_by('name').prefetch_related('data_files')
    
    context = {
        'radars': radars,
        'system_info': system_info,
    }
    return render(request, 'app/home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@permission_required('app.view_systemsettings', raise_exception=True)
def settings(request):
    settings = SystemSettings.get_settings()
    if request.method == 'POST':
        if not request.user.is_superuser and not request.user.has_perm('app.change_systemsettings'):
            messages.error(request, 'You do not have permission to modify settings.')
            return redirect('settings')
            
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
@permission_required('app.view_radarconfig', raise_exception=True)
def config(request):
    # Get or create notification settings
    notification_settings, created = NotificationSettings.objects.get_or_create(
        pk=1,
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
            if not request.user.is_superuser and not request.user.has_perm('app.change_tcpipconfig'):
                messages.error(request, 'You do not have permission to modify TCP/IP settings.')
                return redirect('config')
            tcp_form = TCPIPForm(request.POST, instance=TCPIPConfig.objects.first())
            if tcp_form.is_valid():
                tcp_form.save()
                messages.success(request, 'TCP/IP settings updated successfully.')
                return redirect('config')
        elif form_type == 'time':
            if not request.user.is_superuser and not request.user.has_perm('app.change_timeconfig'):
                messages.error(request, 'You do not have permission to modify time settings.')
                return redirect('config')
            time_form = TimeForm(request.POST, instance=TimeConfig.objects.first())
            if time_form.is_valid():
                time_form.save()
                messages.success(request, 'Time settings updated successfully.')
                return redirect('config')
        elif form_type == 'ftp':
            if not request.user.is_superuser and not request.user.has_perm('app.change_ftpconfig'):
                messages.error(request, 'You do not have permission to modify FTP settings.')
                return redirect('config')
            ftp_form = FTPForm(request.POST, instance=FTPConfig.objects.first())
            if ftp_form.is_valid():
                ftp_form.save()
                messages.success(request, 'FTP settings updated successfully.')
                return redirect('config')
        elif form_type == 'radar':
            if not request.user.is_superuser and not request.user.has_perm('app.add_radarconfig'):
                messages.error(request, 'You do not have permission to add radar configurations.')
                return redirect('config')
            radar_form = RadarForm(request.POST)
            if radar_form.is_valid():
                radar_form.save()
                messages.success(request, 'Radar configuration added successfully.')
                return redirect('config')
        elif form_type == 'notification':
            if not request.user.is_superuser and not request.user.has_perm('app.change_notificationsettings'):
                messages.error(request, 'You do not have permission to modify notification settings.')
                return redirect('config')
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

@login_required
def update_system_info(request):
    """API endpoint to update system info and save to database"""
    if request.method == 'POST':
        try:
            # Get system info
            info = get_system_info()
            
            # Update global variable with thread safety
            with system_info_lock:
                global latest_system_info
                latest_system_info = info
            
            # Save to database
            SystemInfo.objects.create(
                disk_usage=info['disk']['percent'],
                ram_usage=info['ram']['percent'],
                cpu_temp=info['cpu_temp'],
                timestamp=datetime.now()
            )
            
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@login_required
def system_info_api(request):
    """API endpoint to get latest system info"""
    with system_info_lock:
        if latest_system_info is None:
            # If no cached info, get fresh info
            latest_system_info = get_system_info()
        return JsonResponse(latest_system_info)

@login_required
@require_GET
def radar_data_api(request, radar_id):
    """API endpoint for streaming radar data."""
    try:
        radar = get_object_or_404(RadarConfig, id=radar_id)
        
        if not radar.is_active:
            return JsonResponse({
                'status': 'error',
                'message': 'Radar is not active',
                'connection_status': 'inactive'
            })
        
        # Get data from the background service
        data_service = RadarDataService()
        data = data_service.get_latest_data(radar_id)
        
        if data is None:
            return JsonResponse({
                'status': 'success',
                'message': 'No new data available',
                'timestamp': time.time(),
                'connection_status': 'connected'
            })
            
        return JsonResponse(data)
            
    except Exception as e:
        logger.error(f"Error in radar_data_api: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Error: {str(e)}',
            'connection_status': 'error'
        })

@login_required
@permission_required('app.view_user', raise_exception=True)
def user_list(request):
    search_form = UserSearchForm(request.GET)
    users = User.objects.all()

    if search_form.is_valid():
        search = search_form.cleaned_data.get('search')
        role = search_form.cleaned_data.get('role')

        if search:
            users = users.filter(
                Q(username__icontains=search) |
                Q(email__icontains=search) |
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(department__icontains=search)
            )
        if role:
            users = users.filter(role=role)

    context = {
        'users': users,
        'search_form': search_form,
    }
    return render(request, 'app/user_list.html', context)

@login_required
@permission_required('app.add_user', raise_exception=True)
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'User {user.username} created successfully.')
            return redirect('user_list')
    else:
        form = UserForm()

    context = {
        'form': form,
        'title': 'Create User',
    }
    return render(request, 'app/user_form.html', context)

@login_required
@permission_required('app.change_user', raise_exception=True)
def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Prevent non-superusers from editing superusers
    if user.is_superuser and not request.user.is_superuser:
        messages.error(request, 'You do not have permission to edit superusers.')
        return redirect('user_list')
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'User {user.username} updated successfully.')
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    context = {
        'form': form,
        'title': 'Edit User',
    }
    return render(request, 'app/user_form.html', context)

@login_required
@permission_required('app.delete_user', raise_exception=True)
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Prevent non-superusers from deleting superusers
    if user.is_superuser and not request.user.is_superuser:
        messages.error(request, 'You do not have permission to delete superusers.')
        return redirect('user_list')
    
    if request.method == 'POST':
        username = user.username
        user.delete()
        messages.success(request, f'User {username} deleted successfully.')
        return redirect('user_list')
    
    context = {
        'user': user,
    }
    return render(request, 'app/user_confirm_delete.html', context)

@login_required
@superuser_required
def user_permissions_api(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'GET':
        # Get all permissions for the user
        permissions = user.user_permissions.values_list('codename', flat=True)
        return JsonResponse({
            'permissions': list(permissions)
        })
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            permissions = data.get('permissions', [])
            
            # Clear existing permissions
            user.user_permissions.clear()
            
            # Add new permissions
            for perm_codename in permissions:
                try:
                    perm = Permission.objects.get(codename=perm_codename)
                    user.user_permissions.add(perm)
                except Permission.DoesNotExist:
                    continue
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@login_required
@permission_required('app.view_radardatafile', raise_exception=True)
def download_radar_file(request, file_id):
    """Download a radar data file."""
    try:
        data_file = get_object_or_404(RadarDataFile, id=file_id)
        
        # Check if file exists
        if not os.path.exists(data_file.file_path):
            messages.error(request, 'File not found on server.')
            return redirect('home')
            
        # Open and read the file
        with open(data_file.file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/json')
            response['Content-Disposition'] = f'attachment; filename="{data_file.filename}"'
            return response
            
    except Exception as e:
        messages.error(request, f'Error downloading file: {str(e)}')
        return redirect('home')

@login_required
@permission_required('app.delete_radardatafile', raise_exception=True)
@require_POST
def delete_radar_file(request, file_id):
    """Delete a radar data file."""
    try:
        data_file = get_object_or_404(RadarDataFile, id=file_id)
        
        # Delete the physical file
        if os.path.exists(data_file.file_path):
            os.remove(data_file.file_path)
            
        # Delete the database record
        data_file.delete()
        
        return JsonResponse({
            'status': 'success',
            'message': 'File deleted successfully'
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Error deleting file: {str(e)}'
        }, status=500)
