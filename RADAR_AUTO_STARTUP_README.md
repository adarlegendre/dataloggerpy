# 🚀 Automatic Radar Data Collection Startup System

This system automatically starts reading sensor data when the Django application starts, even without any user accessing the web interface.

## 🎯 **How It Works**

### **1. Automatic Startup**
- When Django starts (via `runserver`, `uwsgi`, etc.), the `AppConfig.ready()` method is called
- This automatically initializes the radar data collection service
- All configured active radars begin reading data immediately
- No user interaction required

### **2. Background Processing**
- Each radar runs in its own background thread
- Data is continuously read from serial ports
- Files are automatically saved based on configured intervals
- Object detections are processed and stored in the database

### **3. Health Monitoring**
- Background monitoring thread checks radar service health every 30 seconds
- Automatically restarts any radar threads that have stopped
- Comprehensive logging of all activities

## 📁 **Files Overview**

### **Core Components**
- `app/utils/startup_service.py` - Main startup service with health monitoring
- `app/services.py` - Radar data collection and processing service
- `app/apps.py` - Django app configuration with automatic startup
- `app/management/commands/check_radar_service.py` - Management command for service control

### **Integration Points**
- `app/views.py` - Web interface integration showing service status
- `app/templates/app/home.html` - Status display in web interface

## 🔧 **System Flow**

```
Django Startup → AppConfig.ready() → StartupService → RadarDataService
     ↓
Background Threads → Serial Port Reading → Data Processing → File Saving
     ↓
Health Monitoring → Thread Status Check → Auto-Restart (if needed)
     ↓
Web Interface → Status Display → Real-time Monitoring
```

## 🚀 **Automatic Startup Process**

### **1. Django App Initialization**
```python
# app/apps.py
def ready(self):
    # Start radar data collection service
    from .utils.startup_service import initialize_radar_data_collection
    success = initialize_radar_data_collection()
```

### **2. Service Startup**
```python
# app/utils/startup_service.py
def start_radar_data_collection(self):
    # Import and start the radar data service
    from ..services import RadarDataService
    self.radar_service = RadarDataService()
    self.radar_service.start_service()
    
    # Start monitoring thread
    self._start_monitoring_thread()
```

### **3. Radar Thread Creation**
```python
# app/services.py
def start_service(self):
    RadarConfig = apps.get_model('app', 'RadarConfig')
    radars = RadarConfig.objects.filter(is_active=True)
    
    for radar in radars:
        self.start_radar_stream(radar)
```

## 📊 **Current Configuration**

Based on your system:
- **Radar**: `radar 3` on port `/dev/ttyAMA0`
- **Status**: Active (configured but not connected on Windows)
- **Update Interval**: 100ms
- **File Save Interval**: 5 minutes
- **Auto-Start**: Enabled

## 🎛️ **Management Commands**

### **Check Service Status**
```bash
python manage.py check_radar_service
```

### **Start Service**
```bash
python manage.py check_radar_service --start
```

### **Restart Service**
```bash
python manage.py check_radar_service --restart
```

## 🖥️ **Web Interface Integration**

### **Status Display**
The home page shows:
- ✅ **Service Status**: Running/Stopped
- 📡 **Radar Service**: Active/Inactive
- 🔢 **Active Radars**: Number of configured radars
- 🧵 **Active Threads**: Number of running threads
- ⏰ **Last Check**: When status was last updated

### **Real-time Monitoring**
- Service status updates automatically
- Connection status for each radar
- Data collection statistics
- Error reporting and alerts

## 🔍 **Monitoring and Logging**

### **Service Logs**
- All startup activities are logged
- Radar connection attempts and failures
- Data processing statistics
- Health monitoring results

### **Log Locations**
- **Application Logs**: Django logging system
- **Service Logs**: `logs/` directory
- **Error Logs**: Console and file output

### **Health Monitoring**
- **Thread Status**: Checks if radar threads are alive
- **Auto-Restart**: Automatically restarts failed threads
- **Connection Monitoring**: Tracks serial port connections
- **Performance Metrics**: Monitors data processing rates

## 🚨 **Troubleshooting**

### **Common Issues**

1. **"Service Status: STOPPED"**
   - Service failed to start during Django initialization
   - Run: `python manage.py check_radar_service --start`

2. **"Connection error for radar"**
   - Serial port not available (expected on Windows with Linux ports)
   - Check radar configuration in web interface
   - Verify serial port settings

3. **"Active Threads: 0"**
   - Radar threads have stopped
   - Run: `python manage.py check_radar_service --restart`
   - Check logs for connection errors

4. **"No active radars found"**
   - No radars configured as active
   - Configure radars in web interface
   - Set `is_active=True` for desired radars

### **Debug Commands**

```bash
# Check service status
python manage.py check_radar_service

# Start service manually
python manage.py check_radar_service --start

# Restart service
python manage.py check_radar_service --restart

# Check Django logs
python manage.py runserver --verbosity=2
```

## 📈 **Benefits**

### **✅ Automatic Operation**
- No manual intervention required
- Starts immediately when system boots
- Continues running in background

### **✅ Reliability**
- Health monitoring and auto-restart
- Comprehensive error handling
- Detailed logging for troubleshooting

### **✅ Integration**
- Seamless web interface integration
- Real-time status monitoring
- Management commands for control

### **✅ Scalability**
- Supports multiple radars
- Independent thread per radar
- Configurable intervals and settings

## 🎉 **Success Indicators**

When everything is working correctly, you should see:

1. **In Management Command:**
   ```
   Service Status: RUNNING
   Radar Service: ACTIVE
   Active Radars: 1
   Active Threads: 1
   ```

2. **In Web Interface:**
   - Service status shows "Running"
   - Active radar count matches configured radars
   - Real-time data updates

3. **In Logs:**
   - "Radar data collection started successfully"
   - "Active radars: 1"
   - Regular health monitoring messages

The system now automatically reads sensor data when the application starts, providing continuous data collection without requiring user interaction! 🚀 