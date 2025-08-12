#!/usr/bin/env python3
"""
CP5200 LED Display Library - Example Usage
This file demonstrates various ways to use the CP5200 library
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

def example_basic_setup():
    """Example 1: Basic setup and connection"""
    print("=== Example 1: Basic Setup ===")
    
    try:
        # Create display instance with default settings
        display = create_display("192.168.1.100", 5200, debug=True)
        print("✓ Display connected successfully")
        
        # Get library version
        version = display.get_version()
        print(f"Library version: {version}")
        
        return display
    except CP5200Error as e:
        print(f"✗ Connection failed: {e}")
        return None

def example_text_display(display):
    """Example 2: Text display with various effects"""
    print("\n=== Example 2: Text Display ===")
    
    if not display:
        print("No display connection available")
        return
    
    # Basic text display
    print("Displaying basic text...")
    display.send_text(0, "Hello CP5200!", 1, 16, 5, 1, 10, 0)
    time.sleep(2)
    
    # Text with different colors
    colors = [1, 2, 3, 4, 5]
    for i, color in enumerate(colors):
        print(f"Displaying text with color {color}...")
        display.send_text(0, f"Color Test {i+1}", color, 18, 3, 2, 5, 1)
        time.sleep(1)
    
    # Text with different effects
    effects = [1, 2, 3, 4, 5]
    for i, effect in enumerate(effects):
        print(f"Displaying text with effect {effect}...")
        display.send_text(0, f"Effect Test {i+1}", 1, 16, 4, effect, 5, 0)
        time.sleep(1)
    
    # Scrolling text
    print("Displaying scrolling text...")
    display.send_text(0, "This is a scrolling text message that demonstrates the scrolling effect", 2, 14, 2, 1, 15, 0)
    time.sleep(3)

def example_clock_display(display):
    """Example 3: Clock and date display"""
    print("\n=== Example 3: Clock Display ===")
    
    if not display:
        print("No display connection available")
        return
    
    # Gregorian calendar with date and time
    print("Displaying current date and time...")
    format_array = [1, 0, 0, 0, 0, 0, 0, 0]  # Multiline
    content_array = [1, 1, 1, 0, 0, 0, 0, 0]  # Show date, time
    colors = [255, 255, 255]  # White
    
    display.send_clock(0, 30, 0, format_array, content_array, "Current Time", colors, 16)
    time.sleep(5)
    
    # Moon calendar
    print("Displaying moon calendar...")
    display.send_clock(0, 20, 1, format_array, content_array, "Moon Phase", colors, 14)
    time.sleep(5)

def example_brightness_control(display):
    """Example 4: Brightness control"""
    print("\n=== Example 4: Brightness Control ===")
    
    if not display:
        print("No display connection available")
        return
    
    # Get current brightness
    current = display.get_brightness()
    print(f"Current brightness: {current}")
    
    # Brightness demonstration
    brightness_levels = [5, 10, 15, 20, 25, 30]
    for level in brightness_levels:
        print(f"Setting brightness to {level}...")
        display.set_brightness(level)
        display.send_text(0, f"Brightness: {level}", 1, 16, 5, 1, 3, 0)
        time.sleep(2)
    
    # Auto brightness
    print("Setting auto brightness...")
    display.set_brightness(255)
    display.send_text(0, "Auto Brightness", 2, 16, 5, 1, 5, 0)
    time.sleep(3)

def example_multi_window(display):
    """Example 5: Multi-window display"""
    print("\n=== Example 5: Multi-Window Display ===")
    
    if not display:
        print("No display connection available")
        return
    
    # Display different content in different windows
    print("Displaying content in multiple windows...")
    
    # Window 0: Time
    display.send_text(0, "TIME", 1, 16, 5, 1, 10, 0)
    
    # Window 1: Temperature
    display.send_text(1, "TEMP: 22°C", 2, 14, 5, 1, 10, 0)
    
    # Window 2: Status
    display.send_text(2, "STATUS: OK", 3, 14, 5, 1, 10, 0)
    
    # Window 3: Alert
    display.send_text(3, "ALERT!", 4, 18, 3, 2, 10, 0)
    
    time.sleep(5)

def example_picture_display(display):
    """Example 6: Picture display"""
    print("\n=== Example 6: Picture Display ===")
    
    if not display:
        print("No display connection available")
        return
    
    # Note: This requires a valid GIF file
    # For demonstration, we'll show how to use the function
    print("Picture display example (requires GIF file)...")
    
    # Example usage (commented out as it requires a real file)
    # display.send_picture(0, 0, 0, "logo.gif", 5, 1, 10)
    
    print("To display a picture, use:")
    print("display.send_picture(window, x, y, 'path/to/image.gif', speed, effect, stay_time)")

def example_communication_modes(display):
    """Example 7: Different communication modes"""
    print("\n=== Example 7: Communication Modes ===")
    
    if not display:
        print("No display connection available")
        return
    
    # Network mode (TCP/IP)
    print("Switching to network mode...")
    display.set_network_mode("192.168.1.100", 5200)
    display.send_text(0, "Network Mode", 1, 16, 5, 1, 3, 0)
    time.sleep(2)
    
    # Serial mode (RS-232)
    print("Switching to serial mode...")
    display.set_serial_mode("/dev/ttyAMA0", 115200)
    display.send_text(0, "Serial Mode", 2, 16, 5, 1, 3, 0)
    time.sleep(2)
    
    # Switch back to network mode
    display.set_network_mode("192.168.1.100", 5200)
    print("Switched back to network mode")

def example_error_handling(display):
    """Example 8: Error handling"""
    print("\n=== Example 8: Error Handling ===")
    
    if not display:
        print("No display connection available")
        return
    
    try:
        # Test with invalid parameters
        print("Testing error handling...")
        
        # Invalid window number
        result = display.send_text(-1, "Invalid Window", 1, 16, 5, 1, 10, 0)
        print(f"Invalid window result: {result}")
        
        # Empty text
        result = display.send_text(0, "", 1, 16, 5, 1, 10, 0)
        print(f"Empty text result: {result}")
        
    except Exception as e:
        print(f"Error occurred: {e}")

def example_real_world_scenario(display):
    """Example 9: Real-world scenario - Information display"""
    print("\n=== Example 9: Real-World Scenario ===")
    
    if not display:
        print("No display connection available")
        return
    
    print("Running real-world scenario: Information Display System")
    
    # Simulate a real-world information display system
    messages = [
        "Welcome to CP5200",
        "System Online",
        "Temperature: 22°C",
        "Humidity: 45%",
        "Status: Normal",
        "Last Update: " + datetime.now().strftime("%H:%M:%S")
    ]
    
    for i, message in enumerate(messages):
        print(f"Displaying: {message}")
        display.send_text(0, message, 1, 16, 4, 1, 4, 0)
        time.sleep(2)
    
    # Show clock for a while
    print("Displaying clock...")
    format_array = [1, 0, 0, 0, 0, 0, 0, 0]
    content_array = [1, 1, 1, 0, 0, 0, 0, 0]
    colors = [255, 255, 255]
    display.send_clock(0, 15, 0, format_array, content_array, "Current Time", colors, 16)
    time.sleep(5)

def main():
    """Main function to run all examples"""
    print("CP5200 LED Display Library - Example Usage")
    print("=" * 50)
    print("This script demonstrates various features of the CP5200 library")
    print("Make sure your CP5200 display controller is connected and configured")
    print("=" * 50)
    
    # Get user input for IP address
    ip_address = input("Enter CP5200 IP address (default: 192.168.1.100): ").strip()
    if not ip_address:
        ip_address = "192.168.1.100"
    
    port = input("Enter port (default: 5200): ").strip()
    if not port:
        port = 5200
    else:
        port = int(port)
    
    # Setup display
    try:
        display = create_display(ip_address, port, debug=True)
        print(f"✓ Connected to CP5200 at {ip_address}:{port}")
    except CP5200Error as e:
        print(f"✗ Failed to connect: {e}")
        print("Please check your network connection and CP5200 configuration")
        return
    
    # Run examples
    try:
        example_text_display(display)
        example_clock_display(display)
        example_brightness_control(display)
        example_multi_window(display)
        example_picture_display(display)
        example_communication_modes(display)
        example_error_handling(display)
        example_real_world_scenario(display)
        
        print("\n" + "=" * 50)
        print("All examples completed successfully!")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print("\nExamples interrupted by user")
    except Exception as e:
        print(f"\nError during examples: {e}")

if __name__ == "__main__":
    main()
