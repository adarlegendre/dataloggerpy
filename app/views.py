from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import SystemSettingsForm
from .models import SystemSettings

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
