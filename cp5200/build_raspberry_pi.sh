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
g++ -std=c++11 -I../cp5200 ../simple_example.cpp -L. -lcp5200 -Wl,-rpath,. -o simple_example

if [ $? -ne 0 ]; then
    echo "✗ Example compilation failed!"
    echo "Please check the error messages above"
    exit 1
fi

# Compile the test program
echo "Compiling test program..."
g++ -std=c++11 -I../cp5200 ../test_cp5200.cpp -L. -lcp5200 -Wl,-rpath,. -o test_cp5200

if [ $? -ne 0 ]; then
    echo "✗ Test compilation failed!"
    echo "Please check the error messages above"
    exit 1
fi

# Compile the simple test program
echo "Compiling simple test program..."
g++ -std=c++11 -I../cp5200 ../test_simple.cpp -L. -lcp5200 -Wl,-rpath,. -o test_simple

if [ $? -ne 0 ]; then
    echo "✗ Simple test compilation failed!"
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
echo "  - test_simple (simple test program)"
echo ""
echo "Installing library system-wide..."
echo "This requires sudo privileges to copy files to system directories."

# Install the library system-wide
sudo cp libcp5200.a /usr/local/lib/
sudo cp libcp5200.so /usr/local/lib/
sudo cp ../cp5200/cp5200.h /usr/local/include/

# Update the dynamic linker cache
echo "Updating dynamic linker cache..."
sudo ldconfig

echo ""
echo "✓ Library installed system-wide!"
echo "  - Static library: /usr/local/lib/libcp5200.a"
echo "  - Shared library: /usr/local/lib/libcp5200.so"
echo "  - Header file: /usr/local/include/cp5200.h"
echo ""
echo "Now you can run the examples from anywhere:"
echo "  ./simple_example"
echo "  ./test_cp5200"
echo "  python3 ../quick_start.py"
echo ""
echo "To test network connectivity first:"
echo "  python3 ../test_network.py"

cd ..
