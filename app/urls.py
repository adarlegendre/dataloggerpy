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
] 