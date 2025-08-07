# CP5200 LED Display - Raspberry Pi Setup Guide

## Quick Start

### 1. Test Connection
First, test if your Raspberry Pi can connect to the CP5200 display:

```bash
python3 test_cp5200_connection.py
```

This will test:
- Network connectivity (ping)
- Socket connection to port 5200
- Display readiness

### 2. Send Your First Message
If the connection test passes, send a test message:

```bash
python3 cp5200_raspberry_pi.py --message "Hello World!"
```

### 3. Run Demo
See the display in action with a demo sequence:

```bash
python3 cp5200_raspberry_pi.py --demo
```

### 4. Interactive Mode
Use the interactive controller:

```bash
python3 cp5200_raspberry_pi.py
```

Then type commands like:
- `message Hello Raspberry Pi!`
- `demo` - Run demo sequence
- `clock` - Show clock
- `test` - Test communication
- `quit` - Exit

## Display Configuration

Your CP5200 display is configured at:
- **IP Address**: 192.168.1.222
- **Port**: 5200
- **Protocol**: TCP/IP

## Available Commands

### Command Line Options
```bash
# Send a single message
python3 cp5200_raspberry_pi.py --message "Your message here"

# Run demo sequence
python3 cp5200_raspberry_pi.py --demo

# Show clock
python3 cp5200_raspberry_pi.py --clock

# Test communication
python3 cp5200_raspberry_pi.py --test

# Get controller time
python3 cp5200_raspberry_pi.py --time

# Use different IP (if needed)
python3 cp5200_raspberry_pi.py --ip 192.168.1.100 --message "Test"
```

### Interactive Commands
When running in interactive mode:
- `message <text>` - Send a message
- `demo` - Run demo sequence
- `clock` - Show clock
- `test` - Test communication
- `time` - Get controller time
- `quit` - Exit

## Message Parameters

You can customize messages with different parameters:

```python
# Example: Custom message with parameters
controller.send_instant_message(
    text="Custom Message",
    font_size=20,        # Font size (8-32)
    color=0xFF0000,      # Red color
    effect=1,            # 1=Draw, 2=Scroll
    speed=5,             # Speed (1-10)
    stay_time=3          # Display time in seconds
)
```

## Color Codes

Common color values:
- `0xFF0000` - Red
- `0x00FF00` - Green  
- `0x0000FF` - Blue
- `0xFFFF00` - Yellow
- `0xFF00FF` - Magenta
- `0x00FFFF` - Cyan
- `0xFFFFFF` - White

## Effect Types

- `1` - Draw effect (text appears character by character)
- `2` - Scroll effect (text scrolls across screen)

## Troubleshooting

### Connection Issues

1. **Ping fails**
   ```bash
   ping 192.168.1.222
   ```
   - Check if display is powered on
   - Verify network cable connection
   - Check IP address is correct

2. **Socket connection fails**
   ```bash
   telnet 192.168.1.222 5200
   ```
   - Check if port 5200 is open
   - Verify display is listening on network
   - Check firewall settings

3. **Permission denied**
   ```bash
   sudo chmod +x cp5200_raspberry_pi.py
   sudo chmod +x test_cp5200_connection.py
   ```

### Display Issues

1. **No text appears**
   - Check font size (try smaller values)
   - Verify text length (not too long)
   - Try different colors

2. **Text appears but disappears quickly**
   - Increase `stay_time` parameter
   - Check if display is in correct mode

3. **Wrong colors**
   - Verify color codes are correct
   - Check display color settings

## Integration with Your Project

### Basic Integration
```python
from cp5200_raspberry_pi import CP5200Controller

# Initialize controller
controller = CP5200Controller(ip_address='192.168.1.222')

# Connect and send message
if controller.connect():
    controller.send_instant_message("Hello from my app!")
    controller.disconnect()
```

### Continuous Display
```python
import time
from cp5200_raspberry_pi import CP5200Controller

controller = CP5200Controller()
controller.connect()

# Send messages continuously
messages = ["Message 1", "Message 2", "Message 3"]
for msg in messages:
    controller.send_instant_message(msg)
    time.sleep(5)  # Wait 5 seconds between messages

controller.disconnect()
```

## Log Files

The controller creates log files:
- `cp5200_controller.log` - Main application log
- Console output shows real-time status

## Advanced Features

### Multi-Window Support
```python
# Send to different windows
controller.send_text("Window 1", window_no=0)
controller.send_text("Window 2", window_no=1)
```

### Clock Display
```python
# Show current time
controller.send_clock(
    window_no=0,
    stay_time=10,
    format_type=1,  # 12/24 hour format
    font_size=16,
    red=255, green=255, blue=255  # White color
)
```

### Custom Effects
```python
# Custom message with specific parameters
controller.send_instant_message(
    text="Custom Effect",
    font_size=18,
    color=0x00FF00,  # Green
    effect=2,         # Scroll effect
    speed=3,          # Fast speed
    stay_time=5       # 5 seconds
)
```

## Performance Tips

1. **Reuse connections** - Don't connect/disconnect for each message
2. **Batch messages** - Send multiple messages in sequence
3. **Error handling** - Always check connection status
4. **Logging** - Monitor logs for issues

## Security Notes

- The display uses plain TCP/IP communication
- No authentication is required
- Consider network security for production use
- Keep display on isolated network if possible

## Support

If you encounter issues:

1. Run the connection test first
2. Check the log files for errors
3. Verify display settings
4. Test with simple messages first
5. Check network connectivity

The CP5200 SDK provides a robust foundation for LED display control, and this implementation makes it easy to use with Raspberry Pi for various applications including digital signage, information displays, and real-time data visualization. 