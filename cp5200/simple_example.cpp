#include <iostream>
#include <cstring>
#include "cp5200.h"

int main() {
    // Enable debug output
    _set_cp5200_debug();
    
    // Print library version
    _get_cp5200_version();
    
    // Set communication mode: 0=TCP/IP, 1=RS232, 2=RS485
    _set_cp5200_send_mode(0);  // Use TCP/IP
    
    // Set TCP/IP communication parameters
    _set_cp5200_ipcomm((char*)"192.168.1.200", 5200);
    
    // Alternative: Use RS232
    // _set_cp5200_send_mode(1);
    // _set_cp5200_rs232comm((char*)"/dev/ttyAMA0", 115200);
    
    // Sync time with the display
    std::cout << "Syncing time..." << std::endl;
    int result = SyncTime();
    if (result == 0) {
        std::cout << "Time sync successful" << std::endl;
    } else {
        std::cout << "Time sync failed with error: " << result << std::endl;
    }
    
    // Set brightness (0-31, or 255 for auto)
    std::cout << "Setting brightness..." << std::endl;
    result = BrightnessControl(0, 20);  // Set brightness to 20
    if (result == 0) {
        std::cout << "Brightness set successfully" << std::endl;
    } else {
        std::cout << "Brightness setting failed with error: " << result << std::endl;
    }
    
    // Split display into windows (example: 2 windows)
    std::cout << "Splitting display into windows..." << std::endl;
    int windowConfig[] = {0, 64, 64, 128};  // 2 windows: 0-64 and 64-128
    result = SplitWindow(2, windowConfig, 4);
    if (result == 0) {
        std::cout << "Window split successful" << std::endl;
    } else {
        std::cout << "Window split failed with error: " << result << std::endl;
    }
    
    // Send text to window 0
    std::cout << "Sending text to window 0..." << std::endl;
    result = SendText(0, (char*)"Hello Raspberry Pi!", 0xFF0000, 16, 1, 0, 5, 0);
    if (result == 0) {
        std::cout << "Text sent successfully" << std::endl;
    } else {
        std::cout << "Text sending failed with error: " << result << std::endl;
    }
    
    // Send text to window 1
    std::cout << "Sending text to window 1..." << std::endl;
    result = SendText(1, (char*)"CP5200 Library", 0x00FF00, 14, 2, 1, 3, 1);
    if (result == 0) {
        std::cout << "Text sent successfully" << std::endl;
    } else {
        std::cout << "Text sending failed with error: " << result << std::endl;
    }
    
    // Send clock display to window 0
    std::cout << "Sending clock display..." << std::endl;
    int format[] = {1, 1, 1, 1, 1, 1, 1, 1};  // All elements enabled
    int content[] = {1, 1, 1, 1, 1, 1, 1, 1}; // All content enabled
    int colors[] = {0xFF, 0xFF, 0x00};          // RGB colors
    result = SendClock(0, 10, 0, format, content, (char*)"", colors, 16);
    if (result == 0) {
        std::cout << "Clock display sent successfully" << std::endl;
    } else {
        std::cout << "Clock display failed with error: " << result << std::endl;
    }
    
    std::cout << "Example completed!" << std::endl;
    return 0;
}
