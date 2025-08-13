#!/bin/bash
# CP5200 Raspberry Pi Setup Script
# This script helps set up the CP5200 library for Raspberry Pi usage

echo "🍓 CP5200 Raspberry Pi Setup Script"
echo "=================================="

# Check if we're on Raspberry Pi
if [ -f /proc/cpuinfo ] && grep -q "Raspberry Pi" /proc/cpuinfo; then
    echo "✓ Raspberry Pi detected"
else
    echo "⚠ This script is designed for Raspberry Pi"
    echo "   It may work on other Linux systems but is not guaranteed"
fi

# Check current directory
CURRENT_DIR=$(pwd)
echo "Current directory: $CURRENT_DIR"

# Check if we're in the right place
if [[ "$CURRENT_DIR" == *"cp5200Original"* ]]; then
    echo "✓ In cp5200Original directory"
    LIBRARY_PATH="./dist/Release/GNU-Linux/libcp5200.a"
elif [ -d "cp5200Original" ]; then
    echo "✓ cp5200Original directory found"
    LIBRARY_PATH="./cp5200Original/dist/Release/GNU-Linux/libcp5200.a"
else
    echo "❌ cp5200Original directory not found"
    echo "   Please run this script from the parent directory of cp5200Original"
    exit 1
fi

# Check if library exists
if [ -f "$LIBRARY_PATH" ]; then
    echo "✓ Found CP5200 library: $LIBRARY_PATH"
    echo "  Size: $(ls -lh "$LIBRARY_PATH" | awk '{print $5}')"
else
    echo "❌ CP5200 library not found at: $LIBRARY_PATH"
    echo "   Please ensure the library is compiled"
    exit 1
fi

# Check library permissions
if [ -r "$LIBRARY_PATH" ]; then
    echo "✓ Library is readable"
else
    echo "⚠ Library permissions issue, attempting to fix..."
    chmod +r "$LIBRARY_PATH"
    if [ -r "$LIBRARY_PATH" ]; then
        echo "✓ Library permissions fixed"
    else
        echo "❌ Could not fix library permissions"
        exit 1
    fi
fi

# Check Python availability
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo "✓ Python 3 found: $(python3 --version)"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    echo "✓ Python found: $(python --version)"
else
    echo "❌ Python not found"
    echo "   Please install Python 3: sudo apt install python3"
    exit 1
fi

# Check if test file exists
if [ -f "test_czech_plates.py" ]; then
    echo "✓ Test file found: test_czech_plates.py"
else
    echo "❌ Test file not found: test_czech_plates.py"
    echo "   Please ensure the test file is in the current directory"
    exit 1
fi

# Test library loading
echo ""
echo "🧪 Testing library loading..."
if $PYTHON_CMD -c "
import ctypes
try:
    lib = ctypes.CDLL('$LIBRARY_PATH')
    print('✓ Library loaded successfully')
    print('✓ Library functions available')
except Exception as e:
    print(f'❌ Library loading failed: {e}')
    exit(1)
"; then
    echo "✓ Library test passed"
else
    echo "❌ Library test failed"
    exit 1
fi

echo ""
echo "🎯 Setup Complete! You can now run the test:"
echo ""
echo "Option 1: Run from current directory"
echo "  $PYTHON_CMD test_czech_plates.py"
echo ""
echo "Option 2: Specify library path explicitly"
echo "  $PYTHON_CMD test_czech_plates.py $LIBRARY_PATH"
echo ""
echo "Option 3: Run from cp5200Original directory"
echo "  cd cp5200Original"
echo "  $PYTHON_CMD ../test_czech_plates.py"
echo ""
echo "🍓 Happy testing on your Raspberry Pi!"
