# CP5200 LED Controller SDK - Raspberry Pi Implementation Guide

## SDK Analysis

### Overview
The CP5200 SDK provides a comprehensive API for controlling LED displays through multiple communication protocols. The SDK is designed for Windows but can be adapted for Raspberry Pi using Python.

### Key Components

#### 1. Communication Types
```c
#define  COMMDATA_TYPE_RS232        0   // rs232 or rs485, GPRS with external DTU
#define  COMMDATA_TYPE_NETWORK      1   // network (LED controller as net server)
#define  COMMDATA_TYPE_NETCLIENT    2   // network (LED controller as net client)
#define  COMMDATA_TYPE_GPRS         3   // GPRS (LED controller with GPRS board)
```

#### 2. Screen Configuration
- **Width**: 128 pixels (default)
- **Height**: 128 pixels (default)  
- **Color**: 119 (0x77) - grayscale level
- **Color Depth**: Configurable grayscale levels

#### 3. Communication Protocols

##### RS232/RS485 Protocol
- **Baud Rate**: 115200 (default)
- **Data Bits**: 8
- **Stop Bits**: 1
- **Parity**: None
- **Flow Control**: None

##### Network Protocol
- **Default Port**: 5200
- **Protocol**: TCP/IP
- **Card ID**: 1 (default)
- **ID Code**: -1 (default)

### SDK Functions Analysis

#### Core Functions for Raspberry Pi Implementation

1. **Communication Setup**
```c
// RS232 Functions
CP5200_RS232_Init(const char *fName, int nBaudrate)
CP5200_RS232_Open(void)
CP5200_RS232_Close(void)
CP5200_RS232_Write(const void* pBuf, int nLength)
CP5200_RS232_Read(void* pBuf, int nBufSize)

// Network Functions  
CP5200_Net_Init(DWORD dwIP, int nIPPort, DWORD dwIDCode, int nTimeOut)
CP5200_Net_Connect(void)
CP5200_Net_Write(const BYTE* pBuf, int nLength)
CP5200_Net_Read(BYTE* pBuf, int nSize)
```

2. **Display Control Functions**
```c
// Send instant messages
CP5200_RS232_SendInstantMessage(BYTE nCardID, BYTE byPlayTimes, int x, int y, int cx, int cy, BYTE byFontSizeColor, int nEffect, BYTE nSpeed, BYTE byStayTime, const char* pText)

// Send text to specific window
CP5200_RS232_SendText(int nCardID, int nWndNo, const char *pText, COLORREF crColor, int nFontSize, int nSpeed, int nEffect, int nStayTime, int nAlignment)

// Send clock
CP5200_RS232_SendClock(int nCardID, int nWinNo, int nStayTime, int nCalendar, int nFormat, int nContent, int nFont, int nRed, int nGreen, int nBlue, LPCSTR pTxt)
```

3. **System Control Functions**
```c
// Test communication
CP5200_RS232_TestCommunication(int nCardID)

// Get/set time
CP5200_RS232_GetTime(int nCardID, BYTE *pBuf, int nBufSize)
CP5200_RS232_SetTime(BYTE nCardID, const BYTE *pInfo)

// Restart functions
CP5200_RS232_RestartApp(BYTE nCardID)
CP5200_RS232_RestartSys(BYTE nCardID)
```

## Raspberry Pi Implementation

### Prerequisites

1. **Hardware Requirements**
   - Raspberry Pi (3B+, 4B recommended)
   - USB-to-RS232 converter (for serial communication)
   - Ethernet cable (for network communication)
   - Power supply for LED controller

2. **Software Requirements**
   ```bash
   # Install required packages
   sudo apt-get update
   sudo apt-get install python3-pip python3-serial
   pip3 install pyserial
   ```

### Implementation Options

#### Option 1: Python Serial Communication (Recommended)

```python
#!/usr/bin/env python3
"""
CP5200 LED Controller - Raspberry Pi Implementation
Using Python serial communication
"""

import serial
import time
import struct
import logging

class CP5200Controller:
    def __init__(self, port='/dev/ttyUSB0', baudrate=115200, card_id=1):
        self.port = port
        self.baudrate = baudrate
        self.card_id = card_id
        self.serial = None
        self.logger = logging.getLogger(__name__)
        
    def connect(self):
        """Initialize serial connection"""
        try:
            self.serial = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=1
            )
            self.logger.info(f"Connected to CP5200 on {self.port}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to connect: {e}")
            return False
    
    def disconnect(self):
        """Close serial connection"""
        if self.serial and self.serial.is_open:
            self.serial.close()
            self.logger.info("Disconnected from CP5200")
    
    def send_instant_message(self, text, x=0, y=0, width=128, height=128, 
                           font_size=16, color=0xFF0000, effect=1, speed=5, stay_time=3):
        """Send instant message to display"""
        try:
            # Build CP5200 protocol packet
            packet = self._build_instant_message_packet(
                text, x, y, width, height, font_size, color, effect, speed, stay_time
            )
            
            # Send packet
            self.serial.write(packet)
            self.logger.info(f"Sent message: {text}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to send message: {e}")
            return False
    
    def _build_instant_message_packet(self, text, x, y, width, height, 
                                    font_size, color, effect, speed, stay_time):
        """Build CP5200 protocol packet for instant message"""
        
        # Convert text to bytes with 0x12 suffix for each character
        text_bytes = b''
        for char in text:
            text_bytes += char.encode('ascii') + b'\x12'
        
        # Calculate packet length
        data_length = len(text_bytes) + 20  # Base length + text length
        
        # Build packet
        packet = bytearray()
        
        # Header (4 bytes)
        packet.extend(b'\xFF\xFF\xFF\xFF')
        
        # Length (4 bytes, little endian)
        packet.extend(struct.pack('<I', data_length))
        
        # Command/parameters
        packet.extend(b'\x68\x32\x01\x7B')
        
        # Font size, effect, alignment, color
        packet.extend(bytes([font_size, effect, 0x01, color & 0xFF, 0x00]))
        
        # Text parameters
        packet.extend(b'\x02\x00\x00\x01\x06\x00\x00')
        
        # Text data
        packet.extend(text_bytes)
        
        # Footer
        packet.extend(b'\x00\x00\x00\x68\x03')
        
        return bytes(packet)
    
    def test_communication(self):
        """Test communication with controller"""
        try:
            # Send test packet
            test_packet = b'\xFF\xFF\xFF\xFF\x00\x00\x00\x00'
            self.serial.write(test_packet)
            
            # Read response
            response = self.serial.read(10)
            if response:
                self.logger.info("Communication test successful")
                return True
            else:
                self.logger.warning("No response from controller")
                return False
                
        except Exception as e:
            self.logger.error(f"Communication test failed: {e}")
            return False

# Usage example
def main():
    # Initialize controller
    controller = CP5200Controller(port='/dev/ttyUSB0', baudrate=115200)
    
    # Connect to controller
    if controller.connect():
        # Test communication
        if controller.test_communication():
            # Send test message
            controller.send_instant_message("Hello Raspberry Pi!", 
                                         font_size=16, 
                                         color=0xFF0000,  # Red
                                         effect=1,         # Draw effect
                                         speed=5,          # Medium speed
                                         stay_time=3)      # 3 seconds
            
            # Wait and send another message
            time.sleep(5)
            controller.send_instant_message("CP5200 Working!", 
                                         font_size=20, 
                                         color=0x00FF00,  # Green
                                         effect=2,         # Scroll effect
                                         speed=3,          # Fast speed
                                         stay_time=5)      # 5 seconds
        
        # Disconnect
        controller.disconnect()

if __name__ == "__main__":
    main()
```

#### Option 2: Network Communication

```python
#!/usr/bin/env python3
"""
CP5200 LED Controller - Network Communication
Using TCP/IP communication
"""

import socket
import struct
import time
import logging

class CP5200NetworkController:
    def __init__(self, ip_address, port=5200, card_id=1):
        self.ip_address = ip_address
        self.port = port
        self.card_id = card_id
        self.socket = None
        self.logger = logging.getLogger(__name__)
    
    def connect(self):
        """Connect to CP5200 via network"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.ip_address, self.port))
            self.logger.info(f"Connected to CP5200 at {self.ip_address}:{self.port}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to connect: {e}")
            return False
    
    def disconnect(self):
        """Close network connection"""
        if self.socket:
            self.socket.close()
            self.logger.info("Disconnected from CP5200")
    
    def send_message(self, text, font_size=16, color=0xFF0000, effect=1, speed=5, stay_time=3):
        """Send message via network"""
        try:
            # Build network packet
            packet = self._build_network_packet(text, font_size, color, effect, speed, stay_time)
            
            # Send packet
            self.socket.send(packet)
            self.logger.info(f"Sent message via network: {text}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to send message: {e}")
            return False
    
    def _build_network_packet(self, text, font_size, color, effect, speed, stay_time):
        """Build network protocol packet"""
        
        # Convert text to bytes
        text_bytes = text.encode('ascii')
        
        # Build packet header
        packet = bytearray()
        
        # Network header
        packet.extend(struct.pack('<I', self.card_id))  # Card ID
        packet.extend(struct.pack('<I', len(text_bytes) + 16))  # Data length
        
        # Command and parameters
        packet.extend(b'\x68\x32\x01\x7B')
        
        # Font and display parameters
        packet.extend(bytes([font_size, effect, 0x01, color & 0xFF, 0x00]))
        
        # Text data
        packet.extend(text_bytes)
        
        return bytes(packet)

# Usage example
def main():
    # Initialize network controller
    controller = CP5200NetworkController(ip_address='192.168.1.100', port=5200)
    
    # Connect to controller
    if controller.connect():
        # Send test messages
        controller.send_message("Network Test", font_size=16, color=0xFF0000)
        time.sleep(3)
        controller.send_message("CP5200 Network", font_size=20, color=0x00FF00)
        
        # Disconnect
        controller.disconnect()

if __name__ == "__main__":
    main()
```

### Configuration Files

#### 1. CP5200 Configuration (testcp5200.ini)
```ini
[SCREEN]
Width=128
Height=128
Color=119

[COMM]
Type=0          # 0=RS232, 1=Network, 2=Network Client, 3=GPRS
Port=1          # COM port for RS232
Baudrate=115200
CardID=1
IPAddress=-1062731420  # Network IP (if using network)
IPPort=5200
IDCode=-1
```

#### 2. Raspberry Pi Configuration
```bash
# Enable serial port
sudo raspi-config
# Navigate to: Interface Options > Serial Port
# Enable serial port and disable serial console

# Check available serial ports
ls /dev/tty*

# Set permissions for USB serial device
sudo chmod 666 /dev/ttyUSB0
```

### Advanced Features

#### 1. Multi-Window Support
```python
def send_multi_window_message(self, messages):
    """Send messages to multiple windows"""
    for i, (text, x, y, width, height) in enumerate(messages):
        self.send_instant_message(text, x, y, width, height)
```

#### 2. Clock Display
```python
def send_clock(self, format_type=1, stay_time=10):
    """Send clock display"""
    # Build clock packet
    clock_packet = self._build_clock_packet(format_type, stay_time)
    self.serial.write(clock_packet)
```

#### 3. Temperature/Humidity Display
```python
def send_temperature(self, temperature, humidity, stay_time=5):
    """Send temperature and humidity data"""
    text = f"Temp: {temperature}°C  Hum: {humidity}%"
    self.send_instant_message(text, font_size=14, color=0x00FFFF)
```

### Troubleshooting

#### Common Issues

1. **Permission Denied**
   ```bash
   sudo chmod 666 /dev/ttyUSB0
   sudo usermod -a -G dialout $USER
   ```

2. **No Response from Controller**
   - Check baud rate settings
   - Verify cable connections
   - Test with different USB ports

3. **Network Connection Issues**
   - Verify IP address and port
   - Check firewall settings
   - Test with ping command

#### Debug Commands
```bash
# Check serial port
ls -la /dev/tty*

# Monitor serial communication
sudo apt-get install minicom
minicom -D /dev/ttyUSB0 -b 115200

# Test network connectivity
ping 192.168.1.100
telnet 192.168.1.100 5200
```

### Performance Optimization

1. **Connection Pooling**
   - Reuse connections when possible
   - Implement connection timeouts

2. **Message Queuing**
   - Queue messages for smooth display
   - Implement priority system

3. **Error Handling**
   - Implement retry mechanisms
   - Log all communication errors

### Security Considerations

1. **Network Security**
   - Use VPN for remote connections
   - Implement authentication if supported

2. **Physical Security**
   - Secure physical access to controller
   - Use tamper-evident enclosures

3. **Data Validation**
   - Validate all input data
   - Sanitize text messages

## Conclusion

The CP5200 SDK provides a robust foundation for LED display control. By implementing the Python-based solutions above, you can successfully use the CP5200 LED controller with Raspberry Pi for various applications including:

- Digital signage
- Information displays
- Status indicators
- Real-time data visualization
- Interactive displays

The modular design allows for easy customization and extension based on specific requirements. 