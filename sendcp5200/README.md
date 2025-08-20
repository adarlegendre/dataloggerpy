# CP5200 Display Controller - Raspberry Pi Edition

This project provides a Python interface to control CP5200 displays using the original C++ code. It's designed to work on Raspberry Pi and makes it easy to send text and other content to your display.

## 🚀 Quick Start

### 1. Setup on Raspberry Pi

```bash
# Make the setup script executable and run it
chmod +x setup_raspberry_pi.sh
./setup_raspberry_pi.sh
```

### 2. Run the Python Controller

```bash
# Interactive mode (recommended for first use)
python3 run_cp5200_display.py --interactive

# Or send text directly
python3 run_cp5200_display.py --text "Hello World!"
```

## 📋 Prerequisites

- Raspberry Pi (any model)
- Network connection to your CP5200 display
- CP5200 library installed (libcp5200.so)
- Display IP address and port number

## 🔧 Installation

### Automatic Setup (Recommended)
```bash
./setup_raspberry_pi.sh
```

### Manual Setup
```bash
# Install build tools
sudo apt-get update
sudo apt-get install -y build-essential g++ make python3 python3-pip

# Make scripts executable
chmod +x run_cp5200_display.py
chmod +x setup_raspberry_pi.sh
```

## 📖 Usage

### Command Line Options

```bash
python3 run_cp5200_display.py [OPTIONS]

Options:
  --ip IP_ADDRESS     Display IP address (default: 192.168.1.222)
  --port PORT         Display port (default: 5200)
  --text TEXT         Text to send immediately
  --window NUMBER     Window number (default: 1)
  --color NUMBER      Text color 1-16 (default: 1)
  --font-size NUMBER  Font size (default: 16)
  --speed NUMBER      Animation speed 1-10 (default: 5)
  --effect NUMBER     Animation effect 1-10 (default: 1)
  --stay SECONDS      Stay time in seconds (default: 10)
  --alignment NUMBER  Text alignment: 1=left, 2=center, 3=right (default: 1)
  --interactive       Run in interactive mode
  --no-debug          Disable debug mode
```

### Examples

```bash
# Send simple text
python3 run_cp5200_display.py --text "Welcome!"

# Send text with custom settings
python3 run_cp5200_display.py --text "Alert!" --color 2 --font-size 24 --speed 3

# Use different display
python3 run_cp5200_display.py --ip 192.168.1.222 --port 5200 --text "Test"

# Interactive mode for testing
python3 run_cp5200_display.py --interactive
```

## 🎮 Interactive Mode

Interactive mode provides a menu-driven interface:

1. **Send Text** - Enter text to display
2. **Change Settings** - Modify IP, port, debug mode
3. **Test Connection** - Verify network connectivity
4. **Exit** - Quit the program

## 🔍 Troubleshooting

### Common Issues

1. **Build Failed**
   - Ensure build-essential is installed: `sudo apt-get install build-essential`
   - Check that Makefile exists in the current directory

2. **Library Not Found**
   - Install the cp5200 library (check manufacturer documentation)
   - Verify library path: `/usr/local/lib/libcp5200.so` or `/usr/lib/libcp5200.so`

3. **Network Connection Failed**
   - Verify display IP address and port
   - Check network connectivity: `ping [DISPLAY_IP]`
   - Ensure firewall allows the connection

4. **Permission Denied**
   - Make scripts executable: `chmod +x *.py *.sh`

### Debug Mode

Enable debug mode to see detailed output:
```bash
python3 run_cp5200_display.py --text "Test" --debug
```

## 📁 File Structure

```
sendcp5200/
├── run_cp5200_display.py    # Main Python controller
├── setup_raspberry_pi.sh    # Setup script for Raspberry Pi
├── sendcp5200.cpp           # Original C++ source code
├── Makefile                 # Build configuration
├── nbproject/               # NetBeans project files
└── README.md                # This file
```

## 🔗 How It Works

1. **Python Interface** - Provides easy-to-use commands and interactive mode
2. **C++ Compilation** - Automatically builds the original C++ code
3. **Display Communication** - Sends commands to CP5200 display via TCP/IP
4. **Error Handling** - Provides clear feedback and troubleshooting information

## 📚 Function Reference

The script supports these CP5200 functions:

- **Function 2** - Send Text (primary function)
  - Parameters: window, text, color, font_size, speed, effect, stay_time, alignment

## 🤝 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Verify your display settings (IP, port)
3. Ensure the cp5200 library is properly installed
4. Check network connectivity between Pi and display

## 📄 License

This project is based on the original CP5200 SDK. Please refer to the manufacturer's documentation for licensing terms.
