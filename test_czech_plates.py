#!/usr/bin/env python3
"""
CP5200 Czech Number Plates Test for Raspberry Pi
Simple test functionality for sending Czech number plates to CP5200 display
without modifying the original SDK files.

Target: 192.168.1.222:5200
Optimized for Raspberry Pi with existing Linux library
"""

import ctypes
import ctypes.util
import os
import sys
import platform
from typing import Optional

class CP5200Test:
    """Simple CP5200 test class for Czech number plates on Raspberry Pi"""
    
    def __init__(self, library_path: Optional[str] = None):
        """
        Initialize CP5200 test interface for Raspberry Pi
        
        Args:
            library_path: Path to the libcp5200 library file
        """
        self.lib = None
        self.is_raspberry_pi = self._detect_raspberry_pi()
        self._load_library(library_path)
        self._setup_functions()
        
        # Initialize with default settings
        self.set_tcp_mode()
        self.set_ip_address("192.168.1.222", 5200)
        self.enable_debug()
        
        # Raspberry Pi specific optimizations
        if self.is_raspberry_pi:
            self._setup_raspberry_pi()
    
    def _detect_raspberry_pi(self) -> bool:
        """Detect if running on Raspberry Pi"""
        try:
            with open('/proc/cpuinfo', 'r') as f:
                if 'Raspberry Pi' in f.read():
                    return True
        except:
            pass
        
        # Alternative detection methods
        if platform.system() == 'Linux':
            if os.path.exists('/etc/rpi-issue'):
                return True
            if os.path.exists('/proc/device-tree/model'):
                try:
                    with open('/proc/device-tree/model', 'r') as f:
                        if 'Raspberry Pi' in f.read():
                            return True
                except:
                    pass
        
        return False
    
    def _setup_raspberry_pi(self):
        """Setup Raspberry Pi specific optimizations"""
        print("🍓 Raspberry Pi detected - applying optimizations")
        
        # Set optimal library search paths for Raspberry Pi
        self.raspberry_pi_paths = [
            "./libcp5200.so",
            "./libcp5200.a",
            "../cp5200Original/dist/Release/GNU-Linux/libcp5200.a",
            "../cp5200Original/dist/Debug/GNU-Linux/libcp5200.a",
            "/usr/local/lib/libcp5200.so",
            "/usr/local/lib/libcp5200.a",
            "/usr/lib/libcp5200.so",
            "/usr/lib/libcp5200.a"
        ]
        
        # Check if we're in the right directory structure
        current_dir = os.getcwd()
        if 'cp5200Original' in current_dir:
            # We're in the SDK directory, adjust paths
            self.raspberry_pi_paths.insert(0, "./dist/Release/GNU-Linux/libcp5200.a")
            self.raspberry_pi_paths.insert(0, "./dist/Debug/GNU-Linux/libcp5200.a")
    
    def _load_library(self, library_path: Optional[str] = None):
        """Load the CP5200 library with Raspberry Pi optimizations"""
        try:
            if library_path and os.path.exists(library_path):
                self.lib = ctypes.CDLL(library_path)
                print(f"✓ Loaded library from: {library_path}")
                return
            
            # Try to find library in system paths
            lib_path = ctypes.util.find_library("cp5200")
            if lib_path:
                self.lib = ctypes.CDLL(lib_path)
                print(f"✓ Loaded library from system: {lib_path}")
                return
            
            # Try Raspberry Pi specific paths first
            if self.is_raspberry_pi and hasattr(self, 'raspberry_pi_paths'):
                for path in self.raspberry_pi_paths:
                    if os.path.exists(path):
                        try:
                            self.lib = ctypes.CDLL(path)
                            print(f"✓ Loaded library from Raspberry Pi path: {path}")
                            return
                        except Exception as e:
                            print(f"⚠ Failed to load from {path}: {e}")
                            continue
            
            # Try common library names
            common_paths = [
                "./libcp5200.so",
                "./libcp5200.dll", 
                "./cp5200.dll",
                "../cp5200/dist/Release/GNU-Linux/libcp5200.so",
                "../cp5200/dist/Debug/GNU-Linux/libcp5200.so",
                "../cp5200Original/dist/Release/GNU-Linux/libcp5200.a",
                "../cp5200Original/dist/Debug/GNU-Linux/libcp5200.a"
            ]
            
            for path in common_paths:
                if os.path.exists(path):
                    try:
                        self.lib = ctypes.CDLL(path)
                        print(f"✓ Loaded library from: {path}")
                        return
                    except Exception as e:
                        print(f"⚠ Failed to load from {path}: {e}")
                        continue
            
            # If we get here, no library was found
            raise RuntimeError("Could not find CP5200 library. Please specify the path.")
                        
        except Exception as e:
            print(f"❌ Error loading library: {e}")
            print("\nTroubleshooting for Raspberry Pi:")
            print("1. Make sure the CP5200 library is compiled for ARM architecture")
            print("2. Check if you're in the right directory (cp5200Original)")
            print("3. Try specifying the full path to the library file")
            print("4. Ensure the library file has proper permissions")
            print("\nCommon Raspberry Pi library locations:")
            if self.is_raspberry_pi and hasattr(self, 'raspberry_pi_paths'):
                for path in self.raspberry_pi_paths[:5]:  # Show first 5 paths
                    print(f"   - {path}")
            sys.exit(1)
    
    def _setup_functions(self):
        """Setup function signatures for proper Python integration"""
        if not self.lib:
            return
            
        # Core configuration functions
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
        
        # Additional functions for Raspberry Pi
        self.lib.SyncTime.argtypes = []
        self.lib.SyncTime.restype = ctypes.c_int
        
        self.lib.BrightnessControl.argtypes = [ctypes.c_int, ctypes.c_int]
        self.lib.BrightnessControl.restype = ctypes.c_int
        
        print("✓ Function signatures configured")
    
    def enable_debug(self):
        """Enable debug output"""
        if self.lib:
            self.lib._set_cp5200_debug()
            print("✓ Debug mode enabled")
    
    def set_tcp_mode(self):
        """Set communication mode to TCP/IP"""
        if self.lib:
            self.lib._set_cp5200_send_mode(0)
            print("✓ Set to TCP/IP mode")
    
    def set_ip_address(self, ip: str, port: int):
        """Set IP address and port"""
        if self.lib:
            self.lib._set_cp5200_ipcomm(ip.encode('utf-8'), port)
            print(f"✓ Set IP address: {ip}:{port}")
    
    def split_windows(self, window_count: int, config: list):
        """Split display into windows"""
        if self.lib:
            # Convert Python list to C array
            c_config = (ctypes.c_int * len(config))(*config)
            result = self.lib.SplitWindow(window_count, c_config, len(config))
            
            if result == 0:
                print(f"✓ Split display into {window_count} windows")
            else:
                print(f"⚠ Window split failed with error: {result}")
            
            return result
        return -1
    
    def send_text(self, window: int, text: str, color: int, font_size: int = 16, 
                  speed: int = 1, effect: int = 0, stay_time: int = 5, align: int = 1):
        """
        Send text to specified window
        
        Args:
            window: Window number (0-based)
            text: Text to display
            color: Color in RGB format (0xFF0000 = red, 0x00FF00 = green)
            font_size: Font size (10-16)
            speed: Effect speed (1-10)
            effect: Visual effect (0=static, 1=scroll)
            stay_time: Display duration in seconds
            align: Alignment (0=left, 1=center, 2=right)
        """
        if self.lib:
            # Convert text to bytes
            text_bytes = text.encode('utf-8')
            
            result = self.lib.SendText(window, text_bytes, color, font_size, 
                                     speed, effect, stay_time, align)
            
            if result == 0:
                print(f"✓ Text sent to window {window}: '{text}'")
            else:
                print(f"❌ Failed to send text to window {window}, error: {result}")
            
            return result
        return -1
    
    def sync_time(self):
        """Synchronize time with the CP5200 display"""
        if self.lib:
            result = self.lib.SyncTime()
            if result == 0:
                print("✓ Time synchronized with display")
            else:
                print(f"⚠ Time sync failed with error: {result}")
            return result
        return -1
    
    def set_brightness(self, brightness: int):
        """Set display brightness (0-31, or 255 for auto)"""
        if self.lib:
            result = self.lib.BrightnessControl(0, brightness)  # 0 = set brightness
            if result == 0:
                print(f"✓ Brightness set to {brightness}")
            else:
                print(f"⚠ Brightness setting failed with error: {result}")
            return result
        return -1
    
    def test_czech_plates(self):
        """Test sending Czech number plates to the display"""
        print("\n🚗 Testing Czech Number Plates Display on Raspberry Pi")
        print("=" * 60)
        
        # Test 1: Sync time (important for Raspberry Pi)
        print("\n1. Synchronizing time with display...")
        self.sync_time()
        
        # Test 2: Set optimal brightness for Raspberry Pi
        print("\n2. Setting optimal brightness...")
        self.set_brightness(20)  # Good visibility level
        
        # Test 3: Split display into 2 windows
        print("\n3. Setting up display windows...")
        window_config = [0, 0, 64, 64, 64, 0, 128, 64]  # 2 windows
        self.split_windows(2, window_config)
        
        # Test 4: Send red Czech plate to window 0
        print("\n4. Sending red Czech plate to window 0...")
        czech_plate_1 = "3A8 1234"  # Example Czech plate format
        self.send_text(0, czech_plate_1, 0xFF0000, 16, 1, 0, 8, 1)
        
        # Test 5: Send green Czech plate to window 1
        print("\n5. Sending green Czech plate to window 1...")
        czech_plate_2 = "1AB 5678"  # Another example
        self.send_text(1, czech_plate_2, 0x00FF00, 14, 2, 1, 6, 1)
        
        # Test 6: Send additional Czech plates
        print("\n6. Sending additional Czech plates...")
        
        # More Czech plate examples
        plates = [
            ("P 999 99", 0xFF0000, 0),  # Red plate in window 0
            ("A 123 45", 0x00FF00, 1),  # Green plate in window 1
            ("E 777 77", 0x0000FF, 0),  # Blue plate in window 0
            ("T 555 55", 0xFFFF00, 1),  # Yellow plate in window 1
        ]
        
        for i, (plate, color, window) in enumerate(plates, 1):
            print(f"   {i}. Sending '{plate}' to window {window}...")
            self.send_text(window, plate, color, 16, 1, 0, 4, 1)
        
        print("\n✅ Czech number plates test completed on Raspberry Pi!")
        print("Check your CP5200 display at 192.168.1.222:5200")
        
        # Raspberry Pi specific success message
        if self.is_raspberry_pi:
            print("🍓 Raspberry Pi test completed successfully!")

def main():
    """Main test function for Raspberry Pi"""
    print("🚀 CP5200 Czech Number Plates Test for Raspberry Pi")
    print("=" * 60)
    
    # Show system information
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python: {platform.python_version()}")
    
    # Try to find the library automatically
    library_path = None
    
    # Check if user provided library path as argument
    if len(sys.argv) > 1:
        library_path = sys.argv[1]
        print(f"Using library path: {library_path}")
    
    try:
        # Initialize CP5200 test interface
        cp = CP5200Test(library_path)
        
        # Run the Czech plates test
        cp.test_czech_plates()
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        print("\nTroubleshooting for Raspberry Pi:")
        print("1. Make sure the CP5200 display is powered on")
        print("2. Verify network connectivity to 192.168.1.222")
        print("3. Check if port 5200 is open")
        print("4. Ensure the library file exists and is accessible")
        print("5. Check if you're in the cp5200Original directory")
        print("\nQuick fixes:")
        print("- Run: cd cp5200Original")
        print("- Run: python3 ../test_czech_plates.py")
        print("- Or specify path: python3 test_czech_plates.py ./dist/Release/GNU-Linux/libcp5200.a")
        sys.exit(1)

if __name__ == "__main__":
    main()
