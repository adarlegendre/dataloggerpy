#!/usr/bin/env python3
"""
Czech License Plates Display for CP5200 LED Display
Generates and displays Czech license plates on the LED display
"""

import random
import string
import time
import argparse
from cp5200_raspberry_pi import CP5200Controller

class CzechPlateGenerator:
    def __init__(self):
        # Czech license plate format: 3 letters + space + 4 digits
        self.letters = string.ascii_uppercase
        self.digits = string.digits
    
    def generate_plate(self):
        """Generate a random Czech license plate"""
        # Generate 3 random uppercase letters
        letters = ''.join(random.choices(self.letters, k=3))
        
        # Generate 4 random digits
        digits = ''.join(random.choices(self.digits, k=4))
        
        # Format: ABC 1234
        plate = f"{letters} {digits}"
        return plate
    
    def generate_multiple_plates(self, count=10):
        """Generate multiple unique Czech license plates"""
        plates = set()
        while len(plates) < count:
            plates.add(self.generate_plate())
        return list(plates)

def display_czech_plates(controller, plates, font_size=16, color=0xFF0000, 
                        effect=1, speed=5, stay_time=3):
    """Display Czech license plates on the LED display"""
    print(f"Displaying {len(plates)} Czech license plates...")
    print("=" * 50)
    
    for i, plate in enumerate(plates, 1):
        print(f"Plate {i}/{len(plates)}: {plate}")
        
        # Send to display
        success = controller.send_instant_message(
            text=plate,
            font_size=font_size,
            color=color,
            effect=effect,
            speed=speed,
            stay_time=stay_time
        )
        
        if success:
            print(f"  ✓ Sent: {plate}")
        else:
            print(f"  ✗ Failed to send: {plate}")
        
        # Wait for message to complete plus a small delay
        time.sleep(stay_time + 1)

def continuous_plate_display(controller, interval=5, max_plates=None):
    """Continuously display random Czech plates"""
    generator = CzechPlateGenerator()
    plate_count = 0
    
    print("Starting continuous Czech plate display...")
    print("Press Ctrl+C to stop")
    print("=" * 50)
    
    try:
        while True:
            if max_plates and plate_count >= max_plates:
                print(f"Reached maximum plates ({max_plates}). Stopping.")
                break
            
            # Generate a new plate
            plate = generator.generate_plate()
            plate_count += 1
            
            print(f"Plate #{plate_count}: {plate}")
            
            # Send to display
            success = controller.send_instant_message(
                text=plate,
                font_size=18,
                color=0x00FF00,  # Green for continuous mode
                effect=2,         # Scroll effect
                speed=4,
                stay_time=interval
            )
            
            if success:
                print(f"  ✓ Displayed: {plate}")
            else:
                print(f"  ✗ Failed: {plate}")
            
            # Wait for next plate
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\nStopping continuous display...")

def demo_czech_plates(controller):
    """Run a demo with sample Czech plates"""
    sample_plates = [
        "ABC 1234",
        "XYZ 5678", 
        "DEF 9012",
        "GHI 3456",
        "JKL 7890",
        "MNO 2345",
        "PQR 6789",
        "STU 0123",
        "VWX 4567",
        "YZA 8901"
    ]
    
    print("Czech License Plates Demo")
    print("=" * 50)
    
    # Display with different colors and effects
    colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF]  # Red, Green, Blue, Yellow, Magenta
    effects = [1, 2]  # Draw, Scroll
    
    for i, plate in enumerate(sample_plates):
        color = colors[i % len(colors)]
        effect = effects[i % len(effects)]
        
        print(f"Demo Plate {i+1}: {plate} (Color: {color:06X}, Effect: {effect})")
        
        controller.send_instant_message(
            text=plate,
            font_size=16,
            color=color,
            effect=effect,
            speed=5,
            stay_time=3
        )
        
        time.sleep(4)  # Wait for message to complete

def main():
    parser = argparse.ArgumentParser(description='Czech License Plates Display')
    parser.add_argument('--ip', default='192.168.1.222', help='Display IP address')
    parser.add_argument('--port', type=int, default=5200, help='Display port')
    parser.add_argument('--count', type=int, default=10, help='Number of plates to generate')
    parser.add_argument('--continuous', action='store_true', help='Continuous display mode')
    parser.add_argument('--interval', type=int, default=5, help='Interval between plates (seconds)')
    parser.add_argument('--max-plates', type=int, help='Maximum plates in continuous mode')
    parser.add_argument('--demo', action='store_true', help='Run demo with sample plates')
    parser.add_argument('--font-size', type=int, default=16, help='Font size (8-32)')
    parser.add_argument('--color', default='0xFF0000', help='Color in hex (e.g., 0xFF0000 for red)')
    parser.add_argument('--effect', type=int, default=1, help='Effect: 1=Draw, 2=Scroll')
    parser.add_argument('--speed', type=int, default=5, help='Speed (1-10)')
    parser.add_argument('--stay-time', type=int, default=3, help='Display time (seconds)')
    
    args = parser.parse_args()
    
    # Parse color
    try:
        color = int(args.color, 16)
    except ValueError:
        print(f"Invalid color format: {args.color}. Using red (0xFF0000)")
        color = 0xFF0000
    
    # Initialize controller
    controller = CP5200Controller(ip_address=args.ip, port=args.port)
    
    # Connect to display
    if controller.connect():
        try:
            if args.demo:
                # Run demo
                demo_czech_plates(controller)
                
            elif args.continuous:
                # Continuous mode
                continuous_plate_display(controller, args.interval, args.max_plates)
                
            else:
                # Generate and display plates
                generator = CzechPlateGenerator()
                plates = generator.generate_multiple_plates(args.count)
                
                print(f"Generated {len(plates)} Czech license plates:")
                for i, plate in enumerate(plates, 1):
                    print(f"  {i}. {plate}")
                print()
                
                # Display plates
                display_czech_plates(
                    controller, 
                    plates, 
                    font_size=args.font_size,
                    color=color,
                    effect=args.effect,
                    speed=args.speed,
                    stay_time=args.stay_time
                )
        
        finally:
            # Disconnect
            controller.disconnect()
    else:
        print(f"Failed to connect to display at {args.ip}:{args.port}")
        print("Please check:")
        print("1. Display is powered on and connected to network")
        print("2. IP address is correct")
        print("3. Port 5200 is open")
        print("4. Network connectivity (try: ping 192.168.1.222)")

if __name__ == "__main__":
    main() 