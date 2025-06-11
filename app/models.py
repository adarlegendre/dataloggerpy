from django.db import models

# Create your models here.

class SystemSettings(models.Model):
    system_name = models.CharField(max_length=100, default="Secure Login")
    login_title = models.CharField(max_length=100, default="Welcome Back")
    primary_color = models.CharField(max_length=7, default="#1a237e")
    secondary_color = models.CharField(max_length=7, default="#283593")
    accent_color = models.CharField(max_length=7, default="#3949ab")
    text_color = models.CharField(max_length=7, default="#2b2d42")
    background_color = models.CharField(max_length=7, default="#f8f9fa")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "System Settings"
        verbose_name_plural = "System Settings"

    def __str__(self):
        return f"Settings (Last updated: {self.updated_at})"

    @classmethod
    def get_settings(cls):
        settings = cls.objects.first()
        if not settings:
            settings = cls.objects.create()
        return settings
