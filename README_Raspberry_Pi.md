# 🍓 CP5200 Czech Number Plates Test for Raspberry Pi

This is a **Raspberry Pi optimized** version of the CP5200 test that automatically finds and imports the existing Linux library without any modifications to the original SDK files.

## 🎯 What's Special for Raspberry Pi

- **Automatic Raspberry Pi detection** - Detects if running on Raspberry Pi
- **Optimized library search paths** - Finds the existing Linux library automatically
- **Raspberry Pi specific functions** - Time sync, brightness control, and more
- **No compilation needed** - Uses the pre-compiled library from the SDK
- **Smart path detection** - Works from any directory in your project

## 🚀 Quick Start on Raspberry Pi

### 1. Prerequisites
- Raspberry Pi (any model) running Raspberry Pi OS
- Python 3.6 or higher
- Network access to 192.168.1.222:5200
- CP5200 display powered on and connected

### 2. Setup (One-time)
```bash
# Make the setup script executable
chmod +x setup_raspberry_pi.sh

# Run the setup script
./setup_raspberry_pi.sh
```

### 3. Run the Test

#### Option A: Automatic (Recommended)
```bash
python3 test_czech_plates.py
```

#### Option B: From cp5200Original directory
```bash
cd cp5200Original
python3 ../test_czech_plates.py
```

#### Option C: Specify library path
```bash
python3 test_czech_plates.py ./cp5200Original/dist/Release/GNU-Linux/libcp5200.a
```

## 📁 Library Importation

The test automatically finds your CP5200 library in these locations:

### Primary Raspberry Pi Paths
- `./dist/Release/GNU-Linux/libcp5200.a` (if in cp5200Original directory)
- `./cp5200Original/dist/Release/GNU-Linux/libcp5200.a` (if in parent directory)
- `/usr/local/lib/libcp5200.so` (system-wide installation)
- `/usr/lib/libcp5200.so` (system-wide installation)

### Fallback Paths
- `./libcp5200.so` (current directory)
- `./libcp5200.a` (current directory)
- System library paths

## 🔧 What the Test Does on Raspberry Pi

### 1. System Detection
- Detects Raspberry Pi hardware
- Shows system information (platform, architecture, Python version)
- Applies Raspberry Pi specific optimizations

### 2. Library Importation
- Automatically finds the existing Linux library
- Sets up proper function signatures
- Tests library loading before proceeding

### 3. Display Setup
- **Time synchronization** with your Raspberry Pi system time
- **Brightness optimization** for Raspberry Pi (level 20)
- **Window splitting** into 2 display regions
- **Czech number plates** with different colors

### 4. Czech Number Plates Sent
- **"3A8 1234"** - Red text in Window 0
- **"1AB 5678"** - Green text in Window 1
- **"P 999 99"** - Red text in Window 0
- **"A 123 45"** - Green text in Window 1
- **"E 777 77"** - Blue text in Window 0
- **"T 555 55"** - Yellow text in Window 1

## 🎨 Color System

- **Red (0xFF0000)**: Czech emergency vehicles
- **Green (0x00FF00)**: Czech regular vehicles  
- **Blue (0x0000FF)**: Czech diplomatic vehicles
- **Yellow (0xFFFF00)**: Czech special vehicles

## 📋 Expected Output on Raspberry Pi

```
🚀 CP5200 Czech Number Plates Test for Raspberry Pi
============================================================
Platform: Linux 5.15.0-rpi
Architecture: aarch64
Python: 3.9.2
🍓 Raspberry Pi detected - applying optimizations
✓ Loaded library from Raspberry Pi path: ./dist/Release/GNU-Linux/libcp5200.a
✓ Function signatures configured
✓ Debug mode enabled
✓ Set to TCP/IP mode
✓ Set IP address: 192.168.1.222:5200

🚗 Testing Czech Number Plates Display on Raspberry Pi
============================================================

1. Synchronizing time with display...
✓ Time synchronized with display

2. Setting optimal brightness...
✓ Brightness set to 20

3. Setting up display windows...
✓ Split display into 2 windows

4. Sending red Czech plate to window 0...
✓ Text sent to window 0: '3A8 1234'

5. Sending green Czech plate to window 1...
✓ Text sent to window 1: '1AB 5678'

6. Sending additional Czech plates...
   1. Sending 'P 999 99' to window 0...
   ✓ Text sent to window 0: 'P 999 99'
   2. Sending 'A 123 45' to window 1...
   ✓ Text sent to window 1: 'A 123 45'
   3. Sending 'E 777 77' to window 0...
   ✓ Text sent to window 0: 'E 777 77'
   4. Sending 'T 555 55' to window 1...
   ✓ Text sent to window 1: 'T 555 55'

✅ Czech number plates test completed on Raspberry Pi!
Check your CP5200 display at 192.168.1.222:5200
🍓 Raspberry Pi test completed successfully!
```

## 🛠️ Troubleshooting on Raspberry Pi

### Library Not Found
```
❌ Error loading library: Could not find CP5200 library
```
**Solutions**:
1. **Run setup script**: `./setup_raspberry_pi.sh`
2. **Check directory**: Make sure you're in the right directory
3. **Verify library exists**: Check if `libcp5200.a` exists in the dist folder

### Permission Denied
```
❌ Error loading library: Permission denied
```
**Solution**:
```bash
chmod +r ./cp5200Original/dist/Release/GNU-Linux/libcp5200.a
```

### Connection Failed
```
❌ Failed to send text to window 0, error: -1
```
**Solutions**:
1. **Check network**: `ping 192.168.1.222`
2. **Check port**: `telnet 192.168.1.222 5200`
3. **Check firewall**: `sudo ufw status`
4. **Verify display power**: Ensure CP5200 is powered on

## 🔍 Debug Features

- **Automatic debug mode** - Shows all function calls
- **Library loading details** - Shows exactly where library was found
- **Function signatures** - Validates all C function calls
- **Error details** - Shows specific error codes from CP5200

## 📚 How Importation Works

1. **Raspberry Pi Detection**: Checks hardware and applies optimizations
2. **Smart Path Detection**: Automatically finds the right library location
3. **Library Loading**: Uses Python's `ctypes` to load the C++ library
4. **Function Setup**: Configures proper function signatures for Python
5. **Testing**: Validates library loading before running tests

## 🎯 Customization for Raspberry Pi

### Add Your Own Czech Plates
```python
# In the test_czech_plates() method
custom_plates = [
    ("ABC 123", 0xFF0000, 0),  # Red plate in window 0
    ("XYZ 789", 0x00FF00, 1),  # Green plate in window 1
]

for plate, color, window in custom_plates:
    self.send_text(window, plate, color, 16, 1, 0, 5, 1)
```

### Adjust Brightness
```python
# Set brightness level (0-31, or 255 for auto)
self.set_brightness(25)  # Brighter for outdoor use
```

## 📞 Raspberry Pi Support

If you encounter issues on Raspberry Pi:
1. **Run the setup script** first: `./setup_raspberry_pi.sh`
2. **Check system info** in the test output
3. **Verify library path** is correct
4. **Check network connectivity** to 192.168.1.222
5. **Ensure CP5200 display** is powered and connected

## 🚀 Performance Tips

- **Use Python 3.9+** for best performance on Raspberry Pi
- **Run from SSD** if possible for faster library loading
- **Close unnecessary applications** to free up memory
- **Use wired Ethernet** for more reliable network communication

This Raspberry Pi optimized version provides the simplest way to test your CP5200 display with Czech number plates without any SDK modifications!
