#include <iostream>
#include <cstring>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <fcntl.h>
#include "cp5200.h"

int main() {
    std::cout << "=== CP5200 Timeout Test ===" << std::endl;
    
    // Enable debug
    _set_cp5200_debug();
    _get_cp5200_version();
    
    // Set TCP/IP mode
    _set_cp5200_send_mode(0);
    _set_cp5200_ipcomm((char*)"192.168.1.222", 5200);
    
    std::cout << "\nTesting with timeout handling..." << std::endl;
    
    // Test 1: Try to send text with a timeout
    std::cout << "\n1. Testing SendText with timeout expectation..." << std::endl;
    
    // Set a timer for this operation
    alarm(10); // 10 second timeout
    
    int result = SendText(0, (char*)"TEST", 0xFF0000, 16, 1, 0, 10, 0);
    
    // Cancel the alarm
    alarm(0);
    
    std::cout << "SendText result: " << result << std::endl;
    
    if (result == 0) {
        std::cout << "✓ Text sent successfully!" << std::endl;
    } else {
        std::cout << "✗ Text sending failed with code: " << result << std::endl;
    }
    
    // Test 2: Try window splitting
    std::cout << "\n2. Testing window splitting..." << std::endl;
    int winConfig[8] = {0, 1, 0, 32, 32, 32, 0, 64};
    result = SplitWindow(2, winConfig, 8);
    std::cout << "SplitWindow result: " << result << std::endl;
    
    std::cout << "\n=== Timeout Test Complete ===" << std::endl;
    std::cout << "If the program didn't hang, the timeout handling worked!" << std::endl;
    
    return 0;
}
