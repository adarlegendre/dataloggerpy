#!/usr/bin/env python3
"""
Test script for CP5200 VMS display protocol - Send sample license plate
"""

import sys
import os
import socket
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.services import build_cp5200_protocol, get_effect_code, get_alignment_code, get_color_code, send_cp5200_message
from app.models import DisplayConfig

def send_sample_plate(ip_address='192.168.1.222', port=80, continuous=False, interval=3):
    """Send a sample Czech license plate to the display"""
    
    # Create a test display config for Czech license plate
    config = DisplayConfig(
        ip_address=ip_address,
        port=port,
        font_size=16,
        effect_type='draw',
        justify='center',
        color='red',
        test_message='ABC 1234'  # Czech license plate format
    )
    
    print("Sending Czech License Plates to Display")
    print("=" * 60)
    print(f"Target: {config.ip_address}:{config.port}")
    print(f"Font Size: {config.font_size}")
    print(f"Effect Type: {config.effect_type}")
    print(f"Alignment: {config.justify}")
    print(f"Color: {config.color}")
    print(f"Continuous Mode: {'Yes' if continuous else 'No'}")
    if continuous:
        print(f"Interval: {interval} seconds")
    print()
    
    # Sample license plates to cycle through
    sample_plates = [
        "ABC 1234",
        "XYZ 5678", 
        "DEF 9012",
        "GHI 3456",
        "JKL 7890",
        "MNO 2345",
        "PQR 6789",
        "STU 0123"
    ]
    
    plate_index = 0
    message_counter = 0
    
    try:
        if continuous:
            print("Starting continuous sending... Press Ctrl+C to stop")
            print()
            
            while True:
                # Get current plate
                current_plate = sample_plates[plate_index]
                message_counter += 1
                
                # Send the license plate to the display
                send_cp5200_message(current_plate, config.ip_address, config.port, config)
                print(f"[{message_counter:03d}] ✓ Sent '{current_plate}' to {config.ip_address}:{config.port}")
                
                # Move to next plate
                plate_index = (plate_index + 1) % len(sample_plates)
                
                # Wait for next interval
                time.sleep(interval)
                
        else:
            # Send just a few sample plates
            for i, plate in enumerate(sample_plates[:3]):
                send_cp5200_message(plate, config.ip_address, config.port, config)
                print(f"✓ Successfully sent '{plate}' to {config.ip_address}:{config.port}")
                
                if i < 2:  # Don't sleep after the last one
                    time.sleep(2)
            
            print("\n✓ All sample plates sent successfully!")
        
    except KeyboardInterrupt:
        if continuous:
            print("\n\n✓ Continuous sending stopped by user")
        else:
            print("\n\n✓ Sending interrupted by user")
    except Exception as e:
        print(f"✗ Error sending to display: {str(e)}")
        print("\nTroubleshooting tips:")
        print("- Check if the display is powered on and connected")
        print("- Verify the IP address and port are correct")
        print("- Check network connectivity")
        print("- Try running as administrator (for port 80)")

def test_protocol_only(ip_address='192.168.1.222', port=80):
    """Test the CP5200 protocol implementation without sending"""
    
    # Create a test display config for Czech license plate
    config = DisplayConfig(
        ip_address=ip_address,
        port=port,
        font_size=16,
        effect_type='draw',
        justify='center',
        color='red',
        test_message='ABC 1234'  # Czech license plate format
    )
    
    print("Testing CP5200 Protocol Implementation - Czech License Plate")
    print("=" * 60)
    print(f"Czech License Plate: {config.test_message}")
    print(f"Font Size: {config.font_size}")
    print(f"Effect Type: {config.effect_type} (code: {get_effect_code(config.effect_type)})")
    print(f"Alignment: {config.justify} (code: {get_alignment_code(config.justify)})")
    print(f"Color: {config.color} (code: {get_color_code(config.color)})")
    print()
    
    # Build protocol data
    protocol_data = build_cp5200_protocol(config.test_message, config)
    
    print("Protocol Data (hex):")
    print(protocol_data.hex())
    print()
    
    print("Protocol Data (bytes):")
    for i, byte in enumerate(protocol_data):
        if i % 16 == 0:
            print(f"{i:04x}: ", end="")
        print(f"{byte:02x} ", end="")
        if i % 16 == 15:
            print()
    print()
    
    return protocol_data

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Test CP5200 display protocol')
    parser.add_argument('--ip', default='192.168.1.222', help='Target IP address (default: 192.168.1.222)')
    parser.add_argument('--port', type=int, default=80, help='Target port (default: 80)')
    parser.add_argument('--continuous', action='store_true', help='Send continuously (default: send 3 samples)')
    parser.add_argument('--interval', type=int, default=3, help='Interval between sends in seconds (default: 3)')
    parser.add_argument('--test-only', action='store_true', help='Only test protocol, don\'t send to display')
    
    args = parser.parse_args()
    
    if args.test_only:
        test_protocol_only(args.ip, args.port)
    else:
        send_sample_plate(args.ip, args.port, args.continuous, args.interval) 