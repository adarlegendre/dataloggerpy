# PowerShell script to run continuous display data sender
Write-Host "Starting Continuous Display Data Sender..." -ForegroundColor Green
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path "venv\Scripts\Activate.ps1")) {
    Write-Host "Virtual environment not found. Please run setup first." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Activate virtual environment
& "venv\Scripts\Activate.ps1"

# Run the continuous sender
Write-Host "Running continuous display sender to port 80..." -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop" -ForegroundColor Cyan
Write-Host ""

try {
    python continuous_display_sender.py --ip localhost --port 80 --interval 5
}
catch {
    Write-Host "Error running the script: $_" -ForegroundColor Red
}
finally {
    Read-Host "Press Enter to exit"
} 