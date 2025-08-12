#!/bin/bash

# Test compilation script for CP5200 library
# This tests if the compilation errors are fixed before running the full build

echo "Testing CP5200 library compilation..."
echo "====================================="

# Test basic compilation
echo "Testing basic compilation..."
g++ -c -O2 -std=c++11 -fPIC -D_GNU_SOURCE cp5200/cp5200.cpp -o test_cp5200.o

if [ $? -eq 0 ]; then
    echo "✓ Basic compilation successful"
    rm -f test_cp5200.o
else
    echo "✗ Basic compilation failed"
    echo "Please check the error messages above"
    exit 1
fi

# Test with warnings
echo "Testing compilation with warnings enabled..."
g++ -c -O2 -std=c++11 -fPIC -D_GNU_SOURCE -Wall -Wextra cp5200/cp5200.cpp -o test_cp5200.o

if [ $? -eq 0 ]; then
    echo "✓ Compilation with warnings successful"
    rm -f test_cp5200.o
else
    echo "✗ Compilation with warnings failed"
    echo "Please check the error messages above"
    exit 1
fi

echo ""
echo "🎉 All compilation tests passed!"
echo "You can now run the full build:"
echo "  ./build_raspberry_pi.sh"
