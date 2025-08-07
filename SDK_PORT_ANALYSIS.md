# CP5200 SDK - Connection Ports Analysis

## 🔍 **How to Get Connection Ports from the SDK**

### **📋 Default Port Configuration:**

From the SDK configuration file (`testcp5200.ini`):
```ini
[COMM]
Type=0          # 0=RS232, 1=Network
Port=1          # COM port for RS232
Baudrate=115200 # Baud rate for RS232
CardID=1        # Controller card ID
IPAddress=-1062731420  # Network IP (encoded)
IPPort=5200     # Network port (default)
IDCode=-1       # Device ID code
```

### **🌐 Network Connection Ports:**

#### **1. Default Network Port:**
- **Port**: `5200` (default)
- **Protocol**: TCP/IP
- **Function**: `CP5200_Net_Init(dwIP, nIPPort, dwIDCode, nTimeOut)`

#### **2. SDK Network Functions:**
```cpp
// Network initialization
CP5200API int CALLING_CONV CP5200_Net_Init(DWORD dwIP, int nIPPort, DWORD dwIDCode, int nTimeOut);

// Network connection
CP5200API int CALLING_CONV CP5200_Net_Connect(void);
CP5200API int CALLING_CONV CP5200_Net_IsConnected(void);
CP5200API int CALLING_CONV CP5200_Net_Disconnect(void);

// Network data transfer
CP5200API int CALLING_CONV CP5200_Net_Write(const BYTE* pBuf, int nLength);
CP5200API int CALLING_CONV CP5200_Net_Read(BYTE* pBuf, int nSize);
```

### **🔌 Serial Connection Ports:**

#### **1. Default Serial Settings:**
- **Port**: `COM1` (Port=1 in config)
- **Baudrate**: `115200`
- **Protocol**: RS232/RS485

#### **2. SDK Serial Functions:**
```cpp
// Serial initialization
CP5200API int CALLING_CONV CP5200_RS232_Init(const char *fName, int nBaudrate);
CP5200API int CALLING_CONV CP5200_RS232_InitEx(const char *fName, int nBaudrate, DWORD dwTimeout);

// Serial connection
CP5200API int CALLING_CONV CP5200_RS232_Open(void);
CP5200API int CALLING_CONV CP5200_RS232_OpenEx(DWORD dwReadTimeout, DWORD dwWriteTimeout);
CP5200API int CALLING_CONV CP5200_RS232_Close(void);
CP5200API int CALLING_CONV CP5200_RS232_IsOpened(void);

// Serial data transfer
CP5200API int CALLING_CONV CP5200_RS232_Write(const void* pBuf, int nLength);
CP5200API int CALLING_CONV CP5200_RS232_Read(void* pBuf, int nBufSize);
```

### **🔧 How to Get Port Information:**

#### **1. From Configuration File:**
```cpp
// Read from testcp5200.ini
IPPort=5200        // Network port
Port=1             // Serial port (COM1)
Baudrate=115200    // Serial baud rate
```

#### **2. From SDK Functions:**
```cpp
// Network port is passed as parameter
CP5200_Net_Init(dwIP, nIPPort, dwIDCode, nTimeOut);
//                    ^^^^^^^^
//                    This is the port number

// Serial port is passed as string
CP5200_RS232_InitEx("COM1", 115200, timeout);
//                    ^^^^^
//                    This is the port name
```

#### **3. From GUI Application:**
```cpp
// From CPower_VCDlg.cpp
void CPower_VCDlg::InitComm()
{
    if (m_nCommType == 1) // Network
    {
        DWORD dwIPAddr, dwIDCode;
        m_ctrlIPAddr.GetAddress(dwIPAddr);
        m_ctrlIDCode.GetAddress(dwIDCode);
        CP5200_Net_Init(dwIPAddr, m_nPort, dwIDCode, m_nTimeOut);
        //                           ^^^^^^^
        //                           Port from GUI
    }
    else // Serial
    {
        CString strPort;
        strPort.Format("%d", m_cmbPort.GetCurSel()+1);
        CP5200_RS232_InitEx("COM" + strPort, glBaudrete[m_cmbBaudrate.GetCurSel()], m_nTimeOut);
        //                                    ^^^^^^^^^^^^^
        //                                    Port from GUI
    }
}
```

### **📊 Port Configuration Options:**

#### **Network Ports:**
- **Default**: `5200`
- **Common Alternatives**: `23` (Telnet), `80` (HTTP), `8080` (HTTP Alt)
- **Range**: `1-65535`

#### **Serial Ports:**
- **Default**: `COM1`
- **Common**: `COM1`, `COM2`, `COM3`, `COM4`
- **Baudrates**: `9600`, `19200`, `38400`, `57600`, `115200`

### **🔍 How to Discover Ports:**

#### **1. Network Port Discovery:**
```python
# Scan common ports
ports = [5200, 23, 22, 80, 8080, 5000, 5001]

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"✅ Port {port} is open")
        sock.close()
    except:
        pass
```

#### **2. Serial Port Discovery:**
```python
import serial.tools.list_ports

# List available serial ports
ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"Found: {port.device} - {port.description}")
```

### **🎯 Port Usage in Python Implementation:**

#### **Network Connection:**
```python
class CP5200Controller:
    def __init__(self, ip_address='192.168.1.222', port=5200):
        self.ip_address = ip_address
        self.port = port  # Default from SDK
        self.socket = None
    
    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5)
            self.socket.connect((self.ip_address, self.port))
            return True
        except Exception as e:
            print(f"Failed to connect: {e}")
            return False
```

#### **Serial Connection:**
```python
import serial

class CP5200SerialController:
    def __init__(self, port='COM1', baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.serial = None
    
    def connect(self):
        try:
            self.serial = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=5
            )
            return True
        except Exception as e:
            print(f"Failed to connect: {e}")
            return False
```

### **📋 Summary:**

#### **Default Ports from SDK:**
- **Network**: `5200` (TCP/IP)
- **Serial**: `COM1` (RS232/RS485 at 115200 baud)

#### **How to Get Ports:**
1. **From config file**: `testcp5200.ini`
2. **From SDK functions**: Parameters in `CP5200_Net_Init()` and `CP5200_RS232_Init()`
3. **From GUI**: User interface controls
4. **From discovery**: Network/port scanning

#### **Port Discovery Methods:**
1. **Network scanning**: Try common ports (5200, 23, 80, etc.)
2. **Serial enumeration**: List available COM ports
3. **Configuration files**: Read device settings
4. **Device documentation**: Check manufacturer specs

### **🚀 Quick Port Test:**

```python
def test_ports(ip):
    """Test common CP5200 ports"""
    ports = [5200, 23, 80, 8080, 5000]
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"✅ Port {port} is open")
            sock.close()
        except:
            pass

# Test your device
test_ports('192.168.1.222')
``` 