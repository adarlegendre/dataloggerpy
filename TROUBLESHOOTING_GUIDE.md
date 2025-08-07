# CP5200 Troubleshooting Guide

## 🔍 **Step-by-Step Troubleshooting**

### **1. Network Scanner First**

Before trying to connect, scan your network to find the device:

```bash
# Scan for CP5200 devices
python network_scanner.py --scan

# Test specific device
python network_scanner.py --test 192.168.1.222

# Scan different network range
python network_scanner.py --scan --network 192.168.0.0/24
```

### **2. Common Issues and Solutions**

#### **❌ Issue: Connection Timeout**

**Symptoms:**
- `Failed to connect: [Errno 110] Connection timed out`
- `Failed to connect: [Errno 111] Connection refused`

**Solutions:**
1. **Check IP Address:**
   ```bash
   # Verify the device IP
   ping 192.168.1.222
   ```

2. **Check Port:**
   ```bash
   # Test if port 5200 is open
   telnet 192.168.1.222 5200
   # or
   nc -zv 192.168.1.222 5200
   ```

3. **Check Network Configuration:**
   ```bash
   # Check your network interface
   ip addr show
   
   # Check routing
   ip route show
   ```

#### **❌ Issue: Device Not Found**

**Solutions:**
1. **Scan Different Network Ranges:**
   ```bash
   python network_scanner.py --scan --network 192.168.0.0/24
   python network_scanner.py --scan --network 10.0.0.0/24
   python network_scanner.py --scan --network 172.16.0.0/24
   ```

2. **Check Device Settings:**
   - Verify the display is powered on
   - Check if the display has a static IP or DHCP
   - Look for network settings on the display itself

#### **❌ Issue: Protocol Errors**

**Symptoms:**
- `Failed to send message: [Errno 32] Broken pipe`
- No response from device

**Solutions:**
1. **Check Packet Structure:**
   - Verify the device expects the same protocol
   - Try different packet formats

2. **Test with Different Parameters:**
   ```python
   # Try different settings
   controller.send_instant_message("TEST", font_size=16, color=0xFF0000, effect=1, speed=5, stay_time=3)
   ```

### **3. Network Configuration**

#### **Check Your Network:**
```bash
# Check your IP address
ip addr show

# Check network connectivity
ping 8.8.8.8

# Check if you're on the same network as the device
ip route show
```

#### **Common Network Configurations:**
- **Device IP**: 192.168.1.222
- **Your IP**: Should be 192.168.1.x (same subnet)
- **Gateway**: Usually 192.168.1.1
- **Subnet**: 255.255.255.0

### **4. Device-Specific Issues**

#### **CP5200 Display Settings:**
1. **Network Mode**: Ensure the display is in network mode
2. **IP Address**: Verify the IP is set correctly
3. **Port**: Default is 5200, but could be different
4. **Protocol**: Should be TCP/IP

#### **Display Configuration:**
- Check if the display has a web interface (try http://192.168.1.222)
- Look for configuration menus on the display
- Check for any password or authentication requirements

### **5. Testing Commands**

#### **Basic Network Tests:**
```bash
# Test basic connectivity
ping 192.168.1.222

# Test port connectivity
telnet 192.168.1.222 5200

# Scan for open ports
nmap -p 5200,23,22,80,8080 192.168.1.222
```

#### **Python Tests:**
```python
# Test basic socket connection
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)
result = sock.connect_ex(('192.168.1.222', 5200))
print(f"Connection result: {result}")
sock.close()
```

### **6. Alternative Connection Methods**

#### **Serial Connection (if network fails):**
```python
import serial

# Try serial connection
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=5)
# Send serial commands instead of network
```

#### **Different Ports:**
```python
# Try different ports
ports = [5200, 23, 22, 80, 8080, 5000, 5001]

for port in ports:
    try:
        controller = CP5200Controller(ip_address='192.168.1.222', port=port)
        if controller.connect():
            print(f"✅ Connected on port {port}")
            break
    except:
        continue
```

### **7. Debug Mode**

Enable debug logging to see what's happening:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Run with debug output
controller = CP5200Controller(ip_address='192.168.1.222', port=5200)
controller.connect()
```

### **8. Common Solutions**

#### **Solution 1: Wrong IP Address**
```bash
# Scan your network to find the device
python network_scanner.py --scan
```

#### **Solution 2: Wrong Port**
```bash
# Test different ports
python network_scanner.py --test 192.168.1.222 --port 23
python network_scanner.py --test 192.168.1.222 --port 80
```

#### **Solution 3: Network Issues**
```bash
# Check if you're on the same network
ip addr show
ip route show

# Try connecting to gateway
ping 192.168.1.1
```

#### **Solution 4: Device Not Powered/Connected**
- Check if the display is powered on
- Check network cable connection
- Check if the display has network activity lights

### **9. Quick Test Script**

```python
#!/usr/bin/env python3
import socket
import struct

def quick_test(ip, port=5200):
    print(f"Testing {ip}:{port}")
    
    try:
        # Test 1: Basic connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print("✅ Port is open")
            
            # Test 2: Send test packet
            test_packet = b'\xFF\xFF\xFF\xFF\x08\x00\x00\x00\x68\x32\x01\x7B'
            sock.send(test_packet)
            
            # Test 3: Try to read response
            try:
                response = sock.recv(10)
                print(f"✅ Got response: {response.hex()}")
            except socket.timeout:
                print("⚠️  No response (this might be normal)")
            
            sock.close()
            return True
        else:
            print(f"❌ Port {port} is closed")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# Test the device
quick_test('192.168.1.222', 5200)
```

### **10. Next Steps**

1. **Run the network scanner first**
2. **Check basic connectivity**
3. **Test different ports**
4. **Verify device settings**
5. **Try alternative connection methods**

**If nothing works, the device might be:**
- On a different IP address
- Using a different port
- Not configured for network communication
- Using a different protocol
- Not powered on or connected 