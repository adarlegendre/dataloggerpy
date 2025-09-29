#!/usr/bin/env python3
"""
Enable debug logging for Django to see radar data processing
"""

import os
import sys
import django
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

import logging

def enable_debug_logging():
    """Enable debug logging for the radar service"""
    print("Enabling debug logging...")
    
    # Get the logger for the radar service
    logger = logging.getLogger('app.services')
    
    # Set level to DEBUG
    logger.setLevel(logging.DEBUG)
    
    # Create a console handler if it doesn't exist
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(console_handler)
    
    print("✅ Debug logging enabled for radar service")
    print("Now restart Django to see debug logs")

def check_current_logging():
    """Check current logging configuration"""
    print("Current logging configuration:")
    print("=============================")
    
    # Check root logger
    root_logger = logging.getLogger()
    print(f"Root logger level: {logging.getLevelName(root_logger.level)}")
    
    # Check app.services logger
    app_logger = logging.getLogger('app.services')
    print(f"App.services logger level: {logging.getLevelName(app_logger.level)}")
    print(f"App.services logger handlers: {len(app_logger.handlers)}")
    
    # Check Django logger
    django_logger = logging.getLogger('django')
    print(f"Django logger level: {logging.getLevelName(django_logger.level)}")

if __name__ == "__main__":
    check_current_logging()
    print()
    enable_debug_logging()
