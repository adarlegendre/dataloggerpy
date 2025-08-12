# CP5200 Library Installation Guide for Raspberry Pi

This guide provides step-by-step instructions for installing and using the CP5200 LED display library on Raspberry Pi.

## Prerequisites

### Hardware Requirements
- Raspberry Pi (any model with GPIO)
- CP5200 LED display controller
- Connection cable (Ethernet or Serial)
- Power supply for the display

### Software Requirements
- Raspberry Pi OS (Raspbian) or Ubuntu Server
- Internet connection for package installation
- SSH access (recommended)

## Step 1: System Preparation

### 1.1 Update System
```bash
sudo apt update && sudo apt upgrade -y
```

### 1.2 Install Build Tools
```bash
sudo apt install -y build-essential g++ make git cmake
```

### 1.3 Install Additional Dependencies
```bash
sudo apt install -y python3 python3-pip python3-dev
sudo apt install -y libpthread-stubs0-dev
```

## Step 2: Serial Port Configuration (for RS232/RS485)

### 2.1 Enable Serial Interface
```bash
sudo raspi-config
```
Navigate to: **Interface Options** → **Serial Port**
- Enable serial interface: **Yes**
- Disable serial console: **Yes**

### 2.2 Reboot System
```bash
sudo reboot
```

### 2.3 Verify Serial Port
```bash
ls -la /dev/tty*
# You should see /dev/ttyAMA0
```

### 2.4 Set Serial Port Permissions
```bash
sudo usermod -a -G dialout $USER
# Log out and back in, or reboot again
sudo reboot
```

## Step 3: Library Installation

### 3.1 Download Library
```bash
cd ~
# If you have the library files, copy them here
# Otherwise, clone from your repository
```

### 3.2 Build Library

#### Option A: Using Build Script (Recommended)
```bash
cd cp5200
chmod +x build_raspberry_pi.sh
./build_raspberry_pi.sh
```

#### Option B: Using CMake
```bash
cd cp5200
mkdir build && cd build
cmake ..
make -j4
```

#### Option C: Manual Build
```bash
cd cp5200
mkdir build && cd build

# Compile library
g++ -c -O2 -std=c++11 -fPIC ../cp5200/cp5200.cpp -o cp5200.o

# Create static library
ar rcs libcp5200.a cp5200.o
ranlib libcp5200.a

# Create shared library
g++ -shared -fPIC -o libcp5200.so cp5200.o

# Compile examples
g++ -std=c++11 -I.. ../simple_example.cpp -L. -lcp5200 -o simple_example
g++ -std=c++11 -I.. ../test_cp5200.cpp -L. -lcp5200 -o test_cp5200
```

### 3.3 Verify Build
```bash
cd build
ls -la
# You should see:
# - libcp5200.a (static library)
# - libcp5200.so (shared library)
# - simple_example (example program)
# - test_cp5200 (test program)
```

## Step 4: System-Wide Installation (Optional)

### 4.1 Install Libraries
```bash
cd ~/cp5200/build
sudo cp libcp5200.a /usr/local/lib/
sudo cp libcp5200.so /usr/local/lib/
sudo cp ../cp5200/cp5200.h /usr/local/include/
```

### 4.2 Update Library Cache
```bash
sudo ldconfig
```

### 4.3 Verify Installation
```bash
pkg-config --libs cp5200
# Should show: -L/usr/local/lib -lcp5200
```

## Step 5: Testing

### 5.1 Test Library Configuration
```bash
cd ~/cp5200/build
./test_cp5200
```

Expected output:
```
CP5200 Library Test Program
==========================

1. Testing library version...
cp5200 GNU library V3.1

2. Testing debug mode...
Debug mode enabled

[... more test output ...]

All tests completed successfully!
Library is ready for use.
```

### 5.2 Test Basic Functionality
```bash
cd ~/cp5200/build
./simple_example
```

**Note**: This will attempt to communicate with a CP5200 display. 
If no display is connected, you'll see communication errors, but the program will run.

## Step 6: Python Integration (Optional)

### 6.1 Install Python Dependencies
```bash
pip3 install ctypes
```

### 6.2 Test Python Wrapper
```bash
cd ~/cp5200
python3 quick_start.py
```

## Step 7: Configuration

### 7.1 Network Configuration (TCP/IP Mode)
If using network communication:

```bash
# Check network connectivity
ping 192.168.1.100  # Replace with your display's IP

# Configure firewall if needed
sudo ufw allow 5200
```

### 7.2 Serial Configuration (RS232/RS485 Mode)
If using serial communication:

```bash
# Check serial port status
dmesg | grep tty

# Test serial port access
sudo cat /dev/ttyAMA0
# (Press Ctrl+C to stop)

# Check permissions
ls -la /dev/ttyAMA0
# Should show: crw-rw---- 1 root dialout 204, 64
```

## Step 8: Troubleshooting

### 8.1 Common Issues

#### Permission Denied (Serial)
```bash
# Add user to dialout group
sudo usermod -a -G dialout $USER
sudo reboot

# Or run with sudo (not recommended for production)
sudo ./simple_example
```

#### Port Not Found
```bash
# Check if serial interface is enabled
sudo raspi-config
# Interface Options → Serial Port → Enable

# Check for tty devices
ls -la /dev/tty*
```

#### Compilation Errors
```bash
# Check compiler version
g++ --version

# Install build tools
sudo apt install build-essential

# Check C++11 support
g++ -std=c++11 --version
```

#### Runtime Errors
```bash
# Enable debug output in your code
_set_cp5200_debug();

# Check system logs
dmesg | tail

# Test network connectivity
ping [display_ip_address]
```

### 8.2 Debug Mode
Always enable debug mode during development:
```cpp
_set_cp5200_debug();
```

This will show detailed communication logs and help identify issues.

## Step 9: Production Deployment

### 9.1 Create Systemd Service (Optional)
```bash
sudo nano /etc/systemd/system/cp5200-display.service
```

Add content:
```ini
[Unit]
Description=CP5200 Display Service
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/cp5200
ExecStart=/home/pi/cp5200/build/simple_example
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
sudo systemctl enable cp5200-display.service
sudo systemctl start cp5200-display.service
```

### 9.2 Log Rotation
```bash
sudo nano /etc/logrotate.d/cp5200
```

Add content:
```
/home/pi/cp5200/logs/*.log {
    daily
    missingok
    rotate 7
    compress
    delaycompress
    notifempty
    create 644 pi pi
}
```

## Step 10: Verification

### 10.1 Final Test
```bash
# Test library functions
cd ~/cp5200/build
./test_cp5200

# Test communication (if display connected)
./simple_example

# Test Python wrapper
cd ~/cp5200
python3 quick_start.py
```

### 10.2 Check System Status
```bash
# Check library installation
pkg-config --libs cp5200

# Check serial port
ls -la /dev/tty*

# Check network connectivity
netstat -tuln | grep 5200
```

## Support

If you encounter issues:

1. **Check debug output**: Always enable debug mode first
2. **Verify hardware connections**: Ensure proper wiring
3. **Check system logs**: Use `dmesg | tail`
4. **Test with simple examples**: Start with basic functionality
5. **Verify permissions**: Check user group membership

## Next Steps

After successful installation:

1. **Customize your application**: Modify the example code for your needs
2. **Add error handling**: Implement proper error checking
3. **Create your own functions**: Extend the library as needed
4. **Optimize performance**: Adjust timing and communication parameters
5. **Add monitoring**: Implement health checks and logging

## Files Created

After installation, you'll have:
- **Library files**: `libcp5200.a`, `libcp5200.so`
- **Header file**: `cp5200.h`
- **Example programs**: `simple_example`, `test_cp5200`
- **Python wrapper**: `quick_start.py`
- **Build scripts**: `build_raspberry_pi.sh`, `CMakeLists.txt`
- **Documentation**: `README_RaspberryPi.md`, `INSTALL_RaspberryPi.md`

Congratulations! You now have a fully functional CP5200 library on your Raspberry Pi.
