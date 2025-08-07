#!/usr/bin/env python3
"""
Simple test script for CP5200 LED Display at 192.168.1.222
"""

import socket
import time

def test_connection(ip='192.168.1.222', port=5200):
    """Test basic connection to CP5200 display"""
    print(f"Testing connection to {ip}:{port}")
    print("=" * 50)
    
    try:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        
        # Try to connect
        print("Attempting to connect...")
        sock.connect((ip, port))
        print("✓ Connection successful!")
        
        # Test ping
        print("\nTesting ping...")
        import subprocess
        result = subprocess.run(['ping', '-c', '3', ip], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Ping successful!")
        else:
            print("⚠ Ping failed, but socket connection works")
        
        # Close connection
        sock.close()
        return True
        
    except socket.timeout:
        print("✗ Connection timeout")
        return False
    except ConnectionRefusedError:
        print("✗ Connection refused - check if display is powered on and port 5200 is open")
        return False
    except Exception as e:
        print(f"✗ Connection failed: {e}")
        return False

def test_network_connectivity(ip='192.168.1.222'):
    """Test basic network connectivity"""
    print(f"\nTesting network connectivity to {ip}")
    print("=" * 50)
    
    # Test ping
    import subprocess
    print("Running ping test...")
    result = subprocess.run(['ping', '-c', '4', ip], 
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✓ Ping successful!")
        # Extract ping statistics
        lines = result.stdout.split('\n')
        for line in lines:
            if 'packets transmitted' in line:
                print(f"  {line.strip()}")
            elif 'min/avg/max' in line:
                print(f"  {line.strip()}")
    else:
        print("✗ Ping failed")
        print("  This could mean:")
        print("  1. Display is not powered on")
        print("  2. Display is not connected to network")
        print("  3. IP address is incorrect")
        print("  4. Network connectivity issues")
    
    return result.returncode == 0

def main():
    print("CP5200 LED Display Connection Test")
    print("=" * 50)
    
    ip = '192.168.1.222'
    port = 5200
    
    # Test network connectivity first
    network_ok = test_network_connectivity(ip)
    
    # Test socket connection
    socket_ok = test_connection(ip, port)
    
    print("\n" + "=" * 50)
    print("SUMMARY:")
    print(f"Network connectivity: {'✓ OK' if network_ok else '✗ FAILED'}")
    print(f"Socket connection: {'✓ OK' if socket_ok else '✗ FAILED'}")
    
    if network_ok and socket_ok:
        print("\n🎉 All tests passed! Your CP5200 display is ready to use.")
        print("\nYou can now run the main controller:")
        print("  python3 cp5200_raspberry_pi.py")
        print("\nOr test with a simple message:")
        print("  python3 cp5200_raspberry_pi.py --message 'Hello World!'")
        
    elif network_ok and not socket_ok:
        print("\n⚠ Network is reachable but socket connection failed.")
        print("This might mean:")
        print("1. Display is not listening on port 5200")
        print("2. Firewall is blocking the connection")
        print("3. Display needs to be restarted")
        
    elif not network_ok:
        print("\n✗ Network connectivity failed.")
        print("Please check:")
        print("1. Display is powered on")
        print("2. Display is connected to the same network")
        print("3. IP address is correct")
        print("4. Network cables are properly connected")

if __name__ == "__main__":
    main() 