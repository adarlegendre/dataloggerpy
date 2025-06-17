import serial
import time
from datetime import datetime
import json
import os
import sys
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
SERIAL_PORT = 'COM3'  # Change this to match your Arduino's port
BAUD_RATE = 9600
LOG_INTERVAL = 1  # seconds
JSON_FILENAME = 'temperature_humidity_log.json'
API_ENDPOINT = os.getenv('API_ENDPOINT')
API_KEY = os.getenv('API_KEY')

def read_serial_data(ser):
    """Read data from serial port and return temperature and humidity"""
    try:
        if ser.in_waiting:
            # Read the line and decode from bytes to string
            line = ser.readline().decode('utf-8').strip()
            # Remove the * character if present
            if line.startswith('*'):
                line = line[1:]
            # Split the line into temperature and humidity
            temp, hum = map(float, line.split(','))
            # Skip zero values
            if temp == 0.0 and hum == 0.0:
                return None, None
            return temp, hum
    except Exception as e:
        print(f"Error reading serial data: {e}")
    return None, None

def initialize_json():
    """Initialize JSON file with empty array if it doesn't exist"""
    if not os.path.exists(JSON_FILENAME):
        with open(JSON_FILENAME, 'w') as file:
            json.dump([], file)

def log_data(timestamp, temperature, humidity):
    """Log data to JSON file"""
    try:
        # Read existing data
        with open(JSON_FILENAME, 'r') as file:
            data = json.load(file)
        
        # Append new data
        data.append({
            'timestamp': timestamp,
            'temperature': temperature,
            'humidity': humidity
        })
        
        # Write back to file
        with open(JSON_FILENAME, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error logging data to JSON: {e}")

def send_to_api(timestamp, temperature, humidity):
    """Send data to API"""
    if not API_ENDPOINT or not API_KEY:
        print("API configuration missing. Skipping API upload.")
        return

    data = {
        'timestamp': timestamp,
        'temperature': temperature,
        'humidity': humidity
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    
    try:
        response = requests.post(API_ENDPOINT, json=data, headers=headers)
        response.raise_for_status()
        print(f"Data successfully sent to API. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to API: {e}")

def main():
    print("Starting Temperature and Humidity Logger...")
    print(f"Logging to {JSON_FILENAME}")
    print(f"Log interval: {LOG_INTERVAL} seconds")
    print("Press Ctrl+C to stop logging")
    
    try:
        # Initialize serial connection
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for Arduino to reset
        
        # Initialize JSON file
        initialize_json()
        
        while True:
            # Read data from serial port
            temperature, humidity = read_serial_data(ser)
            
            if temperature is not None and humidity is not None:
                # Get current timestamp
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # Log data to JSON
                log_data(timestamp, temperature, humidity)
                
                # Send data to API
                send_to_api(timestamp, temperature, humidity)
                
                # Print data to console
                print(f"Time: {timestamp}")
                print(f"Temperature: {temperature:.1f}°C")
                print(f"Humidity: {humidity:.1f}%")
                print("-" * 40)
            
            time.sleep(LOG_INTERVAL)
            
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        print("Please check if the Arduino is connected and the port is correct.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nLogging stopped by user")
        if 'ser' in locals():
            ser.close()
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        if 'ser' in locals():
            ser.close()
        sys.exit(1)

if __name__ == "__main__":
    main() 