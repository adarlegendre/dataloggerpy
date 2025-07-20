from django.contrib import admin
from .models import SystemSettings, TCPIPConfig, TimeConfig, FTPConfig

@admin.register(TCPIPConfig)
class TCPIPConfigAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'gateway', 'subnet_mask', 'dns', 'timeout', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(TimeConfig)
class TimeConfigAdmin(admin.ModelAdmin):
    list_display = ('timezone', 'date_format', 'time_format', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(FTPConfig)
class FTPConfigAdmin(admin.ModelAdmin):
    list_display = ('server', 'port', 'username', 'remote_directory', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    exclude = ('password',)  # Don't show password in admin


