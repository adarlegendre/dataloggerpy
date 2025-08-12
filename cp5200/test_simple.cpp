#include <iostream>
#include <cstring>
#include "cp5200.h"

int main() {
    std::cout << "Testing SendText function..." << std::endl;
    
    // Enable debug output
    _set_cp5200_debug();
    
    // Print library version
    _get_cp5200_version();
    
    // Set communication mode: 0=TCP/IP, 1=RS232, 2=RS485
    _set_cp5200_send_mode(0);  // Use TCP/IP
    
    // Set TCP/IP communication parameters
    _set_cp5200_ipcomm((char*)"192.168.1.222", 5200);
    
    // Test 1: Simple alphanumeric
    std::cout << "Test 1: Simple alphanumeric..." << std::endl;
    int result = SendText(0, (char*)"aaa", 0xFF0000, 16, 1, 0, 5, 0);
    if (result == 0) {
        std::cout << "✓ Test 1 passed" << std::endl;
    } else {
        std::cout << "✗ Test 1 failed with error: " << result << std::endl;
    }
    
    // Test 2: Numbers
    std::cout << "Test 2: Numbers..." << std::endl;
    result = SendText(0, (char*)"123", 0x00FF00, 14, 1, 0, 3, 1);
    if (result == 0) {
        std::cout << "✓ Test 2 passed" << std::endl;
    } else {
        std::cout << "✗ Test 2 failed with error: " << result << std::endl;
    }
    
    // Test 3: Czech number plate format
    std::cout << "Test 3: Czech number plate..." << std::endl;
    result = SendText(0, (char*)"1A2 3456", 0x0000FF, 12, 1, 0, 4, 0);
    if (result == 0) {
        std::cout << "✓ Test 3 passed" << std::endl;
    } else {
        std::cout << "✗ Test 3 failed with error: " << result << std::endl;
    }
    
    // Test 4: Another Czech number plate
    std::cout << "Test 4: Another Czech plate..." << std::endl;
    result = SendText(0, (char*)"ABC 1234", 0xFFFF00, 16, 1, 0, 5, 0);
    if (result == 0) {
        std::cout << "✓ Test 4 passed" << std::endl;
    } else {
        std::cout << "✗ Test 4 failed with error: " << result << std::endl;
    }
    
    // Test 5: Mixed short text
    std::cout << "Test 5: Mixed short text..." << std::endl;
    result = SendText(0, (char*)"OK", 0xFF00FF, 14, 1, 0, 3, 1);
    if (result == 0) {
        std::cout << "✓ Test 5 passed" << std::endl;
    } else {
        std::cout << "✗ Test 5 failed with error: " << result << std::endl;
    }
    
    std::cout << "All tests completed!" << std::endl;
    return 0;
}
