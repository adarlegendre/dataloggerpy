#!/bin/bash

echo "🚀 Setting up CP5200 Display Controller on Raspberry Pi"
echo "=================================================="

# Update package list
echo "📦 Updating package list..."
sudo apt-get update

# Install build essentials
echo "🔨 Installing build essentials..."
sudo apt-get install -y build-essential g++ make

# Install Python3 and pip if not already installed
echo "🐍 Installing Python3 and pip..."
sudo apt-get install -y python3 python3-pip

# Install required Python packages
echo "📚 Installing Python dependencies..."
pip3 install argparse

# Check if cp5200 library exists
echo "🔍 Checking for cp5200 library..."
if [ -f "/usr/local/lib/libcp5200.so" ] || [ -f "/usr/lib/libcp5200.so" ]; then
    echo "✅ cp5200 library found"
else
    echo "⚠️  cp5200 library not found in standard locations"
    echo "   You may need to install it manually or specify the path"
fi

# Make the Python script executable
echo "🔧 Making Python script executable..."
chmod +x run_cp5200_display.py

# Make the setup script executable
chmod +x setup_raspberry_pi.sh

echo ""
echo "✅ Setup complete!"
echo ""
echo "📖 Next steps:"
echo "   1. Update the IP address and port in the Python script if needed"
echo "   2. Run: python3 run_cp5200_display.py --interactive"
echo "   3. Or send text directly: python3 run_cp5200_display.py --text 'Hello World!'"
echo ""
echo "🔧 If you need to install the cp5200 library manually:"
echo "   - Check the original SDK documentation"
echo "   - Or contact the manufacturer for installation instructions"
echo ""
