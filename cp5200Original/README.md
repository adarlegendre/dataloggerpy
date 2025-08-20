# 🚀 CP5200 SDK - Complete Usage Guide

## **Overview**

The CP5200 is a display controller that supports TCP/IP communication for sending text, pictures, and controlling display settings. This project provides a complete Python SDK with comprehensive testing and examples.

## **📁 Project Structure**

```
cp5200Original/
├── cp5200.cpp              # Main C++ source code
├── cp5200.h                # Header file with function declarations
├── build_cp5200_python.py  # Python-based library builder
├── run_all.py              # Main automation script (BUILD + TEST)
├── comprehensive_sdk_test.py # Complete SDK function testing
├── simple_example.py       # Basic usage example for beginners
├── diagnostic_test.py      # Diagnostic testing
├── simple_diagnostic.py    # Simple diagnostic
├── corrected_diagnostic.py # Corrected diagnostic
├── timeout_test.py         # Timeout handling test
├── test_czech_plates_unified.py # Czech plates test
├── SDK_USAGE_GUIDE.md      # Detailed SDK usage guide
├── README_Python_Builder.md # Builder documentation
└── README.md               # This file
```

## **🚀 Quick Start**

### **Step 1: Build the Library**
```bash
cd cp5200Original
python3 build_cp5200_python.py
```

### **Step 2: Run Complete Automation**
```bash
python3 run_all.py
```

### **Step 3: Test Individual Components**
```bash
# Simple example
python3 simple_example.py

# Comprehensive test
python3 comprehensive_sdk_test.py

# Specific tests
python3 diagnostic_test.py
python3 test_czech_plates_unified.py
```

## **🔧 Available Functions**

### **Configuration Functions**
- `_set_cp5200_debug()` - Enable debug output
- `_set_cp5200_send_mode(mode)` - Set communication mode (0=TCP, 1=RS232, 2=RS485)
- `_set_cp5200_ipcomm(ip, port)` - Set IP address and port

### **Display Functions**
- `SendText(window, text, color, fontSize, speed, effect, stayTime, align)` - Send text
- `SplitWindow(count, config[], size)` - Split display into windows
- `SendPicture(window, x, y, filename, speed, effect, stayTime)` - Send picture

### **Utility Functions**
- `SyncTime()` - Synchronize time with display
- `BrightnessControl(getSet, brightness)` - Get/set brightness (0-31, 255=auto)

## **📝 Usage Examples**

### **Basic Text Display**
```python
import ctypes

# Load library
lib = ctypes.CDLL('./libcp5200.so')

# Setup
lib._set_cp5200_debug()
lib._set_cp5200_send_mode(0)  # TCP mode
lib._set_cp5200_ipcomm(b'192.168.1.222', 5200)

# Send text
lib.SendText(0, b'HELLO WORLD', 0xFF0000, 16, 1, 0, 10, 2)
```

### **Window Management**
```python
# Split into 2 windows
config = [0, 0, 64, 64, 64, 0, 128, 64]
c_config = (ctypes.c_int * len(config))(*config)
lib.SplitWindow(2, c_config, len(config))

# Send text to each window
lib.SendText(0, b'LEFT', 0xFF0000, 14, 1, 0, 8, 2)
lib.SendText(1, b'RIGHT', 0x00FF00, 14, 1, 0, 8, 2)
```

### **Brightness Control**
```python
# Set brightness to level 20
lib.BrightnessControl(0, 20)

# Set to automatic brightness
lib.BrightnessControl(0, 255)
```

## **🧪 Testing Options**

### **1. Complete Automation (`run_all.py`)**
```bash
# Run everything (build + test)
python3 run_all.py

# Only build
python3 run_all.py --build-only

# Only test
python3 run_all.py --test-only

# Verbose output
python3 run_all.py --verbose

# Custom target
python3 run_all.py --target-ip 192.168.1.100 --target-port 5200
```

### **2. Individual Tests**
```bash
# Basic functionality
python3 simple_example.py

# Comprehensive testing
python3 comprehensive_sdk_test.py

# Diagnostic testing
python3 diagnostic_test.py

# Czech plates test
python3 test_czech_plates_unified.py
```

### **3. Test Categories**

#### **Basic Tests**
- `simple_example.py` - Basic text display
- `simple_diagnostic.py` - Simple connectivity test
- `timeout_test.py` - Timeout handling

#### **Advanced Tests**
- `comprehensive_sdk_test.py` - All SDK functions
- `diagnostic_test.py` - Comprehensive diagnostics
- `test_czech_plates_unified.py` - Czech plates display

## **🎨 Display Parameters**

### **Colors (RGB Format)**
```python
COLORS = {
    'RED': 0xFF0000,
    'GREEN': 0x00FF00,
    'BLUE': 0x0000FF,
    'YELLOW': 0xFFFF00,
    'CYAN': 0x00FFFF,
    'MAGENTA': 0xFF00FF,
    'WHITE': 0xFFFFFF,
    'BLACK': 0x000000
}
```

### **Effects**
```python
EFFECTS = {
    'NONE': 0,        # No effect
    'SCROLL': 1,      # Scroll from right to left
    'BLINK': 2,       # Blinking text
    'FADE_IN': 3,     # Fade in effect
    'FADE_OUT': 4,    # Fade out effect
    'SLIDE_UP': 5,    # Slide up from bottom
    'SLIDE_DOWN': 6   # Slide down from top
}
```

### **Alignment**
```python
ALIGNMENT = {
    'LEFT': 1,
    'CENTER': 2,
    'RIGHT': 3
}
```

## **🔍 Troubleshooting**

### **Common Issues**

1. **Library not found**
   ```bash
   # Ensure library is compiled
   python3 build_cp5200_python.py
   ```

2. **Network connectivity**
   ```bash
   # Check if target is reachable
   ping 192.168.1.222
   
   # Check if port is open
   telnet 192.168.1.222 5200
   ```

3. **Permission denied**
   ```bash
   # Fix library permissions
   chmod +r libcp5200.so
   ```

4. **Display not responding**
   - Check power connection
   - Verify network settings
   - Check IP address configuration

### **Debug Mode**
```python
# Enable debug output
lib._set_cp5200_debug()

# Check library version
lib._get_cp5200_version()
```

## **📚 Detailed Documentation**

- **`SDK_USAGE_GUIDE.md`** - Complete SDK reference with examples
- **`README_Python_Builder.md`** - Builder system documentation
- **`cp5200.h`** - C++ header with function declarations
- **`cp5200.cpp`** - C++ implementation source code

## **🚀 Advanced Usage**

### **Custom Window Configurations**
```python
# Four windows (2x2 grid)
config = [0, 0, 64, 32,     # Top-left
          64, 0, 128, 32,   # Top-right
          0, 32, 64, 64,    # Bottom-left
          64, 32, 128, 64]  # Bottom-right

c_config = (ctypes.c_int * len(config))(*config)
lib.SplitWindow(4, c_config, len(config))
```

### **Picture Display**
```python
# Display GIF image
lib.SendPicture(0, 10, 10, "logo.gif", 1, 0, 20)
```

### **Time Synchronization**
```python
# Sync display time with host
lib.SyncTime()
```

## **💡 Best Practices**

1. **Always check return values** from SDK functions
2. **Use appropriate timeouts** for network operations
3. **Test with simple text first** before complex configurations
4. **Verify network connectivity** before sending commands
5. **Use debug mode** during development
6. **Handle errors gracefully** in production code
7. **Test window configurations** before sending content
8. **Use appropriate font sizes** for your display resolution

## **🔧 System Requirements**

- **Python 3.6+**
- **GCC/G++ compiler** (for building)
- **Network access** to CP5200 display
- **Linux/Unix environment** (recommended for Raspberry Pi)

## **📞 Support**

For issues and questions:
1. Check the troubleshooting section above
2. Review the detailed documentation files
3. Check network connectivity and display power
4. Verify library compilation and permissions

## **🎯 Success Indicators**

Your CP5200 SDK is working correctly when:
- ✅ Library compiles without errors
- ✅ Tests run successfully
- ✅ Text appears on your display
- ✅ Network communication is established
- ✅ All function calls return success (0)

Start with `simple_example.py` to verify basic functionality, then progress to more complex tests as needed!






