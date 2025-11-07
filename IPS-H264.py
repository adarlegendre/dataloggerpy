from requests.auth import HTTPDigestAuth
from threading import Thread
import requests
import json
import time
import socket
import os
import base64
from datetime import datetime
import logging
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('error_log.txt', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# Camera configuration
username = 'admin'
password = 'kObliha12@'
cameraIP = '192.168.2.13'
cameraPort = 8090
receiveAlarmDataIP = "192.168.1.196"
receiveAlarmDataPort = 64073
duration = 300
suscribID = -1
url = f'http://{cameraIP}:{cameraPort}/LAPI/V1.0/System/Event/Subscription'

# HTTP request header
headers = {
    'Content-Type': 'application/json',
    'Host': f'{cameraIP}:{cameraPort}',
    'Connection': 'Close',
}

# Create directory for images
image_folder = "camera_images"
try:
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
        logging.info(f"Created image folder: {image_folder}")
except Exception as e:
    logging.error(f"Failed to create image folder {image_folder}: {e}")

# Create/Open text file for logging
log_file_path = "camera_events.txt"
try:
    with open(log_file_path, 'a', encoding='utf-8') as f:
        f.write(f"Log started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    logging.info(f"Initialized log file: {log_file_path}")
except Exception as e:
    logging.error(f"Failed to initialize log file {log_file_path}: {e}")

def keepalive():
    while True:
        keepaliveUrl = f"{url}/{suscribID}"
        data = {'Duration': duration}
        jsonStr = json.dumps(data)
        
        try:
            response = requests.put(url=keepaliveUrl, headers=headers, data=jsonStr, 
                                  auth=HTTPDigestAuth(username, password), timeout=5)
            if response.status_code == 200:
                logging.info(f'keepalive succeeded: {response.text}')
            else:
                logging.error(f'keepalive failure: {response.status_code} {response.text}')
                logging.error('Exiting program')
                raise SystemExit(0)
        except Exception as e:
            logging.error(f'keepalive error: {e}')
            logging.error('Exiting program')
            raise SystemExit(0)
        
        time.sleep(duration / 2)

def save_image_from_base64(base64_data, filename):
    """Convert base64 data to JPG and save to image_folder"""
    try:
        image_data = base64.b64decode(base64_data)
        safe_filename = "".join(c for c in filename if c.isalnum() or c in ('-', '_')) + ".jpg"
        file_path = os.path.join(image_folder, safe_filename)
        with open(file_path, 'wb') as f:
            f.write(image_data)
        logging.info(f"Image saved: {file_path}")
    except Exception as e:
        logging.error(f"Error saving image {filename}: {e}")

def format_event(data_json, event_id):
    """Format event data into a single line for logging"""
    try:
        # Log the entire JSON for debugging
        logging.info(f"Event {event_id}: Full JSON: {json.dumps(data_json, indent=2)}")

        timestamp = data_json.get("TimeStamp", "")
        event_time = (datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') 
                     if timestamp else "Unknown")

        # Handle different event types
        if "AlarmInfo" in data_json:
            # Handle MotionAlarmOff or similar events
            alarm_info = data_json["AlarmInfo"]
            alarm_type = alarm_info.get("AlarmType", "Unknown")
            logging.info(f"Event {event_id}: Alarm event detected, type: {alarm_type}")
            log_line = (f"DateTime:{event_time}, PlateNo:Unknown, VehicleType:Unknown, "
                       f"VehicleColor:Unknown, LaneID:Unknown, EventID:{event_id}, EventType:{alarm_type}")
            return log_line, "Unknown", event_id
        elif "StructureInfo" in data_json:
            # Handle Structure events
            structure_info = data_json.get("StructureInfo", {})
            logging.info(f"Event {event_id}: StructureInfo keys: {list(structure_info.keys())}")
            logging.info(f"Event {event_id}: StructureInfo content: {json.dumps(structure_info, indent=2)}")

            image_info_list = structure_info.get("ImageInfoList", [{}])
            capture_time = image_info_list[0].get("CaptureTime", "") if image_info_list else "Unknown"
            if capture_time and event_time == "Unknown":
                event_time = (capture_time[:10] + " " + capture_time[10:12] + ":" + capture_time[12:14] + ":" + capture_time[14:16] 
                             if capture_time else "Unknown")

            # Access VehicleInfoList from ObjInfo
            obj_info = structure_info.get("ObjInfo", {})
            vehicle_info_list = obj_info.get("VehicleInfoList", [])
            logging.info(f"Event {event_id}: VehicleInfoList type: {type(vehicle_info_list)}, length: {len(vehicle_info_list)}, content: {json.dumps(vehicle_info_list, indent=2)}")

            if not isinstance(vehicle_info_list, list) or not vehicle_info_list:
                logging.warning(f"Event {event_id}: 'VehicleInfoList' is empty or not a list, using default values")
                plate_no = "Unknown"
                vehicle_type = "Unknown"
                vehicle_color = "Unknown"
                lane_id = "Unknown"
            else:
                vehicle_info = vehicle_info_list[0]
                plate_no = vehicle_info.get("PlateAttributeInfo", {}).get("PlateNo", "Unknown")
                vehicle_type = vehicle_info.get("VehicleAttributeInfo", {}).get("Type", "Unknown")
                vehicle_color = vehicle_info.get("VehicleAttributeInfo", {}).get("VehicleColor", "Unknown")
                lane_id = vehicle_info.get("LaneInfo", {}).get("ID", "Unknown")

            logging.info(f"Event {event_id}: Extracted - PlateNo: {plate_no}, VehicleType: {vehicle_type}, "
                        f"VehicleColor: {vehicle_color}, LaneID: {lane_id}, CaptureTime: {capture_time}, "
                        f"TimeStamp: {timestamp}")

            # Map vehicle type and color
            vehicle_types = {9: "Sedan", 10: "SUV", 1: "Truck", 2: "Bus"}
            vehicle_colors = {"6": "Silver", "1": "White", "2": "Black", "7": "Unknown"}

            vehicle_type_str = vehicle_types.get(int(str(vehicle_type)), str(vehicle_type)) if str(vehicle_type).isdigit() else "Unknown"
            vehicle_color_str = vehicle_colors.get(str(vehicle_color), str(vehicle_color)) if vehicle_color != "Unknown" else "Unknown"

            log_line = (f"DateTime:{event_time}, PlateNo:{plate_no}, VehicleType:{vehicle_type_str}, "
                       f"VehicleColor:{vehicle_color_str}, LaneID:{lane_id}, EventID:{event_id}, EventType:Structure")
            return log_line, plate_no, capture_time
        else:
            logging.warning(f"Event {event_id}: Unknown event type, no AlarmInfo or StructureInfo")
            log_line = (f"DateTime:{event_time}, PlateNo:Unknown, VehicleType:Unknown, "
                       f"VehicleColor:Unknown, LaneID:Unknown, EventID:{event_id}, EventType:Unknown")
            return log_line, "Unknown", event_id

    except Exception as e:
        logging.error(f"Event {event_id}: Error formatting event: {e}")
        return None, None, None

def listen():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = ('', receiveAlarmDataPort)
        server_socket.bind(server_address)
        server_socket.listen(99)
        logging.info(f'The socket service is running and listening on port {receiveAlarmDataPort}')
    except Exception as e:
        logging.error(f"Socket setup error: {e}")
        logging.error('Exiting program')
        raise SystemExit(1)
    
    event_counter = 0
    
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            logging.info(f'Alarm data received from {client_address}')
            event_counter += 1
            data = b''
            while True:
                tmp = client_socket.recv(1024)
                if not tmp:
                    break
                data += tmp
            
            # Save raw data for debugging
            with open("raw_data_log.txt", 'a', encoding='utf-8') as f:
                raw_data_str = data.decode('utf-8', errors='ignore')
                f.write(f"Event {event_counter}:\n{raw_data_str}\n{'='*50}\n")
            
            try:
                # Split HTTP headers and body
                body = raw_data_str.split('\r\n\r\n', 1)[1] if '\r\n\r\n' in raw_data_str else raw_data_str
                
                # Log raw body and characters around position 160
                logging.info(f"Event {event_counter}: Raw body before parsing: {body[:200]}...")
                if len(body) >= 160:
                    error_context = body[max(0, 150):min(len(body), 170)]
                    logging.info(f"Event {event_counter}: Characters around position 160: {repr(error_context)}")
                
                # Clean JSON: Remove control characters but preserve valid JSON structure
                body = re.sub(r'[\x00-\x1F\x7F]', '', body)
                data_json = json.loads(body)
                
                log_line, plate_no, capture_time = format_event(data_json, event_counter)
                if log_line:
                    try:
                        with open(log_file_path, 'a', encoding='utf-8') as f:
                            f.write(log_line + '\n')
                        logging.info(f"Logged event: {log_line}")
                    except Exception as e:
                        logging.error(f"Error writing to {log_file_path}: {e}")
                
                if "StructureInfo" in data_json:
                    structure_info = data_json["StructureInfo"]
                    for image_info in structure_info.get("ImageInfoList", []):
                        base64_data = image_info.get("Data", "")
                        if base64_data:
                            image_filename = f"{capture_time or event_counter}_{plate_no or 'Unknown'}_{image_info.get('Index', 'Unknown')}"
                            save_image_from_base64(base64_data, image_filename)
            
            except json.JSONDecodeError as e:
                logging.error(f"JSON decode error for event {event_counter}: {e}")
                logging.error(f"Raw data saved to raw_data_log.txt")
                # Log fallback event
                event_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_line = (f"DateTime:{event_time}, PlateNo:Unknown, VehicleType:Unknown, "
                           f"VehicleColor:Unknown, LaneID:Unknown, EventID:{event_counter}, EventType:ParseError")
                try:
                    with open(log_file_path, 'a', encoding='utf-8') as f:
                        f.write(log_line + '\n')
                    logging.info(f"Logged fallback event: {log_line}")
                except Exception as e:
                    logging.error(f"Error writing fallback event to {log_file_path}: {e}")
            
            except Exception as e:
                logging.error(f"Error processing data for event {event_counter}: {e}")
            
            client_socket.close()
        
        except Exception as e:
            logging.error(f"Socket accept error: {e}")
            continue

def main():
    logging.info("Starting script")
    # Step 1: Subscribe
    data = {
        "AddressType": 0,
        "IPAddress": receiveAlarmDataIP,
        "Port": receiveAlarmDataPort,
        "Duration": duration
    }
    jsonStr = json.dumps(data)

    try:
        response = requests.post(url=url, headers=headers, data=jsonStr, 
                               auth=HTTPDigestAuth(username, password), timeout=5)
        if response.status_code == 200:
            logging.info(f'Subscription Success: {response.text}')
            suscribeResJson = json.loads(response.text)
            global suscribID
            suscribID = suscribeResJson['Response']['Data']['ID']
            logging.info(f'Obtained subscription ID: {suscribID}')
            
            # Step 2: Start keepalive thread
            t1 = Thread(target=keepalive)
            t1.daemon = True
            t1.start()
            
            # Step 3: Start listen thread
            t2 = Thread(target=listen)
            t2.daemon = True
            t2.start()
            
            # Keep main thread alive
            logging.info("Script is running. Press Ctrl+C to stop.")
            while True:
                time.sleep(1)
        else:
            logging.error(f'Subscription Failure: {response.status_code} {response.text}')
            logging.error('Exiting program')
            raise SystemExit(1)
    except Exception as e:
        logging.error(f'Subscription error: {e}')
        logging.error('Exiting program')
        raise SystemExit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Script terminated by user")
        raise SystemExit(0)
    except Exception as e:
        logging.error(f"Main loop error: {e}")
        raise SystemExit(1)