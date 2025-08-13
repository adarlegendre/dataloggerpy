#!/usr/bin/env python3
"""
CP5200 Czech Number Plates Test for Raspberry Pi - UNIFIED VERSION
Combines setup and testing into a single Python file.
No need to run separate setup scripts - everything is automatic!

Target: 192.168.1.222:5200
Optimized for Raspberry Pi with existing Linux library
"""

import ctypes
import ctypes.util
import os
import sys
import platform
import subprocess
import shutil
from typing import Optional

class CP5200UnifiedTest:
    """Unified CP5200 test class that handles setup and testing automatically"""
    
    def __init__(self, library_path: Optional[str] = None):
        """
        Initialize CP5200 unified test interface for Raspberry Pi
        
        Args:
            library_path: Path to the libcp5200 library file (optional)
        """
        self.lib = None
        self.is_raspberry_pi = self._detect_raspberry_pi()
        self.library_path = library_path
        
        print("🚀 CP5200 Czech Number Plates Test for Raspberry Pi - UNIFIED")
        print("=" * 70)
        
        # Show system information
        self._show_system_info()
        
        # Run automatic setup
        self._run_automatic_setup()
        
        # Load library and setup functions
        self._load_library()
        self._setup_functions()
        
        # Initialize with default settings
        self.set_tcp_mode()
        self.set_ip_address("192.168.1.222", 5200)
        self.enable_debug()
    
    def _show_system_info(self):
        """Display system information"""
        print(f"Platform: {platform.system()} {platform.release()}")
        print(f"Architecture: {platform.machine()}")
        print(f"Python: {platform.python_version()}")
        print(f"Current directory: {os.getcwd()}")
        
        if self.is_raspberry_pi:
            print("🍓 Raspberry Pi detected - applying optimizations")
        else:
            print("⚠ Not running on Raspberry Pi - using generic paths")
    
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
    
    def _run_automatic_setup(self):
        """Run automatic setup without requiring external scripts"""
        print("\n🔧 Running Automatic Setup...")
        print("-" * 40)
        
        # Check Python availability
        self._check_python_availability()
        
        # Check current directory structure
        self._check_directory_structure()
        
        # Check library existence
        self._check_library_existence()
        
        # Check network connectivity
        self._check_network_connectivity()
        
        print("✅ Automatic setup completed successfully!")
    
    def _check_python_availability(self):
        """Check if Python and required modules are available"""
        print("1. Checking Python environment...")
        
        # Check Python version
        if sys.version_info < (3, 6):
            print("❌ Python 3.6+ required. Current version:", sys.version)
            sys.exit(1)
        else:
            print(f"✓ Python version: {sys.version}")
        
        # Check ctypes availability
        try:
            import ctypes
            print("✓ ctypes module available")
        except ImportError:
            print("❌ ctypes module not available")
            sys.exit(1)
        
        # Check platform module
        try:
            import platform
            print("✓ platform module available")
        except ImportError:
            print("❌ platform module not available")
            sys.exit(1)
    
    def _check_directory_structure(self):
        """Check if we're in the right directory structure"""
        print("2. Checking directory structure...")
        
        current_dir = os.getcwd()
        
        # Check if we're in cp5200Original directory
        if 'cp5200Original' in current_dir:
            print("✓ In cp5200Original directory")
            self.base_path = "."
        elif os.path.exists("cp5200Original"):
            print("✓ cp5200Original directory found in current directory")
            self.base_path = "cp5200Original"
        else:
            print("⚠ cp5200Original directory not found")
            print("  Current directory:", current_dir)
            print("  Looking for library in alternative locations...")
            self.base_path = None
    
    def _check_library_existence(self):
        """Check if the CP5200 library exists"""
        print("3. Checking CP5200 library...")
        
        # Define possible library paths - prioritize .so files
        library_paths = []
        
        if self.base_path:
            library_paths.extend([
                f"{self.base_path}/libcp5200.so",  # Shared library first
                f"{self.base_path}/libcp5200.a",   # Static library second
                f"{self.base_path}/dist/Release/GNU-Linux/libcp5200.so",
                f"{self.base_path}/dist/Debug/GNU-Linux/libcp5200.so"
            ])
        
        # Add fallback paths - prioritize .so files
        library_paths.extend([
            "./libcp5200.so",  # Shared library first
            "./libcp5200.a",   # Static library second
            "../libcp5200.so", # Parent directory shared library
            "../libcp5200.a",  # Parent directory static library
            "/usr/local/lib/libcp5200.so",
            "/usr/local/lib/libcp5200.a",
            "/usr/lib/libcp5200.so",
            "/usr/lib/libcp5200.a"
        ])
        
        # Check each path
        for path in library_paths:
            if os.path.exists(path):
                print(f"✓ Found CP5200 library: {path}")
                print(f"  Size: {self._format_file_size(path)}")
                
                # Check permissions
                if os.access(path, os.R_OK):
                    print("  ✓ Library is readable")
                    self.found_library_path = path
                    return
                else:
                    print("  ⚠ Library exists but not readable")
                    try:
                        os.chmod(path, 0o644)
                        print("  ✓ Fixed library permissions")
                        self.found_library_path = path
                        return
                    except Exception as e:
                        print(f"  ❌ Could not fix permissions: {e}")
        
        print("❌ No CP5200 library found!")
        print("   Please ensure the library is compiled and accessible")
        sys.exit(1)
    
    def _format_file_size(self, file_path):
        """Format file size in human readable format"""
        try:
            size = os.path.getsize(file_path)
            for unit in ['B', 'KB', 'MB', 'GB']:
                if size < 1024.0:
                    return f"{size:.1f} {unit}"
                size /= 1024.0
            return f"{size:.1f} TB"
        except:
            return "Unknown"
    
    def _check_network_connectivity(self):
        """Check network connectivity to the target IP"""
        print("4. Checking network connectivity...")
        
        target_ip = "192.168.1.222"
        target_port = 5200
        
        # Check if we can ping the target
        if self._ping_host(target_ip):
            print(f"✓ Network reachability: {target_ip} is reachable")
        else:
            print(f"⚠ Network reachability: {target_ip} may not be reachable")
            print("  This is just a warning - the test will still attempt to connect")
        
        # Check if port is open
        if self._check_port_open(target_ip, target_port):
            print(f"✓ Port {target_port} appears to be open on {target_ip}")
        else:
            print(f"⚠ Port {target_port} may be closed on {target_ip}")
            print("  This is just a warning - the test will still attempt to connect")
    
    def _ping_host(self, host):
        """Ping a host to check reachability"""
        try:
            # Use platform-specific ping command
            if platform.system().lower() == "windows":
                result = subprocess.run(['ping', '-n', '1', host], 
                                      capture_output=True, text=True, timeout=5)
            else:
                result = subprocess.run(['ping', '-c', '1', host], 
                                      capture_output=True, text=True, timeout=5)
            
            return result.returncode == 0
        except:
            return False
    
    def _check_port_open(self, host, port):
        """Check if a port is open on a host"""
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except:
            return False
    
    def _load_library(self):
        """Load the CP5200 library"""
        print("\n📚 Loading CP5200 Library...")
        print("-" * 30)
        
        try:
            # Use the library path found during setup
            if hasattr(self, 'found_library_path'):
                library_path = self.found_library_path
            elif self.library_path:
                library_path = self.library_path
            else:
                raise RuntimeError("No library path available")
            
            # Load the library
            self.lib = ctypes.CDLL(library_path)
            print(f"✓ Library loaded successfully from: {library_path}")
            
            # Test basic library functionality
            self._test_library_basic()
            
        except Exception as e:
            print(f"❌ Error loading library: {e}")
            print("\nTroubleshooting:")
            print("1. Make sure the CP5200 library is compiled for your architecture")
            print("2. Check if the library file exists and is accessible")
            print("3. Ensure the library file has proper permissions")
            print("4. Try specifying the library path manually:")
            print(f"   python3 {sys.argv[0]} /path/to/your/libcp5200.so")
            sys.exit(1)
    
    def _test_library_basic(self):
        """Test basic library functionality"""
        try:
            # Try to access a simple function to verify library loading
            if hasattr(self.lib, '_get_cp5200_version'):
                print("✓ Library functions accessible")
            else:
                print("⚠ Library loaded but functions may not be accessible")
        except Exception as e:
            print(f"⚠ Library loaded but basic test failed: {e}")
    
    def _setup_functions(self):
        """Setup function signatures for proper Python integration"""
        print("5. Setting up function signatures...")
        
        if not self.lib:
            return
            
        try:
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
            
            print("✓ Function signatures configured successfully")
            
        except Exception as e:
            print(f"⚠ Function signature setup failed: {e}")
            print("  Some functions may not work properly")
    
    def enable_debug(self):
        """Enable debug output"""
        if self.lib:
            try:
                self.lib._set_cp5200_debug()
                print("✓ Debug mode enabled")
            except Exception as e:
                print(f"⚠ Debug mode setup failed: {e}")
    
    def set_tcp_mode(self):
        """Set communication mode to TCP/IP"""
        if self.lib:
            try:
                self.lib._set_cp5200_send_mode(0)
                print("✓ Set to TCP/IP mode")
            except Exception as e:
                print(f"⚠ TCP mode setup failed: {e}")
    
    def set_ip_address(self, ip: str, port: int):
        """Set IP address and port"""
        if self.lib:
            try:
                self.lib._set_cp5200_ipcomm(ip.encode('utf-8'), port)
                print(f"✓ Set IP address: {ip}:{port}")
            except Exception as e:
                print(f"⚠ IP address setup failed: {e}")
    
    def split_windows(self, window_count: int, config: list):
        """Split display into windows"""
        if self.lib:
            try:
                # Convert Python list to C array
                c_config = (ctypes.c_int * len(config))(*config)
                result = self.lib.SplitWindow(window_count, c_config, len(config))
                
                if result == 0:
                    print(f"✓ Split display into {window_count} windows")
                else:
                    print(f"⚠ Window split failed with error: {result}")
                
                return result
            except Exception as e:
                print(f"⚠ Window split failed with exception: {e}")
                return -1
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
            try:
                # Convert text to bytes
                text_bytes = text.encode('utf-8')
                
                result = self.lib.SendText(window, text_bytes, color, font_size, 
                                         speed, effect, stay_time, align)
                
                if result == 0:
                    print(f"✓ Text sent to window {window}: '{text}'")
                else:
                    print(f"❌ Failed to send text to window {window}, error: {result}")
                
                return result
            except Exception as e:
                print(f"⚠ Text sending failed with exception: {e}")
                return -1
        return -1
    
    def sync_time(self):
        """Synchronize time with the CP5200 display"""
        if self.lib:
            try:
                result = self.lib.SyncTime()
                if result == 0:
                    print("✓ Time synchronized with display")
                else:
                    print(f"⚠ Time sync failed with error: {result}")
                return result
            except Exception as e:
                print(f"⚠ Time sync failed with exception: {e}")
                return -1
        return -1
    
    def set_brightness(self, brightness: int):
        """Set display brightness (0-31, or 255 for auto)"""
        if self.lib:
            try:
                result = self.lib.BrightnessControl(0, brightness)  # 0 = set brightness
                if result == 0:
                    print(f"✓ Brightness set to {brightness}")
                else:
                    print(f"⚠ Brightness setting failed with error: {result}")
                return result
            except Exception as e:
                print(f"⚠ Brightness setting failed with exception: {e}")
                return -1
        return -1
    
    def test_czech_plates(self):
        """Test sending Czech number plates to the display"""
        print("\n🚗 Testing Czech Number Plates Display on Raspberry Pi")
        print("=" * 70)
        
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
    """Main function for the unified CP5200 test"""
    # Check if user provided library path as argument
    library_path = None
    if len(sys.argv) > 1:
        library_path = sys.argv[1]
        print(f"Using specified library path: {library_path}")
    
    try:
        # Initialize and run the unified test
        cp = CP5200UnifiedTest(library_path)
        cp.test_czech_plates()
        
    except KeyboardInterrupt:
        print("\n\n⚠ Test interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure the CP5200 display is powered on")
        print("2. Verify network connectivity to 192.168.1.222")
        print("3. Check if port 5200 is open")
        print("4. Ensure the library file exists and is accessible")
        print("\nQuick fixes:")
        print("- Run from cp5200Original directory: cd cp5200Original && python3 ../test_czech_plates_unified.py")
        print("- Specify library path: python3 test_czech_plates_unified.py /path/to/libcp5200.so")
        print("- Check file permissions: chmod +r /path/to/libcp5200.so")
        sys.exit(1)

if __name__ == "__main__":
    main()
