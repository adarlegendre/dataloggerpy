#!/usr/bin/env python3
"""
Django Integration Example
Shows how to integrate the new A+XXX format radar reader with existing Django system
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

from app.models import RadarConfig, RadarData
from app.services import RadarDataService
from modified_serial_reader import ModifiedSerialReader
import time
import logging

logger = logging.getLogger(__name__)

class DjangoRadarIntegration:
    """
    Integration class that connects the new serial reader with Django models
    """
    
    def __init__(self, radar_config_id: int):
        self.radar_config = RadarConfig.objects.get(id=radar_config_id)
        self.serial_reader = None
        self.running = False
        
    def start_reading(self):
        """Start reading radar data and saving to Django models"""
        try:
            # Initialize the serial reader
            self.serial_reader = ModifiedSerialReader(
                port=self.radar_config.port,
                baudrate=self.radar_config.baud_rate,
                timeout=0.01
            )
            
            if not self.serial_reader.start_reading():
                logger.error(f"Failed to start reading from {self.radar_config.port}")
                return False
            
            self.running = True
            logger.info(f"Started reading radar data for {self.radar_config.name}")
            
            # Main reading loop
            while self.running:
                data = self.serial_reader.get_data(timeout=1.0)
                if data:
                    self._save_radar_data(data)
                    
                    # Print statistics every 100 readings
                    if self.serial_reader.total_readings % 100 == 0:
                        stats = self.serial_reader.get_statistics()
                        logger.info(f"Stats for {self.radar_config.name}: {stats}")
                
        except Exception as e:
            logger.error(f"Error in radar reading loop: {e}")
        finally:
            self.stop_reading()
    
    def stop_reading(self):
        """Stop reading radar data"""
        self.running = False
        if self.serial_reader:
            self.serial_reader.stop_reading()
        logger.info(f"Stopped reading radar data for {self.radar_config.name}")
    
    def _save_radar_data(self, data: dict):
        """
        Save radar data to Django model
        
        Args:
            data: Parsed radar data dictionary
        """
        try:
            # Create RadarData instance
            radar_data = RadarData(
                radar=self.radar_config,
                range=None,  # No range data in A+XXX format
                speed=data['speed'],
                direction=None,  # Direction is in the direction_name field
                raw_data=data['raw_data'],
                status='success',
                connection_status='connected'
            )
            
            # Save to database
            radar_data.save()
            
            logger.debug(f"Saved radar data: {data['raw_data']} -> Speed: {data['speed']}km/h")
            
        except Exception as e:
            logger.error(f"Error saving radar data: {e}")
    
    def get_statistics(self) -> dict:
        """Get reading statistics"""
        if self.serial_reader:
            return self.serial_reader.get_statistics()
        return {}


def test_django_integration():
    """Test function for Django integration"""
    print("Testing Django Integration...")
    print("This will read radar data and save it to your Django database")
    print("Press Ctrl+C to stop")
    
    try:
        # Get the first active radar configuration
        radar_configs = RadarConfig.objects.filter(is_active=True)
        if not radar_configs.exists():
            print("No active radar configurations found. Please create one in Django admin.")
            return
        
        radar_config = radar_configs.first()
        print(f"Using radar configuration: {radar_config.name} on {radar_config.port}")
        
        # Create integration instance
        integration = DjangoRadarIntegration(radar_config.id)
        
        # Start reading
        integration.start_reading()
        
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"Error: {e}")


def create_test_radar_config():
    """Create a test radar configuration for testing"""
    try:
        radar_config = RadarConfig.objects.create(
            name="Test Radar A+XXX",
            port="/dev/ttyAMA0",
            baud_rate=9600,
            data_bits=8,
            parity='N',
            stop_bits=1,
            update_interval=100,
            file_save_interval=5,
            data_storage_path='data',
            is_active=True,
            direction_positive_name='Towards Village',
            direction_negative_name='Towards Town'
        )
        print(f"Created test radar configuration: {radar_config.name}")
        return radar_config
    except Exception as e:
        print(f"Error creating test radar configuration: {e}")
        return None


if __name__ == "__main__":
    print("Django Radar Integration Test")
    print("=============================")
    print("1. Test with existing radar configuration")
    print("2. Create test radar configuration and test")
    print("3. List existing radar configurations")
    
    choice = input("Enter choice (1, 2, or 3): ").strip()
    
    if choice == "1":
        test_django_integration()
    elif choice == "2":
        radar_config = create_test_radar_config()
        if radar_config:
            integration = DjangoRadarIntegration(radar_config.id)
            integration.start_reading()
    elif choice == "3":
        radar_configs = RadarConfig.objects.all()
        print(f"\nFound {radar_configs.count()} radar configurations:")
        for config in radar_configs:
            print(f"  ID: {config.id}, Name: {config.name}, Port: {config.port}, Active: {config.is_active}")
    else:
        print("Invalid choice. Running test with existing configuration...")
        test_django_integration()
