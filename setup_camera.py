#!/usr/bin/env python3
"""
Setup Camera Configuration and Test Connection
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.models import CameraConfig, CameraDetection

def setup_camera():
    """Setup camera configuration"""
    print("=== Camera Setup ===\n")
    
    # Camera details from the image
    camera_data = {
        'name': 'ANPR Camera',
        'ip_address': '192.168.2.13',
        'port': 5000,
        'username': 'admin',
        'password': 'kObliha12@',
        'protocol': 'VIID_2017',
        'is_active': True
    }
    
    print("📷 Setting up camera configuration...")
    print(f"  Name: {camera_data['name']}")
    print(f"  IP: {camera_data['ip_address']}")
    print(f"  Port: {camera_data['port']}")
    print(f"  Username: {camera_data['username']}")
    print(f"  Protocol: {camera_data['protocol']}")
    
    # Create or update camera config
    camera, created = CameraConfig.objects.get_or_create(
        ip_address=camera_data['ip_address'],
        port=camera_data['port'],
        defaults=camera_data
    )
    
    if created:
        print("✅ Camera configuration created")
    else:
        # Update existing config
        for key, value in camera_data.items():
            setattr(camera, key, value)
        camera.save()
        print("✅ Camera configuration updated")
    
    return camera

def test_camera_connection():
    """Test connection to camera"""
    print("\n🔍 Testing camera connection...")
    
    try:
        from viid_camera_listener import VIIDCameraListener
        
        camera = CameraConfig.objects.first()
        if not camera:
            print("❌ No camera configuration found")
            return False
        
        print(f"📡 Testing connection to {camera.ip_address}:{camera.port}")
        
        listener = VIIDCameraListener(
            camera_ip=camera.ip_address,
            camera_port=camera.port,
            username=camera.username,
            password=camera.password
        )
        
        # Test connection
        if listener.connect_to_camera():
            print("✅ Camera connection successful!")
            listener.socket.close()
            return True
        else:
            print("❌ Camera connection failed")
            return False
            
    except Exception as e:
        print(f"❌ Error testing camera connection: {e}")
        return False

def create_test_detection():
    """Create a test camera detection"""
    print("\n🧪 Creating test camera detection...")
    
    camera = CameraConfig.objects.first()
    if not camera:
        print("❌ No camera configuration found")
        return
    
    from datetime import datetime
    from django.utils import timezone
    
    test_detection = CameraDetection.objects.create(
        camera=camera,
        plate_number='ABC123',
        confidence=95.5,
        speed=45.0,
        direction='North',
        vehicle_type='Motor Vehicle',
        timestamp=timezone.now(),
        raw_data='Test detection data',
        data_format='test'
    )
    
    print(f"✅ Test detection created: {test_detection.plate_number}")

def main():
    print("=== Camera Setup and Test ===\n")
    
    # Setup camera configuration
    camera = setup_camera()
    
    # Test connection
    connection_ok = test_camera_connection()
    
    if connection_ok:
        print("\n🎉 Camera setup completed successfully!")
        print("\n📋 Next steps:")
        print("1. Run: python viid_camera_listener.py (to test data reception)")
        print("2. Start the Django camera service")
        print("3. Check the web interface for camera data")
        
        # Create test detection
        create_test = input("\n🧪 Create test detection? (y/n): ")
        if create_test.lower() == 'y':
            create_test_detection()
    else:
        print("\n❌ Camera setup failed")
        print("💡 Please check:")
        print("  - Camera IP address is correct")
        print("  - Camera port is correct")
        print("  - Username and password are correct")
        print("  - Camera is online and configured")
        print("  - Network connectivity")

if __name__ == "__main__":
    main()
