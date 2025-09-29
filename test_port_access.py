#!/usr/bin/env python3
"""
Test script to verify port access using the exact same approach as the working script
"""

import serial
import time

def test_port_access():
    """Test port access using the exact same approach as the working script"""
    print("Testing port access with the same approach as your working script...")
    print("Port: /dev/ttyAMA0, Baudrate: 9600, Timeout: 0.01")
    print("Press Ctrl+C to stop")
    
    try:
        # Use the exact same parameters as your working script
        ser = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=0.01)
        print("✅ Successfully opened serial port")
        
        buffer = b''
        
        while True:
            # Use the exact same reading approach as your working script
            data = ser.read(32)  # Smaller read for fast response
            if data:
                buffer += data
                print(f"Received {len(data)} bytes, buffer now: {len(buffer)} bytes")

                # Process fixed-size messages if they're always 5 bytes like 'A+123'
                while len(buffer) >= 5:
                    chunk = buffer[:5]
                    buffer = buffer[5:]

                    if chunk.startswith(b'A') and len(chunk) == 5:
                        value = chunk[1:].decode(errors='ignore')  # "+123", "-005", etc.
                        if value != '+000' and value != '-000':
                            print("Received:", chunk.decode(errors='ignore'))
                        else:
                            print("Received (zero):", chunk.decode(errors='ignore'))
                    else:
                        print("Received (non-A):", chunk.decode(errors='ignore'))
            else:
                # No data received, small sleep like in your working script
                time.sleep(0.001)
                
    except serial.SerialException as e:
        print(f"❌ Serial port error: {e}")
        print("This usually means:")
        print("1. Port is already in use by another process")
        print("2. Device is disconnected")
        print("3. Permission denied")
        return False
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        try:
            ser.close()
            print("✅ Serial port closed")
        except:
            pass
    
    return True

if __name__ == "__main__":
    success = test_port_access()
    if success:
        print("\n✅ Port access test completed successfully")
        print("The port is working with the same approach as your script")
    else:
        print("\n❌ Port access test failed")
        print("Check if another process is using the port")
