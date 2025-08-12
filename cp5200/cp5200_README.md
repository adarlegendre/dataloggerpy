# CP5200 LED Display Library

A comprehensive C/C++ library for controlling CP5200 series LED display controllers with Python wrapper support.

## Features

- **Multi-Protocol Support**: TCP/IP, RS-232, RS-485 communication
- **Text Display**: UTF-8 support with various fonts, colors, and effects
- **Image Display**: GIF file support with positioning and animation
- **Clock Display**: Multiple calendar types (Gregorian, Moon, Chinese Moon)
- **Brightness Control**: Manual (0-31) and automatic brightness
- **Multi-Window Support**: Split screen and window management
- **Time Synchronization**: Automatic time sync with display controller
- **Python Wrapper**: Full Python support with ctypes integration

## System Requirements

- **OS**: Linux (Ubuntu, Debian, Raspberry Pi OS)
- **Architecture**: x86_64, ARM (Raspberry Pi compatible)
- **Dependencies**: build-essential, g++, make, libiconv-hook-dev

## Quick Installation

### Automated Installation

```bash
# Clone or download the library
cd cp5200

# Run the Python installation script
python3 cp5200_install.py
```

### Manual Installation

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install build-essential g++ make libiconv-hook-dev pkg-config

# Build the library
make clean
make all

# Install (as root)
sudo ./install.sh
```

## Usage

### C/C++ Usage

```c
#include <cp5200.h>

int main() {
    // Enable debug mode
    _set_cp5200_debug();
    
    // Configure network communication
    _set_cp5200_ipcomm("192.168.1.100", 5200);
    _set_cp5200_send_mode(0); // TCP/IP mode
    
    // Send text to display
    SendText(0, "Hello CP5200!", 1, 16, 5, 1, 10, 0);
    
    // Send clock display
    int format[] = {1,0,0,0,0,0,0,0}; // multiline
    int content[] = {1,1,1,0,0,0,0,0}; // show date, time
    int colors[] = {255, 255, 255}; // white
    SendClock(0, 30, 0, format, content, "Current Time", colors, 16);
    
    return 0;
}
```

### Python Usage

```python
from cp5200_wrapper import create_display

# Create display instance
display = create_display("192.168.1.100", 5200, debug=True)

# Send text
display.send_text(0, "Hello CP5200!", 1, 16, 5, 1, 10, 0)

# Send clock
format_array = [1, 0, 0, 0, 0, 0, 0, 0]
content_array = [1, 1, 1, 0, 0, 0, 0, 0]
colors = [255, 255, 255]
display.send_clock(0, 30, 0, format_array, content_array, "Current Time", colors, 16)
```

## API Reference

### C/C++ Functions

#### Communication Setup
- `_set_cp5200_debug()` - Enable debug mode
- `_set_cp5200_send_mode(int mode)` - Set communication mode (0=TCP/IP, 1=RS-232, 2=RS-485)
- `_set_cp5200_ipcomm(char *ip, int port)` - Configure network communication
- `_set_cp5200_rs232comm(char *port, int baud)` - Configure serial communication

#### Display Functions
- `SendText(int window, char *text, int color, int font_size, int speed, int effect, int stay_time, int align)` - Display text
- `SendPicture(int window, int x, int y, char *file, int speed, int effect, int stay_time)` - Display image
- `SendClock(int window, int stay_time, int calendar_type, int format[], int content[], char *text, int colors[], int font_size)` - Display clock
- `SplitWindow(int window, int config[], int count)` - Configure window splitting

#### Control Functions
- `SyncTime()` - Synchronize time with controller
- `BrightnessControl(int get_set, int brightness)` - Get/set brightness (0=get, 1=set)

### Python Methods

#### Display Class
- `set_network_mode(ip_address, port)` - Configure network communication
- `set_serial_mode(port, baud_rate)` - Configure serial communication
- `send_text(window, text, color, font_size, speed, effect, stay_time, align)` - Display text
- `send_picture(window, x, y, file_path, speed, effect, stay_time)` - Display image
- `send_clock(window, stay_time, calendar_type, format_array, content_array, text, colors, font_size)` - Display clock
- `set_brightness(brightness)` - Set brightness (0-31 manual, 255 auto)
- `get_brightness()` - Get current brightness
- `sync_time()` - Synchronize time

## Testing

### Run All Tests

```bash
# Using the test Makefile
make -f cp5200_test_makefile test

# Or run individual tests
make -f cp5200_test_makefile test-c      # C tests
make -f cp5200_test_makefile test-python # Python tests
```

### Custom Configuration

```bash
# Test with custom IP/port
make -f cp5200_test_makefile test-custom

# Test network connectivity
make -f cp5200_test_makefile test-network

# Check system information
make -f cp5200_test_makefile sys-info
```

### Python Test Suite

```bash
# Run Python tests
python3 cp5200_test.py

# Run with custom configuration
python3 cp5200_test.py --ip 192.168.1.100 --port 5200
```

## Examples

### Basic Text Display

```python
from cp5200_wrapper import create_display

display = create_display("192.168.1.100", 5200)

# Simple text
display.send_text(0, "Hello World!", 1, 16, 5, 1, 10, 0)

# Colored text
display.send_text(0, "Red Text", 2, 18, 3, 2, 15, 1)
```

### Clock Display

```python
# Gregorian calendar with date and time
format_array = [1, 0, 0, 0, 0, 0, 0, 0]  # Multiline
content_array = [1, 1, 1, 0, 0, 0, 0, 0]  # Show date, time
colors = [255, 255, 255]  # White

display.send_clock(0, 30, 0, format_array, content_array, "Current Time", colors, 16)
```

### Multi-Window Display

```python
# Display different content in different windows
display.send_text(0, "TIME", 1, 16, 5, 1, 10, 0)
display.send_text(1, "TEMP: 22°C", 2, 14, 5, 1, 10, 0)
display.send_text(2, "STATUS: OK", 3, 14, 5, 1, 10, 0)
```

## Configuration

### Network Configuration

```python
# TCP/IP communication
display.set_network_mode("192.168.1.100", 5200)
```

### Serial Configuration

```python
# RS-232 communication
display.set_serial_mode("/dev/ttyAMA0", 115200)
```

### Brightness Control

```python
# Manual brightness (0-31)
display.set_brightness(15)  # 50% brightness

# Auto brightness
display.set_brightness(255)
```

## Troubleshooting

### Common Issues

#### Connection Failed
- Check IP address and port configuration
- Verify network connectivity: `ping 192.168.1.100`
- Check firewall settings
- Ensure CP5200 controller is powered on

#### Compilation Errors
- Install required dependencies: `sudo apt-get install build-essential g++ make libiconv-hook-dev`
- Check library installation: `make -f cp5200_test_makefile check-lib`
- Verify system architecture compatibility

#### Python Import Errors
- Ensure `cp5200_wrapper.py` is in the current directory
- Check library installation: `ls /usr/local/lib/libcp5200.a`
- Verify Python version: `python3 --version`

#### Serial Communication Issues
- Check serial port permissions: `sudo usermod -a -G dialout $USER`
- Verify port existence: `ls -l /dev/ttyAMA0`
- Test with different baud rates

### Debug Mode

Enable debug mode to see detailed communication logs:

```python
display = create_display("192.168.1.100", 5200, debug=True)
```

### Network Testing

Test network connectivity:

```bash
# Test connection
nc -zv 192.168.1.100 5200

# Check routing
traceroute 192.168.1.100
```

## File Structure

```
cp5200/
├── cp5200.h              # Header file
├── cp5200.cpp            # Main library implementation
├── Makefile              # Build configuration
├── install.sh            # Installation script
├── cp5200_install.py     # Python installation script
├── cp5200_test.c         # C test suite
├── cp5200_test.py        # Python test suite
├── cp5200_test_makefile  # Test Makefile
├── cp5200_example.py     # Usage examples
├── cp5200_README.md      # This documentation
├── nbproject/            # NetBeans project files
└── dist/                 # Build output
```

## Version History

- **v3.1** (2025-03-13): Added brightness query and set functionality
- **v2.5** (2025-02-26): Rebuild on Debian Bookworm
- **v2.1** (2020-10-09): Rebuild with improvements
- **v2.0** (2017-06-15): Major version update
- **v1.0** (2017-02-03): Initial release

## License

This library is provided as-is for educational and commercial use.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Run the test suite to verify installation
3. Enable debug mode for detailed logs
4. Verify network/serial connectivity

## Contributing

To contribute to this library:
1. Test your changes thoroughly
2. Update documentation
3. Follow the existing code style
4. Add appropriate error handling

---

**Note**: This library is specifically designed for CP5200 series LED display controllers. Ensure compatibility with your hardware before use.
