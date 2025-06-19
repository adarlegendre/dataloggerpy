from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from .forms import SystemSettingsForm, TCPIPForm, TimeForm, FTPForm, RadarForm, NotificationForm, UserForm, UserSearchForm, ANPRForm
from .models import SystemSettings, TCPIPConfig, TimeConfig, FTPConfig, RadarConfig, NotificationSettings, User, RadarDataFile, SystemInfo, RadarObjectDetection, ANPRConfig, SummaryStats
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
        
        context = {
            'system_settings': system_settings,
            'radars': radars,
            'radar_detections': radar_detections,
            'system_info': system_info,
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
                notification_form.save()
                messages.success(request, 'Notification settings updated successfully.')
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

    context = {
        'tcp_form': tcp_form,
        'time_form': time_form,
        'ftp_form': ftp_form,
        'radar_form': radar_form,
        'notification_form': notification_form,
        'anpr_form': anpr_form,
        'radar_configs': RadarConfig.objects.all().order_by('-created_at'),
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

@require_http_methods(["GET"])
def radar_detections(request, radar_id):
    """API endpoint to get recent object detections for a radar."""
    try:
        radar = get_object_or_404(RadarConfig, id=radar_id)
        page = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 10))  # Default to 10 records per page
        
        # Get detections ordered by start_time descending
        detections = RadarObjectDetection.objects.filter(radar_id=radar_id).order_by('-start_time')
        paginator = Paginator(detections, per_page)
        page_obj = paginator.get_page(page)
        
        data = {
            'detections': [{
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
            } for d in page_obj],
            'pagination': {
                'total_pages': paginator.num_pages,
                'current_page': page_obj.number,
                'has_next': page_obj.has_next(),
                'has_previous': page_obj.has_previous(),
                'next_page': page_obj.next_page_number() if page_obj.has_next() else None,
                'previous_page': page_obj.previous_page_number() if page_obj.has_previous() else None,
            }
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
        # Get or create latest stats
        stats = SummaryStats.get_latest_stats()
        if not stats:
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
