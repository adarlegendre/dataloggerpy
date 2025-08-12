#include <iostream>
#include <cstring>
#include <unistd.h>
#include "cp5200.h"

int main() {
    std::cout << "=== CP5200 Simple Display Test ===" << std::endl;
    
    // Enable debug
    _set_cp5200_debug();
    _get_cp5200_version();
    
    // Set TCP/IP mode
    _set_cp5200_send_mode(0);
    _set_cp5200_ipcomm((char*)"192.168.1.222", 5200);
    
    std::cout << "\nTesting different approaches..." << std::endl;
    
    // Approach 1: Try without window splitting
    std::cout << "\n1. Trying to send text without window splitting..." << std::endl;
    int result = SendText(0, (char*)"TEST1", 0xFF0000, 16, 1, 0, 10, 0);
    std::cout << "Result: " << result << std::endl;
    sleep(3);
    
    // Approach 2: Try with window splitting
    std::cout << "\n2. Splitting display into windows..." << std::endl;
    int winConfig[8] = {0, 1, 0, 64, 64, 64, 0, 128};
    result = SplitWindow(2, winConfig, 8);
    std::cout << "SplitWindow result: " << result << std::endl;
    sleep(2);
    
    if (result == 0) {
        std::cout << "\n3. Sending text after window split..." << std::endl;
        result = SendText(0, (char*)"TEST2", 0x00FF00, 16, 1, 0, 10, 0);
        std::cout << "Result: " << result << std::endl;
        sleep(3);
        
        std::cout << "\n4. Trying window 1..." << std::endl;
        result = SendText(1, (char*)"TEST3", 0x0000FF, 16, 1, 0, 10, 0);
        std::cout << "Result: " << result << std::endl;
        sleep(3);
    }
    
    // Approach 3: Try different text parameters
    std::cout << "\n5. Trying different text parameters..." << std::endl;
    result = SendText(0, (char*)"TEST4", 0xFFFFFF, 20, 1, 0, 15, 0);
    std::cout << "Result: " << result << std::endl;
    sleep(3);
    
    std::cout << "\n=== Test Complete ===" << std::endl;
    std::cout << "Check your display for any output!" << std::endl;
    
    return 0;
}
