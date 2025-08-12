# Quick Start Guide for Network CP5200 Testing

This guide is specifically for testing your CP5200 display at **192.168.1.200:5200**.

## **Step-by-Step Testing Process**

### **1. Build the Library**
```bash
cd cp5200
chmod +x build_raspberry_pi.sh
./build_raspberry_pi.sh
```

### **2. Test Network Connectivity (IMPORTANT!)**
Before running the main examples, test if your display is reachable:
```bash
cd build
python3 ../test_network.py
```

**Expected Output:**
```
CP5200 Network Connectivity Test
========================================
Target: 192.168.1.200:5200

Testing basic network reachability to 192.168.1.200...
✓ SUCCESS: 192.168.1.200 is reachable

Scanning ports 5195-5205 on 192.168.1.200...
  ✗ Port 5195 is closed
  ✗ Port 5196 is closed
  ✗ Port 5197 is closed
  ✗ Port 5198 is closed
  ✗ Port 5199 is closed
  ✓ Port 5200 is open
  ✗ Port 5201 is closed
  ✗ Port 5202 is closed
  ✗ Port 5203 is closed
  ✗ Port 5204 is closed
  ✗ Port 5205 is closed

Testing TCP connectivity to 192.168.1.200:5200...
✓ SUCCESS: Connected to 192.168.1.200:5200

========================================
TEST SUMMARY:
  Network reachability: ✓
  Port 5200 connectivity: ✓
  Open ports found: 5200

🎉 All tests passed! Your CP5200 display is ready for communication.
```

### **3. Test Library Configuration**
```bash
./test_cp5200
```

This tests the library functions without sending data to the display.

### **4. Test Actual Communication**
```bash
./simple_example
```

**What Will Be Sent to Your Display:**
- **Window 0**: "Hello Raspberry Pi!" in **RED** color
- **Window 1**: "CP5200 Library" in **GREEN** color  
- **Clock display** in window 0 (yellow text)
- **Brightness** set to level 20
- **Time synchronization** with your Raspberry Pi

### **5. Test Python Wrapper (Optional)**
```bash
cd ..
python3 quick_start.py
```

## **Troubleshooting Network Issues**

### **If Network Test Fails:**

1. **Check Display Power**
   - Ensure the CP5200 display is powered on
   - Check power LED indicators

2. **Verify IP Address**
   - Confirm the display is configured for 192.168.1.200
   - Check display configuration menu

3. **Check Network Connection**
   ```bash
   ping 192.168.1.200
   ```

4. **Check Port Configuration**
   - Verify the display is listening on port 5200
   - Check display network settings

5. **Firewall Issues**
   - Ensure port 5200 is not blocked
   - Check both Raspberry Pi and display firewall settings

### **Common Error Codes:**

- **Connection refused**: Display not listening on port 5200
- **Connection timeout**: Network connectivity issues
- **Permission denied**: Firewall blocking the connection

## **Display Configuration Tips**

### **For CP5200 Display:**
1. **Network Settings**
   - IP Address: 192.168.1.200
   - Port: 5200
   - Gateway: Your router's IP (e.g., 192.168.1.1)
   - Subnet: 255.255.255.0

2. **Communication Protocol**
   - Ensure TCP/IP mode is enabled
   - Disable RS232/RS485 if not needed

3. **Display Settings**
   - Set appropriate brightness
   - Configure display resolution
   - Enable network communication

## **What to Expect**

### **Successful Communication:**
- Text appears on the display
- Colors display correctly
- Clock shows current time
- No error messages in console

### **Failed Communication:**
- Console shows error codes
- Display remains unchanged
- Network timeout messages

## **Next Steps After Successful Testing**

1. **Customize the Messages**
   - Edit `simple_example.cpp` to change text
   - Modify colors and effects
   - Adjust timing parameters

2. **Create Your Own Application**
   - Use the library functions in your code
   - Implement dynamic content updates
   - Add error handling and retry logic

3. **Production Deployment**
   - Remove debug output
   - Add logging and monitoring
   - Implement health checks

## **Files to Use**

- **`test_network.py`**: Test network connectivity first
- **`test_cp5200`**: Test library functions
- **`simple_example`**: Test actual display communication
- **`quick_start.py`**: Python wrapper example

## **Quick Commands Summary**

```bash
# Build everything
./build_raspberry_pi.sh

# Test network first
python3 ../test_network.py

# Test library
./test_cp5200

# Test display communication
./simple_example

# Test Python wrapper
python3 ../quick_start.py
```

**Remember**: Always run the network test first to ensure your display is reachable before attempting communication!
