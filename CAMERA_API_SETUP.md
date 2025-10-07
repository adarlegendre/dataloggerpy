# Camera API Listener Setup

## Configuration

### Server (Raspberry Pi at 192.168.2.101)
- **Port**: 5000 (already open)
- **Endpoints**: 
  - `/api/upark/capture` - Main endpoint for vehicle detections
  - `/NotificationInfo/TollgateInfo` - Alternative endpoint
  - `/status` - Status check (no auth required)
- **Authentication**: HTTP Basic Auth
  - **Username**: `admin`
  - **Password**: `kObliha12@`

### Camera (Client at 192.168.2.13)
- Sends POST requests to: `http://192.168.2.101:5000/api/upark/capture`
- Must include HTTP Basic Auth headers
- Content-Type: `application/json`

## Running the Listener

### Start the listener:
```bash
python camera_api_listener.py
```

When prompted, press Enter to use port 5000 (default).

### The listener will:
1. Start HTTP server on port 5000
2. Listen for POST requests from any client (camera at 192.168.2.13)
3. Require authentication (admin/kObliha12@)
4. Parse JSON data and extract vehicle/plate information
5. Log all detections
6. Send success response back to camera

## Expected JSON Format from Camera

```json
{
  "deviceId": "CAMERA_001",
  "params": {
    "plateNo": "{ABC123}",
    "vehicleType": "car",
    "confidence": 95.5,
    "picTime": "2025-10-07T12:30:45",
    "picInfo": [
      {"url": "vehicle_image.jpg"}
    ]
  }
}
```

## Testing the Listener

### Option 1: Check Status
```bash
curl http://localhost:5000/status
```

### Option 2: Send Test Data (with auth)
```bash
curl -X POST http://localhost:5000/api/upark/capture \
  -u admin:kObliha12@ \
  -H "Content-Type: application/json" \
  -d '{
    "deviceId": "TEST_CAMERA",
    "params": {
      "plateNo": "{TEST123}",
      "vehicleType": "car",
      "confidence": 95.5,
      "picTime": "2025-10-07T12:30:45",
      "picInfo": [{"url": "test.jpg"}]
    }
  }'
```

### Option 3: Run Automated Tests
```bash
python test_camera_auth.py
```

## What Happens When Camera Sends Data

1. **Camera** (192.168.2.13) sends POST with auth headers
2. **Server** (192.168.2.101:5000) receives request
3. **Authentication** check (admin/kObliha12@)
4. **Parse** JSON data
5. **Extract** vehicle information:
   - Device ID
   - Plate Number (removes curly braces)
   - Vehicle Type
   - Confidence
   - Picture Info
6. **Process** if plate number exists (following C# logic)
7. **Store** detection data
8. **Respond** with `{"Result": true, "Message": "Success"}`

## Output Example

```
=== Camera API Listener ===

Camera Configuration:
  Camera (Client): 192.168.2.13
  Server (This Raspberry Pi): 192.168.2.101
  Server Port: 5000
  Username: admin
  Password: kObliha12@
  Endpoint: /api/upark/capture
  Method: POST
  Format: JSON
  Authentication: HTTP Basic Auth

Enter listener port [5000]: 

Server listening on: http://192.168.2.101:5000/api/upark/capture
With authentication: admin / kObliha12@
You can check status at: http://localhost:5000/status
Camera at 192.168.2.13 should send POST requests to this endpoint

Starting Camera API Listener...
Listener Port: 5000
Target Camera: 192.168.2.13:5000
Authentication: admin / kObliha12@
Endpoint: http://YOUR_IP:5000/api/upark/capture
Status: http://localhost:5000/status
[OK] HTTP server started on port 5000
[LISTEN] Waiting for camera POST requests...
[INFO] Press Ctrl+C to stop
============================================================

[POST] Request received: /api/upark/capture
[AUTH OK] 192.168.2.13
[REQUEST] From 192.168.2.13 at 2025-10-07 12:30:45.123456
[PATH] /api/upark/capture
[CONTENT-TYPE] application/json
[CONTENT-LENGTH] 234
[JSON] Data received:
{
  "deviceId": "CAMERA_001",
  "params": {
    "plateNo": "{ABC123}",
    ...
  }
}

*** VEHICLE DETECTION DATA ***
*** VEHICLE DETECTION DATA ***
*** VEHICLE DETECTION DATA ***
   Device ID: CAMERA_001
   Plate Number: ABC123
   Vehicle Type: car
   Confidence: 95.5
   Picture Time: 2025-10-07T12:30:45
   Picture Name: vehicle_image.jpg

[PROCESS] Calling processExitting...
[STATS] Total detections: 1
```

## Next Steps

1. ✅ Camera API listener is running on port 5000
2. ✅ Authentication is configured (admin/kObliha12@)
3. ✅ Accepts connections from any client
4. 🔄 Configure camera to send POST requests to this endpoint
5. 📋 Integrate received data into Django application

## Troubleshooting

### Port already in use
```bash
# Check what's using port 5000
netstat -ano | findstr :5000

# Kill the process if needed
taskkill /PID <PID> /F
```

### Authentication fails
- Make sure the camera sends HTTP Basic Auth header
- Credentials: admin:kObliha12@
- Header format: `Authorization: Basic YWRtaW46a09ibGloYTEyQA==`

### No data received
- Check camera configuration
- Verify network connectivity between 192.168.2.13 and 192.168.2.101
- Check firewall rules on port 5000
- Verify endpoint URL: `http://192.168.2.101:5000/api/upark/capture`

