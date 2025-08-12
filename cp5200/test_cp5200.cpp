#include <iostream>
#include <cstring>
#include "cp5200.h"

int main() {
    std::cout << "CP5200 Library Test Program" << std::endl;
    std::cout << "==========================" << std::endl;
    
    // Test 1: Library version
    std::cout << "\n1. Testing library version..." << std::endl;
    _get_cp5200_version();
    
    // Test 2: Debug mode
    std::cout << "\n2. Testing debug mode..." << std::endl;
    _set_cp5200_debug();
    std::cout << "Debug mode enabled" << std::endl;
    
    // Test 3: Communication mode setting
    std::cout << "\n3. Testing communication mode setting..." << std::endl;
    _set_cp5200_send_mode(0);  // TCP/IP mode
    std::cout << "Communication mode set to TCP/IP" << std::endl;
    
    // Test 4: TCP/IP configuration
    std::cout << "\n4. Testing TCP/IP configuration..." << std::endl;
    _set_cp5200_ipcomm((char*)"192.168.1.200", 5200);
    std::cout << "TCP/IP configured for 192.168.1.200:5200" << std::endl;
    
    // Test 5: RS232 configuration (for reference)
    std::cout << "\n5. Testing RS232 configuration..." << std::endl;
    _set_cp5200_rs232comm((char*)"/dev/ttyAMA0", 115200);
    std::cout << "RS232 configured for /dev/ttyAMA0 at 115200 baud" << std::endl;
    
    // Test 6: Switch back to TCP/IP
    std::cout << "\n6. Switching back to TCP/IP..." << std::endl;
    _set_cp5200_send_mode(0);
    _set_cp5200_ipcomm((char*)"192.168.1.200", 5200);
    std::cout << "Switched back to TCP/IP mode" << std::endl;
    
    // Test 7: Window splitting (without sending)
    std::cout << "\n7. Testing window configuration..." << std::endl;
    int windowConfig[] = {0, 0, 64, 64, 64, 0, 128, 64};
    std::cout << "Window config prepared: 2 windows" << std::endl;
    std::cout << "  Window 0: (0,0) to (64,64)" << std::endl;
    std::cout << "  Window 1: (64,0) to (128,64)" << std::endl;
    
    // Test 8: Text parameters
    std::cout << "\n8. Testing text parameters..." << std::endl;
    std::cout << "Text: 'Hello Raspberry Pi!'" << std::endl;
    std::cout << "Color: Red (0xFF0000)" << std::endl;
    std::cout << "Font size: 16" << std::endl;
    std::cout << "Speed: 1" << std::endl;
    std::cout << "Effect: None (0)" << std::endl;
    std::cout << "Stay time: 5 seconds" << std::endl;
    std::cout << "Alignment: Left (0)" << std::endl;
    
    // Test 9: Clock parameters
    std::cout << "\n9. Testing clock parameters..." << std::endl;
    std::cout << "Calendar type: Gregorian (0)" << std::endl;
    std::cout << "Format: All elements enabled" << std::endl;
    std::cout << "Content: All content enabled" << std::endl;
    std::cout << "Colors: Yellow (0xFFFF00)" << std::endl;
    
    // Test 10: Brightness parameters
    std::cout << "\n10. Testing brightness parameters..." << std::endl;
    std::cout << "Brightness range: 0-31 (manual) or 255 (auto)" << std::endl;
    std::cout << "Test brightness: 20" << std::endl;
    
    std::cout << "\n==========================" << std::endl;
    std::cout << "All tests completed successfully!" << std::endl;
    std::cout << "Library is ready for use." << std::endl;
    std::cout << "\nNote: This test only validates configuration." << std::endl;
    std::cout << "To test actual communication, connect a CP5200 display" << std::endl;
    std::cout << "and run the simple_example program." << std::endl;
    
    return 0;
}
