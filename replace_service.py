#!/usr/bin/env python3
"""
Script to replace the existing RadarDataService with the enhanced version
This will backup the original and replace it with A+XXX format support
"""

import shutil
import os
from pathlib import Path

def backup_and_replace_service():
    """Backup the original service and replace with enhanced version"""
    
    # Paths
    original_service = Path("app/services.py")
    enhanced_service = Path("app/services_enhanced.py")
    backup_service = Path("app/services_backup.py")
    
    # Check if files exist
    if not original_service.exists():
        print("Error: app/services.py not found!")
        return False
    
    if not enhanced_service.exists():
        print("Error: app/services_enhanced.py not found!")
        return False
    
    try:
        # Backup original service
        if backup_service.exists():
            print(f"Backup already exists: {backup_service}")
        else:
            shutil.copy2(original_service, backup_service)
            print(f"Backed up original service to: {backup_service}")
        
        # Replace with enhanced service
        shutil.copy2(enhanced_service, original_service)
        print(f"Replaced app/services.py with enhanced version")
        
        # Update the class name in the new file
        with open(original_service, 'r') as f:
            content = f.read()
        
        # Replace class name and instance creation
        content = content.replace('class EnhancedRadarDataService:', 'class RadarDataService:')
        content = content.replace('enhanced_service = EnhancedRadarDataService()', '')
        
        with open(original_service, 'w') as f:
            f.write(content)
        
        print("Updated class name to RadarDataService")
        print("\n✅ Successfully replaced RadarDataService with A+XXX format support!")
        print("\nNext steps:")
        print("1. Restart your Django application")
        print("2. Check the logs to see if it's working with your A+XXX format")
        print("3. If you need to revert, restore from app/services_backup.py")
        
        return True
        
    except Exception as e:
        print(f"Error during replacement: {e}")
        return False

def restore_original_service():
    """Restore the original service from backup"""
    
    original_service = Path("app/services.py")
    backup_service = Path("app/services_backup.py")
    
    if not backup_service.exists():
        print("Error: No backup found at app/services_backup.py")
        return False
    
    try:
        shutil.copy2(backup_service, original_service)
        print("✅ Restored original RadarDataService")
        return True
    except Exception as e:
        print(f"Error during restoration: {e}")
        return False

if __name__ == "__main__":
    print("RadarDataService Replacement Tool")
    print("=================================")
    print("1. Replace with enhanced service (A+XXX format support)")
    print("2. Restore original service")
    print("3. Exit")
    
    choice = input("Enter choice (1, 2, or 3): ").strip()
    
    if choice == "1":
        backup_and_replace_service()
    elif choice == "2":
        restore_original_service()
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice. Exiting...")
