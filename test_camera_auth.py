#!/usr/bin/env python3
"""
Test script to verify camera API listener authentication
"""

import requests
import json
import base64
from datetime import datetime

def test_camera_api():
    """Test the camera API listener with authentication"""
    
    # Configuration
    base_url = "http://localhost:5195"
    username = "admin"
    password = "kObliha12@"
    
    # Create basic auth header
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    auth_header = f"Basic {encoded_credentials}"
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_header
    }
    
    print("🧪 Testing Camera API Listener Authentication")
    print(f"📡 URL: {base_url}")
    print(f"🔐 Auth: {username} / {password}")
    print("=" * 50)
    
    # Test 1: Check status (no auth required)
    print("\n1️⃣ Testing status endpoint (no auth)...")
    try:
        response = requests.get(f"{base_url}/status", timeout=5)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Status endpoint working")
            print(f"   📊 Detections: {data.get('detections_received', 0)}")
            print(f"   📷 Target: {data.get('target_camera', 'unknown')}")
        else:
            print(f"   ❌ Status endpoint failed: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Connection failed: {e}")
        return
    
    # Test 2: Test POST without authentication (should fail)
    print("\n2️⃣ Testing POST without authentication (should fail)...")
    test_data = {
        "deviceId": "TEST_CAMERA_001",
        "params": {
            "plateNo": "TEST123",
            "vehicleType": "car",
            "confidence": 95.5,
            "picTime": datetime.now().isoformat(),
            "picInfo": [{"url": "test_image.jpg"}]
        }
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/upark/capture",
            json=test_data,
            timeout=5
        )
        print(f"   Status: {response.status_code}")
        if response.status_code == 401:
            print(f"   ✅ Authentication correctly required")
        else:
            print(f"   ❌ Expected 401, got {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Request failed: {e}")
    
    # Test 3: Test POST with correct authentication (should succeed)
    print("\n3️⃣ Testing POST with correct authentication...")
    try:
        response = requests.post(
            f"{base_url}/api/upark/capture",
            json=test_data,
            headers=headers,
            timeout=5
        )
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print(f"   ✅ Authentication successful!")
            response_data = response.json()
            print(f"   📋 Response: {response_data}")
        else:
            print(f"   ❌ POST failed: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Request failed: {e}")
    
    # Test 4: Test with wrong credentials (should fail)
    print("\n4️⃣ Testing POST with wrong credentials (should fail)...")
    wrong_credentials = f"wrong:password"
    wrong_encoded = base64.b64encode(wrong_credentials.encode()).decode()
    wrong_auth_header = f"Basic {wrong_encoded}"
    
    wrong_headers = {
        'Content-Type': 'application/json',
        'Authorization': wrong_auth_header
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/upark/capture",
            json=test_data,
            headers=wrong_headers,
            timeout=5
        )
        print(f"   Status: {response.status_code}")
        if response.status_code == 401:
            print(f"   ✅ Wrong credentials correctly rejected")
        else:
            print(f"   ❌ Expected 401, got {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Request failed: {e}")
    
    # Test 5: Check final status
    print("\n5️⃣ Checking final status...")
    try:
        response = requests.get(f"{base_url}/status", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"   📊 Total detections: {data.get('detections_received', 0)}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Status check failed: {e}")
    
    print("\n🎉 Authentication test completed!")

if __name__ == "__main__":
    test_camera_api()
