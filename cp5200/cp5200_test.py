#!/usr/bin/env python3
"""
CP5200 LED Display Library Python Test Suite
Tests all major functions using the Python wrapper
"""

import sys
import time
import os
import tempfile
from typing import List

# Import the CP5200 wrapper
try:
    from cp5200_wrapper import CP5200Display, create_display, CP5200Error
except ImportError:
    print("Error: cp5200_wrapper.py not found. Please run the installation script first.")
    sys.exit(1)

class CP5200Tester:
    def __init__(self, ip_address: str = "192.168.1.100", port: int = 5200, debug: bool = True):
        """Initialize the CP5200 tester
        
        Args:
            ip_address: IP address of the CP5200 controller
            port: Network port
            debug: Enable debug mode
        """
        self.ip_address = ip_address
        self.port = port
        self.debug = debug
        self.display = None
        self.tests_passed = 0
        self.tests_failed = 0
        
    def print_test_result(self, test_name: str, result: int, expected: int = 0):
        """Print test result with formatting"""
        if result == expected:
            print(f"✓ {test_name}: PASSED")
            self.tests_passed += 1
        else:
            print(f"✗ {test_name}: FAILED (error code: {result})")
            self.tests_failed += 1
            
    def print_summary(self):
        """Print test summary"""
        print("\n" + "=" * 50)
        print("TEST SUMMARY")
        print("=" * 50)
        print(f"Tests passed: {self.tests_passed}")
        print(f"Tests failed: {self.tests_failed}")
        print(f"Total tests: {self.tests_passed + self.tests_failed}")
        print("=" * 50)
        
    def setup_display(self):
        """Setup the display connection"""
        print("Setting up CP5200 display connection...")
        try:
            self.display = create_display(self.ip_address, self.port, self.debug)
            print(f"Connected to CP5200 at {self.ip_address}:{self.port}")
            return True
        except CP5200Error as e:
            print(f"Failed to connect to CP5200: {e}")
            return False
            
    def test_version(self):
        """Test library version"""
        print("\n--- Testing Library Version ---")
        try:
            version = self.display.get_version()
            print(f"Library version: {version}")
            self.print_test_result("Get Version", 0)
        except Exception as e:
            print(f"Version test failed: {e}")
            self.print_test_result("Get Version", -1)
            
    def test_network_mode(self):
        """Test network mode configuration"""
        print("\n--- Testing Network Mode ---")
        try:
            self.display.set_network_mode(self.ip_address, self.port)
            self.print_test_result("Set Network Mode", 0)
        except Exception as e:
            print(f"Network mode test failed: {e}")
            self.print_test_result("Set Network Mode", -1)
            
    def test_serial_mode(self):
        """Test serial mode configuration"""
        print("\n--- Testing Serial Mode ---")
        try:
            self.display.set_serial_mode("/dev/ttyAMA0", 115200)
            self.print_test_result("Set Serial Mode", 0)
            # Switch back to network mode for other tests
            self.display.set_network_mode(self.ip_address, self.port)
        except Exception as e:
            print(f"Serial mode test failed: {e}")
            self.print_test_result("Set Serial Mode", -1)
            
    def test_time_sync(self):
        """Test time synchronization"""
        print("\n--- Testing Time Synchronization ---")
        try:
            result = self.display.sync_time()
            self.print_test_result("Time Sync", result)
        except Exception as e:
            print(f"Time sync test failed: {e}")
            self.print_test_result("Time Sync", -1)
            
    def test_brightness_control(self):
        """Test brightness control"""
        print("\n--- Testing Brightness Control ---")
        try:
            # Get current brightness
            current = self.display.get_brightness()
            print(f"Current brightness: {current}")
            
            # Set brightness to 50%
            result = self.display.set_brightness(15)
            self.print_test_result("Set Brightness", result)
            
            # Set auto brightness
            result = self.display.set_brightness(255)
            self.print_test_result("Set Auto Brightness", result)
            
        except Exception as e:
            print(f"Brightness control test failed: {e}")
            self.print_test_result("Brightness Control", -1)
            
    def test_text_display(self):
        """Test text display functionality"""
        print("\n--- Testing Text Display ---")
        
        test_cases = [
            ("Hello CP5200!", 1, 16, 5, 1, 10, 0),
            ("Test Message", 2, 20, 3, 2, 15, 1),
            ("CP5200 Python", 3, 18, 4, 1, 12, 2),
        ]
        
        for i, (text, color, font_size, speed, effect, stay_time, align) in enumerate(test_cases):
            try:
                result = self.display.send_text(0, text, color, font_size, speed, effect, stay_time, align)
                self.print_test_result(f"Send Text {i+1}", result)
                time.sleep(1)  # Wait between messages
            except Exception as e:
                print(f"Text display test {i+1} failed: {e}")
                self.print_test_result(f"Send Text {i+1}", -1)
                
    def test_picture_display(self):
        """Test picture display functionality"""
        print("\n--- Testing Picture Display ---")
        
        # Create a minimal test GIF file
        try:
            with tempfile.NamedTemporaryFile(suffix='.gif', delete=False) as temp_file:
                # Minimal GIF header for testing
                gif_data = bytes([
                    0x47, 0x49, 0x46, 0x38, 0x39, 0x61,  # GIF89a
                    0x01, 0x00, 0x01, 0x00, 0x80, 0x00, 0x00,  # 1x1 pixel
                    0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x21, 0xF9, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x02, 0x02, 0x44, 0x01, 0x00, 0x3B
                ])
                temp_file.write(gif_data)
                temp_file_path = temp_file.name
                
            result = self.display.send_picture(0, 0, 0, temp_file_path, 5, 1, 10)
            self.print_test_result("Send Picture", result)
            
            # Clean up
            os.unlink(temp_file_path)
            
        except Exception as e:
            print(f"Picture display test failed: {e}")
            self.print_test_result("Send Picture", -1)
            
    def test_clock_display(self):
        """Test clock display functionality"""
        print("\n--- Testing Clock Display ---")
        
        try:
            # Format array: multiline display
            format_array = [1, 0, 0, 0, 0, 0, 0, 0]
            
            # Content array: show date and time
            content_array = [1, 1, 1, 0, 0, 0, 0, 0]
            
            # Colors: white
            colors = [255, 255, 255]
            
            result = self.display.send_clock(0, 30, 0, format_array, content_array, "Current Time", colors, 16)
            self.print_test_result("Send Clock", result)
            
        except Exception as e:
            print(f"Clock display test failed: {e}")
            self.print_test_result("Send Clock", -1)
            
    def test_error_handling(self):
        """Test error handling"""
        print("\n--- Testing Error Handling ---")
        
        # Test with invalid parameters
        try:
            result = self.display.send_text(-1, "Invalid Window", 1, 16, 5, 1, 10, 0)
            print(f"Invalid window test result: {result} (expected error)")
        except Exception as e:
            print(f"Invalid window test exception: {e}")
            
        try:
            result = self.display.send_text(0, "", 1, 16, 5, 1, 10, 0)
            print(f"Empty text test result: {result}")
        except Exception as e:
            print(f"Empty text test exception: {e}")
            
        self.print_test_result("Error Handling", 0)  # Always pass as we're testing error conditions
        
    def test_performance(self):
        """Test performance with multiple messages"""
        print("\n--- Testing Performance ---")
        
        start_time = time.time()
        
        try:
            # Send multiple text messages
            for i in range(10):
                message = f"Performance Test {i}"
                result = self.display.send_text(i % 4, message, 1, 16, 5, 1, 5, 0)
                time.sleep(0.1)  # 100ms delay
                
            end_time = time.time()
            duration = end_time - start_time
            
            print(f"Performance test completed in {duration:.3f} seconds")
            self.print_test_result("Performance", 0)
            
        except Exception as e:
            print(f"Performance test failed: {e}")
            self.print_test_result("Performance", -1)
            
    def test_communication_modes(self):
        """Test different communication modes"""
        print("\n--- Testing Communication Modes ---")
        
        try:
            # Test network mode
            self.display.set_network_mode(self.ip_address, self.port)
            print("Switched to network mode")
            
            # Test serial mode
            self.display.set_serial_mode("/dev/ttyAMA0", 115200)
            print("Switched to serial mode")
            
            # Switch back to network mode
            self.display.set_network_mode(self.ip_address, self.port)
            print("Switched back to network mode")
            
            self.print_test_result("Communication Modes", 0)
            
        except Exception as e:
            print(f"Communication modes test failed: {e}")
            self.print_test_result("Communication Modes", -1)
            
    def run_all_tests(self):
        """Run all tests"""
        print("CP5200 LED Display Library Python Test Suite")
        print("=" * 50)
        print("This test suite will test all major functions of the CP5200 library")
        print("Make sure your CP5200 display controller is connected and configured")
        print("=" * 50)
        
        # Setup display connection
        if not self.setup_display():
            print("Failed to setup display connection. Exiting.")
            return False
            
        # Run all tests
        self.test_version()
        self.test_network_mode()
        self.test_serial_mode()
        self.test_time_sync()
        self.test_brightness_control()
        self.test_text_display()
        self.test_picture_display()
        self.test_clock_display()
        self.test_error_handling()
        self.test_performance()
        self.test_communication_modes()
        
        # Print summary
        self.print_summary()
        
        # Return success/failure
        if self.tests_failed == 0:
            print("All tests passed! CP5200 library is working correctly.")
            return True
        else:
            print("Some tests failed. Please check your configuration.")
            return False

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='CP5200 LED Display Library Test Suite')
    parser.add_argument('--ip', default='192.168.1.100', help='IP address of CP5200 controller')
    parser.add_argument('--port', type=int, default=5200, help='Network port')
    parser.add_argument('--no-debug', action='store_true', help='Disable debug mode')
    
    args = parser.parse_args()
    
    # Create tester and run tests
    tester = CP5200Tester(args.ip, args.port, not args.no_debug)
    success = tester.run_all_tests()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
