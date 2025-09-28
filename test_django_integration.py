#!/usr/bin/env python3
"""
Test script to verify Django integration with A+XXX format
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
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_radar_config():
    """Test radar configuration"""
    print("Testing Radar Configuration...")
    
    # Get all radar configurations
    radars = RadarConfig.objects.all()
    print(f"Found {radars.count()} radar configurations:")
    
    for radar in radars:
        print(f"  ID: {radar.id}")
        print(f"  Name: {radar.name}")
        print(f"  Port: {radar.port}")
        print(f"  Baud Rate: {radar.baud_rate}")
        print(f"  Active: {radar.is_active}")
        print(f"  Direction Positive: {radar.direction_positive_name}")
        print(f"  Direction Negative: {radar.direction_negative_name}")
        print()
    
    return radars

def test_radar_data_model():
    """Test radar data model"""
    print("Testing Radar Data Model...")
    
    # Get recent radar data
    recent_data = RadarData.objects.all().order_by('-timestamp')[:10]
    print(f"Found {recent_data.count()} recent radar data entries:")
    
    for data in recent_data:
        print(f"  ID: {data.id}")
        print(f"  Radar: {data.radar.name}")
        print(f"  Timestamp: {data.timestamp}")
        print(f"  Range: {data.range}")
        print(f"  Speed: {data.speed}")
        print(f"  Raw Data: {data.raw_data}")
        print(f"  Status: {data.status}")
        print()

def test_service_initialization():
    """Test service initialization"""
    print("Testing Radar Data Service Initialization...")
    
    try:
        service = RadarDataService()
        print("✅ Service initialized successfully")
        
        # Get service status
        status = service.get_service_status()
        print(f"Service status: {status}")
        
        return service
    except Exception as e:
        print(f"❌ Error initializing service: {e}")
        return None

def test_data_parsing():
    """Test data parsing with sample A+XXX format data"""
    print("Testing Data Parsing...")
    
    # Sample A+XXX format data
    sample_data = [
        "A+044",
        "A+047", 
        "A+000",
        "A-042",
        "A-000"
    ]
    
    # Get the first radar config for testing
    radar = RadarConfig.objects.first()
    if not radar:
        print("❌ No radar configuration found. Please create one first.")
        return
    
    print(f"Testing with radar: {radar.name}")
    
    # Test parsing (this would normally be done by the service)
    for data in sample_data:
        print(f"Sample data: {data}")
        
        # Simulate parsing logic
        if len(data) == 5 and data.startswith('A') and data[1] in '+-':
            direction_sign = data[1]
            speed_str = data[2:]
            speed = int(speed_str)
            
            if direction_sign == '+':
                direction = radar.direction_positive_name
            else:
                direction = radar.direction_negative_name
            
            vehicle_present = speed != 0
            
            print(f"  -> Direction: {direction}")
            print(f"  -> Speed: {speed} km/h")
            print(f"  -> Vehicle Present: {vehicle_present}")
            print()

def test_database_save():
    """Test saving A+XXX format data to database"""
    print("Testing Database Save...")
    
    # Get the first radar config
    radar = RadarConfig.objects.first()
    if not radar:
        print("❌ No radar configuration found. Please create one first.")
        return
    
    # Create test radar data
    test_data = RadarData(
        radar=radar,
        range=None,  # No range data in A+XXX format
        speed=44,
        direction=None,
        raw_data="A+044",
        status='success',
        connection_status='connected'
    )
    
    try:
        test_data.save()
        print(f"✅ Saved test data to database: {test_data.raw_data}")
        print(f"   ID: {test_data.id}")
        print(f"   Timestamp: {test_data.timestamp}")
        print(f"   Speed: {test_data.speed}")
        
        # Clean up - delete the test data
        test_data.delete()
        print("   (Test data deleted)")
        
    except Exception as e:
        print(f"❌ Error saving test data: {e}")

def main():
    """Main test function"""
    print("Django Integration Test for A+XXX Format")
    print("========================================")
    print()
    
    # Test 1: Radar Configuration
    radars = test_radar_config()
    print()
    
    # Test 2: Radar Data Model
    test_radar_data_model()
    print()
    
    # Test 3: Service Initialization
    service = test_service_initialization()
    print()
    
    # Test 4: Data Parsing
    test_data_parsing()
    print()
    
    # Test 5: Database Save
    test_database_save()
    print()
    
    print("Test Summary:")
    print("=============")
    print("✅ All tests completed")
    print()
    print("Next steps:")
    print("1. Run 'python replace_service.py' to replace the service")
    print("2. Restart your Django application")
    print("3. Check the logs to see if it's working with your A+XXX format")
    print("4. Monitor the web interface for real-time data")

if __name__ == "__main__":
    main()
