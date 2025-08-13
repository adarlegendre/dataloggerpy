#!/usr/bin/env python3
"""
CP5200 Complete Automation Script
Runs build and comprehensive testing from the cp5200Original folder

Usage: python3 run_all.py [options]
Options:
  --build-only     Only build the library, skip testing
  --test-only      Only run tests, skip building
  --verbose        Show detailed output
  --target-ip IP   Set target IP address (default: 192.168.1.222)
  --target-port P  Set target port (default: 5200)
"""

import subprocess
import sys
import os
import argparse
import time
from pathlib import Path

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='CP5200 Complete Automation - Build + Test')
    parser.add_argument('--build-only', action='store_true', help='Only build the library, skip testing')
    parser.add_argument('--test-only', action='store_true', help='Only run tests, skip building')
    parser.add_argument('--verbose', action='store_true', help='Show detailed output')
    parser.add_argument('--target-ip', default='192.168.1.222', help='Target IP address (default: 192.168.1.222)')
    parser.add_argument('--target-port', type=int, default=5200, help='Target port (default: 5200)')
    
    return parser.parse_args()

def check_environment():
    """Check if we're in the right directory and environment"""
    print("🔍 Checking environment...")
    
    if not Path('cp5200.cpp').exists():
        print("❌ Error: This script must be run from the cp5200Original directory")
        print("   Please run: cd cp5200Original && python3 run_all.py")
        sys.exit(1)
    
    print("📁 Current directory:", os.getcwd())
    print("✅ Environment check passed")

def build_library(verbose=False):
    """Build the CP5200 library"""
    print("\n🔨 Building CP5200 library...")
    print("-" * 40)
    
    try:
        cmd = [sys.executable, 'build_cp5200_python.py']
        if verbose:
            print(f"Running: {' '.join(cmd)}")
        
        result = subprocess.run(cmd, capture_output=not verbose, text=True)
        
        if result.returncode == 0:
            print("✅ Build completed successfully!")
            if not verbose and result.stdout:
                print("Build output:", result.stdout)
            return True
        else:
            print("❌ Build failed!")
            if result.stderr:
                print("Build errors:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Build error: {e}")
        return False

def run_basic_tests(target_ip, target_port, verbose=False):
    """Run basic connectivity and library tests"""
    print("\n🧪 Running Basic Tests...")
    print("-" * 40)
    
    tests = [
        ('simple_diagnostic.py', 'Simple diagnostic test'),
        ('timeout_test.py', 'Timeout handling test'),
        ('corrected_diagnostic.py', 'Corrected diagnostic test')
    ]
    
    results = {}
    
    for test_file, description in tests:
        if Path(test_file).exists():
            print(f"\n📋 Running: {description}")
            try:
                cmd = [sys.executable, test_file]
                if verbose:
                    print(f"Command: {' '.join(cmd)}")
                
                result = subprocess.run(cmd, capture_output=not verbose, text=True, timeout=60)
                
                if result.returncode == 0:
                    print(f"✅ {description} completed successfully")
                    results[test_file] = 'PASS'
                else:
                    print(f"⚠ {description} had issues (return code: {result.returncode})")
                    if result.stderr and not verbose:
                        print(f"Error output: {result.stderr}")
                    results[test_file] = 'FAIL'
                    
            except subprocess.TimeoutExpired:
                print(f"⏰ {description} timed out after 60 seconds")
                results[test_file] = 'TIMEOUT'
            except Exception as e:
                print(f"❌ {description} failed with exception: {e}")
                results[test_file] = 'ERROR'
        else:
            print(f"⚠ Test file not found: {test_file}")
            results[test_file] = 'NOT_FOUND'
    
    return results

def run_advanced_tests(target_ip, target_port, verbose=False):
    """Run advanced functionality tests"""
    print("\n🚀 Running Advanced Tests...")
    print("-" * 40)
    
    tests = [
        ('test_czech_plates_unified.py', 'Czech plates unified test'),
        ('diagnostic_test.py', 'Comprehensive diagnostic test')
    ]
    
    results = {}
    
    for test_file, description in tests:
        if Path(test_file).exists():
            print(f"\n📋 Running: {description}")
            try:
                cmd = [sys.executable, test_file]
                if verbose:
                    print(f"Command: {' '.join(cmd)}")
                
                result = subprocess.run(cmd, capture_output=not verbose, text=True, timeout=120)
                
                if result.returncode == 0:
                    print(f"✅ {description} completed successfully")
                    results[test_file] = 'PASS'
                else:
                    print(f"⚠ {description} had issues (return code: {result.returncode})")
                    if result.stderr and not verbose:
                        print(f"Error output: {result.stderr}")
                    results[test_file] = 'FAIL'
                    
            except subprocess.TimeoutExpired:
                print(f"⏰ {description} timed out after 120 seconds")
                results[test_file] = 'TIMEOUT'
            except Exception as e:
                print(f"❌ {description} failed with exception: {e}")
                results[test_file] = 'ERROR'
        else:
            print(f"⚠ Test file not found: {test_file}")
            results[test_file] = 'NOT_FOUND'
    
    return results

def show_test_summary(basic_results, advanced_results):
    """Show comprehensive test results summary"""
    print("\n" + "=" * 60)
    print("🎯 TEST RESULTS SUMMARY")
    print("=" * 60)
    
    print("\n📊 Basic Tests:")
    for test, result in basic_results.items():
        status_icon = {
            'PASS': '✅',
            'FAIL': '❌',
            'TIMEOUT': '⏰',
            'ERROR': '💥',
            'NOT_FOUND': '⚠'
        }.get(result, '❓')
        print(f"   {status_icon} {test}: {result}")
    
    print("\n📊 Advanced Tests:")
    for test, result in advanced_results.items():
        status_icon = {
            'PASS': '✅',
            'FAIL': '❌',
            'TIMEOUT': '⏰',
            'ERROR': '💥',
            'NOT_FOUND': '⚠'
        }.get(result, '❓')
        print(f"   {status_icon} {test}: {result}")
    
    # Calculate success rate
    all_results = list(basic_results.values()) + list(advanced_results.values())
    passed = sum(1 for r in all_results if r == 'PASS')
    total = len(all_results)
    
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

def main():
    """Main function"""
    args = parse_arguments()
    
    print("🚀 CP5200 Complete Automation - Build + Test")
    print("=" * 60)
    print(f"Target: {args.target_ip}:{args.target_port}")
    print(f"Verbose: {args.verbose}")
    print("=" * 60)
    
    # Check environment
    check_environment()
    
    # Build phase
    build_success = True
    if not args.test_only:
        build_success = build_library(args.verbose)
        if not build_success:
            print("\n❌ Build failed! Cannot proceed with testing.")
            sys.exit(1)
    
    # Test phase
    if not args.build_only:
        print(f"\n🎯 Starting tests against {args.target_ip}:{args.target_port}")
        
        # Run basic tests
        basic_results = run_basic_tests(args.target_ip, args.target_port, args.verbose)
        
        # Run advanced tests
        advanced_results = run_advanced_tests(args.target_ip, args.target_port, args.verbose)
        
        # Show summary
        show_test_summary(basic_results, advanced_results)
    
    # Final summary
    print("\n" + "=" * 60)
    print("🎯 AUTOMATION COMPLETED!")
    print("=" * 60)
    
    if not args.test_only:
        print("\n📚 Libraries are now available in multiple locations:")
        print("   • Current directory: ./libcp5200.*")
        print("   • Parent directory: ../libcp5200.*")
        print("   • Dist structure: ./dist/Release/GNU-Linux/libcp5200.*")
    
    if not args.build_only:
        print(f"\n🚀 Your CP5200 display should now show test content!")
        print(f"   Target: {args.target_ip}:{args.target_port}")
    
    if os.name == 'posix':  # Linux/Unix
        print("\n🍓 Happy testing on your Raspberry Pi!")
    
    print("\n💡 Usage Tips:")
    print("   • Use --verbose for detailed output")
    print("   • Use --build-only to only compile the library")
    print("   • Use --test-only to skip building")
    print("   • Use --target-ip and --target-port to customize target")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Automation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
