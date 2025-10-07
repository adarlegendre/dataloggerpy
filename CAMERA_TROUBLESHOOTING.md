# UNV ANPR Camera Troubleshooting Guide

## Current Status
✅ Camera registered successfully (Device ID: 001)  
❌ No vehicle detection data received

## Why You're Not Receiving Vehicle Data

The camera has registered, but it needs additional configuration to send vehicle/plate data.

---

## 🔧 Camera Settings to Check

### 1. **Access Camera Web Interface**
```
URL: http://192.168.2.13
Username: admin
Password: kObliha12@
```

### 2. **Platform/Server Settings**
Navigate to: **Configuration → Network → Platform Access**

**Required Settings:**
```
☐ Enable Platform: YES/Checked
☐ Protocol: VIID / GB28181 / HTTP
☐ Server IP: 192.168.2.101
☐ Server Port: 5000
☐ Device ID: 001 (already set ✅)
☐ Register Interval: 60 seconds
☐ Heartbeat Interval: 30 seconds
```

### 3. **Vehicle Detection Upload Settings**
Navigate to: **Configuration → Event → Smart Event → IVS**

**Critical Settings:**
```
☐ Enable Vehicle Detection: YES
☐ Upload to Platform: YES ← MOST IMPORTANT
☐ Upload Method: Platform / HTTP POST
☐ Upload on Detection: YES
☐ Minimum Confidence: 70-80%
```

### 4. **ANPR Settings**
Navigate to: **Configuration → Smart → ANPR**

**Required Settings:**
```
☐ Enable ANPR: YES
☐ Recognition Region: [Set detection area]
☐ Upload Recognition Result: YES ← CRITICAL
☐ Plate Recognition Confidence: 70-80%
☐ Upload Image: YES (optional but recommended)
```

### 5. **Trigger Settings**
Navigate to: **Configuration → Event → Trigger**

**Options:**
```
Option 1: Continuous Mode (recommended for testing)
  - Detects all passing vehicles automatically

Option 2: Video Detection
  - Triggers on motion in detection area

Option 3: External Trigger
  - Requires loop detector or sensor
```

---

## 🧪 Test the Camera

### **Test 1: Manual Trigger (if available)**
- Go to camera web interface
- Find "Test" or "Manual Trigger" option
- Click to send test data
- Check your listener output

### **Test 2: Drive/Walk in Front of Camera**
- Make sure a vehicle/object passes in the detection zone
- Check listener for incoming POST requests

### **Test 3: Check Camera Logs**
In camera web interface:
- **Maintenance → System Log**
- Look for upload errors or connection issues
- Look for "Upload Success" messages

---

## 📊 What You Should See

### **After Fixing Settings:**

```
[POST] Request from 192.168.2.13: /VIID/MotorVehicles
[TIME] 2025-10-07 14:30:45
[HEADERS]:
  Content-Type: application/json
  Content-Length: 1234
[TYPE] Unknown/Vehicle Data endpoint
[CONTENT-LENGTH] 1234 bytes

[RAW DATA FROM /VIID/MotorVehicles]
============================================================
{
  "MotorVehicleListObject": {
    "MotorVehicleObject": [{
      "PlateNo": "ABC123",
      "VehicleColor": "White",
      ...
    }]
  }
}
============================================================

[FOUND] .MotorVehicleListObject.MotorVehicleObject[0].PlateNo = ABC123
```

---

## 🔍 Common Issues

### **Issue 1: "Upload to Platform" is Disabled**
**Fix:** Enable in Platform Access settings

### **Issue 2: Camera in "Manual Trigger" Mode**
**Fix:** Change to Continuous or Video Detection mode

### **Issue 3: Wrong Server IP/Port**
**Fix:** Verify server IP is 192.168.2.101 and port is 5000

### **Issue 4: Detection Area Not Set**
**Fix:** Configure detection region in ANPR settings

### **Issue 5: Confidence Threshold Too High**
**Fix:** Lower to 70-80% for testing

### **Issue 6: Network Issues**
**Test:**
```bash
# From Raspberry Pi, test camera connection:
ping 192.168.2.13

# From camera, it should be able to reach:
ping 192.168.2.101
```

---

## 📱 Alternative: Use Camera SDK/API

If platform upload doesn't work, you can pull data from camera:

### **Option 1: FTP Upload**
Configure camera to upload images to FTP server, then process them.

### **Option 2: ONVIF Events**
Subscribe to ONVIF events from the camera.

### **Option 3: HTTP Pull**
Query camera API periodically for recent detections.

---

## 🆘 Quick Checklist

Before asking for help, verify:

- [ ] Camera can ping server (192.168.2.101)
- [ ] Server can ping camera (192.168.2.13)
- [ ] Port 5000 is open on server
- [ ] "Upload to Platform" is ENABLED
- [ ] "Upload Recognition Result" is ENABLED
- [ ] Camera is in detection mode (not manual trigger)
- [ ] Detection area is configured
- [ ] Listener is running and shows registration
- [ ] A vehicle has actually passed the camera

---

## 📞 Next Steps

1. **Access camera web interface** at http://192.168.2.13
2. **Find Platform/Upload settings** (usually under Network or Event)
3. **Enable "Upload to Platform"** and "Upload Recognition Result"
4. **Set to Continuous mode** for testing
5. **Save and apply settings**
6. **Test with a vehicle** passing the camera
7. **Check listener output** for incoming data

The camera is registered and connected - you just need to enable the upload feature!

