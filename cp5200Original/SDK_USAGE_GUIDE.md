# 🚀 CP5200 SDK Usage Guide

## **Overview**

The CP5200 is a display controller that supports TCP/IP communication for sending text, pictures, and controlling display settings. This guide covers all available functions and provides practical examples.

## **🔧 Basic Setup**

### **1. Load the Library**
```python
import ctypes

# Load the compiled library
lib = ctypes.CDLL('./libcp5200.so')

# Enable debug output (recommended for development)
lib._set_cp5200_debug()

# Set communication mode (0=TCP/IP, 1=RS232, 2=RS485)
lib._set_cp5200_send_mode(0)

# Set IP address and port
lib._set_cp5200_ipcomm(b'192.168.1.222', 5200)
```

### **2. Function Signatures Setup**
```python
# Configure function signatures for proper Python integration
lib._set_cp5200_debug.argtypes = []
lib._set_cp5200_debug.restype = None

lib._set_cp5200_send_mode.argtypes = [ctypes.c_int]
lib._set_cp5200_send_mode.restype = None

lib._set_cp5200_ipcomm.argtypes = [ctypes.c_char_p, ctypes.c_int]
lib._set_cp5200_ipcomm.restype = None

lib.SendText.argtypes = [
    ctypes.c_int,      # window number
    ctypes.c_char_p,   # text
    ctypes.c_int,      # color
    ctypes.c_int,      # font size
    ctypes.c_int,      # speed
    ctypes.c_int,      # effect
    ctypes.c_int,      # stay time
    ctypes.c_int       # alignment
]
lib.SendText.restype = ctypes.c_int
```

## **📝 Text Display Functions**

### **SendText - Display Text on Screen**
```python
def send_text(lib, window, text, color, font_size, speed, effect, stay_time, align):
    """
    Send text to a specific window
    
    Args:
        window: Window number (0, 1, 2, etc.)
        text: Text string to display
        color: RGB color (0xRRGGBB format)
        font_size: Font size (10-20 recommended)
        speed: Effect speed (1-10, 1=slow, 10=fast)
        effect: Effect type (0=none, 1=scroll, 2=blink, etc.)
        stay_time: How long to display (seconds)
        align: Text alignment (1=left, 2=center, 3=right)
    """
    result = lib.SendText(window, text.encode('utf-8'), color, font_size, speed, effect, stay_time, align)
    return result

# Examples:
# Red text, large font, no effect, center aligned
send_text(lib, 0, "HELLO WORLD", 0xFF0000, 16, 1, 0, 10, 2)

# Green text, small font, scroll effect, left aligned
send_text(lib, 1, "SCROLLING TEXT", 0x00FF00, 12, 2, 1, 15, 1)

# Blue text, medium font, blink effect, right aligned
send_text(lib, 2, "BLINKING", 0x0000FF, 14, 1, 2, 8, 3)
```

### **Color Reference**
```python
# Common colors (RGB format)
COLORS = {
    'RED': 0xFF0000,
    'GREEN': 0x00FF00,
    'BLUE': 0x0000FF,
    'YELLOW': 0xFFFF00,
    'CYAN': 0x00FFFF,
    'MAGENTA': 0xFF00FF,
    'WHITE': 0xFFFFFF,
    'BLACK': 0x000000,
    'ORANGE': 0xFF8000,
    'PURPLE': 0x8000FF
}
```

### **Effect Reference**
```python
# Effect types
EFFECTS = {
    'NONE': 0,        # No effect
    'SCROLL': 1,      # Scroll from right to left
    'BLINK': 2,       # Blinking text
    'FADE_IN': 3,     # Fade in effect
    'FADE_OUT': 4,    # Fade out effect
    'SLIDE_UP': 5,    # Slide up from bottom
    'SLIDE_DOWN': 6,  # Slide down from top
}
```

## **🪟 Window Management**

### **SplitWindow - Divide Display into Multiple Areas**
```python
def split_display(lib, window_count, config):
    """
    Split display into multiple windows
    
    Args:
        window_count: Number of windows to create
        config: List of coordinates [x1, y1, x2, y2, x3, y3, x4, y4, ...]
               Each window needs 4 coordinates (x1,y1,x2,y2)
    
    Returns:
        0 on success, error code on failure
    """
    # Convert Python list to C array
    c_config = (ctypes.c_int * len(config))(*config)
    result = lib.SplitWindow(window_count, c_config, len(config))
    return result

# Examples:

# Single window (full display 128x64)
config = [0, 0, 128, 64]
split_display(lib, 1, config)

# Two windows (horizontal split)
config = [0, 0, 64, 64,    # Left window: (0,0) to (64,64)
          64, 0, 128, 64]  # Right window: (64,0) to (128,64)
split_display(lib, 2, config)

# Four windows (2x2 grid)
config = [0, 0, 64, 32,     # Top-left
          64, 0, 128, 32,   # Top-right
          0, 32, 64, 64,    # Bottom-left
          64, 32, 128, 64]  # Bottom-right
split_display(lib, 4, config)
```

## **🖼️ Picture Display**

### **SendPicture - Display GIF Images**
```python
def send_picture(lib, window, x, y, filename, speed, effect, stay_time):
    """
    Send a GIF picture to display
    
    Args:
        window: Target window number
        x, y: Position coordinates
        filename: Path to GIF file
        speed: Effect speed (1-10)
        effect: Effect type (0=none, 1=fade, etc.)
        stay_time: Display duration (seconds)
    
    Returns:
        0 on success, error code on failure
    """
    result = lib.SendPicture(window, x, y, filename.encode('utf-8'), speed, effect, stay_time)
    return result

# Example:
send_picture(lib, 0, 10, 10, "logo.gif", 1, 0, 20)
```

## **⏰ Time and Clock Functions**

### **SyncTime - Synchronize Display Time**
```python
def sync_time(lib):
    """
    Synchronize the display's internal clock with the host system
    """
    result = lib.SyncTime()
    return result

# Example:
sync_time(lib)
```

### **SendClock - Display Clock**
```python
def send_clock(lib, window, stay_time, cal_type, format_array, content_array, text, color_array, font_size):
    """
    Display a clock on the specified window
    
    Args:
        window: Window number
        stay_time: Display duration
        cal_type: Calendar type
        format_array: Format configuration array
        content_array: Content configuration array
        text: Additional text to display
        color_array: Color configuration array
        font_size: Font size array
    """
    # Convert Python arrays to C arrays
    c_format = (ctypes.c_int * len(format_array))(*format_array)
    c_content = (ctypes.c_int * len(content_array))(*content_array)
    c_color = (ctypes.c_int * len(color_array))(*color_array)
    c_font = (ctypes.c_int * len(font_size))(*font_size)
    
    result = lib.SendClock(window, stay_time, cal_type, c_format, c_content, text.encode('utf-8'), c_color, c_font)
    return result
```

## **💡 Brightness Control**

### **BrightnessControl - Adjust Display Brightness**
```python
def set_brightness(lib, brightness):
    """
    Set display brightness
    
    Args:
        brightness: Brightness level (0-31) or 255 for auto
                  0 = darkest, 31 = brightest, 255 = automatic
    
    Returns:
        0 on success, error code on failure
    """
    result = lib.BrightnessControl(0, brightness)  # 0 = set brightness
    return result

def get_brightness(lib):
    """
    Get current brightness level
    
    Returns:
        Brightness level (0-31) or 255 for auto
    """
    result = lib.BrightnessControl(1, 0)  # 1 = get brightness
    return result

# Examples:
set_brightness(lib, 20)      # Set to medium brightness
set_brightness(lib, 255)     # Set to automatic brightness
current = get_brightness(lib) # Get current setting
```

## **🔍 Complete Working Example**

```python
#!/usr/bin/env python3
"""
Complete CP5200 SDK Usage Example
Demonstrates all major functions
"""

import ctypes
import time

def main():
    # Load library
    lib = ctypes.CDLL('./libcp5200.so')
    
    # Setup function signatures
    setup_function_signatures(lib)
    
    # Basic configuration
    lib._set_cp5200_debug()
    lib._set_cp5200_send_mode(0)  # TCP mode
    lib._set_cp5200_ipcomm(b'192.168.1.222', 5200)
    
    print("🚀 CP5200 SDK Test Started")
    
    # 1. Synchronize time
    print("1. Syncing time...")
    lib.SyncTime()
    time.sleep(2)
    
    # 2. Set brightness
    print("2. Setting brightness...")
    lib.BrightnessControl(0, 20)
    time.sleep(1)
    
    # 3. Split into 2 windows
    print("3. Splitting display...")
    config = [0, 0, 64, 64, 64, 0, 128, 64]
    c_config = (ctypes.c_int * len(config))(*config)
    lib.SplitWindow(2, c_config, len(config))
    time.sleep(2)
    
    # 4. Send text to both windows
    print("4. Sending text...")
    lib.SendText(0, b'LEFT WINDOW', 0xFF0000, 14, 1, 0, 10, 2)
    time.sleep(1)
    lib.SendText(1, b'RIGHT WINDOW', 0x00FF00, 14, 1, 0, 10, 2)
    time.sleep(5)
    
    # 5. Test different effects
    print("5. Testing effects...")
    effects = [
        (b'SCROLL TEXT', 1),
        (b'BLINK TEXT', 2),
        (b'FADE TEXT', 3)
    ]
    
    for text, effect in effects:
        lib.SendText(0, text, 0x0000FF, 16, 2, effect, 5, 2)
        time.sleep(6)
    
    print("✅ Test completed!")

def setup_function_signatures(lib):
    """Setup all function signatures"""
    # Configuration functions
    lib._set_cp5200_debug.argtypes = []
    lib._set_cp5200_debug.restype = None
    
    lib._set_cp5200_send_mode.argtypes = [ctypes.c_int]
    lib._set_cp5200_send_mode.restype = None
    
    lib._set_cp5200_ipcomm.argtypes = [ctypes.c_char_p, ctypes.c_int]
    lib._set_cp5200_ipcomm.restype = None
    
    # Display functions
    lib.SendText.argtypes = [
        ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_int,
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int
    ]
    lib.SendText.restype = ctypes.c_int
    
    lib.SplitWindow.argtypes = [
        ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int
    ]
    lib.SplitWindow.restype = ctypes.c_int
    
    lib.SendPicture.argtypes = [
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p,
        ctypes.c_int, ctypes.c_int, ctypes.c_int
    ]
    lib.SendPicture.restype = ctypes.c_int
    
    # Utility functions
    lib.SyncTime.argtypes = []
    lib.SyncTime.restype = ctypes.c_int
    
    lib.BrightnessControl.argtypes = [ctypes.c_int, ctypes.c_int]
    lib.BrightnessControl.restype = ctypes.c_int

if __name__ == "__main__":
    main()
```

## **🚨 Error Handling**

### **Common Error Codes**
```python
# Return values from SDK functions
ERROR_CODES = {
    0: "Success",
    1: "Window configuration error",
    10: "File does not exist",
    11: "File open error",
    12: "Memory allocation error",
    13: "File reading error"
}

def check_result(result, operation):
    """Check and interpret function results"""
    if result == 0:
        print(f"✅ {operation} successful")
    else:
        error_msg = ERROR_CODES.get(result, f"Unknown error {result}")
        print(f"❌ {operation} failed: {error_msg}")
```

### **Network Connectivity Check**
```python
import socket
import subprocess

def check_connectivity(ip, port):
    """Check if target is reachable"""
    # Ping test
    try:
        result = subprocess.run(['ping', '-c', '1', ip], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"✅ Ping to {ip} successful")
        else:
            print(f"❌ Ping to {ip} failed")
            return False
    except:
        print(f"⚠ Ping test not available")
    
    # Port test
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        sock.close()
        
        if result == 0:
            print(f"✅ Port {port} on {ip} is accessible")
            return True
        else:
            print(f"❌ Port {port} on {ip} is not accessible")
            return False
    except Exception as e:
        print(f"❌ Port test failed: {e}")
        return False
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

## **🔧 Troubleshooting**

### **Common Issues**

1. **Library not found**: Ensure `libcp5200.so` is compiled and accessible
2. **Network timeout**: Check IP address, port, and firewall settings
3. **Display not responding**: Verify power and network connection
4. **Text not visible**: Check brightness settings and window configuration
5. **Permission denied**: Ensure library file has read permissions

### **Debug Commands**
```python
# Enable debug output
lib._set_cp5200_debug()

# Check library version
lib._get_cp5200_version()

# Verify configuration
print(f"Debug mode: {lib._cp5200_debug}")
print(f"Send mode: {lib._cp5200_send_mode}")
print(f"IP address: {lib._ip_address}")
print(f"IP port: {lib._ip_port}")
```

This guide covers all the essential functions of the CP5200 SDK. Start with simple text display and gradually add more complex features like window splitting and picture display.






