# CP5200 LED Display Library - Build Instructions

## Overview
The CP5200 library provides communication and control capabilities for LED display controllers through TCP/IP, RS-232, or RS-485 protocols.

## Prerequisites
- GCC/G++ compiler with C++11 support
- Linux system (tested on Debian/Ubuntu/Raspberry Pi OS)
- `libiconv` development library

### Install Dependencies (Ubuntu/Debian/Raspberry Pi OS)
```bash
sudo apt-get update
sudo apt-get install build-essential libiconv-hook-dev
```

## Build Options

### Option 1: Standalone Build (Recommended)
Use the standalone Makefile that doesn't require NetBeans project files:

```bash
# Build the library
make -f Makefile.standalone

# Build and test the library
make -f Makefile.standalone test

# Clean build files
make -f Makefile.standalone clean

# Install to system
make -f Makefile.standalone install

# Show help
make -f Makefile.standalone help
```

### Option 2: NetBeans Project Build
If you have the complete NetBeans project structure:

```bash
# Build debug version
make -f nbproject/Makefile-Debug.mk

# Build release version
make -f nbproject/Makefile-Release.mk
```

## What Was Fixed
The original compilation errors were caused by:

1. **Type casting issues**: `(int)cd == -1` was changed to `cd == (iconv_t)-1`
2. **Size type mismatches**: `unsigned int` was changed to `size_t` for `iconv` function parameters
3. **Missing iconv_close**: Added proper cleanup to prevent memory leaks

## Testing
After building, you can test the library:

```bash
# Build test program
make -f Makefile.standalone test

# Run test
./test_cp5200
```

## Installation
The library will be installed to:
- Header: `/usr/local/include/cp5200.h`
- Library: `/usr/local/lib/libcp5200.a`

## Usage Example
```cpp
#include <cp5200.h>

int main() {
    // Set debug mode
    _set_cp5200_debug();
    
    // Configure network communication
    _set_cp5200_ipcomm("192.168.1.100", 5200);
    _set_cp5200_send_mode(0); // TCP/IP mode
    
    // Send text to display
    SendText(0, "Hello World!", 1, 16, 5, 1, 10, 0);
    
    return 0;
}
```

## Compile Your Program
```bash
g++ -o my_program my_program.cpp -lcp5200 -liconv
```

## Troubleshooting

### Common Issues
1. **Missing iconv.h**: Install `libiconv-hook-dev`
2. **Permission denied**: Use `sudo` for install commands
3. **Library not found**: Ensure `/usr/local/lib` is in your library path

### Library Path Issues
If you get "library not found" errors, add to `/etc/ld.so.conf.d/`:
```bash
echo "/usr/local/lib" | sudo tee /etc/ld.so.conf.d/local.conf
sudo ldconfig
```

## Support
This library supports:
- TCP/IP communication (default port 5200)
- RS-232 serial communication
- RS-485 communication
- Text, image, and clock displays
- Multi-window management
- Brightness control
