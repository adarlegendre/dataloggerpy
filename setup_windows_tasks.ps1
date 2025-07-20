# PowerShell script to set up Windows Task Scheduler for radar notifications
# Run this script as Administrator

param(
    [string]$ProjectPath = $PSScriptRoot,
    [string]$TaskName = "RadarNotificationTask"
)

Write-Host "Setting up Windows Task Scheduler for radar notifications..." -ForegroundColor Green

# Get the Python executable path
$PythonPath = Join-Path $ProjectPath "venv\Scripts\python.exe"
$ManagePyPath = Join-Path $ProjectPath "manage.py"

# Check if Python exists
if (-not (Test-Path $PythonPath)) {
    Write-Host "Error: Python executable not found at $PythonPath" -ForegroundColor Red
    Write-Host "Make sure the virtual environment is set up correctly." -ForegroundColor Yellow
    exit 1
}

# Check if manage.py exists
if (-not (Test-Path $ManagePyPath)) {
    Write-Host "Error: manage.py not found at $ManagePyPath" -ForegroundColor Red
    exit 1
}

# Create logs directory
$LogsDir = Join-Path $ProjectPath "logs"
if (-not (Test-Path $LogsDir)) {
    New-Item -ItemType Directory -Path $LogsDir -Force | Out-Null
    Write-Host "Created logs directory: $LogsDir" -ForegroundColor Green
}

# Remove existing task if it exists
try {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host "Removed existing task: $TaskName" -ForegroundColor Yellow
} catch {
    # Task doesn't exist, which is fine
}

# Create the action
$Action = New-ScheduledTaskAction -Execute $PythonPath -Argument "`"$ManagePyPath`" check_notification_schedule" -WorkingDirectory $ProjectPath

# Create the trigger (run every minute)
$Trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 1) -RepetitionDuration (New-TimeSpan -Days 365)

# Create the settings
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RunOnlyIfNetworkAvailable

# Create the principal (run as current user)
$Principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Highest

# Register the task
try {
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Principal $Principal -Description "Radar notification system - runs check_notification_schedule every minute"
    Write-Host "Successfully created scheduled task: $TaskName" -ForegroundColor Green
} catch {
    Write-Host "Error creating scheduled task: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Make sure you're running this script as Administrator." -ForegroundColor Yellow
    exit 1
}

# Test the task
Write-Host "Testing the scheduled task..." -ForegroundColor Yellow
try {
    Start-ScheduledTask -TaskName $TaskName
    Write-Host "Task started successfully!" -ForegroundColor Green
} catch {
    Write-Host "Warning: Could not start task for testing: $($_.Exception.Message)" -ForegroundColor Yellow
}

Write-Host "`nSetup completed!" -ForegroundColor Green
Write-Host "The task '$TaskName' will run every minute and check for notifications." -ForegroundColor Cyan
Write-Host "You can manage this task in Windows Task Scheduler." -ForegroundColor Cyan
Write-Host "Logs will be written to: $LogsDir" -ForegroundColor Cyan 