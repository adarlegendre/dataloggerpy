#!/usr/bin/env python3
"""
CP5200 LED Display Library Installation Script
Compatible with Raspberry Pi and Linux systems
"""

import os
import sys
import subprocess
import shutil
import platform
from pathlib import Path

class CP5200Installer:
    def __init__(self):
        self.library_name = "cp5200"
        self.version = "3.1"
        self.install_prefix = "/usr/local"
        self.build_dir = "build"
        self.dist_dir = "dist"
        
    def print_banner(self):
        """Print installation banner"""
        print("=" * 60)
        print(f"CP5200 LED Display Library Installer v{self.version}")
        print("=" * 60)
        print("This script will install the CP5200 library for LED display control")
        print("Supports: TCP/IP, RS-232, RS-485 communication")
        print("=" * 60)
        
    def check_system(self):
        """Check system compatibility"""
        print("Checking system compatibility...")
        
        # Check OS
        system = platform.system()
        if system != "Linux":
            print(f"Warning: This library is designed for Linux. Current OS: {system}")
            response = input("Continue anyway? (y/N): ")
            if response.lower() != 'y':
                sys.exit(1)
        
        # Check architecture
        arch = platform.machine()
        print(f"Architecture: {arch}")
        
        # Check if running as root (for system installation)
        if os.geteuid() == 0:
            print("Running as root - will install system-wide")
        else:
            print("Not running as root - will install to user directory")
            self.install_prefix = os.path.expanduser("~/.local")
            
        return True
        
    def install_dependencies(self):
        """Install required system dependencies"""
        print("Installing system dependencies...")
        
        dependencies = [
            "build-essential",
            "g++",
            "make",
            "libiconv-hook-dev",
            "pkg-config"
        ]
        
        try:
            # Detect package manager
            if shutil.which("apt-get"):
                cmd = ["apt-get", "update"]
                subprocess.run(cmd, check=True, capture_output=True)
                
                cmd = ["apt-get", "install", "-y"] + dependencies
                subprocess.run(cmd, check=True, capture_output=True)
                print("Dependencies installed successfully")
                
            elif shutil.which("yum"):
                cmd = ["yum", "install", "-y"] + dependencies
                subprocess.run(cmd, check=True, capture_output=True)
                print("Dependencies installed successfully")
                
            elif shutil.which("pacman"):
                cmd = ["pacman", "-S", "--noconfirm"] + dependencies
                subprocess.run(cmd, check=True, capture_output=True)
                print("Dependencies installed successfully")
                
            else:
                print("Warning: Could not detect package manager")
                print("Please install the following packages manually:")
                for dep in dependencies:
                    print(f"  - {dep}")
                    
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            return False
            
        return True
        
    def build_library(self):
        """Build the CP5200 library"""
        print("Building CP5200 library...")
        
        try:
            # Create build directory
            os.makedirs(self.build_dir, exist_ok=True)
            
            # Run make
            cmd = ["make", "clean"]
            subprocess.run(cmd, check=True, capture_output=True)
            
            cmd = ["make", "all"]
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print("Build completed successfully")
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Build failed: {e}")
            print(f"Error output: {e.stderr}")
            return False
            
    def install_library(self):
        """Install the built library"""
        print("Installing CP5200 library...")
        
        try:
            # Create installation directories
            include_dir = os.path.join(self.install_prefix, "include")
            lib_dir = os.path.join(self.install_prefix, "lib")
            
            os.makedirs(include_dir, exist_ok=True)
            os.makedirs(lib_dir, exist_ok=True)
            
            # Copy header file
            header_src = "cp5200.h"
            header_dst = os.path.join(include_dir, "cp5200.h")
            shutil.copy2(header_src, header_dst)
            print(f"Installed header: {header_dst}")
            
            # Copy library file
            lib_src = os.path.join(self.dist_dir, "Release", "GNU-Linux", "libcp5200.a")
            lib_dst = os.path.join(lib_dir, "libcp5200.a")
            
            if os.path.exists(lib_src):
                shutil.copy2(lib_src, lib_dst)
                print(f"Installed library: {lib_dst}")
            else:
                print(f"Warning: Library file not found at {lib_src}")
                return False
                
            # Update library cache
            if os.geteuid() == 0:
                cmd = ["ldconfig"]
                subprocess.run(cmd, check=True, capture_output=True)
                print("Updated library cache")
                
            return True
            
        except Exception as e:
            print(f"Installation failed: {e}")
            return False
            
    def create_python_wrapper(self):
        """Create Python wrapper for the library"""
        print("Creating Python wrapper...")
        
        wrapper_code = '''#!/usr/bin/env python3
"""
CP5200 LED Display Library Python Wrapper
"""

import ctypes
import os
from typing import List, Optional

class CP5200Error(Exception):
    """Exception raised for CP5200 library errors"""
    pass

class CP5200Display:
    """Python wrapper for CP5200 LED display library"""
    
    def __init__(self, library_path: str = "/usr/local/lib/libcp5200.a"):
        """Initialize CP5200 display controller
        
        Args:
            library_path: Path to the CP5200 library
        """
        try:
            self.lib = ctypes.CDLL(library_path)
            self._setup_function_signatures()
        except Exception as e:
            raise CP5200Error(f"Failed to load CP5200 library: {e}")
    
    def _setup_function_signatures(self):
        """Setup function signatures for the C library"""
        # Set return types
        self.lib._get_cp5200_version.restype = None
        self.lib._set_cp5200_debug.restype = None
        self.lib._set_cp5200_send_mode.restype = None
        self.lib._set_cp5200_ipcomm.restype = None
        self.lib._set_cp5200_rs232comm.restype = None
        self.lib.SyncTime.restype = ctypes.c_int
        self.lib.BrightnessControl.restype = ctypes.c_int
        self.lib.SplitWindow.restype = ctypes.c_int
        self.lib.SendText.restype = ctypes.c_int
        self.lib.SendPicture.restype = ctypes.c_int
        self.lib.SendClock.restype = ctypes.c_int
        
        # Set argument types
        self.lib._set_cp5200_send_mode.argtypes = [ctypes.c_int]
        self.lib._set_cp5200_ipcomm.argtypes = [ctypes.c_char_p, ctypes.c_int]
        self.lib._set_cp5200_rs232comm.argtypes = [ctypes.c_char_p, ctypes.c_int]
        self.lib.SyncTime.restype = ctypes.c_int
        self.lib.BrightnessControl.argtypes = [ctypes.c_int, ctypes.c_int]
        self.lib.SplitWindow.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
        self.lib.SendText.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, 
                                     ctypes.c_int, ctypes.c_int, ctypes.c_int, 
                                     ctypes.c_int, ctypes.c_int]
        self.lib.SendPicture.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, 
                                        ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.lib.SendClock.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, 
                                      ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), 
                                      ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    
    def get_version(self) -> str:
        """Get library version"""
        self.lib._get_cp5200_version()
        return "CP5200 Library v3.1"
    
    def set_debug(self, enabled: bool = True):
        """Enable/disable debug mode"""
        if enabled:
            self.lib._set_cp5200_debug()
    
    def set_network_mode(self, ip_address: str, port: int = 5200):
        """Set network communication mode
        
        Args:
            ip_address: IP address of the display controller
            port: Network port (default: 5200)
        """
        self.lib._set_cp5200_ipcomm(ip_address.encode('utf-8'), port)
        self.lib._set_cp5200_send_mode(0)  # TCP/IP mode
    
    def set_serial_mode(self, port: str = "/dev/ttyAMA0", baud_rate: int = 115200):
        """Set serial communication mode
        
        Args:
            port: Serial port path
            baud_rate: Baud rate
        """
        self.lib._set_cp5200_rs232comm(port.encode('utf-8'), baud_rate)
        self.lib._set_cp5200_send_mode(1)  # RS-232 mode
    
    def sync_time(self) -> int:
        """Synchronize time with display controller"""
        return self.lib.SyncTime()
    
    def set_brightness(self, brightness: int) -> int:
        """Set display brightness
        
        Args:
            brightness: Brightness level (0-31 for manual, 255 for auto)
        """
        return self.lib.BrightnessControl(1, brightness)
    
    def get_brightness(self) -> int:
        """Get current brightness level"""
        return self.lib.BrightnessControl(0, 0)
    
    def send_text(self, window: int, text: str, color: int = 1, font_size: int = 16,
                  speed: int = 5, effect: int = 1, stay_time: int = 10, align: int = 0) -> int:
        """Send text to display
        
        Args:
            window: Window number
            text: Text to display
            color: Text color
            font_size: Font size
            speed: Animation speed
            effect: Display effect
            stay_time: Display duration
            align: Text alignment
        """
        return self.lib.SendText(window, text.encode('utf-8'), color, font_size, 
                                speed, effect, stay_time, align)
    
    def send_picture(self, window: int, pos_x: int, pos_y: int, picture_file: str,
                    speed: int = 5, effect: int = 1, stay_time: int = 10) -> int:
        """Send picture to display
        
        Args:
            window: Window number
            pos_x: X position
            pos_y: Y position
            picture_file: Path to GIF file
            speed: Animation speed
            effect: Display effect
            stay_time: Display duration
        """
        return self.lib.SendPicture(window, pos_x, pos_y, picture_file.encode('utf-8'),
                                   speed, effect, stay_time)
    
    def send_clock(self, window: int, stay_time: int, calendar_type: int,
                   format_array: List[int], content_array: List[int], text: str,
                   colors: List[int], font_size: int) -> int:
        """Send clock display
        
        Args:
            window: Window number
            stay_time: Display duration
            calendar_type: Calendar type (0=Gregorian, 1=Moon, 2=Chinese Moon, 3=Moon+Sun)
            format_array: Format array (8 elements)
            content_array: Content array (8 elements)
            text: Display text
            colors: RGB colors [R, G, B]
            font_size: Font size
        """
        format_ptr = (ctypes.c_int * 8)(*format_array)
        content_ptr = (ctypes.c_int * 8)(*content_array)
        colors_ptr = (ctypes.c_int * 3)(*colors)
        
        return self.lib.SendClock(window, stay_time, calendar_type, format_ptr, 
                                 content_ptr, text.encode('utf-8'), colors_ptr, font_size)

# Convenience function for quick setup
def create_display(ip_address: str = "192.168.1.100", port: int = 5200, debug: bool = False) -> CP5200Display:
    """Create a CP5200 display instance with network configuration
    
    Args:
        ip_address: IP address of the display controller
        port: Network port
        debug: Enable debug mode
    
    Returns:
        CP5200Display instance
    """
    display = CP5200Display()
    if debug:
        display.set_debug(True)
    display.set_network_mode(ip_address, port)
    return display
'''
        
        wrapper_path = "cp5200_wrapper.py"
        with open(wrapper_path, 'w') as f:
            f.write(wrapper_code)
            
        print(f"Created Python wrapper: {wrapper_path}")
        return True
        
    def run_tests(self):
        """Run basic tests to verify installation"""
        print("Running installation tests...")
        
        # Test 1: Check if library files exist
        header_path = os.path.join(self.install_prefix, "include", "cp5200.h")
        lib_path = os.path.join(self.install_prefix, "lib", "libcp5200.a")
        
        if not os.path.exists(header_path):
            print(f"ERROR: Header file not found at {header_path}")
            return False
            
        if not os.path.exists(lib_path):
            print(f"ERROR: Library file not found at {lib_path}")
            return False
            
        print("✓ Library files found")
        
        # Test 2: Test compilation
        test_code = '''
#include <cp5200.h>
int main() {
    _get_cp5200_version();
    return 0;
}
'''
        
        test_file = "cp5200_test.c"
        with open(test_file, 'w') as f:
            f.write(test_code)
            
        try:
            cmd = ["gcc", "-o", "cp5200_test", test_file, "-lcp5200"]
            subprocess.run(cmd, check=True, capture_output=True)
            print("✓ Compilation test passed")
            
            # Clean up test files
            os.remove(test_file)
            os.remove("cp5200_test")
            
        except subprocess.CalledProcessError as e:
            print(f"ERROR: Compilation test failed: {e}")
            return False
            
        return True
        
    def install(self):
        """Main installation process"""
        self.print_banner()
        
        if not self.check_system():
            return False
            
        if not self.install_dependencies():
            return False
            
        if not self.build_library():
            return False
            
        if not self.install_library():
            return False
            
        if not self.create_python_wrapper():
            return False
            
        if not self.run_tests():
            return False
            
        print("\n" + "=" * 60)
        print("CP5200 Library Installation Completed Successfully!")
        print("=" * 60)
        print("Files installed:")
        print(f"  Header: {self.install_prefix}/include/cp5200.h")
        print(f"  Library: {self.install_prefix}/lib/libcp5200.a")
        print("  Python wrapper: cp5200_wrapper.py")
        print("\nUsage examples:")
        print("  C/C++: #include <cp5200.h>")
        print("  Python: from cp5200_wrapper import CP5200Display")
        print("=" * 60)
        
        return True

def main():
    """Main entry point"""
    installer = CP5200Installer()
    
    try:
        success = installer.install()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\nInstallation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Installation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
