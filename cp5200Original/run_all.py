#!/usr/bin/env python3
"""
CP5200 Complete Automation Script
Runs build and test from the cp5200Original folder

Usage: python3 run_all.py
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    """Run complete build and test process"""
    print("🚀 CP5200 Complete Automation - Build + Test")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path('cp5200.cpp').exists():
        print("❌ Error: This script must be run from the cp5200Original directory")
        print("   Please run: cd cp5200Original && python3 run_all.py")
        sys.exit(1)
    
    print("📁 Current directory:", os.getcwd())
    print("🍓 Starting complete automation...")
    
    # Step 1: Build the library
    print("\n🔨 Step 1: Building CP5200 library...")
    print("-" * 40)
    
    try:
        result = subprocess.run([sys.executable, 'build_cp5200_python.py'], 
                              capture_output=False, text=True)
        
        if result.returncode == 0:
            print("✅ Build completed successfully!")
        else:
            print("❌ Build failed!")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Build error: {e}")
        sys.exit(1)
    
    # Step 2: Test the library
    print("\n🧪 Step 2: Testing CP5200 library...")
    print("-" * 40)
    
    try:
        result = subprocess.run([sys.executable, 'test_czech_plates_unified.py'], 
                              capture_output=False, text=True)
        
        if result.returncode == 0:
            print("✅ Test completed successfully!")
        else:
            print("⚠ Test had issues (check output above)")
            
    except Exception as e:
        print(f"❌ Test error: {e}")
    
    # Final summary
    print("\n" + "=" * 50)
    print("🎯 AUTOMATION COMPLETED!")
    print("=" * 50)
    
    print("\n📚 Libraries are now available in multiple locations:")
    print("   • Current directory: ./libcp5200.*")
    print("   • Parent directory: ../libcp5200.*")
    print("   • Dist structure: ./dist/Release/GNU-Linux/libcp5200.*")
    
    print("\n🚀 Your CP5200 display should now show Czech number plates!")
    print("   Target: 192.168.1.222:5200")
    
    if os.name == 'posix':  # Linux/Unix
        print("\n🍓 Happy testing on your Raspberry Pi!")

if __name__ == "__main__":
    main()
