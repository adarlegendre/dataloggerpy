from requests.auth import HTTPDigestAuth
from threading import Thread
import requests
import json
import time
import socket
import re

# Camera configuration
username = 'admin'
password = 'kObliha12@'
cameraIP = '192.168.2.13'
cameraPort = 80
receiveAlarmDataIP = "192.168.2.101"
receiveAlarmDataPort = 8090
duration = 300
suscribID = -1
url = f'http://{cameraIP}:{cameraPort}/LAPI/V1.0/System/Event/Subscription'

# HTTP request header
headers = {
    'Content-Type': 'application/json',
    'Host': f'{cameraIP}:{cameraPort}',
    'Connection': 'Close',
}

def keepalive():
    while True:
        keepaliveUrl = f"{url}/{suscribID}"
        data = {'Duration': duration}
        jsonStr = json.dumps(data)
        
        try:
            response = requests.put(url=keepaliveUrl, headers=headers, data=jsonStr, 
                                  auth=HTTPDigestAuth(username, password), timeout=5)
            if response.status_code != 200:
                print(f'Keepalive failure: {response.status_code}')
                raise SystemExit(0)
        except Exception as e:
            print(f'Keepalive error: {e}')
            raise SystemExit(0)
        
        time.sleep(duration / 2)

def extract_plate_number(data_json):
    """Extract plate number from event data"""
    try:
        if "StructureInfo" in data_json:
            structure_info = data_json.get("StructureInfo", {})
            obj_info = structure_info.get("ObjInfo", {})
            vehicle_info_list = obj_info.get("VehicleInfoList", [])
            
            if isinstance(vehicle_info_list, list) and vehicle_info_list:
                vehicle_info = vehicle_info_list[0]
                plate_no = vehicle_info.get("PlateAttributeInfo", {}).get("PlateNo", None)
                # Only return valid plate numbers (not None, not "Unknown", not empty)
                if plate_no and plate_no != "Unknown" and plate_no.strip():
                    return plate_no
        return None
    except Exception:
        return None

def listen():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = ('', receiveAlarmDataPort)
        server_socket.bind(server_address)
        server_socket.listen(99)
        print(f'Listening for camera events on port {receiveAlarmDataPort}...')
    except Exception as e:
        print(f"Socket setup error: {e}")
        raise SystemExit(1)
    
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            data = b''
            while True:
                tmp = client_socket.recv(1024)
                if not tmp:
                    break
                data += tmp
            
            try:
                # Split HTTP headers and body
                raw_data_str = data.decode('utf-8', errors='ignore')
                body = raw_data_str.split('\r\n\r\n', 1)[1] if '\r\n\r\n' in raw_data_str else raw_data_str
                
                # Clean JSON: Remove control characters but preserve valid JSON structure
                body = re.sub(r'[\x00-\x1F\x7F]', '', body)
                data_json = json.loads(body)
                
                # Extract and print plate number
                plate_no = extract_plate_number(data_json)
                if plate_no:
                    print(plate_no, flush=True)
            
            except json.JSONDecodeError:
                pass  # Silently ignore JSON decode errors
            except Exception:
                pass  # Silently ignore other errors
            
            client_socket.close()
        
        except Exception:
            continue

def main():
    print("Starting plate number capture...")
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
            suscribeResJson = json.loads(response.text)
            global suscribID
            suscribID = suscribeResJson['Response']['Data']['ID']
            print(f'Subscribed successfully. Waiting for plate numbers...\n')
            
            # Step 2: Start keepalive thread
            t1 = Thread(target=keepalive)
            t1.daemon = True
            t1.start()
            
            # Step 3: Start listen thread
            t2 = Thread(target=listen)
            t2.daemon = True
            t2.start()
            
            # Keep main thread alive
            while True:
                time.sleep(1)
        else:
            print(f'Subscription Failure: {response.status_code} {response.text}')
            raise SystemExit(1)
    except Exception as e:
        print(f'Subscription error: {e}')
        raise SystemExit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript terminated by user")
        raise SystemExit(0)
    except Exception as e:
        print(f"Error: {e}")
        raise SystemExit(1)

