@echo off
echo Starting Continuous Display Data Sender...
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Virtual environment not found. Please run setup first.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the continuous sender
echo Running continuous display sender to port 80...
echo Press Ctrl+C to stop
echo.

python continuous_display_sender.py --ip localhost --port 80 --interval 5

pause 