# Continuous Display Data Sender

This script continuously sends display data to port 80 using the CP5200 VMS display protocol.

## Files Created

1. **`continuous_display_sender.py`** - Main script that sends display data continuously
2. **`test_receiver.py`** - Test server to receive and display the data
3. **`run_continuous_sender.bat`** - Windows batch script to run the sender
4. **`run_continuous_sender.ps1`** - PowerShell script to run the sender

## Usage

### Option 1: Using the Batch Script (Windows)
```cmd
run_continuous_sender.bat
```

### Option 2: Using the PowerShell Script (Windows)
```powershell
.\run_continuous_sender.ps1
```

### Option 3: Direct Python Execution
```bash
# Activate virtual environment first
venv\Scripts\activate

# Run with default settings (localhost:80, 5-second interval)
python continuous_display_sender.py

# Run with custom settings
python continuous_display_sender.py --ip 192.168.1.100 --port 80 --interval 10

# Run a single test send
python continuous_display_sender.py --test
```

## Command Line Options

- `--ip` - Target IP address (default: localhost)
- `--port` - Target port (default: 80)
- `--interval` - Interval between sends in seconds (default: 5)
- `--test` - Run a single test send instead of continuous

## Testing with Receiver

To test the sender, you can run the test receiver in another terminal:

```bash
# Run test receiver (requires admin privileges for port 80)
python test_receiver.py

# Or use a different port
python test_receiver.py --port 8080
```

Then run the sender pointing to the test receiver:

```bash
python continuous_display_sender.py --ip localhost --port 8080
```

## Features

- **Continuous sending** - Sends display data at regular intervals
- **CP5200 protocol** - Uses the proper VMS display protocol
- **Configurable** - IP, port, and interval can be customized
- **Logging** - Detailed logs saved to `continuous_display.log`
- **Graceful shutdown** - Handles Ctrl+C and system signals
- **Error handling** - Continues running even if individual sends fail
- **Database integration** - Uses Django models for configuration

## Message Format

The script sends test messages in the format:
```
MSG 001 14:30:25
MSG 002 14:30:30
MSG 003 14:30:35
...
```

Each message includes:
- Message counter (3-digit number)
- Current timestamp (HH:MM:SS)

## Protocol Details

The script uses the CP5200 VMS display protocol with:
- 4-byte header (FF FF FF FF)
- 4-byte length field (little endian)
- Command and parameter bytes
- Font size, effect, alignment, and color settings
- Text data (each character followed by 0x12)
- Footer bytes

## Troubleshooting

### Port 80 Permission Denied
If you get permission denied for port 80:
1. Run as administrator (Windows)
2. Use a different port (e.g., 8080)
3. Use `--port 8080` option

### Connection Refused
- Make sure the target device is running and listening on the specified port
- Check firewall settings
- Verify IP address is correct

### Django Setup Issues
- Make sure the virtual environment is activated
- Ensure Django settings are properly configured
- Check that the database is accessible

## Log Files

- `continuous_display.log` - Main application log
- Console output shows real-time status

## Stopping the Script

- Press `Ctrl+C` to stop gracefully
- The script will complete the current send before stopping
- Logs will show the shutdown process 