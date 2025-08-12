#!/usr/bin/env python3
"""
CP5200 LED Display Library - Czech License Plates Example
This file demonstrates how to display various Czech license plate formats
"""

import time
import sys
from datetime import datetime

# Import the CP5200 wrapper
try:
    from cp5200_wrapper import CP5200Display, create_display, CP5200Error
except ImportError:
    print("Error: cp5200_wrapper.py not found. Please run the installation script first.")
    sys.exit(1)

class CzechLicensePlateDisplay:
    def __init__(self, ip_address: str = "192.168.1.100", port: int = 5200):
        """Initialize the Czech license plate display system
        
        Args:
            ip_address: IP address of the CP5200 controller
            port: Network port
        """
        self.display = None
        self.ip_address = ip_address
        self.port = port
        self.connected = False
        
    def connect(self):
        """Connect to the CP5200 display"""
        try:
            self.display = create_display(self.ip_address, self.port, debug=True)
            self.connected = True
            print(f"✓ Connected to CP5200 display at {self.ip_address}:{self.port}")
            return True
        except CP5200Error as e:
            print(f"✗ Connection failed: {e}")
            return False
    
    def display_czech_plate(self, plate_text: str, font_size: int = 48, color: str = "red"):
        """Display a Czech license plate
        
        Args:
            plate_text: License plate text (e.g., "1A2 3456")
            font_size: Font size for display
            color: Text color (red, green, yellow, etc.)
        """
        if not self.connected:
            print("✗ Not connected to display")
            return False
            
        try:
            # Format the plate text with proper spacing
            formatted_text = f"  {plate_text}  "
            
            # Clear the display first
            self.display.clear_display()
            
            # Display the license plate
            result = self.display.send_text(formatted_text, font_size, color)
            
            if result == 0:
                print(f"✓ Displayed Czech plate: {plate_text}")
                return True
            else:
                print(f"✗ Failed to display plate: {plate_text} (error: {result})")
                return False
                
        except CP5200Error as e:
            print(f"✗ Error displaying plate: {e}")
            return False
    
    def display_plate_with_animation(self, plate_text: str, animation_type: str = "scroll"):
        """Display a license plate with animation effects
        
        Args:
            plate_text: License plate text
            animation_type: Type of animation (scroll, blink, fade)
        """
        if not self.connected:
            print("✗ Not connected to display")
            return False
            
        try:
            if animation_type == "scroll":
                # Scroll the plate text from right to left
                for i in range(len(plate_text) + 10):
                    scroll_text = " " * i + plate_text
                    self.display.send_text(scroll_text, 48, "red")
                    time.sleep(0.3)
                    
            elif animation_type == "blink":
                # Blink the plate text
                for _ in range(6):
                    self.display.send_text(plate_text, 48, "red")
                    time.sleep(0.5)
                    self.display.clear_display()
                    time.sleep(0.5)
                    
            elif animation_type == "fade":
                # Fade effect by changing colors
                colors = ["red", "yellow", "green", "blue", "red"]
                for color in colors:
                    self.display.send_text(plate_text, 48, color)
                    time.sleep(0.8)
                    
            print(f"✓ Displayed animated plate: {plate_text}")
            return True
            
        except CP5200Error as e:
            print(f"✗ Error displaying animated plate: {e}")
            return False
    
    def display_multiple_plates(self, plates: list, delay: float = 2.0):
        """Display multiple license plates in sequence
        
        Args:
            plates: List of license plate texts
            delay: Delay between plates in seconds
        """
        if not self.connected:
            print("✗ Not connected to display")
            return False
            
        print(f"Displaying {len(plates)} Czech license plates...")
        
        for i, plate in enumerate(plates, 1):
            print(f"Plate {i}/{len(plates)}: {plate}")
            self.display_czech_plate(plate)
            time.sleep(delay)
    
    def display_plate_with_info(self, plate_text: str, info_text: str = ""):
        """Display a license plate with additional information
        
        Args:
            plate_text: License plate text
            info_text: Additional information to display
        """
        if not self.connected:
            print("✗ Not connected to display")
            return False
            
        try:
            # Clear display
            self.display.clear_display()
            
            # Display main plate text
            self.display.send_text(plate_text, 48, "red")
            
            if info_text:
                # Display info text below (smaller font)
                time.sleep(1)
                self.display.send_text(info_text, 24, "yellow")
                
            print(f"✓ Displayed plate with info: {plate_text} - {info_text}")
            return True
            
        except CP5200Error as e:
            print(f"✗ Error displaying plate with info: {e}")
            return False
    
    def display_emergency_plate(self, plate_text: str):
        """Display an emergency vehicle license plate with special formatting
        
        Args:
            plate_text: Emergency vehicle plate text
        """
        if not self.connected:
            print("✗ Not connected to display")
            return False
            
        try:
            # Clear display
            self.display.clear_display()
            
            # Display emergency plate with flashing effect
            for _ in range(10):
                self.display.send_text(f"EMERGENCY: {plate_text}", 36, "red")
                time.sleep(0.3)
                self.display.clear_display()
                time.sleep(0.3)
                
            print(f"✓ Displayed emergency plate: {plate_text}")
            return True
            
        except CP5200Error as e:
            print(f"✗ Error displaying emergency plate: {e}")
            return False
    
    def close(self):
        """Close the display connection"""
        if self.display:
            self.display.close()
            self.connected = False
            print("✓ Display connection closed")

def main():
    """Main function demonstrating Czech license plate display"""
    print("=" * 60)
    print("CP5200 Czech License Plate Display Example")
    print("=" * 60)
    
    # Create display instance
    plate_display = CzechLicensePlateDisplay("192.168.1.100", 5200)
    
    # Connect to display
    if not plate_display.connect():
        print("Failed to connect. Exiting...")
        return
    
    try:
        # Example 1: Basic Czech license plates
        print("\n=== Example 1: Basic Czech License Plates ===")
        basic_plates = [
            "1A2 3456",      # Prague region
            "2B3 4567",      # Central Bohemia
            "3C4 5678",      # South Bohemia
            "4D5 6789",      # Plzeň region
            "5E6 7890"       # Karlovy Vary region
        ]
        
        plate_display.display_multiple_plates(basic_plates, 2.0)
        
        # Example 2: Animated plates
        print("\n=== Example 2: Animated License Plates ===")
        animated_plates = ["6F7 8901", "7G8 9012", "8H9 0123"]
        
        for plate in animated_plates:
            plate_display.display_plate_with_animation(plate, "scroll")
            time.sleep(1)
        
        # Example 3: Plates with additional information
        print("\n=== Example 3: Plates with Information ===")
        plate_info = [
            ("9I0 1234", "Prague - City Center"),
            ("0J1 2345", "Brno - South Moravia"),
            ("1K2 3456", "Ostrava - Moravian-Silesian")
        ]
        
        for plate, info in plate_info:
            plate_display.display_plate_with_info(plate, info)
            time.sleep(3)
        
        # Example 4: Emergency vehicle plates
        print("\n=== Example 4: Emergency Vehicle Plates ===")
        emergency_plates = ["POLICE", "AMBULANCE", "FIRE"]
        
        for plate in emergency_plates:
            plate_display.display_emergency_plate(plate)
            time.sleep(2)
        
        # Example 5: Custom plate formats
        print("\n=== Example 5: Custom Plate Formats ===")
        custom_plates = [
            "VIP 1234",      # VIP plates
            "TEST 5678",     # Test plates
            "DEMO 9012"      # Demo plates
        ]
        
        for plate in custom_plates:
            plate_display.display_czech_plate(plate, 56, "green")
            time.sleep(2)
        
        print("\n=== All Examples Completed Successfully ===")
        
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    except Exception as e:
        print(f"\nError during execution: {e}")
    finally:
        # Clean up
        plate_display.close()
        print("\nExample completed. Display connection closed.")

if __name__ == "__main__":
    main()
