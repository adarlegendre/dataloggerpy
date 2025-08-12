#!/bin/bash

# CP5200 Library Build Script for Raspberry Pi
# This script compiles the CP5200 library and example program on Raspberry Pi

echo "Building CP5200 Library for Raspberry Pi..."

# Check if we're on Raspberry Pi
if ! grep -q "Raspberry Pi" /proc/cpuinfo 2>/dev/null; then
    echo "Warning: This script is designed for Raspberry Pi"
    echo "You may need to adjust paths and settings for your system"
fi

# Create build directory
mkdir -p build
cd build

# Compile the library
echo "Compiling CP5200 library..."
g++ -c -O2 -std=c++11 -fPIC -D_GNU_SOURCE -Wall -Wextra ../cp5200/cp5200.cpp -o cp5200.o

if [ $? -ne 0 ]; then
    echo "✗ Library compilation failed!"
    echo "Please check the error messages above"
    exit 1
fi

# Create static library
echo "Creating static library..."
ar rcs libcp5200.a cp5200.o
ranlib libcp5200.a

# Create shared library
echo "Creating shared library..."
g++ -shared -fPIC -o libcp5200.so cp5200.o

# Compile the example program
echo "Compiling example program..."
g++ -std=c++11 -I../cp5200 ../simple_example.cpp -L. -lcp5200 -o simple_example

if [ $? -ne 0 ]; then
    echo "✗ Example compilation failed!"
    echo "Please check the error messages above"
    exit 1
fi

# Compile the test program
echo "Compiling test program..."
g++ -std=c++11 -I../cp5200 ../test_cp5200.cpp -L. -lcp5200 -o test_cp5200

if [ $? -ne 0 ]; then
    echo "✗ Test compilation failed!"
    echo "Please check the error messages above"
    exit 1
fi

# Check if all compilation was successful
echo "✓ All compilation successful!"
echo "Build successful!"
echo ""
echo "Files created:"
echo "  - libcp5200.a (static library)"
echo "  - libcp5200.so (shared library)"
echo "  - simple_example (example program)"
echo "  - test_cp5200 (test program)"
echo ""
echo "To test network connectivity first:"
echo "  python3 ../test_network.py"
echo ""
echo "To run the example:"
echo "  ./simple_example"
echo ""
echo "Note: No sudo needed for network communication"
echo ""
echo "To install the library system-wide:"
echo "  sudo cp libcp5200.a /usr/local/lib/"
echo "  sudo cp libcp5200.so /usr/local/lib/"
echo "  sudo cp ../cp5200/cp5200.h /usr/local/include/"
echo "  sudo ldconfig"

cd ..
