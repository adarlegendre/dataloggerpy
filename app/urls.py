from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.settings, name='settings'),
    path('config/', views.config, name='config'),
    path('radar/<int:radar_id>/edit/', views.edit_radar, name='edit_radar'),
    path('radar/<int:radar_id>/delete/', views.delete_radar, name='delete_radar'),
    path('radar/<int:radar_id>/data/', views.radar_data_view, name='radar_data'),
    path('api/system-info/', views.system_info_api, name='system_info_api'),
    path('api/radar-data/<int:radar_id>/', views.radar_data_api, name='radar_data_api'),
    path('api/serial-ports/', views.serial_ports_api, name='serial_ports_api'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:user_id>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('api/user-permissions/<int:user_id>/', views.user_permissions_api, name='user_permissions_api'),
    path('radar-file/<int:file_id>/download/', views.download_radar_file, name='download_radar_file'),
    path('api/radar-file/<int:file_id>/delete/', views.delete_radar_file, name='delete_radar_file'),
    path('api/radar-files/<int:radar_id>/', views.radar_files_api, name='radar_files_api'),
    path('api/toggle-test-mode/', views.toggle_test_mode, name='toggle_test_mode'),
    path('api/test-mode/', views.toggle_test_mode, name='toggle_test_mode'),
    path('api/test-mode-status/', views.test_mode_status, name='test_mode_status'),
    path('api/radar-detections/<int:radar_id>/', views.radar_detections, name='radar_detections'),
    path('api/radar-detection/<int:detection_id>/', views.radar_detection_details, name='radar_detection_details'),
    path('api/test-anpr-connection/', views.test_anpr_connection, name='test_anpr_connection'),
    path('api/summary-stats/', views.summary_stats, name='summary_stats'),
] 