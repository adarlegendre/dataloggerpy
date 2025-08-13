# CP5200 Czech Number Plates Test

This is a simple Python test file that allows you to test sending Czech number plates to a CP5200 LED display without modifying the original SDK files.

## 🎯 What This Test Does

- **Imports the CP5200 SDK** without any modifications
- **Sends Czech number plates** to the display at 192.168.1.222:5200
- **Tests different colors**: Red, Green, Blue, Yellow
- **Uses two display windows** for better visibility
- **No compilation required** - pure Python with ctypes

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.6 or higher
- Compiled CP5200 library file (`.so`, `.dll`, or `.a`)
- Network access to 192.168.1.222:5200
- CP5200 display powered on and connected

### 2. Run the Test

#### Option A: Automatic Library Detection
```bash
python3 test_czech_plates.py
```

#### Option B: Specify Library Path
```bash
python3 test_czech_plates.py /path/to/your/libcp5200.so
```

#### Option C: Windows
```cmd
python test_czech_plates.py C:\path\to\your\cp5200.dll
```

## 📁 Library File Locations

The test will automatically search for the CP5200 library in these locations:

- `./libcp5200.so` (Linux)
- `./libcp5200.dll` (Windows)
- `./cp5200.dll` (Windows)
- `../cp5200/dist/Release/GNU-Linux/libcp5200.so`
- `../cp5200/dist/Debug/GNU-Linux/libcp5200.so`
- System library paths

## 🔧 What the Test Sends

### Display Setup
- **Window 0**: Left half of display (0,0) to (64,64)
- **Window 1**: Right half of display (64,0) to (128,64)

### Czech Number Plates Sent
1. **"3A8 1234"** - Red text in Window 0
2. **"1AB 5678"** - Green text in Window 1
3. **"P 999 99"** - Red text in Window 0
4. **"A 123 45"** - Green text in Window 1
5. **"E 777 77"** - Blue text in Window 0
6. **"T 555 55"** - Yellow text in Window 1

## 🎨 Color Codes Used

- **Red**: `0xFF0000` (Czech emergency vehicles)
- **Green**: `0x00FF00` (Czech regular vehicles)
- **Blue**: `0x0000FF` (Czech diplomatic vehicles)
- **Yellow**: `0xFFFF00` (Czech special vehicles)

## 📋 Expected Output

```
🚀 CP5200 Czech Number Plates Test
==================================================
✓ Loaded library from: ./libcp5200.so
✓ Function signatures configured
✓ Debug mode enabled
✓ Set to TCP/IP mode
✓ Set IP address: 192.168.1.222:5200

🚗 Testing Czech Number Plates Display
==================================================

1. Setting up display windows...
✓ Split display into 2 windows

2. Sending red Czech plate to window 0...
✓ Text sent to window 0: '3A8 1234'

3. Sending green Czech plate to window 1...
✓ Text sent to window 1: '1AB 5678'

4. Sending additional Czech plates...
   1. Sending 'P 999 99' to window 0...
   ✓ Text sent to window 0: 'P 999 99'
   2. Sending 'A 123 45' to window 1...
   ✓ Text sent to window 1: 'A 123 45'
   3. Sending 'E 777 77' to window 0...
   ✓ Text sent to window 0: 'E 777 77'
   4. Sending 'T 555 55' to window 1...
   ✓ Text sent to window 1: 'T 555 55'

✅ Czech number plates test completed!
Check your CP5200 display at 192.168.1.222:5200
```

## 🛠️ Troubleshooting

### Library Not Found
```
❌ Error loading library: Could not find CP5200 library
```
**Solution**: Specify the full path to your library file:
```bash
python3 test_czech_plates.py /full/path/to/libcp5200.so
```

### Connection Failed
```
❌ Failed to send text to window 0, error: -1
```
**Solutions**:
1. Check if CP5200 display is powered on
2. Verify network connectivity: `ping 192.168.1.222`
3. Check if port 5200 is open: `telnet 192.168.1.222 5200`
4. Ensure firewall allows connections to port 5200

### Permission Denied
```
❌ Error loading library: Permission denied
```
**Solution**: Make sure the library file is readable:
```bash
chmod +r /path/to/libcp5200.so
```

## 🔍 Debug Mode

The test automatically enables debug mode, which will show:
- Function entry/exit points
- Network communication details
- Packet construction information
- Error details from the CP5200 controller

## 📚 How It Works

1. **Library Loading**: Uses Python's `ctypes` to load the compiled C++ library
2. **Function Setup**: Configures proper function signatures for Python integration
3. **Communication**: Sets TCP/IP mode and configures IP address 192.168.1.222:5200
4. **Display Setup**: Splits the display into two windows
5. **Text Sending**: Sends Czech number plates with different colors to each window
6. **Error Handling**: Provides detailed feedback for troubleshooting

## 🎯 Customization

To test different Czech number plates, modify the `test_czech_plates()` method:

```python
# Add your own Czech plates
custom_plates = [
    ("ABC 123", 0xFF0000, 0),  # Red plate in window 0
    ("XYZ 789", 0x00FF00, 1),  # Green plate in window 1
]

for plate, color, window in custom_plates:
    self.send_text(window, plate, color, 16, 1, 0, 5, 1)
```

## 📞 Support

If you encounter issues:
1. Check the debug output for detailed error information
2. Verify network connectivity to 192.168.1.222
3. Ensure the CP5200 library is properly compiled
4. Check CP5200 display power and network settings

This test file provides a simple, non-intrusive way to verify your CP5200 setup and test Czech number plate display functionality!
