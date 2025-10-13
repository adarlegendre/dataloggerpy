# How Radar Data Reading Works

## Overview

The system reads radar data from a **serial port** (USB/RS232 connection) and processes it in real-time.

## Step-by-Step Process

### 1. Serial Port Connection

**Configuration** (from RadarConfig model):
```python
Port: /dev/ttyUSB0 (or COM3 on Windows)
Baud Rate: 9600 (default) - configurable
Timeout: 0.01 seconds (10ms)
```

**Connection Code:**
```python
with serial.Serial(
    port=radar.port,              # e.g., /dev/ttyUSB0
    baudrate=radar.baud_rate,     # e.g., 9600
    timeout=0.01,                 # 10ms timeout
    write_timeout=0.01,
    inter_byte_timeout=0.01
) as ser:
```

### 2. Continuous Reading Loop

**The radar sends data continuously:**
```
A+000  A+000  A+005  A+012  A+018  A+015  A+008  A+000  A+000
```

**Reading Process:**
```python
while not stop_event.is_set():
    # Read 32 bytes at a time
    data = ser.read(32)
    
    # Add to buffer
    buffer += data
    
    # Process complete messages (5 bytes each)
    while len(buffer) >= 5:
        chunk = buffer[:5]  # e.g., b'A+012'
        buffer = buffer[5:]  # Remove processed chunk
        
        # Decode and process
        process_chunk(chunk)
```

### 3. Data Format

**Radar sends 5-byte messages:**

| Byte | Meaning | Example |
|------|---------|---------|
| 0 | Command | `A` (always 'A' for speed data) |
| 1 | Direction | `+` (approaching) or `-` (receding) |
| 2-4 | Speed | `012` (3 digits, 0-255 km/h) |

**Examples:**
- `A+000` = Approaching, 0 km/h (no vehicle)
- `A+045` = Approaching, 45 km/h
- `A-030` = Receding, 30 km/h

### 4. Parsing the Data

```python
# Example: chunk = b'A+045'
decoded = chunk.decode('utf-8')  # 'A+045'

direction_sign = decoded[1]      # '+'
speed_str = decoded[2:]          # '045'
speed_val = int(speed_str)       # 45

if direction_sign == '+':
    direction_name = "Approaching"  # From radar config
else:
    direction_name = "Receding"     # From radar config
```

### 5. Data Queue System

**Processed data goes into a queue:**

```python
display_data = {
    'status': 'success',
    'range': None,                    # Not available in this format
    'speed': 45,                      # km/h
    'timestamp': 1697123456.789,
    'connection_status': 'connected',
    'raw_data': 'A+045',
    'display_text': '[CONNECTED] Speed: 45km/h',
    'direction_name': 'Approaching',
    'direction_prefix': 'A+'
}

data_queue.put(display_data)  # Send to frontend
```

### 6. Frontend Retrieval

**API endpoint** (`/api/radar-data/{radar_id}/`):

```python
def radar_data_api(request, radar_id):
    # Get latest data from queue
    data = data_queue.get_nowait()
    return JsonResponse(data)
```

**Frontend polls** every 1 second (1000ms):
```javascript
setInterval(updateRadarData, 1000);  // Update every 1 second
```

## Reading Speed vs Display Speed

### Backend (Radar Reading):
- **Sampling Rate**: 100ms (10 times/second) - configurable via `update_interval`
- **Data Rate**: Radar sends ~10 messages/second
- **Processing**: Every message is processed and queued

### Frontend (Display Update):
- **Update Rate**: 1000ms (1 time/second)
- **Data Pulled**: Gets newest data from queue
- **Charts**: Update smoothly with new data point

## Buffer Management

**Why we use a buffer:**
```
Radar sends:    A+012A+015A+018A+020
                ^^^^^^ ^^^^^^ ^^^^^^ ^^^^^^
                Msg 1  Msg 2  Msg 3  Msg 4

Without buffer: Might read partial message: A+012A+
With buffer:    Reads all, processes complete 5-byte chunks
```

**Buffer Processing:**
```python
# Incoming: b'A+012A+015A+'
buffer = b'A+012A+015A+'

# Process 5 bytes at a time:
chunk1 = b'A+012'  → Process → Speed: 12 km/h
chunk2 = b'A+015'  → Process → Speed: 15 km/h
remaining = b'A+'  → Wait for more data
```

## Detection Logic

**The system tracks vehicle passages:**

### Zero Detection:
```python
consecutive_zeros = 0
max_consecutive_zeros = 10  # 10 consecutive zeros = detection complete

if speed_val == 0:
    consecutive_zeros += 1
    if consecutive_zeros >= max_consecutive_zeros:
        # Vehicle has passed, save detection
        save_detection(current_detection)
        current_detection = []
else:
    consecutive_zeros = 0
    current_detection.append(data)  # Add to ongoing detection
```

### Example Detection:
```
A+000  A+000  → No vehicle (zeros ignored)
A+005  A+012  → Vehicle detected! Start tracking
A+025  A+032  → Continuing...
A+028  A+020  → Vehicle moving away
A+010  A+005  → Still tracking
A+000  A+000  → 1st zero
A+000  A+000  → More zeros...
(10 zeros total)
→ Detection complete! Save to database
```

## Data Flow Diagram

```
┌─────────────┐
│   Radar     │ Sends: A+045
│   Device    │
└──────┬──────┘
       │ Serial Port (/dev/ttyUSB0)
       ▼
┌─────────────┐
│Serial Reader│ Read 32 bytes
│   Thread    │
└──────┬──────┘
       │ Buffer: b'A+045A+048...'
       ▼
┌─────────────┐
│   Parser    │ Extract 5-byte chunks
└──────┬──────┘
       │ Decoded: 'A+045'
       ▼
┌─────────────┐
│  Processor  │ Parse: speed=45, dir='+'
└──────┬──────┘
       │ Data object
       ▼
┌─────────────┐
│    Queue    │ Store for API
└──────┬──────┘
       │ Latest data
       ▼
┌─────────────┐
│  API/View   │ GET /api/radar-data/{id}/
└──────┬──────┘
       │ JSON response
       ▼
┌─────────────┐
│  Frontend   │ Update charts/display
│  (Browser)  │
└─────────────┘
```

## Configuration Options

**All configurable via Django Admin:**

| Setting | Default | Range | Purpose |
|---------|---------|-------|---------|
| **Port** | /dev/ttyUSB0 | Any serial port | Where radar is connected |
| **Baud Rate** | 9600 | 1200-115200 | Communication speed |
| **Update Interval** | 100ms | 50-1000ms | How often to read radar |
| **File Save Interval** | 5 min | 1-60 min | How often to save data files |
| **Direction Names** | Approaching/Receding | Text | Display labels |

## Reading Intervals

### Current Setup (After Fixes):

**Backend Reading:**
```python
while True:
    data = ser.read(32)           # Read from radar
    process_data(data)            # Parse and queue
    time.sleep(0.1)               # 100ms delay (from update_interval)
    # Results in ~10 readings/second
```

**Frontend Polling:**
```javascript
setInterval(updateRadarData, 1000);  // Poll every 1 second
// Gets newest data point from queue
```

**Why different rates?**
- Backend reads fast (100ms) to catch all vehicle movements
- Frontend updates slower (1000ms) for smooth display without overwhelming browser
- Queue holds recent data between frontend polls

## Error Handling

### Connection Errors:
```python
try:
    with serial.Serial(...) as ser:
        # Read data
except serial.SerialException as e:
    # Reconnect after 5 seconds
    connection_retry_delay = 5
    time.sleep(connection_retry_delay)
    # Try again (max 3 attempts)
```

### Data Timeout:
```python
data_timeout = 30  # seconds
if current_time - last_valid_data_time > data_timeout:
    logger.warning("No data for 30 seconds, reconnecting...")
    break  # Reconnect
```

### Malformed Data:
```python
try:
    speed_val = int(speed_str)
except ValueError:
    logger.debug("Invalid speed value, skipping")
    continue  # Skip this chunk
```

## Performance Optimization

### Memory Management:
- **Queue Size**: Limited to 500 items
- **Cache Size**: Limited to 1000 items
- **Auto-cleanup**: Removes old data when limits reached

### CPU Optimization:
- **Small reads**: 32 bytes at a time (fast response)
- **Sleep interval**: 100ms between reads (not spinning)
- **Buffer processing**: Only processes complete messages

## Summary

**How it works:**
1. 🔌 Connect to radar via serial port (9600 baud)
2. 📡 Read data in 32-byte chunks
3. 🔄 Buffer incomplete messages
4. ✂️ Extract 5-byte messages (`A+045`)
5. 🔍 Parse direction and speed
6. 📊 Queue for frontend
7. 🌐 API serves latest data
8. 🖥️ Frontend displays on charts

**Key Points:**
- ⏱️ Backend reads every 100ms (10 samples/sec)
- 🌐 Frontend polls every 1000ms (1 time/sec)
- 0️⃣ All values including zeros are now sent
- 📈 Proper 0 → peak → 0 wave pattern
- 🔁 Auto-reconnect on errors

