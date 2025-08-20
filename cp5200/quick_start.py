#!/usr/bin/env python3
"""
CP5200 Library Python Wrapper Example
This demonstrates how to use the CP5200 library from Python using ctypes
"""

import ctypes
import ctypes.util
import os
import sys
from typing import List, Optional

class CP5200:
    """Python wrapper for the CP5200 C library"""
    
    def __init__(self, library_path: Optional[str] = None):
        """
        Initialize the CP5200 library wrapper
        
        Args:
            library_path: Path to the libcp5200.so file. If None, will search system paths.
        """
        if library_path and os.path.exists(library_path):
            self.lib = ctypes.CDLL(library_path)
        else:
            # Try to find the library in system paths
            lib_path = ctypes.util.find_library("cp5200")
            if lib_path:
                self.lib = ctypes.CDLL(lib_path)
            else:
                raise RuntimeError("Could not find libcp5200 library. Please ensure it's installed.")
        
        # Set function argument types and return types
        self._setup_function_signatures()
        
        # Initialize communication mode to TCP/IP by default
        self.set_send_mode(0)  # TCP/IP mode
        self.set_ip_comm("192.168.1.222", 5200)
    
    def _setup_function_signatures(self):
        """Setup the C function signatures for proper Python integration"""
        # Core functions
        self.lib._set_cp5200_debug.argtypes = []
        self.lib._set_cp5200_debug.restype = None
        
        self.lib._set_cp5200_send_mode.argtypes = [ctypes.c_int]
        self.lib._set_cp5200_send_mode.restype = None
        
        self.lib._set_cp5200_ipcomm.argtypes = [ctypes.c_char_p, ctypes.c_int]
        self.lib._set_cp5200_ipcomm.restype = None
        
        self.lib._set_cp5200_rs232comm.argtypes = [ctypes.c_char_p, ctypes.c_int]
        self.lib._set_cp5200_rs232comm.restype = None
        
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
        
        self.lib.SendClock.argtypes = [
            ctypes.c_int,      # window number
            ctypes.c_int,      # stay time
            ctypes.c_int,      # calendar type
            ctypes.POINTER(ctypes.c_int),  # format array
            ctypes.POINTER(ctypes.c_int),  # content array
            ctypes.c_char_p,   # text
            ctypes.POINTER(ctypes.c_int),  # colors array
            ctypes.c_int       # font size
        ]
        self.lib.SendClock.restype = ctypes.c_int
        
        self.lib.SplitWindow.argtypes = [
            ctypes.c_int,      # window count
            ctypes.POINTER(ctypes.c_int),  # config array
            ctypes.c_int       # array size
        ]
        self.lib.SplitWindow.restype = ctypes.c_int
        
        self.lib.BrightnessControl.argtypes = [ctypes.c_int, ctypes.c_int]
        self.lib.BrightnessControl.restype = ctypes.c_int
        
        self.lib.SyncTime.argtypes = []
        self.lib.SyncTime.restype = ctypes.c_int
    
    def enable_debug(self):
        """Enable debug output"""
        self.lib._set_cp5200_debug()
        print("Debug mode enabled")
    
    def set_send_mode(self, mode: int):
        """
        Set communication mode
        
        Args:
            mode: 0=TCP/IP, 1=RS232, 2=RS485
        """
        self.lib._set_cp5200_send_mode(mode)
        modes = {0: "TCP/IP", 1: "RS232", 2: "RS485"}
        print(f"Communication mode set to: {modes.get(mode, 'Unknown')}")
    
    def set_ip_comm(self, ip_address: str, port: int):
        """
        Set IP communication parameters
        
        Args:
            ip_address: IP address of the display
            port: Port number (default: 5200)
        """
        self.lib._set_cp5200_ipcomm(ip_address.encode('utf-8'), port)
        print(f"IP communication set to {ip_address}:{port}")
    
    def set_rs232_comm(self, port: str, baud_rate: int):
        """
        Set RS232 communication parameters
        
        Args:
            port: Serial port (e.g., "/dev/ttyAMA0")
            baud_rate: Baud rate (e.g., 115200)
        """
        self.lib._set_cp5200_rs232comm(port.encode('utf-8'), baud_rate)
        print(f"RS232 communication set to {port} at {baud_rate} baud")
    
    def send_text(self, window: int, text: str, color: int = 0xFFFFFF, 
                  font_size: int = 16, speed: int = 1, effect: int = 0, 
                  stay_time: int = 5, alignment: int = 0) -> int:
        """
        Send text to a display window
        
        Args:
            window: Window number
            text: Text to display
            color: RGB color (0xRRGGBB format)
            font_size: Font size (8-32)
            speed: Animation speed (1-10)
            effect: Display effect (0=none, 1=scroll left, etc.)
            stay_time: How long to stay on screen (seconds)
            alignment: Text alignment (0=left, 1=center, 2=right)
        
        Returns:
            0 on success, error code on failure
        """
        result = self.lib.SendText(
            window, text.encode('utf-8'), color, font_size, 
            speed, effect, stay_time, alignment
        )
        
        if result == 0:
            print(f"Text sent successfully to window {window}")
        else:
            print(f"Failed to send text to window {window}, error: {result}")
        
        return result
    
    def send_clock(self, window: int, stay_time: int = 10, 
                   calendar_type: int = 0, font_size: int = 16) -> int:
        """
        Display clock in a window
        
        Args:
            window: Window number
            stay_time: How long to stay on screen (seconds)
            calendar_type: 0=Gregorian, 1=Moon, 2=Chinese Moon, 3=Moon and Sun
            font_size: Font size (8-32)
        
        Returns:
            0 on success, error code on failure
        """
        # Enable all format and content elements
        format_array = (ctypes.c_int * 8)(*[1] * 8)
        content_array = (ctypes.c_int * 8)(*[1] * 8)
        colors_array = (ctypes.c_int * 3)(0xFF, 0xFF, 0x00)  # Yellow
        
        result = self.lib.SendClock(
            window, stay_time, calendar_type, format_array, 
            content_array, "".encode('utf-8'), colors_array, font_size
        )
        
        if result == 0:
            print(f"Clock display sent successfully to window {window}")
        else:
            print(f"Failed to send clock to window {window}, error: {result}")
        
        return result
    
    def split_window(self, window_count: int, config: List[int]) -> int:
        """
        Split display into multiple windows
        
        Args:
            window_count: Number of windows to create
            config: List of window coordinates [x1, y1, x2, y2, ...]
        
        Returns:
            0 on success, error code on failure
        """
        if len(config) != window_count * 4:
            raise ValueError(f"Config array must have {window_count * 4} elements")
        
        config_array = (ctypes.c_int * len(config))(*config)
        result = self.lib.SplitWindow(window_count, config_array, len(config))
        
        if result == 0:
            print(f"Successfully split display into {window_count} windows")
        else:
            print(f"Failed to split display, error: {result}")
        
        return result
    
    def set_brightness(self, brightness: int) -> int:
        """
        Set display brightness
        
        Args:
            brightness: Brightness level (0-31, or 255 for auto)
        
        Returns:
            0 on success, error code on failure
        """
        result = self.lib.BrightnessControl(0, brightness)
        
        if result == 0:
            print(f"Brightness set to {brightness}")
        else:
            print(f"Failed to set brightness, error: {result}")
        
        return result
    
    def sync_time(self) -> int:
        """
        Synchronize display time with system time
        
        Returns:
            0 on success, error code on failure
        """
        result = self.lib.SyncTime()
        
        if result == 0:
            print("Time synchronized successfully")
        else:
            print(f"Time synchronization failed, error: {result}")
        
        return result


def main():
    """Example usage of the CP5200 Python wrapper"""
    try:
        # Initialize the library
        print("Initializing CP5200 library...")
        cp = CP5200()
        
        # Enable debug output
        cp.enable_debug()
        
        # Set to RS232 mode (uncomment if using serial)
        # cp.set_send_mode(1)
        # cp.set_rs232_comm("/dev/ttyAMA0", 115200)
        
        # Split display into 2 windows
        print("\nSplitting display into windows...")
        cp.split_window(2, [0, 0, 64, 64, 64, 0, 128, 64])
        
        # Send text to window 0
        print("\nSending text to window 0...")
        cp.send_text(0, "Hello Raspberry Pi!", 0xFF0000, 16, 1, 0, 5, 0)
        
        # Send text to window 1
        print("\nSending text to window 1...")
        cp.send_text(1, "CP5200 Python", 0x00FF00, 14, 2, 1, 3, 1)
        
        # Show clock in window 0
        print("\nDisplaying clock...")
        cp.send_clock(0, 10, 0, 16)
        
        # Set brightness
        print("\nSetting brightness...")
        cp.set_brightness(20)
        
        # Sync time
        print("\nSynchronizing time...")
        cp.sync_time()
        
        print("\nExample completed successfully!")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
