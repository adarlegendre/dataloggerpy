#!/usr/bin/env python3
"""
CP5200 Comprehensive SDK Test
Demonstrates all available functions with proper error handling

Usage: python3 comprehensive_sdk_test.py [--target-ip IP] [--target-port PORT]
"""

import ctypes
import time
import sys
import argparse
import socket
import subprocess
from pathlib import Path

class CP5200ComprehensiveTest:
    """Comprehensive test class for all CP5200 SDK functions"""
    
    def __init__(self, target_ip='192.168.1.222', target_port=5200):
        self.target_ip = target_ip
        self.target_port = target_port
        self.lib = None
        
        print("🚀 CP5200 Comprehensive SDK Test")
        print("=" * 60)
        print(f"Target: {target_ip}:{target_port}")
        print("=" * 60)
        
        # Load library and setup
        self._load_library()
        self._setup_function_signatures()
        self._configure_basic_settings()
    
    def _load_library(self):
        """Load the CP5200 library"""
        print("📚 Loading CP5200 library...")
        
        # Try multiple library paths
        library_paths = [
            './libcp5200.so',
            './libcp5200.a',
            '../libcp5200.so',
            '../libcp5200.a',
            '/usr/local/lib/libcp5200.so',
            '/usr/local/lib/libcp5200.a'
        ]
        
        for path in library_paths:
            if Path(path).exists():
                try:
                    self.lib = ctypes.CDLL(path)
                    print(f"✅ Library loaded from: {path}")
                    return
                except Exception as e:
                    print(f"⚠ Failed to load from {path}: {e}")
                    continue
        
        print("❌ No CP5200 library found!")
        print("Please ensure the library is compiled and accessible")
        sys.exit(1)
    
    def _setup_function_signatures(self):
        """Setup all function signatures for proper Python integration"""
        print("🔧 Setting up function signatures...")
        
        try:
            # Configuration functions
            self.lib._set_cp5200_debug.argtypes = []
            self.lib._set_cp5200_debug.restype = None
            
            self.lib._set_cp5200_send_mode.argtypes = [ctypes.c_int]
            self.lib._set_cp5200_send_mode.restype = None
            
            self.lib._set_cp5200_ipcomm.argtypes = [ctypes.c_char_p, ctypes.c_int]
            self.lib._set_cp5200_ipcomm.restype = None
            
            # Display functions
            self.lib.SendText.argtypes = [
                ctypes.c_int,      # window number
                ctypes.c_char_p,   # text
                ctypes.c_int,      # color
                ctypes.c_int,      # font size
                ctypes.c_int,      # speed
                ctypes.c_int,      # effect
                ctypes.c_int,      # stay time
                ctypes.c_int       # alignment
            ]
            self.lib.SendText.restype = ctypes.c_int
            
            self.lib.SplitWindow.argtypes = [
                ctypes.c_int,      # window count
                ctypes.POINTER(ctypes.c_int),  # config array
                ctypes.c_int       # array size
            ]
            self.lib.SplitWindow.restype = ctypes.c_int
            
            self.lib.SendPicture.argtypes = [
                ctypes.c_int,      # window
                ctypes.c_int,      # x position
                ctypes.c_int,      # y position
                ctypes.c_char_p,   # filename
                ctypes.c_int,      # speed
                ctypes.c_int,      # effect
                ctypes.c_int       # stay time
            ]
            self.lib.SendPicture.restype = ctypes.c_int
            
            # Utility functions
            self.lib.SyncTime.argtypes = []
            self.lib.SyncTime.restype = ctypes.c_int
            
            self.lib.BrightnessControl.argtypes = [ctypes.c_int, ctypes.c_int]
            self.lib.BrightnessControl.restype = ctypes.c_int
            
            print("✅ Function signatures configured successfully")
            
        except Exception as e:
            print(f"⚠ Function signature setup failed: {e}")
            print("Some functions may not work properly")
    
    def _configure_basic_settings(self):
        """Configure basic communication settings"""
        print("⚙️ Configuring basic settings...")
        
        try:
            # Enable debug mode
            self.lib._set_cp5200_debug()
            print("✅ Debug mode enabled")
            
            # Set TCP/IP mode
            self.lib._set_cp5200_send_mode(0)
            print("✅ Set to TCP/IP mode")
            
            # Set IP address and port
            self.lib._set_cp5200_ipcomm(self.target_ip.encode('utf-8'), self.target_port)
            print(f"✅ Set IP address: {self.target_ip}:{self.target_port}")
            
        except Exception as e:
            print(f"❌ Basic configuration failed: {e}")
            sys.exit(1)
    
    def check_network_connectivity(self):
        """Check network connectivity to target"""
        print("\n🌐 Checking network connectivity...")
        print("-" * 40)
        
        # Ping test
        try:
            if sys.platform.startswith('win'):
                result = subprocess.run(['ping', '-n', '1', self.target_ip], 
                                      capture_output=True, text=True, timeout=5)
            else:
                result = subprocess.run(['ping', '-c', '1', self.target_ip], 
                                      capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0:
                print("✅ Ping successful")
            else:
                print("⚠ Ping failed (this may not affect functionality)")
        except Exception as e:
            print(f"⚠ Ping test not available: {e}")
        
        # Port connectivity test
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((self.target_ip, self.target_port))
            sock.close()
            
            if result == 0:
                print("✅ Port connectivity confirmed")
                return True
            else:
                print(f"⚠ Port {self.target_port} may not be accessible")
                return False
        except Exception as e:
            print(f"❌ Port test failed: {e}")
            return False
    
    def test_time_synchronization(self):
        """Test time synchronization function"""
        print("\n⏰ Testing time synchronization...")
        print("-" * 40)
        
        try:
            result = self.lib.SyncTime()
            if result == 0:
                print("✅ Time synchronization successful")
            else:
                print(f"⚠ Time synchronization returned: {result}")
            return result == 0
        except Exception as e:
            print(f"❌ Time synchronization failed: {e}")
            return False
    
    def test_brightness_control(self):
        """Test brightness control functions"""
        print("\n💡 Testing brightness control...")
        print("-" * 40)
        
        try:
            # Test setting brightness
            test_levels = [15, 20, 25, 255]  # 255 = auto
            
            for level in test_levels:
                if level == 255:
                    print(f"Setting brightness to AUTO...")
                else:
                    print(f"Setting brightness to {level}...")
                
                result = self.lib.BrightnessControl(0, level)  # 0 = set
                if result == 0:
                    print(f"✅ Brightness set to {level}")
                else:
                    print(f"⚠ Brightness setting failed: {result}")
                
                time.sleep(1)
            
            # Test getting brightness
            print("Getting current brightness...")
            result = self.lib.BrightnessControl(1, 0)  # 1 = get
            if result >= 0:
                print(f"✅ Current brightness: {result}")
            else:
                print(f"⚠ Failed to get brightness: {result}")
            
            return True
            
        except Exception as e:
            print(f"❌ Brightness control test failed: {e}")
            return False
    
    def test_window_configuration(self):
        """Test different window configurations"""
        print("\n🪟 Testing window configurations...")
        print("-" * 40)
        
        configurations = [
            {
                'name': 'Single Window (Full Display)',
                'count': 1,
                'config': [0, 0, 128, 64],
                'description': 'Full 128x64 display'
            },
            {
                'name': 'Two Windows (Horizontal Split)',
                'count': 2,
                'config': [0, 0, 64, 64, 64, 0, 128, 64],
                'description': 'Left and right halves'
            },
            {
                'name': 'Four Windows (2x2 Grid)',
                'count': 4,
                'config': [0, 0, 64, 32, 64, 0, 128, 32, 0, 32, 64, 64, 64, 32, 128, 64],
                'description': 'Four quadrants'
            }
        ]
        
        for config in configurations:
            print(f"\nTesting: {config['name']}")
            print(f"Description: {config['description']}")
            
            try:
                # Convert Python list to C array
                c_config = (ctypes.c_int * len(config['config']))(*config['config'])
                result = self.lib.SplitWindow(config['count'], c_config, len(config['config']))
                
                if result == 0:
                    print(f"✅ {config['name']} configured successfully")
                    
                    # Send test text to each window
                    for i in range(config['count']):
                        test_text = f"WIN{i}"
                        color = 0xFF0000 if i == 0 else 0x00FF00 if i == 1 else 0x0000FF
                        self.lib.SendText(i, test_text.encode('utf-8'), color, 12, 1, 0, 3, 2)
                        time.sleep(0.5)
                    
                    time.sleep(2)
                else:
                    print(f"⚠ {config['name']} configuration failed: {result}")
                
            except Exception as e:
                print(f"❌ {config['name']} test failed: {e}")
    
    def test_text_display(self):
        """Test text display with various parameters"""
        print("\n📝 Testing text display...")
        print("-" * 40)
        
        # Test different text parameters
        text_tests = [
            {
                'text': 'HELLO WORLD',
                'color': 0xFF0000,  # Red
                'font_size': 16,
                'speed': 1,
                'effect': 0,        # No effect
                'stay_time': 5,
                'align': 2          # Center
            },
            {
                'text': 'SCROLLING TEXT',
                'color': 0x00FF00,  # Green
                'font_size': 14,
                'speed': 2,
                'effect': 1,        # Scroll
                'stay_time': 8,
                'align': 1          # Left
            },
            {
                'text': 'BLINKING',
                'color': 0x0000FF,  # Blue
                'font_size': 18,
                'speed': 1,
                'effect': 2,        # Blink
                'stay_time': 6,
                'align': 3          # Right
            }
        ]
        
        # First, set up a single window
        config = [0, 0, 128, 64]
        c_config = (ctypes.c_int * len(config))(*config)
        self.lib.SplitWindow(1, c_config, len(config))
        time.sleep(1)
        
        for i, test in enumerate(text_tests, 1):
            print(f"\nTest {i}: {test['text']}")
            print(f"Color: 0x{test['color']:06X}, Font: {test['font_size']}, Effect: {test['effect']}")
            
            try:
                result = self.lib.SendText(
                    0,  # window 0
                    test['text'].encode('utf-8'),
                    test['color'],
                    test['font_size'],
                    test['speed'],
                    test['effect'],
                    test['stay_time'],
                    test['align']
                )
                
                if result == 0:
                    print(f"✅ Text sent successfully")
                else:
                    print(f"⚠ Text sending failed: {result}")
                
                # Wait for effect to complete
                time.sleep(test['stay_time'] + 1)
                
            except Exception as e:
                print(f"❌ Text test failed: {e}")
    
    def test_picture_display(self):
        """Test picture display functionality"""
        print("\n🖼️ Testing picture display...")
        print("-" * 40)
        
        # Check if test GIF files exist
        test_files = ['test.gif', 'logo.gif', 'sample.gif']
        found_files = []
        
        for filename in test_files:
            if Path(filename).exists():
                found_files.append(filename)
        
        if not found_files:
            print("⚠ No test GIF files found")
            print("Create test.gif, logo.gif, or sample.gif to test picture display")
            return False
        
        # Set up single window for picture display
        config = [0, 0, 128, 64]
        c_config = (ctypes.c_int * len(config))(*config)
        self.lib.SplitWindow(1, c_config, len(config))
        time.sleep(1)
        
        for filename in found_files:
            print(f"\nTesting picture: {filename}")
            
            try:
                result = self.lib.SendPicture(0, 10, 10, filename.encode('utf-8'), 1, 0, 10)
                
                if result == 0:
                    print(f"✅ Picture {filename} displayed successfully")
                    time.sleep(12)  # Wait for display + stay time
                else:
                    print(f"⚠ Picture display failed: {result}")
                
            except Exception as e:
                print(f"❌ Picture test failed: {e}")
        
        return True
    
    def test_advanced_features(self):
        """Test advanced features and combinations"""
        print("\n🚀 Testing advanced features...")
        print("-" * 40)
        
        # Test multiple windows with different content
        print("Testing multi-window content...")
        
        # Configure 2 windows
        config = [0, 0, 64, 64, 64, 0, 128, 64]
        c_config = (ctypes.c_int * len(config))(*config)
        self.lib.SplitWindow(2, c_config, len(config))
        time.sleep(1)
        
        # Send different content to each window
        try:
            # Window 0: Red text
            self.lib.SendText(0, b'LEFT SIDE', 0xFF0000, 14, 1, 0, 8, 2)
            
            # Window 1: Green text with effect
            self.lib.SendText(1, b'RIGHT SIDE', 0x00FF00, 14, 2, 1, 8, 2)
            
            print("✅ Multi-window content test completed")
            time.sleep(10)
            
        except Exception as e:
            print(f"❌ Multi-window test failed: {e}")
        
        # Test rapid text changes
        print("Testing rapid text changes...")
        try:
            rapid_texts = ['FAST', 'CHANGE', 'TEST', 'COMPLETE']
            colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00]
            
            for text, color in zip(rapid_texts, colors):
                self.lib.SendText(0, text.encode('utf-8'), color, 16, 1, 0, 2, 2)
                time.sleep(3)
            
            print("✅ Rapid text change test completed")
            
        except Exception as e:
            print(f"❌ Rapid text test failed: {e}")
    
    def run_comprehensive_test(self):
        """Run all tests in sequence"""
        print("\n🎯 Starting comprehensive CP5200 SDK test...")
        print("=" * 60)
        
        # Check connectivity first
        if not self.check_network_connectivity():
            print("⚠ Network connectivity issues detected")
            print("Tests will continue but may fail")
        
        # Run all test functions
        tests = [
            ("Time Synchronization", self.test_time_synchronization),
            ("Brightness Control", self.test_brightness_control),
            ("Window Configuration", self.test_window_configuration),
            ("Text Display", self.test_text_display),
            ("Picture Display", self.test_picture_display),
            ("Advanced Features", self.test_advanced_features)
        ]
        
        results = {}
        
        for test_name, test_func in tests:
            print(f"\n{'='*20} {test_name} {'='*20}")
            try:
                start_time = time.time()
                success = test_func()
                end_time = time.time()
                
                if success:
                    print(f"✅ {test_name} completed successfully")
                    results[test_name] = 'PASS'
                else:
                    print(f"⚠ {test_name} completed with issues")
                    results[test_name] = 'PARTIAL'
                
                print(f"Duration: {end_time - start_time:.1f} seconds")
                
            except Exception as e:
                print(f"❌ {test_name} failed: {e}")
                results[test_name] = 'FAIL'
        
        # Show final summary
        self._show_test_summary(results)
    
    def _show_test_summary(self, results):
        """Show comprehensive test results"""
        print("\n" + "=" * 60)
        print("🎯 COMPREHENSIVE TEST RESULTS")
        print("=" * 60)
        
        for test_name, result in results.items():
            status_icon = {
                'PASS': '✅',
                'PARTIAL': '⚠',
                'FAIL': '❌'
            }.get(result, '❓')
            print(f"{status_icon} {test_name}: {result}")
        
        # Calculate success rate
        passed = sum(1 for r in results.values() if r == 'PASS')
        total = len(results)
        
        if total > 0:
            success_rate = (passed / total) * 100
            print(f"\n📈 Success Rate: {passed}/{total} ({success_rate:.1f}%)")
            
            if success_rate >= 80:
                print("🎉 Excellent! Most tests passed successfully!")
            elif success_rate >= 60:
                print("👍 Good! Most tests passed with some issues.")
            elif success_rate >= 40:
                print("⚠ Fair. Some tests passed but there are issues to address.")
            else:
                print("❌ Poor. Many tests failed. Check your setup and configuration.")
        
        print(f"\n🎯 Test completed against {self.target_ip}:{self.target_port}")
        print("Check your CP5200 display for test content!")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='CP5200 Comprehensive SDK Test')
    parser.add_argument('--target-ip', default='192.168.1.222', 
                       help='Target IP address (default: 192.168.1.222)')
    parser.add_argument('--target-port', type=int, default=5200,
                       help='Target port (default: 5200)')
    
    args = parser.parse_args()
    
    try:
        # Create and run comprehensive test
        tester = CP5200ComprehensiveTest(args.target_ip, args.target_port)
        tester.run_comprehensive_test()
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Test interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure CP5200 display is powered on and connected")
        print("2. Verify network connectivity to target IP")
        print("3. Check if port is open and accessible")
        print("4. Ensure library file exists and is accessible")
        sys.exit(1)

if __name__ == "__main__":
    main()
