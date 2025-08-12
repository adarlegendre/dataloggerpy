# CP5200 LED Display Library for Raspberry Pi

This library provides a simple interface to control CP5200 LED display controllers from a Raspberry Pi running Linux.

## Overview

The CP5200 library supports communication with LED display controllers via:
- **TCP/IP** (Ethernet)
- **RS232** (Serial)
- **RS485** (Serial with differential signaling)

## Features

- **Text Display**: Send text to specific display windows with customizable colors, fonts, and effects
- **Clock Display**: Show time and date with various calendar types
- **Window Management**: Split the display into multiple windows
- **Brightness Control**: Adjust display brightness (0-31 or auto)
- **Time Synchronization**: Sync the display clock with system time
- **Picture Display**: Send image files to the display
- **Multi-language Support**: UTF-8 to Extended ASCII conversion

## Prerequisites

### Hardware
- Raspberry Pi (any model)
- CP5200 LED display controller
- Connection cable (Ethernet or Serial)

### Software Dependencies
```bash
# Update system
sudo apt update && sudo apt upgrade

# Install required packages
sudo apt install build-essential g++ make git

# For serial communication (if using RS232/RS485)
sudo apt install python3-serial
```

## Installation

### Option 1: Build from Source (Recommended)

1. **Clone or download the library**
   ```bash
   cd ~/your_project_directory
   # Copy the cp5200 folder here
   ```

2. **Make the build script executable**
   ```bash
   chmod +x cp5200/build_raspberry_pi.sh
   ```

3. **Run the build script**
   ```bash
   cd cp5200
   ./build_raspberry_pi.sh
   ```

4. **Install system-wide (optional)**
   ```bash
   cd build
   sudo cp libcp5200.a /usr/local/lib/
   sudo cp libcp5200.so /usr/local/lib/
   sudo cp ../cp5200.h /usr/local/include/
   sudo ldconfig
   ```

### Option 2: Manual Build

```bash
cd cp5200
mkdir build && cd build

# Compile library
g++ -c -O2 -std=c++11 -fPIC ../cp5200.cpp -o cp5200.o

# Create static library
ar rcs libcp5200.a cp5200.o
ranlib libcp5200.a

# Create shared library
g++ -shared -fPIC -o libcp5200.so cp5200.o

# Compile example
g++ -std=c++11 -I.. ../simple_example.cpp -L. -lcp5200 -o simple_example
```

## Configuration

### Serial Communication (RS232/RS485)

1. **Enable Serial Interface**
   ```bash
   sudo raspi-config
   # Navigate to: Interface Options > Serial Port
   # Enable serial interface
   # Disable serial console
   ```

2. **Set Serial Port Permissions**
   ```bash
   sudo usermod -a -G dialout $USER
   # Log out and back in, or reboot
   ```

3. **Check Serial Port**
   ```bash
   ls -la /dev/tty*
   # Look for /dev/ttyAMA0 or /dev/ttyS0
   ```

### Network Communication (TCP/IP)

1. **Ensure network connectivity**
   ```bash
   ping 192.168.1.100  # Replace with your display's IP
   ```

2. **Check firewall settings**
   ```bash
   sudo ufw status
   # Allow port 5200 if needed
   sudo ufw allow 5200
   ```

## Usage Examples

### Basic Setup

```cpp
#include "cp5200.h"

int main() {
    // Enable debug output
    _set_cp5200_debug();
    
    // Set communication mode (0=TCP/IP, 1=RS232, 2=RS485)
    _set_cp5200_send_mode(1);
    
    // Configure serial communication
    _set_cp5200_rs232comm((char*)"/dev/ttyAMA0", 115200);
    
    // Or configure network communication
    // _set_cp5200_send_mode(0);
    // _set_cp5200_ipcomm((char*)"192.168.1.100", 5200);
    
    return 0;
}
```

### Display Text

```cpp
// Send text to window 0
// Parameters: window, text, color, font_size, speed, effect, stay_time, alignment
int result = SendText(0, (char*)"Hello World!", 0xFF0000, 16, 1, 0, 5, 0);

if (result == 0) {
    printf("Text sent successfully\n");
} else {
    printf("Error: %d\n", result);
}
```

### Window Management

```cpp
// Split display into 2 windows
int windowConfig[] = {0, 64, 64, 128};  // 2 windows: 0-64 and 64-128
int result = SplitWindow(2, windowConfig, 4);
```

### Clock Display

```cpp
// Show clock in window 0
int format[] = {1, 1, 1, 1, 1, 1, 1, 1};  // All elements enabled
int content[] = {1, 1, 1, 1, 1, 1, 1, 1}; // All content enabled
int colors[] = {0xFF, 0xFF, 0x00};          // RGB colors

int result = SendClock(0, 10, 0, format, content, (char*)"", colors, 16);
```

### Brightness Control

```cpp
// Set brightness to 20 (0-31, or 255 for auto)
int result = BrightnessControl(0, 20);

// Get current brightness
int brightness = BrightnessControl(1, 0);
```

### Time Synchronization

```cpp
// Sync display time with system time
int result = SyncTime();
```

## API Reference

### Core Functions

| Function | Description | Parameters |
|----------|-------------|------------|
| `_set_cp5200_debug()` | Enable debug output | None |
| `_set_cp5200_send_mode(int)` | Set communication mode | 0=TCP/IP, 1=RS232, 2=RS485 |
| `_set_cp5200_ipcomm(char*, int)` | Set IP address and port | IP string, port number |
| `_set_cp5200_rs232comm(char*, int)` | Set serial port and baud rate | Port string, baud rate |

### Display Functions

| Function | Description | Parameters |
|----------|-------------|------------|
| `SendText(int, char*, int, int, int, int, int, int)` | Send text to window | window, text, color, font_size, speed, effect, stay_time, alignment |
| `SendClock(int, int, int, int[], int[], char*, int[], int)` | Display clock | window, stay_time, calendar_type, format, content, text, colors, font_size |
| `SplitWindow(int, int[], int)` | Split display into windows | window_count, config_array, array_size |
| `BrightnessControl(int, int)` | Get/set brightness | 0=set, 1=get; brightness_value |
| `SyncTime()` | Sync display time | None |

### Parameter Details

#### Colors
- Format: RGB hex (0xRRGGBB)
- Example: 0xFF0000 (red), 0x00FF00 (green), 0x0000FF (blue)

#### Font Sizes
- Range: 8-32 pixels
- Common sizes: 8, 12, 16, 20, 24, 32

#### Effects
- 0: No effect
- 1: Scroll left
- 2: Scroll right
- 3: Scroll up
- 4: Scroll down
- 5: Blink
- 6: Marquee

#### Alignment
- 0: Left
- 1: Center
- 2: Right

## Troubleshooting

### Common Issues

1. **Permission Denied (Serial)**
   ```bash
   sudo usermod -a -G dialout $USER
   # Reboot or log out/in
   ```

2. **Port Not Found**
   ```bash
   ls -la /dev/tty*
   # Check if /dev/ttyAMA0 exists
   # Enable serial interface in raspi-config
   ```

3. **Compilation Errors**
   ```bash
   # Ensure C++11 support
   g++ --version
   # Install build tools if needed
   sudo apt install build-essential
   ```

4. **Runtime Errors**
   - Check debug output with `_set_cp5200_debug()`
   - Verify communication parameters
   - Test network connectivity (ping)
   - Check serial port with `dmesg | grep tty`

### Debug Mode

Enable debug output to see detailed communication logs:
```cpp
_set_cp5200_debug();
```

## Performance Considerations

- **Serial Communication**: 115200 baud is recommended for reliable operation
- **Network Communication**: Ensure stable network connection
- **Text Length**: Very long text may require multiple packets
- **Window Updates**: Frequent updates may cause display flicker

## License

This library is provided as-is for educational and development purposes.

## Support

For issues and questions:
1. Check the debug output
2. Verify hardware connections
3. Test with simple examples first
4. Check system logs: `dmesg | tail`

## Version History

- **V3.0** (2025-03-13): Added brightness query and control
- **V2.5** (2025-02-26): Rebuilt for Bookworm
- **V2.1** (2020-10-09): Rebuild
- **V2.0** (2017-06-15): Major update
- **V1.0** (2017-02-03): Initial release
