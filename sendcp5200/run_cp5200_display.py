#!/usr/bin/env python3
"""
CP5200 Display Controller - Python Interface
This script helps you build and run the C++ code to send text to your CP5200 display.
"""

import os
import sys
import subprocess
import argparse

class CP5200Controller:
    def __init__(self, ip_address="192.168.1.222", port=5200, connection_code="255.255.255.255", debug=True):
        self.ip_address = ip_address
        self.port = port
        self.connection_code = connection_code
        self.debug = debug
        self.executable_path = "./dist/Debug/GNU-Linux/sendcp5200"
        
    def check_dependencies(self):
        """Check if required dependencies are installed"""
        print("🔍 Checking dependencies...")
        
        # Check for g++ compiler
        try:
            result = subprocess.run(["g++", "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ g++ compiler found")
            else:
                print("❌ g++ compiler not found")
                return False
        except FileNotFoundError:
            print("❌ g++ compiler not found. Please install build-essential:")
            print("   sudo apt-get update && sudo apt-get install build-essential")
            return False
            
        # Check for cp5200 library
        if os.path.exists("/usr/local/lib/libcp5200.so") or os.path.exists("/usr/lib/libcp5200.so"):
            print("✅ cp5200 library found")
        else:
            print("⚠️  cp5200 library not found in standard locations")
            print("   You may need to install it or specify the path")
            
        return True
    
    def build_cpp_code(self):
        """Build the C++ code using make"""
        print(f"\n🔨 Building C++ code...")
        
        if not os.path.exists("Makefile"):
            print("❌ Makefile not found!")
            return False
            
        try:
            # Clean previous build
            subprocess.run(["make", "clean"], capture_output=True)
            
            # Build the project
            result = subprocess.run(["make"], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Build successful!")
                return True
            else:
                print("❌ Build failed!")
                print("Build output:")
                print(result.stdout)
                print("Build errors:")
                print(result.stderr)
                return False
                
        except Exception as e:
            print(f"❌ Build error: {e}")
            return False
    
    def send_text(self, text, window_number=1, color=1, font_size=16, speed=5, effect=1, stay_time=10, alignment=1, use_connection_code=False):
        """
        Send text to the CP5200 display
        
        Args:
            text: Text to display
            window_number: Display window number
            color: Text color (1-16)
            font_size: Font size
            speed: Animation speed (1-10)
            effect: Animation effect (1-10)
            stay_time: How long to stay on screen (seconds)
            alignment: Text alignment (1=left, 2=center, 3=right)
            use_connection_code: Use connection code instead of specific IP
        """
        print(f"\n📤 Sending text to display...")
        print(f"   Text: '{text}'")
        print(f"   Window: {window_number}")
        print(f"   Color: {color}")
        print(f"   Font Size: {font_size}")
        print(f"   Speed: {speed}")
        print(f"   Effect: {effect}")
        print(f"   Stay Time: {stay_time}s")
        print(f"   Alignment: {alignment}")
        
        # Choose IP address based on connection code setting
        target_ip = self.connection_code if use_connection_code else self.ip_address
        print(f"   Target: {target_ip} (connection code)" if use_connection_code else f"   Target: {target_ip}")
        
        # Build command arguments
        debug_mode = 1 if self.debug else 0
        args = [
            self.executable_path,
            str(debug_mode),      # debug + output mode
            target_ip,            # IP address (or connection code)
            str(self.port),       # port
            "2",                  # function 2 = send text
            str(window_number),   # window number
            text,                 # text to send
            str(color),           # color
            str(font_size),       # font size
            str(speed),           # speed
            str(effect),          # effect
            str(stay_time),       # stay time
            str(alignment)        # alignment
        ]
        
        print(f"\n🚀 Executing command:")
        print(f"   {' '.join(args)}")
        
        try:
            result = subprocess.run(args, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print("✅ Text sent successfully!")
                if result.stdout:
                    print("Output:")
                    print(result.stdout)
            else:
                print("❌ Failed to send text!")
                if result.stderr:
                    print("Error:")
                    print(result.stderr)
                if result.stdout:
                    print("Output:")
                    print(result.stdout)
                    
        except subprocess.TimeoutExpired:
            print("❌ Command timed out after 30 seconds")
        except Exception as e:
            print(f"❌ Error executing command: {e}")

def main():
    parser = argparse.ArgumentParser(description="CP5200 Display Controller")
    parser.add_argument("--ip", default="192.168.1.222", help="Display IP address")
    parser.add_argument("--connection-code", default="255.255.255.255", help="Connection code for network range")
    parser.add_argument("--port", type=int, default=5200, help="Display port")
    parser.add_argument("--text", help="Text to send immediately")
    parser.add_argument("--window", type=int, default=1, help="Window number")
    parser.add_argument("--color", type=int, default=1, help="Text color (1-16)")
    parser.add_argument("--font-size", type=int, default=16, help="Font size")
    parser.add_argument("--speed", type=int, default=5, help="Animation speed (1-10)")
    parser.add_argument("--effect", type=int, default=1, help="Animation effect (1-10)")
    parser.add_argument("--stay", type=int, default=10, help="Stay time in seconds")
    parser.add_argument("--alignment", type=int, default=1, help="Text alignment (1=left, 2=center, 3=right)")
    parser.add_argument("--connection-code-mode", action="store_true", help="Send message using connection code")
    parser.add_argument("--no-debug", action="store_true", help="Disable debug mode")
    
    args = parser.parse_args()
    
    print("🚀 CP5200 Display Controller")
    print("=" * 40)
    
    # Create controller instance
    controller = CP5200Controller(
        ip_address=args.ip,
        port=args.port,
        connection_code=args.connection_code,
        debug=not args.no_debug
    )
    
    # Check dependencies
    if not controller.check_dependencies():
        print("\n❌ Please install missing dependencies and try again.")
        sys.exit(1)
    
    # Build C++ code
    if not controller.build_cpp_code():
        print("\n❌ Build failed. Please check the errors above.")
        sys.exit(1)
    
    # If text is provided, send it immediately
    if args.text:
        controller.send_text(
            text=args.text,
            window_number=args.window,
            color=args.color,
            font_size=args.font_size,
            speed=args.speed,
            effect=args.effect,
            stay_time=args.stay,
            alignment=args.alignment,
            use_connection_code=args.connection_code_mode
        )
    else:
        # Show usage
        print("\n📖 Usage examples:")
        print("   # Send text immediately:")
        print("   python3 run_cp5200_display.py --text 'Hello World!'")
        print("   # Send text using connection code:")
        print("   python3 run_cp5200_display.py --text 'Hello World!' --connection-code-mode")
        print("   # Custom settings:")
        print("   python3 run_cp5200_display.py --ip 192.168.1.222 --port 5200 --text 'Test'")
        print("   # Custom connection code:")
        print("   python3 run_cp5200_display.py --connection-code 255.255.255.0 --text 'Test' --connection-code-mode")

if __name__ == "__main__":
    main()
