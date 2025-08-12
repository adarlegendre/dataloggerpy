#!/usr/bin/env python3
"""
Network Connectivity Test for CP5200 Display
Tests if the display at 192.168.1.200:5200 is reachable
"""

import socket
import time
import sys

def test_tcp_connectivity(host, port, timeout=5):
    """Test TCP connectivity to the display"""
    print(f"Testing TCP connectivity to {host}:{port}...")
    
    try:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # Attempt connection
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"✓ SUCCESS: Connected to {host}:{port}")
            sock.close()
            return True
        else:
            print(f"✗ FAILED: Could not connect to {host}:{port}")
            print(f"  Error code: {result}")
            sock.close()
            return False
            
    except socket.timeout:
        print(f"✗ TIMEOUT: Connection to {host}:{port} timed out after {timeout}s")
        return False
    except socket.error as e:
        print(f"✗ ERROR: Socket error: {e}")
        return False
    except Exception as e:
        print(f"✗ ERROR: Unexpected error: {e}")
        return False

def test_ping(host):
    """Test basic network reachability using ping"""
    print(f"Testing basic network reachability to {host}...")
    
    try:
        import subprocess
        result = subprocess.run(['ping', '-c', '3', '-W', '5', host], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(f"✓ SUCCESS: {host} is reachable")
            return True
        else:
            print(f"✗ FAILED: {host} is not reachable")
            print(f"  Ping output: {result.stdout}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"✗ TIMEOUT: Ping to {host} timed out")
        return False
    except FileNotFoundError:
        print("⚠ WARNING: ping command not found, skipping ping test")
        return True
    except Exception as e:
        print(f"✗ ERROR: Ping test failed: {e}")
        return False

def test_port_scan(host, start_port=5195, end_port=5205):
    """Scan a range of ports to see what's open"""
    print(f"Scanning ports {start_port}-{end_port} on {host}...")
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((host, port))
            sock.close()
            
            if result == 0:
                open_ports.append(port)
                print(f"  ✓ Port {port} is open")
            else:
                print(f"  ✗ Port {port} is closed")
                
        except Exception as e:
            print(f"  ? Port {port}: Error testing")
    
    return open_ports

def main():
    """Main test function"""
    host = "192.168.1.222"
    port = 5200
    
    print("CP5200 Network Connectivity Test")
    print("=" * 40)
    print(f"Target: {host}:{port}")
    print()
    
    # Test 1: Basic ping
    ping_success = test_ping(host)
    print()
    
    # Test 2: Port scan around 5200
    open_ports = test_port_scan(host)
    print()
    
    # Test 3: Specific port test
    port_success = test_tcp_connectivity(host, port)
    print()
    
    # Summary
    print("=" * 40)
    print("TEST SUMMARY:")
    print(f"  Network reachability: {'✓' if ping_success else '✗'}")
    print(f"  Port {port} connectivity: {'✓' if port_success else '✗'}")
    
    if open_ports:
        print(f"  Open ports found: {', '.join(map(str, open_ports))}")
    
    print()
    
    if ping_success and port_success:
        print("🎉 All tests passed! Your CP5200 display is ready for communication.")
        print("You can now run the main examples:")
        print("  ./simple_example")
        print("  python3 quick_start.py")
    elif ping_success and not port_success:
        print("⚠ Network is reachable but port 5200 is not accessible.")
        print("  - Check if the display is powered on")
        print("  - Verify the display is configured for port 5200")
        print("  - Check firewall settings on the display")
    elif not ping_success:
        print("❌ Network connectivity failed.")
        print("  - Check your network connection")
        print("  - Verify the IP address 192.168.1.222")
        print("  - Check if the display is powered on")
    else:
        print("❌ Multiple issues detected. Check network and display configuration.")
    
    return 0 if (ping_success and port_success) else 1

if __name__ == "__main__":
    sys.exit(main())
