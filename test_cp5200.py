#!/usr/bin/env python3
"""
Test script for CP5200 VMS display protocol
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.services import build_cp5200_protocol, get_effect_code, get_alignment_code, get_color_code
from app.models import DisplayConfig

def test_cp5200_protocol():
    """Test the CP5200 protocol implementation"""
    
    # Create a test display config
    config = DisplayConfig(
        ip_address='192.168.1.222',
        port=8080,
        font_size=16,
        effect_type='draw',
        justify='center',
        color='red',
        test_message='1A2 3456'
    )
    
    print("Testing CP5200 Protocol Implementation")
    print("=" * 50)
    print(f"Text: {config.test_message}")
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
    
    # Compare with expected sample
    print("Expected sample from your specification:")
    print("FF FF FF FF 2D 00 00 00 68 32 01 7B 01 22 00 00")
    print("00 02 00 00 01 06 00 00 12 00 31 12 00 41 12 00")
    print("32 12 00 20 12 00 33 12 00 34 12 00 35 12 00 36")
    print("00 00 00 68 03")
    print()
    
    print("Our generated protocol:")
    hex_data = protocol_data.hex()
    for i in range(0, len(hex_data), 32):
        print(hex_data[i:i+32])
    
    return protocol_data

if __name__ == "__main__":
    test_cp5200_protocol() 