#include <iostream>
#include <cstring>
#include <unistd.h>
#include "cp5200.h"

int main() {
    std::cout << "=== CP5200 Display Fix Program ===" << std::endl;
    
    // Step 1: Initialize and get version
    std::cout << "\n1. Getting library version..." << std::endl;
    _get_cp5200_version();
    
    // Step 2: Enable debug mode
    std::cout << "\n2. Enabling debug mode..." << std::endl;
    _set_cp5200_debug();
    
    // Step 3: Set TCP/IP mode
    std::cout << "\n3. Setting TCP/IP communication mode..." << std::endl;
    _set_cp5200_send_mode(0);
    
    // Step 4: Set IP address
    std::cout << "\n4. Setting IP address to 192.168.1.222:5200..." << std::endl;
    _set_cp5200_ipcomm((char*)"192.168.1.222", 5200);
    
    // Step 5: Clear display first (reset to default state)
    std::cout << "\n5. Clearing display..." << std::endl;
    int result = SendText(0, (char*)"", 0xFFFFFF, 16, 1, 0, 1, 0);
    std::cout << "Clear display result: " << result << std::endl;
    
    // Step 6: Wait for display to reset
    std::cout << "\n6. Waiting 3 seconds for display reset..." << std::endl;
    sleep(3);
    
    // Step 7: Split display into windows (REQUIRED)
    std::cout << "\n7. Splitting display into 2 windows..." << std::endl;
    int winConfig[8] = {0, 1, 0, 64, 64, 64, 0, 128};
    result = SplitWindow(2, winConfig, 8);
    std::cout << "SplitWindow result: " << result << std::endl;
    
    if (result != 0) {
        std::cout << "ERROR: Failed to split display windows!" << std::endl;
        std::cout << "This is required before sending text. Check your display connection." << std::endl;
        return 1;
    }
    
    // Step 8: Wait for window configuration to take effect
    std::cout << "\n8. Waiting 2 seconds for window configuration..." << std::endl;
    sleep(2);
    
    // Step 9: Send simple text with basic parameters
    std::cout << "\n9. Sending simple text 'TEST'..." << std::endl;
    result = SendText(0, (char*)"TEST", 0xFF0000, 16, 1, 0, 10, 0);
    std::cout << "SendText result: " << result << std::endl;
    
    if (result != 0) {
        std::cout << "ERROR: Failed to send text!" << std::endl;
        std::cout << "Error code: " << result << std::endl;
        return 1;
    }
    
    // Step 10: Wait and check if text appears
    std::cout << "\n10. Waiting 5 seconds to see if text appears..." << std::endl;
    sleep(5);
    
    // Step 11: Send another text with different parameters
    std::cout << "\n11. Sending 'HELLO'..." << std::endl;
    result = SendText(0, (char*)"HELLO", 0x00FF00, 14, 1, 0, 8, 1);
    std::cout << "SendText result: " << result << std::endl;
    
    // Step 12: Wait and check again
    std::cout << "\n12. Waiting 5 seconds to see if text appears..." << std::endl;
    sleep(5);
    
    // Step 13: Try sending to window 1 instead of 0
    std::cout << "\n13. Trying window 1..." << std::endl;
    result = SendText(1, (char*)"WINDOW1", 0x0000FF, 16, 1, 0, 10, 0);
    std::cout << "SendText to window 1 result: " << result << std::endl;
    
    // Step 14: Wait and check
    std::cout << "\n14. Waiting 5 seconds to see if text appears..." << std::endl;
    sleep(5);
    
    std::cout << "\n=== Display Fix Program Complete ===" << std::endl;
    std::cout << "Check your LED display for output!" << std::endl;
    
    if (result == 0) {
        std::cout << "✓ All operations completed successfully!" << std::endl;
        std::cout << "If you still don't see text, the issue might be:" << std::endl;
        std::cout << "  - Display brightness is too low" << std::endl;
        std::cout << "  - Display is in sleep mode" << std::endl;
        std::cout << "  - Display needs physical reset" << std::endl;
    } else {
        std::cout << "⚠ Some operations had issues. Check the error codes above." << std::endl;
    }
    
    return 0;
}
