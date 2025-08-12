#include <iostream>
#include <cstring>
#include <unistd.h>
#include "cp5200.h"

int main() {
    std::cout << "=== CP5200 Display Debug Program ===" << std::endl;
    
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
    
    // Step 5: Split display into windows first (required before sending text)
    std::cout << "\n5. Splitting display into 2 windows..." << std::endl;
    int winConfig[8] = {0, 1, 0, 64, 64, 64, 0, 128};
    int result = SplitWindow(2, winConfig, 8);
    std::cout << "SplitWindow result: " << result << std::endl;
    
    if (result != 0) {
        std::cout << "ERROR: Failed to split display windows!" << std::endl;
        std::cout << "This is required before sending text. Check your display connection." << std::endl;
        return 1;
    }
    
    // Step 6: Wait a moment for display to process
    std::cout << "\n6. Waiting 2 seconds for display to process..." << std::endl;
    sleep(2);
    
    // Step 7: Send simple text
    std::cout << "\n7. Sending simple text 'TEST'..." << std::endl;
    result = SendText(0, (char*)"TEST", 0xFF0000, 16, 1, 0, 10, 0);
    std::cout << "SendText result: " << result << std::endl;
    
    if (result != 0) {
        std::cout << "ERROR: Failed to send text!" << std::endl;
        std::cout << "Error code: " << result << std::endl;
        return 1;
    }
    
    // Step 8: Wait and send another text
    std::cout << "\n8. Waiting 3 seconds..." << std::endl;
    sleep(3);
    
    std::cout << "\n9. Sending 'HELLO'..." << std::endl;
    result = SendText(0, (char*)"HELLO", 0x00FF00, 14, 1, 0, 8, 1);
    std::cout << "SendText result: " << result << std::endl;
    
    // Step 9: Test brightness control
    std::cout << "\n10. Setting brightness to 20..." << std::endl;
    result = BrightnessControl(0, 20);
    std::cout << "BrightnessControl result: " << result << std::endl;
    
    // Step 10: Sync time
    std::cout << "\n11. Syncing time..." << std::endl;
    result = SyncTime();
    std::cout << "SyncTime result: " << result << std::endl;
    
    std::cout << "\n=== Debug Program Complete ===" << std::endl;
    std::cout << "Check your LED display for output!" << std::endl;
    
    if (result == 0) {
        std::cout << "✓ All operations completed successfully!" << std::endl;
    } else {
        std::cout << "⚠ Some operations had issues. Check the error codes above." << std::endl;
    }
    
    return 0;
}
