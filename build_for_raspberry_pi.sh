#!/bin/bash
# Build CP5200 Library for Raspberry Pi (ARM Architecture)
# This script compiles the library specifically for Raspberry Pi
# AND places the files exactly where the test script expects them

echo "🍓 Building CP5200 Library for Raspberry Pi"
echo "=========================================="

# Check if we're on Raspberry Pi
if [ -f /proc/cpuinfo ] && grep -q "Raspberry Pi" /proc/cpuinfo; then
    echo "✓ Running on Raspberry Pi - building natively"
    TARGET_ARCH="native"
elif [ -f /proc/cpuinfo ] && grep -q "ARM" /proc/cpuinfo; then
    echo "✓ Running on ARM system - building natively"
    TARGET_ARCH="native"
else
    echo "⚠ Not on Raspberry Pi - this script is designed for Pi systems"
    echo "   For cross-compilation, use the cross-compile script instead"
    exit 1
fi

# Check prerequisites
echo "🔍 Checking prerequisites..."

# Check if g++ is available
if ! command -v g++ &> /dev/null; then
    echo "❌ g++ compiler not found"
    echo "   Install with: sudo apt install build-essential"
    exit 1
fi

# Check if make is available
if ! command -v make &> /dev/null; then
    echo "❌ make not found"
    echo "   Install with: sudo apt install build-essential"
    exit 1
fi

echo "✓ Prerequisites check passed"

# Create build directory
echo "📁 Setting up build environment..."
BUILD_DIR="build_raspberry_pi"
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

# Compile for Raspberry Pi ARM
echo "🔨 Compiling for Raspberry Pi ARM architecture..."

# Compile with ARM-specific flags
g++ -c -O2 -std=c++11 -fPIC \
    -march=native \
    -mtune=native \
    -D__ARM_ARCH \
    -I../ \
    ../cp5200.cpp \
    -o cp5200.o

if [ $? -ne 0 ]; then
    echo "❌ Compilation failed"
    exit 1
fi

echo "✓ Compilation successful"

# Create static library
echo "📚 Creating static library..."
ar rcs libcp5200.a cp5200.o
ranlib libcp5200.a

if [ $? -ne 0 ]; then
    echo "❌ Library creation failed"
    exit 1
fi

echo "✓ Static library created"

# Create shared library (recommended for Python)
echo "🔗 Creating shared library..."
g++ -shared -fPIC -o libcp5200.so cp5200.o

if [ $? -ne 0 ]; then
    echo "⚠ Shared library creation failed (this is optional)"
else
    echo "✓ Shared library created"
fi

# Show results
echo ""
echo "🎯 Build Results:"
echo "================="
echo "Static library: $(pwd)/libcp5200.a"
echo "Shared library: $(pwd)/libcp5200.so"
echo ""

# Check file sizes
echo "📊 File Information:"
ls -lh libcp5200.*

# Now place the libraries where the test script will find them automatically
echo ""
echo "📦 Placing libraries for automatic discovery..."
echo "=============================================="

# Go back to cp5200Original directory
cd ..

# Strategy 1: Place in current directory (highest priority for test script)
echo "1. Placing libraries in current directory (cp5200Original)..."
cp build_raspberry_pi/libcp5200.* ./
echo "   ✓ Libraries placed in: $(pwd)/"

# Strategy 2: Place in parent directory (root project directory)
echo "2. Placing libraries in parent directory (root project)..."
cp build_raspberry_pi/libcp5200.* ../
echo "   ✓ Libraries placed in: $(dirname $(pwd))/"

# Strategy 3: Place in the dist structure (for compatibility)
echo "3. Placing libraries in dist structure..."
mkdir -p dist/Release/GNU-Linux/
cp build_raspberry_pi/libcp5200.* dist/Release/GNU-Linux/
echo "   ✓ Libraries placed in: $(pwd)/dist/Release/GNU-Linux/"

# Strategy 4: Place in system directories (optional, requires sudo)
echo "4. Placing libraries in system directories..."
if [ -w /usr/local/lib ]; then
    sudo cp build_raspberry_pi/libcp5200.* /usr/local/lib/
    echo "   ✓ Libraries placed in: /usr/local/lib/"
else
    echo "   ⚠ /usr/local/lib not writable (requires sudo)"
fi

# Test library discovery
echo ""
echo "🧪 Testing library discovery..."
echo "=============================="

# Go to root project directory for testing
cd ..

echo "Testing from root project directory: $(pwd)"

# Test if libraries are discoverable
if [ -f "./libcp5200.so" ]; then
    echo "✓ Found libcp5200.so in root directory"
elif [ -f "./libcp5200.a" ]; then
    echo "✓ Found libcp5200.a in root directory"
else
    echo "⚠ No libraries found in root directory"
fi

if [ -f "cp5200Original/libcp5200.so" ]; then
    echo "✓ Found libcp5200.so in cp5200Original directory"
elif [ -f "cp5200Original/libcp5200.a" ]; then
    echo "✓ Found libcp5200.a in cp5200Original directory"
else
    echo "⚠ No libraries found in cp5200Original directory"
fi

# Test library loading
echo ""
echo "🧪 Testing library loading..."
if python3 -c "
import ctypes
import os

# Test loading from current directory
try:
    lib = ctypes.CDLL('./libcp5200.so')
    print('✓ Library loaded from root directory: SUCCESS')
except Exception as e:
    print(f'⚠ Library loading from root directory: {e}')

# Test loading from cp5200Original directory
try:
    lib = ctypes.CDLL('./cp5200Original/libcp5200.so')
    print('✓ Library loaded from cp5200Original: SUCCESS')
except Exception as e:
    print(f'⚠ Library loading from cp5200Original: {e}')
"; then
    echo "✓ Library test completed"
else
    echo "⚠ Library test had issues"
fi

echo ""
echo "✅ Build and placement completed successfully!"
echo ""
echo "🎯 Libraries are now available in multiple locations:"
echo "   • Root project directory: ./libcp5200.*"
echo "   • cp5200Original directory: ./cp5200Original/libcp5200.*"
echo "   • Dist structure: ./cp5200Original/dist/Release/GNU-Linux/libcp5200.*"
echo "   • System directory: /usr/local/lib/libcp5200.* (if writable)"
echo ""
echo "🚀 Your test script will now find the libraries automatically!"
echo ""
echo "🍓 Happy testing on your Raspberry Pi!"
echo ""
echo "💡 Next step: Run your test from the root project directory:"
echo "   python3 test_czech_plates_unified.py"
