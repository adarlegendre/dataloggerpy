# PowerShell script to set up Windows Task Scheduler for daily radar notification emails
# Run this script as Administrator

param(
    [string]$ProjectPath = $PSScriptRoot,
    [string]$TaskName = "RadarDailyNotificationTask"
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Radar Daily Notification Scheduler  " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get the Python executable path
$PythonPath = Join-Path $ProjectPath "venv\Scripts\python.exe"
$ManagePyPath = Join-Path $ProjectPath "manage.py"

# Check if Python exists
if (-not (Test-Path $PythonPath)) {
    Write-Host "❌ Error: Python executable not found at $PythonPath" -ForegroundColor Red
    Write-Host "   Make sure the virtual environment is set up correctly." -ForegroundColor Yellow
    exit 1
}

# Check if manage.py exists
if (-not (Test-Path $ManagePyPath)) {
    Write-Host "❌ Error: manage.py not found at $ManagePyPath" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Found Python at: $PythonPath" -ForegroundColor Green
Write-Host "✓ Found manage.py at: $ManagePyPath" -ForegroundColor Green
Write-Host ""

# Create logs directory
$LogsDir = Join-Path $ProjectPath "logs"
if (-not (Test-Path $LogsDir)) {
    New-Item -ItemType Directory -Path $LogsDir -Force | Out-Null
    Write-Host "✓ Created logs directory: $LogsDir" -ForegroundColor Green
}

# Remove existing task if it exists
Write-Host "Checking for existing task..." -ForegroundColor Yellow
try {
    $ExistingTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    if ($ExistingTask) {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
        Write-Host "✓ Removed existing task: $TaskName" -ForegroundColor Yellow
    }
} catch {
    # Task doesn't exist, which is fine
}

Write-Host ""
Write-Host "Creating scheduled task..." -ForegroundColor Yellow

# Create the action
$Action = New-ScheduledTaskAction -Execute $PythonPath -Argument "`"$ManagePyPath`" check_notification_schedule" -WorkingDirectory $ProjectPath

# Create the trigger (run every minute)
# This allows the check_notification_schedule command to determine if it's time to send
$Trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 1) -RepetitionDuration ([TimeSpan]::MaxValue)

# Create the settings
$Settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -DontStopOnIdleEnd `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 10)

# Create the principal (run as current user)
$Principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Highest

# Register the task
try {
    Register-ScheduledTask `
        -TaskName $TaskName `
        -Action $Action `
        -Trigger $Trigger `
        -Settings $Settings `
        -Principal $Principal `
        -Description "Radar daily notification system - checks every minute if it's time to send summary emails based on configured schedule" `
        -Force
    
    Write-Host "✓ Successfully created scheduled task: $TaskName" -ForegroundColor Green
} catch {
    Write-Host "❌ Error creating scheduled task: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "   Make sure you're running PowerShell as Administrator." -ForegroundColor Yellow
    Write-Host "   Right-click PowerShell and select 'Run as Administrator'" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Testing the scheduled task..." -ForegroundColor Yellow
try {
    Start-ScheduledTask -TaskName $TaskName
    Start-Sleep -Seconds 2
    
    $TaskInfo = Get-ScheduledTask -TaskName $TaskName
    $LastRunTime = (Get-ScheduledTaskInfo -TaskName $TaskName).LastRunTime
    $NextRunTime = (Get-ScheduledTaskInfo -TaskName $TaskName).NextRunTime
    
    Write-Host "✓ Task started successfully!" -ForegroundColor Green
    Write-Host "   Last Run: $LastRunTime" -ForegroundColor Cyan
    Write-Host "   Next Run: $NextRunTime" -ForegroundColor Cyan
} catch {
    Write-Host "⚠ Warning: Could not start task for testing: $($_.Exception.Message)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "           Setup Complete!              " -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "📝 Task Details:" -ForegroundColor Cyan
Write-Host "   Task Name: $TaskName" -ForegroundColor White
Write-Host "   Schedule: Every 1 minute" -ForegroundColor White
Write-Host "   Command: python manage.py check_notification_schedule" -ForegroundColor White
Write-Host "   Log File: $LogsDir\notification_service.log" -ForegroundColor White
Write-Host ""
Write-Host "🎯 What happens next:" -ForegroundColor Cyan
Write-Host "   1. The task runs every minute" -ForegroundColor White
Write-Host "   2. It checks your notification settings" -ForegroundColor White
Write-Host "   3. If it's time to send (e.g., 00:00), it sends the daily summary" -ForegroundColor White
Write-Host "   4. Email includes aggregated detection data as JSON" -ForegroundColor White
Write-Host ""
Write-Host "⚙️  Manage the task:" -ForegroundColor Cyan
Write-Host "   • Open Task Scheduler: Win+R, type 'taskschd.msc'" -ForegroundColor White
Write-Host "   • View task status: Get-ScheduledTask -TaskName '$TaskName'" -ForegroundColor White
Write-Host "   • View task history: Get-ScheduledTaskInfo -TaskName '$TaskName'" -ForegroundColor White
Write-Host "   • Remove task: Unregister-ScheduledTask -TaskName '$TaskName'" -ForegroundColor White
Write-Host ""
Write-Host "📊 Test the email system:" -ForegroundColor Cyan
Write-Host "   python manage.py test_summary_email --preview" -ForegroundColor White
Write-Host ""
Write-Host "📋 View logs:" -ForegroundColor Cyan
Write-Host "   Get-Content $LogsDir\notification_service.log -Tail 50" -ForegroundColor White
Write-Host ""

