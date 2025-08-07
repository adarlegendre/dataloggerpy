#!/usr/bin/env python3
"""
Example: How to Read Data from CP5200 SDK
Based on the SDK header file functions
"""

import socket
import struct
from datetime import datetime

def read_from_cp5200_sdk():
    """
    Example of reading data from CP5200 using SDK functions
    
    Based on these SDK functions:
    - CP5200_MakeReadTimeData() / CP5200_ParseReadTimeRet()
    - CP5200_MakeGetTempHumiData() / CP5200_ParseGetTempHumiRet()
    - CP5200_MakeReadVersionData() / CP5200_ParseReadVersionRet()
    """
    
    # Connect to CP5200
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect(('192.168.1.222', 5200))
    
    print("Reading data from CP5200 SDK...")
    print("=" * 50)
    
    # 1. READ TIME (CP5200_MakeReadTimeData)
    print("\n1. Reading controller time...")
    try:
        # Build time request packet
        time_packet = bytearray()
        time_packet.extend(struct.pack('<I', 1))  # Card ID
        time_packet.extend(struct.pack('<I', 8))  # Data length
        time_packet.extend(b'\x68\x32\x01\x7B')  # Command
        
        sock.send(time_packet)
        time_response = sock.recv(20)
        
        if time_response and len(time_response) >= 8:
            time_bytes = time_response[4:8]
            timestamp = struct.unpack('<I', time_bytes)[0]
            controller_time = datetime.fromtimestamp(timestamp)
            print(f"   ✓ Controller time: {controller_time}")
        else:
            print("   ✗ Failed to read time")
    except Exception as e:
        print(f"   ✗ Error reading time: {e}")
    
    # 2. READ TEMPERATURE/HUMIDITY (CP5200_MakeGetTempHumiData)
    print("\n2. Reading temperature and humidity...")
    try:
        # Build temp/humi request packet
        temp_packet = bytearray()
        temp_packet.extend(struct.pack('<I', 1))  # Card ID
        temp_packet.extend(struct.pack('<I', 12))  # Data length
        temp_packet.extend(b'\x68\x32\x01\x7B')  # Command
        temp_packet.extend(bytes([0, 0, 0, 0]))  # Flag and padding
        
        sock.send(temp_packet)
        temp_response = sock.recv(20)
        
        if temp_response and len(temp_response) >= 8:
            temp_bytes = temp_response[4:6]
            humi_bytes = temp_response[6:8]
            
            temperature = struct.unpack('<H', temp_bytes)[0] / 10.0
            humidity = struct.unpack('<H', humi_bytes)[0] / 10.0
            
            print(f"   ✓ Temperature: {temperature}°C ({temperature * 9/5 + 32}°F)")
            print(f"   ✓ Humidity: {humidity}%")
        else:
            print("   ✗ Failed to read temperature/humidity")
    except Exception as e:
        print(f"   ✗ Error reading temp/humi: {e}")
    
    # 3. READ VERSION (CP5200_MakeReadVersionData)
    print("\n3. Reading version information...")
    try:
        # Build version request packet
        version_packet = bytearray()
        version_packet.extend(struct.pack('<I', 1))  # Card ID
        version_packet.extend(struct.pack('<I', 8))  # Data length
        version_packet.extend(b'\x68\x32\x01\x7B')  # Command
        
        sock.send(version_packet)
        version_response = sock.recv(50)
        
        if version_response and len(version_response) >= 8:
            version_bytes = version_response[4:]
            version_str = version_bytes.decode('ascii', errors='ignore').strip('\x00')
            print(f"   ✓ Version: {version_str}")
        else:
            print("   ✗ Failed to read version")
    except Exception as e:
        print(f"   ✗ Error reading version: {e}")
    
    # 4. READ TYPE INFO (CP5200_MakeGetTypeInfoData)
    print("\n4. Reading type information...")
    try:
        # Build type info request packet
        type_packet = bytearray()
        type_packet.extend(struct.pack('<I', 1))  # Card ID
        type_packet.extend(struct.pack('<I', 8))  # Data length
        type_packet.extend(b'\x68\x32\x01\x7B')  # Command
        
        sock.send(type_packet)
        type_response = sock.recv(50)
        
        if type_response and len(type_response) >= 8:
            type_bytes = type_response[4:]
            type_str = type_bytes.decode('ascii', errors='ignore').strip('\x00')
            print(f"   ✓ Type info: {type_str}")
        else:
            print("   ✗ Failed to read type info")
    except Exception as e:
        print(f"   ✗ Error reading type info: {e}")
    
    sock.close()
    print("\n" + "=" * 50)
    print("SDK reading example complete!")

if __name__ == "__main__":
    read_from_cp5200_sdk() 