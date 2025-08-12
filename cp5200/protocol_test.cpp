#include <iostream>
#include <cstring>
#include <unistd.h>
#include "cp5200.h"

int main() {
    std::cout << "=== CP5200 Protocol Test ===" << std::endl;
    
    // Enable debug
    _set_cp5200_debug();
    _get_cp5200_version();
    
    // Set TCP/IP mode
    _set_cp5200_send_mode(0);
    _set_cp5200_ipcomm((char*)"192.168.1.222", 5200);
    
    std::cout << "\nTesting minimal protocol..." << std::endl;
    
    // Test 1: Send a simple ping-like command
    std::cout << "\n1. Testing basic connectivity..." << std::endl;
    
    // Try to send a minimal command - just the header
    int result = SendText(0, (char*)"", 0xFFFFFF, 16, 1, 0, 1, 0);
    std::cout << "SendText result: " << result << std::endl;
    
    if (result == 0) {
        std::cout << "✓ Basic communication working!" << std::endl;
        
        // Test 2: Try window splitting
        std::cout << "\n2. Testing window splitting..." << std::endl;
        int winConfig[8] = {0, 1, 0, 32, 32, 32, 0, 64}; // Smaller windows
        result = SplitWindow(2, winConfig, 8);
        std::cout << "SplitWindow result: " << result << std::endl;
        
        if (result == 0) {
            std::cout << "✓ Window splitting working!" << std::endl;
            
            // Test 3: Send text to window 0
            std::cout << "\n3. Testing text display..." << std::endl;
            result = SendText(0, (char*)"HI", 0xFF0000, 16, 1, 0, 5, 0);
            std::cout << "SendText result: " << result << std::endl;
            
            if (result == 0) {
                std::cout << "✓ Text sending working!" << std::endl;
                std::cout << "\n🎉 All tests passed! Check your display for 'HI' text." << std::endl;
            } else {
                std::cout << "✗ Text sending failed with code: " << result << std::endl;
            }
        } else {
            std::cout << "✗ Window splitting failed with code: " << result << std::endl;
        }
    } else {
        std::cout << "✗ Basic communication failed with code: " << result << std::endl;
    }
    
    std::cout << "\n=== Protocol Test Complete ===" << std::endl;
    return 0;
}
