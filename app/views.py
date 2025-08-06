from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from .forms import SystemSettingsForm, TCPIPForm, TimeForm, FTPForm, DisplayForm, RadarForm, NotificationForm, UserForm, UserSearchForm, ANPRForm
from .models import SystemSettings, TCPIPConfig, TimeConfig, FTPConfig, DisplayConfig, RadarConfig, NotificationSettings, User, RadarDataFile, SystemInfo, RadarObjectDetection, ANPRConfig, SummaryStats
from app.utils import get_system_info
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.models import Permission
import serial
import time
import json
from django.db.models import Q, Max, Min, Avg, Count
from functools import wraps
from .services import RadarDataService
import logging
import os
import threading
from datetime import datetime, timedelta
from collections import deque
from django.core.paginator import Paginator
from django.utils import timezone
from app.utils.notification_utils import create_notification, create_notification_for_today
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from app.shared_state import recent_anpr_events

logger = logging.getLogger(__name__)

# Global variables for system info caching
latest_system_info = None
system_info_lock = threading.Lock()
system_info_history = deque(maxlen=1440)  # Store last 24 hours of data (1 reading per minute)

def update_system_info_thread():
    """Background thread to update system info every minute"""
    global latest_system_info
    while True:
        try:
            # Get system info
            info = get_system_info()
            
            # Update global variable with thread safety
            with system_info_lock:
                latest_system_info = info
                
                # Add to history
                system_info_history.append({
                    'disk_usage': info['disk']['percent'],
                    'ram_usage': info['ram']['percent'],
                    'cpu_temp': info['cpu_temp'],
                    'timestamp': datetime.now()
                })
                
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
    """Home page view"""
    try:
        # Get system settings
        system_settings = SystemSettings.get_settings()
        
        # Get active radars
        radars = RadarConfig.objects.filter(is_active=True)
        
        # Get latest object detections for each radar (last 100 detections)
        radar_detections = {}
        for radar in radars:
            detections = RadarObjectDetection.objects.filter(
                radar=radar
            ).order_by('-start_time')[:100]  # Order by start_time descending
            radar_detections[radar.id] = detections
        
        # Get system info
        system_info = get_system_info()
        
        # Get radar service status
        try:
            from app.utils.startup_service import get_radar_service_status
            radar_service_status = get_radar_service_status()
        except Exception as e:
            logger.error(f"Error getting radar service status: {str(e)}")
            radar_service_status = {
                'started': False,
                'radar_service': 'error',
                'active_radars': 0,
                'active_threads': 0,
                'last_check': timezone.now().isoformat()
            }
        
        context = {
            'system_settings': system_settings,
            'radars': radars,
            'radar_detections': radar_detections,
            'system_info': system_info,
            'radar_service_status': radar_service_status,
        }
        return render(request, 'app/home.html', context)
    except Exception as e:
        logger.error(f"Error in home view: {str(e)}")
        messages.error(request, f"Error loading home page: {str(e)}")
        return redirect('login')

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

    # Get or create ANPR settings
    anpr_settings, created = ANPRConfig.objects.get_or_create(
        pk=1,
        defaults={
            'ip_address': '192.168.1.200',
            'port': 8080,
            'polling_interval': 1000,
            'timeout': 5,
            'endpoint': '/api/plate',
            'enable_continuous_reading': True,
            'enable_logging': True,
            'log_path': 'logs/anpr'
        }
    )

    # Initialize forms
    tcp_form = TCPIPForm(instance=TCPIPConfig.objects.first())
    time_form = TimeForm(instance=TimeConfig.objects.first())
    ftp_form = FTPForm(instance=FTPConfig.objects.first())
    display_form = DisplayForm(instance=DisplayConfig.objects.first())
    radar_form = RadarForm()
    notification_form = NotificationForm(instance=notification_settings)
    anpr_form = ANPRForm(instance=anpr_settings)

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
        elif form_type == 'display':
            if not request.user.is_superuser and not request.user.has_perm('app.change_displayconfig'):
                messages.error(request, 'You do not have permission to modify display settings.')
                return redirect('config')
            display_form = DisplayForm(request.POST, instance=DisplayConfig.objects.first())
            if display_form.is_valid():
                display_form.save()
                messages.success(request, 'Display settings updated successfully.')
                return redirect('config')
        elif form_type == 'radar':
            if not request.user.is_superuser and not request.user.has_perm('app.add_radarconfig'):
                messages.error(request, 'You do not have permission to add radar configurations.')
                return redirect('config')
            radar_form = RadarForm(request.POST)
            if radar_form.is_valid():
                radar = radar_form.save()
                # Handle ANPR configuration
                anpr_config = radar_form.cleaned_data.get('anpr_config')
                if anpr_config:
                    # Detach this ANPR config from any previous radar
                    anpr_config.radar = radar
                    anpr_config.save()
                messages.success(request, 'Radar configuration added successfully.')
                return redirect('config')
        elif form_type == 'notification':
            if not request.user.is_superuser and not request.user.has_perm('app.change_notificationsettings'):
                messages.error(request, 'You do not have permission to modify notification settings.')
                return redirect('config')
            notification_form = NotificationForm(request.POST, instance=notification_settings)
            if notification_form.is_valid():
                saved_settings = notification_form.save()
                messages.success(request, 'Notification settings updated successfully.')
                return redirect('config')
            else:
                messages.error(request, f'Notification settings update failed: {notification_form.errors}')
                return redirect('config')
        elif form_type == 'anpr':
            if not request.user.is_superuser and not request.user.has_perm('app.change_anprconfig'):
                messages.error(request, 'You do not have permission to modify ANPR settings.')
                return redirect('config')
            anpr_form = ANPRForm(request.POST, instance=anpr_settings)
            if anpr_form.is_valid():
                anpr_form.save()
                messages.success(request, 'ANPR settings updated successfully.')
                return redirect('config')


    # Get cron status
    try:
        from app.utils.cron_manager import cron_manager
        cron_status = cron_manager.get_cron_status()
    except Exception as e:
        logger.error(f"Error getting cron status: {e}")
        cron_status = {'installed': False, 'cron_job': None, 'log_file': None}

    # Build the camera URL for display
    protocol = getattr(anpr_settings, 'protocol', 'http') if anpr_settings else 'http'
    camera_url = f"{protocol}://{anpr_settings.ip_address}:{anpr_settings.port}/api/upark/capture" if anpr_settings else None

    context = {
        'tcp_form': tcp_form,
        'time_form': time_form,
        'ftp_form': ftp_form,
        'display_form': display_form,
        'radar_form': radar_form,
        'notification_form': notification_form,
        'anpr_form': anpr_form,
        'radar_configs': RadarConfig.objects.all().order_by('-created_at'),
        'cron_status': cron_status,
        'camera_url': camera_url,
    }
    
    return render(request, 'app/config.html', context)

@login_required
@permission_required('app.change_radarconfig', raise_exception=True)
def edit_radar(request, radar_id):
    radar = get_object_or_404(RadarConfig, id=radar_id)
    if request.method == 'POST':
        form = RadarForm(request.POST, instance=radar)
        if form.is_valid():
            radar = form.save()
            # Handle ANPR configuration
            anpr_config = form.cleaned_data.get('anpr_config')
            # Detach any ANPRConfig currently attached to this radar
            ANPRConfig.objects.filter(radar=radar).exclude(pk=anpr_config.pk if anpr_config else None).update(radar=None)
            if anpr_config:
                anpr_config.radar = radar
                anpr_config.save()
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
    try:
        global latest_system_info
        with system_info_lock:
            if latest_system_info is None:
                # If no system info is available yet, get it immediately
                latest_system_info = get_system_info()
            return JsonResponse(latest_system_info)
    except Exception as e:
        logger.error(f"Error in system_info_api: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Error getting system info: {str(e)}'
        }, status=500)

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
@require_GET
def serial_ports_api(request):
    """API endpoint for checking available serial ports."""
    try:
        data_service = RadarDataService()
        ports = data_service.check_serial_ports()
        return JsonResponse({
            'status': 'success',
            'ports': ports
        })
    except Exception as e:
        logger.error(f"Error in serial_ports_api: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Error: {str(e)}'
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
            try:
                os.remove(data_file.file_path)
                logger.info(f"Deleted file: {data_file.file_path}")
            except Exception as e:
                logger.error(f"Error deleting physical file {data_file.file_path}: {str(e)}")
                return JsonResponse({
                    'status': 'error',
                    'message': f'Error deleting physical file: {str(e)}'
                }, status=500)
            
        # Delete the database record
        data_file.delete()
        logger.info(f"Deleted database record for file ID: {file_id}")
        
        return JsonResponse({
            'status': 'success',
            'message': 'File deleted successfully'
        })
        
    except Exception as e:
        logger.error(f"Error in delete_radar_file: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Error deleting file: {str(e)}'
        }, status=500)

@login_required
@permission_required('app.view_radardatafile', raise_exception=True)
def radar_data_view(request, radar_id):
    """View for displaying radar data in a paginated table"""
    radar = get_object_or_404(RadarConfig, id=radar_id)
    
    # Get all data files for this radar
    data_files = RadarDataFile.objects.filter(radar=radar).order_by('-timestamp')
    
    # Get pagination parameters
    per_page = int(request.GET.get('per_page', 10))  # Default to 10 files per page
    page_number = request.GET.get('page', 1)
    
    # Paginate the data files
    paginator = Paginator(data_files, per_page)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'radar': radar,
        'page_obj': page_obj,
        'data_files': page_obj,
    }
    return render(request, 'app/radar_data.html', context)

@login_required
@permission_required('app.view_radardatafile', raise_exception=True)
def radar_files_api(request, radar_id):
    """API endpoint for getting radar data files."""
    try:
        radar = get_object_or_404(RadarConfig, id=radar_id)
        data_files = RadarDataFile.objects.filter(radar=radar).order_by('-timestamp')
        
        # Format the data for DataTables
        data = []
        for file in data_files:
            data.append({
                'filename': file.filename,
                'timestamp': file.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'record_count': file.record_count,
                'file_size': file.file_size,
                'is_valid': file.is_valid,
                'email_sent': file.email_sent,
                'id': file.id
            })
        
        return JsonResponse({
            'status': 'success',
            'data': data
        })
    except Exception as e:
        logger.error(f"Error in radar_files_api: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Error: {str(e)}'
        }, status=500)

@login_required
@require_POST
def toggle_test_mode(request):
    """Toggle test mode for radar data service"""
    try:
        data_service = RadarDataService()
        enabled = request.POST.get('enabled', 'false').lower() == 'true'
        data_service.set_test_mode(enabled)
        return JsonResponse({
            'status': 'success',
            'message': f'Test mode {"enabled" if enabled else "disabled"}',
            'test_mode': enabled
        })
    except Exception as e:
        logger.error(f"Error toggling test mode: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Error: {str(e)}'
        }, status=500)

@login_required
@require_GET
def test_mode_status(request):
    """Get current test mode status"""
    try:
        data_service = RadarDataService()
        return JsonResponse({
            'status': 'success',
            'test_mode': data_service.get_test_mode()
        })
    except Exception as e:
        logger.error(f"Error getting test mode status: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Error: {str(e)}'
        }, status=500)

@login_required
@require_http_methods(["GET"])
def radar_detections(request, radar_id):
    """API endpoint to get recent object detections for a radar."""
    try:
        radar = get_object_or_404(RadarConfig, id=radar_id)
        
        # Get DataTables parameters
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        
        # Get detections ordered by start_time descending
        detections = RadarObjectDetection.objects.filter(radar_id=radar_id).order_by('-start_time')
        total_records = detections.count()
        
        # Apply pagination
        detections = detections[start:start + length]
        
        data = {
            'draw': int(request.GET.get('draw', 1)),  # Required by DataTables
            'recordsTotal': total_records,  # Total records before filtering
            'recordsFiltered': total_records,  # Total records after filtering
            'data': [{
                'id': d.id,
                'start_time': d.start_time.isoformat(),
                'end_time': d.end_time.isoformat(),
                'duration': d.duration,
                'detection_count': d.detection_count,
                'min_range': d.min_range,
                'max_range': d.max_range,
                'avg_range': d.avg_range,
                'min_speed': d.min_speed,
                'max_speed': d.max_speed,
                'avg_speed': d.avg_speed,
                'anpr_detected': d.anpr_detected,
                'license_plate': d.license_plate,
                'direction_name': d.direction_name,
            } for d in detections]
        }
        return JsonResponse(data)
    except Exception as e:
        logger.error(f"Error fetching radar detections: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def radar_detection_details(request, detection_id):
    """API endpoint to get detailed information about a specific object detection."""
    try:
        detection = get_object_or_404(RadarObjectDetection, id=detection_id)
        
        # Get the raw data readings for this detection
        raw_data = []
        for reading in detection.raw_data:
            raw_data.append({
                'timestamp': reading['timestamp'],
                'raw_data': reading['raw_data']
            })
        
        data = {
            'id': detection.id,
            'radar_id': detection.radar.id,
            'start_time': detection.start_time.isoformat(),
            'end_time': detection.end_time.isoformat(),
            'duration': detection.duration,
            'detection_count': detection.detection_count,
            'min_range': detection.min_range,
            'max_range': detection.max_range,
            'avg_range': detection.avg_range,
            'min_speed': detection.min_speed,
            'max_speed': detection.max_speed,
            'avg_speed': detection.avg_speed,
            'raw_data': raw_data,
            'direction': getattr(detection, 'direction', None),
        }
        return JsonResponse(data)
    except Exception as e:
        logger.error(f"Error fetching detection details: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

@login_required
@require_POST
def test_anpr_connection(request):
    """Test the connection to the ANPR server"""
    try:
        data = json.loads(request.body)
        ip_address = data.get('ip_address')
        port = data.get('port')
        endpoint = data.get('endpoint')
        api_key = data.get('api_key')

        # Construct the URL
        url = f"http://{ip_address}:{port}{endpoint}"
        
        # Make the request
        import requests
        headers = {}
        if api_key:
            headers['X-API-Key'] = api_key
        
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        
        # Parse the response
        result = response.json()
        
        return JsonResponse({
            'success': True,
            'plate_number': result.get('plate_number'),
            'confidence': result.get('confidence'),
            'message': 'Successfully connected to ANPR server'
        })
    except requests.exceptions.RequestException as e:
        return JsonResponse({
            'success': False,
            'message': f'Failed to connect to ANPR server: {str(e)}'
        }, status=400)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid response from ANPR server'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error testing ANPR connection: {str(e)}'
        }, status=500)

@login_required
def create_notification_view(request):
    if request.method == 'POST':
        try:
            # Get date range from form
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            
            if start_date and end_date:
                # Convert string dates to datetime objects
                start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
                end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
                notification = create_notification(start_datetime, end_datetime)
            else:
                # Create notification for today
                notification = create_notification_for_today()
            
            messages.success(request, f'Notification created successfully! ID: {notification.id}')
            return redirect('notification_list')  # Redirect to a list view
            
        except Exception as e:
            messages.error(request, f'Error creating notification: {str(e)}')
            return redirect('create_notification')
    
    return render(request, 'notifications/create.html')

@require_http_methods(["GET"])
def summary_stats(request):
    """API endpoint to get summary statistics for the dashboard."""
    try:
        # Always update stats before returning
        stats = SummaryStats.update_stats()
        if not stats:
            return JsonResponse({
                'error': 'Unable to get or create summary statistics'
            }, status=500)
        # Return the stats as JSON
        return JsonResponse({
            'total_objects': stats.total_objects,
            'active_radars': stats.active_radars,
            'last_detection': stats.last_detection.isoformat() if stats.last_detection else None
        })
    except Exception as e:
        logger.error(f"Error in summary_stats view: {str(e)}")
        return JsonResponse({
            'error': 'Internal server error'
        }, status=500)

@csrf_exempt
@require_POST
def send_test_email(request):
    try:
        settings = NotificationSettings.objects.first()
        if not settings:
            return JsonResponse({'success': False, 'message': 'No notification settings found.'}, status=400)
        
        # Prepare recipient information
        to_emails = [settings.primary_email]
        cc_emails = settings.get_cc_emails_list()
        
        email = EmailMessage(
            subject='Test Email from Datalogger',
            body='This is a test email to confirm your SMTP settings.',
            from_email=settings.smtp_username,
            to=to_emails,
            cc=cc_emails,
            connection=settings.get_email_connection(),
        )
        email.send()
        
        # Create detailed success message with recipient information
        message = f'Test email sent successfully!'
        if to_emails:
            message += f' To: {", ".join(to_emails)}'
        if cc_emails:
            message += f' CC: {", ".join(cc_emails)}'
        
        return JsonResponse({
            'success': True, 
            'message': message,
            'recipients': {
                'to': to_emails,
                'cc': cc_emails,
                'from': settings.smtp_username
            }
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Failed to send test email: {str(e)}'}, status=500)

@login_required
@require_POST
def update_system_from_radar(request, system_id):
    """API endpoint to update system details from radar data"""
    try:
        system_detail = get_object_or_404(SystemDetails, id=system_id)
        system_detail.update_from_radar_data()
        return JsonResponse({'success': True, 'message': 'System details updated successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
@require_GET
def system_directions(request, system_id):
    """API endpoint to get system directions"""
    try:
        system_detail = get_object_or_404(SystemDetails, id=system_id)
        directions = system_detail.directions.all()
        directions_data = []
        
        for direction in directions:
            directions_data.append({
                'direction_id': direction.direction_id,
                'name': direction.name,
                'detections': direction.detections,
                'detections_ANPR': direction.detections_ANPR
            })
        
        return JsonResponse({'success': True, 'directions': directions_data})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@csrf_exempt
@require_POST
def receive_anpr_capture(request):
    """Endpoint to receive ANPR vehicle capture data from Dahua camera."""
    import json
    from datetime import datetime
    from app.models import ANPRConfig
    import logging
    try:
        # Load ANPRConfig settings
        anpr_settings = ANPRConfig.objects.first()
        if anpr_settings:
            camera_url = f"http://{anpr_settings.ip_address}:{anpr_settings.port}/api/upark/capture"
            logging.getLogger(__name__).info(f"[ANPR] Camera should POST to: {camera_url}")
        else:
            logging.getLogger(__name__).warning("[ANPR] No ANPRConfig found to construct camera URL.")

        data = json.loads(request.body)
        params = data.get('params', {})
        plate = params.get('plateNo')
        pic_time = params.get('picTime')
        device_id = data.get('deviceId')
        confidence = params.get('confidence')
        pic_info = params.get('picInfo', [])
        image_url = pic_info[0]['url'] if pic_info else None
        record_id = params.get('recordId')

        # Convert pic_time to datetime
        anpr_time = datetime.fromisoformat(pic_time) if pic_time else None

        # Store in memory for matching with radar
        recent_anpr_events.append({
            'plate': plate,
            'timestamp': anpr_time,
            'device_id': device_id,
            'confidence': confidence,
            'image_url': image_url,
            'record_id': record_id,
        })
        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@login_required
@require_POST
def test_display(request):
    """Test sending a message to the display"""
    try:
        from app.models import DisplayConfig
        from app.services import send_cp5200_message, build_cp5200_protocol
        
        # Get display configuration
        display_config = DisplayConfig.objects.first()
        if not display_config:
            return JsonResponse({
                'status': 'error',
                'message': 'No display configuration found'
            })
        
        # Send test message using database settings
        test_message = display_config.test_message or "TEST MESSAGE"
        
        # Build protocol data for display
        protocol_data = build_cp5200_protocol(test_message, display_config)
        
        # Send using CP5200 protocol
        send_cp5200_message(test_message, display_config.ip_address, display_config.port, display_config)
        
        return JsonResponse({
            'status': 'ok',
            'message': f'Test message sent to {display_config.ip_address}:{display_config.port}',
            'protocol_data': protocol_data.hex(),
            'settings': {
                'font_size': display_config.font_size,
                'effect_type': display_config.effect_type,
                'justify': display_config.justify,
                'color': display_config.color
            }
        })
    except Exception as e:
        logger.error(f"Error testing display: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Failed to send test message: {str(e)}'
        })
