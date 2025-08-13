#!/usr/bin/env python3
"""
CP5200 Library Builder for Raspberry Pi - Python Version
Automatically compiles, sets permissions, and places libraries for seamless testing

This script:
1. Detects Raspberry Pi environment
2. Compiles CP5200 library for ARM architecture
3. Sets proper permissions
4. Places libraries in all locations where test script expects them
5. Verifies everything works automatically

Usage: python3 build_cp5200_python.py
"""

import os
import sys
import subprocess
import shutil
import platform
import stat
from pathlib import Path
from typing import List, Tuple, Optional

class CP5200Builder:
    """Python-based CP5200 library builder for Raspberry Pi"""
    
    def __init__(self):
        self.is_raspberry_pi = self._detect_raspberry_pi()
        self.current_dir = Path.cwd()
        self.build_dir = self.current_dir / "build_raspberry_pi"
        self.source_files = {
            'cpp': self.current_dir / "cp5200.cpp",
            'header': self.current_dir / "cp5200.h"
        }
        self.library_names = ['libcp5200.a', 'libcp5200.so']
        
        print("🚀 CP5200 Library Builder for Raspberry Pi - Python Version")
        print("=" * 70)
        
    def _detect_raspberry_pi(self) -> bool:
        """Detect if running on Raspberry Pi"""
        try:
            # Method 1: Check /proc/cpuinfo
            if Path('/proc/cpuinfo').exists():
                with open('/proc/cpuinfo', 'r') as f:
                    if 'Raspberry Pi' in f.read():
                        return True
            
            # Method 2: Check /etc/rpi-issue
            if Path('/etc/rpi-issue').exists():
                return True
                
            # Method 3: Check device tree
            if Path('/proc/device-tree/model').exists():
                with open('/proc/device-tree/model', 'r') as f:
                    if 'Raspberry Pi' in f.read():
                        return True
                        
            # Method 4: Check platform
            if platform.system() == 'Linux' and 'arm' in platform.machine().lower():
                return True
                
        except Exception:
            pass
            
        return False
    
    def _show_system_info(self):
        """Display system information"""
        print(f"Platform: {platform.system()} {platform.release()}")
        print(f"Architecture: {platform.machine()}")
        print(f"Python: {platform.python_version()}")
        print(f"Current directory: {self.current_dir}")
        
        if self.is_raspberry_pi:
            print("🍓 Raspberry Pi detected - applying optimizations")
        else:
            print("⚠ Not running on Raspberry Pi - using generic paths")
    
    def _check_prerequisites(self) -> bool:
        """Check if required tools are available"""
        print("\n🔍 Checking prerequisites...")
        
        required_tools = ['g++', 'ar', 'ranlib']
        missing_tools = []
        
        for tool in required_tools:
            if shutil.which(tool) is None:
                missing_tools.append(tool)
            else:
                print(f"✓ {tool} found")
        
        if missing_tools:
            print(f"❌ Missing required tools: {', '.join(missing_tools)}")
            print("   Install with: sudo apt install build-essential")
            return False
        
        print("✅ All prerequisites are available")
        return True
    
    def _check_source_files(self) -> bool:
        """Check if source files exist"""
        print("\n📁 Checking source files...")
        
        for file_type, file_path in self.source_files.items():
            if file_path.exists():
                size = file_path.stat().st_size
                print(f"✓ {file_type.upper()} file found: {file_path.name} ({size:,} bytes)")
            else:
                print(f"❌ {file_type.upper()} file missing: {file_path}")
                return False
        
        return True
    
    def _setup_build_environment(self):
        """Create and setup build directory"""
        print("\n📁 Setting up build environment...")
        
        # Remove existing build directory
        if self.build_dir.exists():
            shutil.rmtree(self.build_dir)
            print("✓ Removed existing build directory")
        
        # Create fresh build directory
        self.build_dir.mkdir(exist_ok=True)
        print(f"✓ Created build directory: {self.build_dir}")
    
    def _compile_source(self) -> bool:
        """Compile the source code for ARM architecture"""
        print("\n🔨 Compiling for Raspberry Pi ARM architecture...")
        
        try:
            # Compile with ARM-specific flags
            compile_cmd = [
                'g++', '-c', '-O2', '-std=c++11', '-fPIC',
                '-march=native', '-mtune=native',
                '-I', str(self.current_dir),
                str(self.source_files['cpp']),
                '-o', str(self.build_dir / 'cp5200.o')
            ]
            
            print(f"Running: {' '.join(compile_cmd)}")
            
            result = subprocess.run(
                compile_cmd,
                capture_output=True,
                text=True,
                cwd=self.build_dir
            )
            
            if result.returncode == 0:
                print("✅ Compilation successful")
                return True
            else:
                print(f"❌ Compilation failed:")
                print(f"stdout: {result.stdout}")
                print(f"stderr: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Compilation error: {e}")
            return False
    
    def _create_libraries(self) -> bool:
        """Create static and shared libraries"""
        print("\n📚 Creating libraries...")
        
        try:
            # Create static library (.a)
            print("Creating static library...")
            ar_cmd = ['ar', 'rcs', 'libcp5200.a', 'cp5200.o']
            result = subprocess.run(ar_cmd, cwd=self.build_dir, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"❌ Static library creation failed: {result.stderr}")
                return False
            
            # Run ranlib on static library
            ranlib_cmd = ['ranlib', 'libcp5200.a']
            result = subprocess.run(ranlib_cmd, cwd=self.build_dir, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"⚠ ranlib failed: {result.stderr}")
            else:
                print("✓ Static library created")
            
            # Create shared library (.so)
            print("Creating shared library...")
            gcc_cmd = [
                'g++', '-shared', '-fPIC',
                '-o', 'libcp5200.so', 'cp5200.o'
            ]
            
            result = subprocess.run(gcc_cmd, cwd=self.build_dir, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✓ Shared library created")
            else:
                print(f"⚠ Shared library creation failed: {result.stderr}")
            
            return True
            
        except Exception as e:
            print(f"❌ Library creation error: {e}")
            return False
    
    def _set_library_permissions(self):
        """Set proper permissions for library files"""
        print("\n🔐 Setting library permissions...")
        
        for lib_name in self.library_names:
            lib_path = self.build_dir / lib_name
            if lib_path.exists():
                try:
                    # Set read permissions for all users
                    lib_path.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
                    print(f"✓ Set permissions for {lib_name}")
                except Exception as e:
                    print(f"⚠ Could not set permissions for {lib_name}: {e}")
    
    def _place_libraries_automatically(self):
        """Place libraries in all locations where test script expects them"""
        print("\n📦 Placing libraries for automatic discovery...")
        print("=" * 50)
        
        placement_strategies = [
            # Strategy 1: Current directory (cp5200Original)
            {
                'name': 'Current directory (cp5200Original)',
                'path': self.current_dir,
                'priority': 'Highest'
            },
            # Strategy 2: Parent directory (root project)
            {
                'name': 'Parent directory (root project)',
                'path': self.current_dir.parent,
                'priority': 'High'
            },
            # Strategy 3: Dist structure (for compatibility)
            {
                'name': 'Dist structure',
                'path': self.current_dir / 'dist' / 'Release' / 'GNU-Linux',
                'priority': 'Medium'
            }
        ]
        
        for strategy in placement_strategies:
            print(f"\n{strategy['priority']} Priority: {strategy['name']}")
            
            # Create directory if it doesn't exist
            strategy['path'].mkdir(parents=True, exist_ok=True)
            
            # Copy libraries
            for lib_name in self.library_names:
                source = self.build_dir / lib_name
                destination = strategy['path'] / lib_name
                
                if source.exists():
                    try:
                        # Remove existing file if it exists
                        if destination.exists():
                            destination.unlink()
                            print(f"  ✓ Removed existing {lib_name}")
                        
                        shutil.copy2(source, destination)
                        print(f"  ✓ {lib_name} → {destination}")
                    except Exception as e:
                        print(f"  ❌ Failed to copy {lib_name}: {e}")
                else:
                    print(f"  ⚠ Source {lib_name} not found")
        
        # Strategy 4: System directories (optional)
        print(f"\nOptional: System directories")
        system_lib_path = Path('/usr/local/lib')
        
        if system_lib_path.exists() and os.access(system_lib_path, os.W_OK):
            try:
                for lib_name in self.library_names:
                    source = self.build_dir / lib_name
                    destination = system_lib_path / lib_name
                    
                    if source.exists():
                        # Use sudo for system directories
                        sudo_cmd = ['sudo', 'cp', str(source), str(destination)]
                        result = subprocess.run(sudo_cmd, capture_output=True, text=True)
                        
                        if result.returncode == 0:
                            print(f"  ✓ {lib_name} → {destination} (system)")
                        else:
                            print(f"  ⚠ Failed to copy to system: {result.stderr}")
            except Exception as e:
                print(f"  ⚠ System copy failed: {e}")
        else:
            print("  ⚠ /usr/local/lib not writable (requires sudo)")
    
    def _verify_library_placement(self):
        """Verify that libraries are discoverable"""
        print("\n🧪 Verifying library placement...")
        print("=" * 40)
        
        verification_locations = [
            self.current_dir,
            self.current_dir.parent,
            self.current_dir / 'dist' / 'Release' / 'GNU-Linux'
        ]
        
        for location in verification_locations:
            print(f"\nChecking: {location}")
            
            for lib_name in self.library_names:
                lib_path = location / lib_name
                if lib_path.exists():
                    size = lib_path.stat().st_size
                    print(f"  ✓ {lib_name} found ({size:,} bytes)")
                else:
                    print(f"  ❌ {lib_name} missing")
    
    def _test_library_loading(self):
        """Test if libraries can be loaded by Python"""
        print("\n🧪 Testing library loading...")
        print("=" * 35)
        
        test_locations = [
            (self.current_dir.parent, "Root project directory"),
            (self.current_dir, "cp5200Original directory"),
            (self.current_dir / 'dist' / 'Release' / 'GNU-Linux', "Dist structure")
        ]
        
        for location, description in test_locations:
            print(f"\nTesting from: {description}")
            
            for lib_name in self.library_names:
                lib_path = location / lib_name
                if lib_path.exists():
                    try:
                        # Test library loading with ctypes
                        test_script = f"""
import ctypes
try:
    lib = ctypes.CDLL('{lib_path}')
    print('    ✓ {lib_name} loaded successfully')
except Exception as e:
    print(f'    ❌ {lib_name} failed to load: {{e}}')
"""
                        
                        result = subprocess.run(
                            [sys.executable, '-c', test_script],
                            capture_output=True,
                            text=True,
                            cwd=location
                        )
                        
                        if result.returncode == 0:
                            print(result.stdout.strip())
                        else:
                            print(f"    ⚠ Test script failed: {result.stderr}")
                            
                    except Exception as e:
                        print(f"    ⚠ Library test failed: {e}")
                else:
                    print(f"    ⚠ {lib_name} not found in {description}")
    
    def _show_final_summary(self):
        """Show final summary and next steps"""
        print("\n" + "=" * 70)
        print("🎯 BUILD COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        
        print("\n📚 Libraries are now available in multiple locations:")
        print("   • Root project directory: ./libcp5200.*")
        print("   • cp5200Original directory: ./cp5200Original/libcp5200.*")
        print("   • Dist structure: ./cp5200Original/dist/Release/GNU-Linux/libcp5200.*")
        print("   • System directory: /usr/local/lib/libcp5200.* (if copied)")
        
        print("\n🚀 Your test script will now find the libraries automatically!")
        print("\n💡 Next step: Run your test from the root project directory:")
        print("   cd ..")
        print("   python3 test_czech_plates_unified.py")
        
        if self.is_raspberry_pi:
            print("\n🍓 Happy testing on your Raspberry Pi!")
        else:
            print("\n⚠ Note: This was built for the current architecture")
    
    def build(self) -> bool:
        """Main build process"""
        try:
            # Show system information
            self._show_system_info()
            
            # Check prerequisites
            if not self._check_prerequisites():
                return False
            
            # Check source files
            if not self._check_source_files():
                return False
            
            # Setup build environment
            self._setup_build_environment()
            
            # Compile source
            if not self._compile_source():
                return False
            
            # Create libraries
            if not self._create_libraries():
                return False
            
            # Set permissions
            self._set_library_permissions()
            
            # Place libraries automatically
            self._place_libraries_automatically()
            
            # Verify placement
            self._verify_library_placement()
            
            # Test loading
            self._test_library_loading()
            
            # Show summary
            self._show_final_summary()
            
            return True
            
        except Exception as e:
            print(f"\n❌ Build process failed: {e}")
            return False

def main():
    """Main function"""
    try:
        # Check if we're in the right directory
        if not Path('cp5200.cpp').exists():
            print("❌ Error: This script must be run from the cp5200Original directory")
            print("   Please run: cd cp5200Original && python3 build_cp5200_python.py")
            sys.exit(1)
        
        # Create builder and run build
        builder = CP5200Builder()
        success = builder.build()
        
        if success:
            print("\n✅ Build completed successfully!")
            sys.exit(0)
        else:
            print("\n❌ Build failed!")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⚠ Build interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
