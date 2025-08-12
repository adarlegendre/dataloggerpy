#include <iostream>
#include "cp5200.h"

int main() {
    std::cout << "Testing CP5200 LED Display Library..." << std::endl;
    
    // Test version function
    _get_cp5200_version();
    
    // Test debug mode
    _set_cp5200_debug();
    
    // Test IP communication setup
    _set_cp5200_ipcomm("192.168.1.100", 5200);
    _set_cp5200_send_mode(0); // TCP/IP mode
    
    std::cout << "Library functions loaded successfully!" << std::endl;
    std::cout << "You can now use the library with your LED display." << std::endl;
    
    return 0;
}
