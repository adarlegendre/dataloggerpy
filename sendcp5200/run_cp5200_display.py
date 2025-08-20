#!/usr/bin/env python3
"""
CP5200 Display Controller - Python Interface
This script helps you build and run the C++ code to send text to your CP5200 display.
"""

import os
import sys
import subprocess
import argparse
import logging
from datetime import datetime

class CP5200Controller:
    def __init__(self, ip_address="192.168.1.222", port=5200, connection_code="255.255.255.255", debug=True):
        self.ip_address = ip_address
        self.port = port
        self.connection_code = connection_code
        self.debug = debug
        self.executable_path = "./dist/Debug/GNU-Linux/sendcp5200"
        
        # Setup logging
        self.setup_logging()
        
    def setup_logging(self):
        """Setup comprehensive logging"""
        # Create logs directory if it doesn't exist
        os.makedirs("logs", exist_ok=True)
        
        # Create timestamp for log file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"logs/cp5200_display_{timestamp}.log"
        
        # Configure logging
        logging.basicConfig(
            level=logging.DEBUG if self.debug else logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"CP5200 Controller initialized - IP: {self.ip_address}, Port: {self.port}, Connection Code: {self.connection_code}")
        
    def check_dependencies(self):
        """Check if required dependencies are installed"""
        self.logger.info("🔍 Checking dependencies...")
        
        # Check for g++ compiler
        try:
            result = subprocess.run(["g++", "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                self.logger.info("✅ g++ compiler found")
                self.logger.debug(f"g++ version: {result.stdout.split(chr(10))[0]}")
            else:
                self.logger.error("❌ g++ compiler not found")
                return False
        except FileNotFoundError:
            self.logger.error("❌ g++ compiler not found. Please install build-essential:")
            self.logger.error("   sudo apt-get update && sudo apt-get install build-essential")
            return False
            
        # Check for cp5200 library
        if os.path.exists("/usr/local/lib/libcp5200.so") or os.path.exists("/usr/lib/libcp5200.so"):
            self.logger.info("✅ cp5200 library found")
            # Try to get library version
            try:
                result = subprocess.run(["strings", "/usr/local/lib/libcp5200.so"], capture_output=True, text=True, timeout=10)
                if "V3.1" in result.stdout:
                    self.logger.info("📚 cp5200 library version: V3.1")
            except:
                pass
        else:
            self.logger.warning("⚠️  cp5200 library not found in standard locations")
            self.logger.warning("   You may need to install it or specify the path")
            
        return True
    
    def build_cpp_code(self):
        """Build the C++ code using make"""
        self.logger.info("🔨 Building C++ code...")
        
        if not os.path.exists("Makefile"):
            self.logger.error("❌ Makefile not found!")
            return False
            
        try:
            # Clean previous build
            self.logger.debug("Cleaning previous build...")
            subprocess.run(["make", "clean"], capture_output=True)
            
            # Build the project
            self.logger.debug("Building project with make...")
            result = subprocess.run(["make"], capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info("✅ Build successful!")
                self.logger.debug(f"Build output: {result.stdout}")
                return True
            else:
                self.logger.error("❌ Build failed!")
                self.logger.error(f"Build output: {result.stdout}")
                self.logger.error(f"Build errors: {result.stderr}")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Build error: {e}")
            return False
    
    def parse_cpp_output(self, output):
        """Parse C++ output for detailed information"""
        lines = output.split('\n')
        parsed_data = {
            'library_version': None,
            'arguments': [],
            'hex_data': None,
            'network_info': {},
            'response_data': None,
            'result_code': None
        }
        
        for line in lines:
            line = line.strip()
            
            # Extract library version
            if "cp5200 GNU library V" in line:
                parsed_data['library_version'] = line.split("V")[1]
                
            # Extract arguments
            elif "Argument list:" in line:
                continue
            elif line.startswith("0:") or line.startswith("1:") or line.startswith("2:") or line.startswith("3:") or line.startswith("4:") or line.startswith("5:") or line.startswith("6:") or line.startswith("7:") or line.startswith("8:") or line.startswith("9:") or line.startswith("10:") or line.startswith("11:") or line.startswith("12:"):
                parsed_data['arguments'].append(line)
                
            # Extract hex data
            elif "sendable hex:" in line:
                parsed_data['hex_data'] = line.split("sendable hex:")[1].strip()
                
            # Extract network information
            elif "IP address:" in line:
                parsed_data['network_info']['ip'] = line.split("IP address:")[1].strip()
            elif "IP port:" in line:
                parsed_data['network_info']['port'] = line.split("IP port:")[1].strip()
                
            # Extract response data
            elif "ff ff ff ff" in line:
                parsed_data['response_data'] = line.strip()
                
            # Extract result code
            elif "result:" in line:
                result_part = line.split("result:")[1].strip()
                parsed_data['result_code'] = result_part
                
        return parsed_data
    
    def send_text_positioned(self, text, x=0, y=0, window_number=1, color=1, font_size=16, speed=5, effect=1, stay_time=10, alignment=1, use_connection_code=False):
        """
        Send text to the CP5200 display at a specific position
        
        Args:
            text: Text to display
            x: X coordinate (horizontal position)
            y: Y coordinate (vertical position)
            window_number: Display window number
            color: Text color (1-16)
            font_size: Font size
            speed: Animation speed (1-10)
            effect: Animation effect (1-10)
            stay_time: How long to stay on screen (seconds)
            alignment: Text alignment (1=left, 2=center, 3=right)
            use_connection_code: Use connection code instead of specific IP
        """
        self.logger.info("📤 Sending positioned text to display...")
        self.logger.info(f"   Text: '{text}'")
        self.logger.info(f"   Position: ({x}, {y})")
        self.logger.info(f"   Window: {window_number}")
        self.logger.info(f"   Color: {color}")
        self.logger.info(f"   Font Size: {font_size}")
        self.logger.info(f"   Speed: {speed}")
        self.logger.info(f"   Effect: {effect}")
        self.logger.info(f"   Stay Time: {stay_time}s")
        self.logger.info(f"   Alignment: {alignment}")
        
        # Choose IP address based on connection code setting
        target_ip = self.connection_code if use_connection_code else self.ip_address
        self.logger.info(f"   Target: {target_ip} (connection code)" if use_connection_code else f"   Target: {target_ip}")
        
        # Step 1: Create/position window using SplitWindow (function 1)
        self.logger.info("🔧 Step 1: Creating positioned window...")
        debug_mode = 1 if self.debug else 0
        window_args = [
            self.executable_path,
            str(debug_mode),      # debug + output mode
            target_ip,            # IP address (or connection code)
            str(self.port),       # port
            "1",                  # function 1 = split window
            str(window_number),   # window number
            str(x),               # X coordinate
            str(y)                # Y coordinate
        ]
        
        self.logger.info("🚀 Executing window creation command:")
        self.logger.info(f"   {' '.join(window_args)}")
        
        try:
            # Create positioned window
            window_result = subprocess.run(window_args, capture_output=True, text=True, timeout=30)
            
            if window_result.returncode == 0:
                self.logger.info("✅ Window positioned successfully!")
                if window_result.stdout:
                    self.logger.debug(f"Window creation output: {window_result.stdout}")
            else:
                self.logger.error("❌ Failed to position window!")
                if window_result.stderr:
                    self.logger.error(f"Window error: {window_result.stderr}")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Window creation error: {e}")
            return False
        
        # Step 2: Send text to the positioned window
        self.logger.info("🔧 Step 2: Sending text to positioned window...")
        text_args = [
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
        
        self.logger.info("🚀 Executing text sending command:")
        self.logger.info(f"   {' '.join(text_args)}")
        
        try:
            self.logger.debug("Starting text subprocess execution...")
            result = subprocess.run(text_args, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                self.logger.info("✅ Positioned text sent successfully!")
                
                # Parse and log detailed output
                if result.stdout:
                    self.logger.info("📋 Raw Output:")
                    self.logger.info(result.stdout)
                    
                    # Parse the output for detailed information
                    parsed = self.parse_cpp_output(result.stdout)
                    
                    # Log parsed information
                    self.logger.info("🔍 Parsed Information:")
                    if parsed['library_version']:
                        self.logger.info(f"   Library Version: V{parsed['library_version']}")
                    if parsed['arguments']:
                        self.logger.info("   Arguments:")
                        for arg in parsed['arguments']:
                            self.logger.info(f"      {arg}")
                    if parsed['hex_data']:
                        self.logger.info(f"   Hex Data: {parsed['hex_data']}")
                    if parsed['network_info']:
                        self.logger.info("   Network Info:")
                        for key, value in parsed['network_info'].items():
                            self.logger.info(f"      {key}: {value}")
                    if parsed['response_data']:
                        self.logger.info(f"   Response Data: {parsed['response_data']}")
                    if parsed['result_code']:
                        self.logger.info(f"   Result Code: {parsed['result_code']}")
                        
                        # Interpret result code
                        try:
                            result_code = int(parsed['result_code'])
                            if result_code == 0:
                                self.logger.info("   ✅ Result: Success (0)")
                            elif result_code == 1:
                                self.logger.warning("   ⚠️  Result: Warning/Info (1)")
                            elif result_code >= 2 and result_code <= 13:
                                self.logger.error(f"   ❌ Result: Library Error ({result_code})")
                            elif result_code == 100:
                                self.logger.error("   ❌ Result: Argument Error (100)")
                            elif result_code == 200:
                                self.logger.error("   ❌ Result: Argument Error (200)")
                            else:
                                self.logger.info(f"   ℹ️  Result: Unknown ({result_code})")
                        except ValueError:
                            self.logger.warning(f"   ⚠️  Could not parse result code: {parsed['result_code']}")
                            
                if result.stderr:
                    self.logger.warning("⚠️  stderr output:")
                    self.logger.warning(result.stderr)
                    
            else:
                self.logger.error("❌ Failed to send positioned text!")
                if result.stderr:
                    self.logger.error("Error:")
                    self.logger.error(result.stderr)
                if result.stdout:
                    self.logger.error("Output:")
                    self.logger.error(result.stdout)
                    
        except subprocess.TimeoutExpired:
            self.logger.error("❌ Command timed out after 30 seconds")
        except Exception as e:
            self.logger.error(f"❌ Error executing command: {e}")

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
        self.logger.info("📤 Sending text to display...")
        self.logger.info(f"   Text: '{text}'")
        self.logger.info(f"   Window: {window_number}")
        self.logger.info(f"   Color: {color}")
        self.logger.info(f"   Font Size: {font_size}")
        self.logger.info(f"   Speed: {speed}")
        self.logger.info(f"   Effect: {effect}")
        self.logger.info(f"   Stay Time: {stay_time}s")
        self.logger.info(f"   Alignment: {alignment}")
        
        # Choose IP address based on connection code setting
        target_ip = self.connection_code if use_connection_code else self.ip_address
        self.logger.info(f"   Target: {target_ip} (connection code)" if use_connection_code else f"   Target: {target_ip}")
        
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
        
        self.logger.info("🚀 Executing command:")
        self.logger.info(f"   {' '.join(args)}")
        
        try:
            self.logger.debug("Starting subprocess execution...")
            result = subprocess.run(args, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                self.logger.info("✅ Text sent successfully!")
                
                # Parse and log detailed output
                if result.stdout:
                    self.logger.info("📋 Raw Output:")
                    self.logger.info(result.stdout)
                    
                    # Parse the output for detailed information
                    parsed = self.parse_cpp_output(result.stdout)
                    
                    # Log parsed information
                    self.logger.info("🔍 Parsed Information:")
                    if parsed['library_version']:
                        self.logger.info(f"   Library Version: V{parsed['library_version']}")
                    if parsed['arguments']:
                        self.logger.info("   Arguments:")
                        for arg in parsed['arguments']:
                            self.logger.info(f"      {arg}")
                    if parsed['hex_data']:
                        self.logger.info(f"   Hex Data: {parsed['hex_data']}")
                    if parsed['network_info']:
                        self.logger.info("   Network Info:")
                        for key, value in parsed['network_info'].items():
                            self.logger.info(f"      {key}: {value}")
                    if parsed['response_data']:
                        self.logger.info(f"   Response Data: {parsed['response_data']}")
                    if parsed['result_code']:
                        self.logger.info(f"   Result Code: {parsed['result_code']}")
                        
                        # Interpret result code
                        try:
                            result_code = int(parsed['result_code'])
                            if result_code == 0:
                                self.logger.info("   ✅ Result: Success (0)")
                            elif result_code == 1:
                                self.logger.warning("   ⚠️  Result: Warning/Info (1)")
                            elif result_code >= 2 and result_code <= 13:
                                self.logger.error(f"   ❌ Result: Library Error ({result_code})")
                            elif result_code == 100:
                                self.logger.error("   ❌ Result: Argument Error (100)")
                            elif result_code == 200:
                                self.logger.error("   ❌ Result: Argument Error (200)")
                            else:
                                self.logger.info(f"   ℹ️  Result: Unknown ({result_code})")
                        except ValueError:
                            self.logger.warning(f"   ⚠️  Could not parse result code: {parsed['result_code']}")
                            
                if result.stderr:
                    self.logger.warning("⚠️  stderr output:")
                    self.logger.warning(result.stderr)
                    
            else:
                self.logger.error("❌ Failed to send text!")
                if result.stderr:
                    self.logger.error("Error:")
                    self.logger.error(result.stderr)
                if result.stdout:
                    self.logger.error("Output:")
                    self.logger.error(result.stdout)
                    
        except subprocess.TimeoutExpired:
            self.logger.error("❌ Command timed out after 30 seconds")
        except Exception as e:
            self.logger.error(f"❌ Error executing command: {e}")

def main():
    parser = argparse.ArgumentParser(description="CP5200 Display Controller")
    parser.add_argument("--ip", default="192.168.1.222", help="Display IP address")
    parser.add_argument("--connection-code", default="255.255.255.255", help="Connection code for network range")
    parser.add_argument("--port", type=int, default=5200, help="Display port")
    parser.add_argument("--text", help="Text to send immediately")
    parser.add_argument("--x", type=int, default=0, help="X coordinate for positioned text (default: 0)")
    parser.add_argument("--y", type=int, default=0, help="Y coordinate for positioned text (default: 0)")
    parser.add_argument("--positioned", action="store_true", help="Send text at specific position using SplitWindow")
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
        if args.positioned:
            # Use positioned text function
            controller.send_text_positioned(
                text=args.text,
                x=args.x,
                y=args.y,
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
            # Use regular text function
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
        print("   # Send text at specific position (top-left corner):")
        print("   python3 run_cp5200_display.py --text 'Top Left Text' --positioned --x 0 --y 0")
        print("   # Send text at custom position:")
        print("   python3 run_cp5200_display.py --text 'Custom Position' --positioned --x 100 --y 50")
        print("   # Custom settings:")
        print("   python3 run_cp5200_display.py --ip 192.168.1.222 --port 5200 --text 'Test'")
        print("   # Custom connection code:")
        print("   python3 run_cp5200_display.py --connection-code 255.255.255.0 --text 'Test' --connection-code-mode")
        print("\n📝 Logs are saved in the 'logs' directory with timestamps")

if __name__ == "__main__":
    main()
