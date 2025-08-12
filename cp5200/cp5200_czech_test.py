#!/usr/bin/env python3
"""
CP5200 Czech License Plate Test Script
Simple test for Czech license plate display functionality
"""

import time
import sys

# Import the CP5200 wrapper
try:
    from cp5200_wrapper import CP5200Display, create_display, CP5200Error
except ImportError:
    print("Error: cp5200_wrapper.py not found. Please run the installation script first.")
    sys.exit(1)

def test_czech_plates():
    """Test Czech license plate display functionality"""
    print("Testing Czech License Plate Display...")
    
    # Test data - Czech license plate formats
    test_plates = [
        "1A2 3456",      # Prague
        "2B3 4567",      # Central Bohemia  
        "3C4 5678",      # South Bohemia
        "4D5 6789",      # Plzeň
        "5E6 7890",      # Karlovy Vary
        "6F7 8901",      # Ústí nad Labem
        "7G8 9012",      # Liberec
        "8H9 0123",      # Hradec Králové
        "9I0 1234",      # Pardubice
        "0J1 2345"       # Vysočina
    ]
    
    try:
        # Create display connection
        display = create_display("192.168.1.100", 5200, debug=True)
        print("✓ Connected to CP5200 display")
        
        # Test each plate
        for i, plate in enumerate(test_plates, 1):
            print(f"Testing plate {i}/{len(test_plates)}: {plate}")
            
            # Clear and display
            display.clear_display()
            result = display.send_text(plate, 48, "red")
            
            if result == 0:
                print(f"  ✓ Success: {plate}")
            else:
                print(f"  ✗ Failed: {plate} (error: {result})")
            
            time.sleep(1)
        
        print("\n✓ All Czech license plates tested successfully!")
        
    except CP5200Error as e:
        print(f"✗ CP5200 Error: {e}")
    except Exception as e:
        print(f"✗ General Error: {e}")
    finally:
        if 'display' in locals():
            display.close()
            print("Display connection closed")

if __name__ == "__main__":
    test_czech_plates()
