/*
 * CP5200 LED Display Library Test Suite
 * Tests all major functions of the CP5200 library
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <cp5200.h>

// Test configuration
#define TEST_IP_ADDRESS "192.168.1.100"
#define TEST_PORT 5200
#define TEST_SERIAL_PORT "/dev/ttyAMA0"
#define TEST_BAUD_RATE 115200

// Test results
int tests_passed = 0;
int tests_failed = 0;

void print_test_result(const char* test_name, int result) {
    if (result == 0) {
        printf("✓ %s: PASSED\n", test_name);
        tests_passed++;
    } else {
        printf("✗ %s: FAILED (error code: %d)\n", test_name, result);
        tests_failed++;
    }
}

void print_summary() {
    printf("\n" "=" * 50 "\n");
    printf("TEST SUMMARY\n");
    printf("=" * 50 "\n");
    printf("Tests passed: %d\n", tests_passed);
    printf("Tests failed: %d\n", tests_failed);
    printf("Total tests: %d\n", tests_passed + tests_failed);
    printf("=" * 50 "\n");
}

// Test 1: Library version
int test_version() {
    printf("\n--- Testing Library Version ---\n");
    _get_cp5200_version();
    return 0; // Version function doesn't return error codes
}

// Test 2: Debug mode
int test_debug_mode() {
    printf("\n--- Testing Debug Mode ---\n");
    _set_cp5200_debug();
    return 0;
}

// Test 3: Network communication setup
int test_network_setup() {
    printf("\n--- Testing Network Setup ---\n");
    _set_cp5200_ipcomm(TEST_IP_ADDRESS, TEST_PORT);
    _set_cp5200_send_mode(0); // TCP/IP mode
    return 0;
}

// Test 4: Serial communication setup
int test_serial_setup() {
    printf("\n--- Testing Serial Setup ---\n");
    _set_cp5200_rs232comm(TEST_SERIAL_PORT, TEST_BAUD_RATE);
    _set_cp5200_send_mode(1); // RS-232 mode
    return 0;
}

// Test 5: Time synchronization
int test_sync_time() {
    printf("\n--- Testing Time Synchronization ---\n");
    int result = SyncTime();
    print_test_result("Time Sync", result);
    return result;
}

// Test 6: Brightness control
int test_brightness_control() {
    printf("\n--- Testing Brightness Control ---\n");
    
    // Test getting current brightness
    int current_brightness = BrightnessControl(0, 0);
    printf("Current brightness: %d\n", current_brightness);
    
    // Test setting brightness to 50%
    int result = BrightnessControl(1, 15);
    print_test_result("Set Brightness", result);
    
    // Test setting auto brightness
    result = BrightnessControl(1, 255);
    print_test_result("Set Auto Brightness", result);
    
    return result;
}

// Test 7: Text display
int test_text_display() {
    printf("\n--- Testing Text Display ---\n");
    
    // Test basic text
    int result = SendText(0, "Hello CP5200!", 1, 16, 5, 1, 10, 0);
    print_test_result("Send Text - Basic", result);
    
    // Test with different parameters
    result = SendText(1, "Test Message", 2, 20, 3, 2, 15, 1);
    print_test_result("Send Text - Advanced", result);
    
    // Test UTF-8 text (if supported)
    result = SendText(2, "CP5200 Test", 3, 18, 4, 1, 12, 2);
    print_test_result("Send Text - UTF8", result);
    
    return result;
}

// Test 8: Picture display
int test_picture_display() {
    printf("\n--- Testing Picture Display ---\n");
    
    // Test with a sample GIF file (create a dummy file for testing)
    FILE* test_file = fopen("test_image.gif", "wb");
    if (test_file) {
        // Write minimal GIF header
        unsigned char gif_header[] = {
            0x47, 0x49, 0x46, 0x38, 0x39, 0x61, // GIF89a
            0x01, 0x00, 0x01, 0x00, 0x80, 0x00, 0x00, // 1x1 pixel
            0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x21, 0xF9, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x02, 0x02, 0x44, 0x01, 0x00, 0x3B
        };
        fwrite(gif_header, 1, sizeof(gif_header), test_file);
        fclose(test_file);
        
        int result = SendPicture(0, 0, 0, "test_image.gif", 5, 1, 10);
        print_test_result("Send Picture", result);
        
        // Clean up test file
        unlink("test_image.gif");
        return result;
    } else {
        printf("Could not create test image file\n");
        return -1;
    }
}

// Test 9: Clock display
int test_clock_display() {
    printf("\n--- Testing Clock Display ---\n");
    
    // Format array: multiline display
    int format[] = {1, 0, 0, 0, 0, 0, 0, 0};
    
    // Content array: show date and time
    int content[] = {1, 1, 1, 0, 0, 0, 0, 0};
    
    // Colors: white
    int colors[] = {255, 255, 255};
    
    int result = SendClock(0, 30, 0, format, content, "Current Time", colors, 16);
    print_test_result("Send Clock", result);
    
    return result;
}

// Test 10: Window splitting
int test_window_splitting() {
    printf("\n--- Testing Window Splitting ---\n");
    
    // Test window configuration
    int window_config[] = {0, 1, 2, 3};
    int result = SplitWindow(0, window_config, 4);
    print_test_result("Split Window", result);
    
    return result;
}

// Test 11: Communication mode switching
int test_communication_modes() {
    printf("\n--- Testing Communication Modes ---\n");
    
    // Test TCP/IP mode
    _set_cp5200_send_mode(0);
    printf("Switched to TCP/IP mode\n");
    
    // Test RS-232 mode
    _set_cp5200_send_mode(1);
    printf("Switched to RS-232 mode\n");
    
    // Test RS-485 mode
    _set_cp5200_send_mode(2);
    printf("Switched to RS-485 mode\n");
    
    return 0;
}

// Test 12: Error handling
int test_error_handling() {
    printf("\n--- Testing Error Handling ---\n");
    
    // Test with invalid parameters
    int result = SendText(-1, "Invalid Window", 1, 16, 5, 1, 10, 0);
    printf("Invalid window test result: %d (expected error)\n", result);
    
    result = SendText(0, "", 1, 16, 5, 1, 10, 0);
    printf("Empty text test result: %d\n", result);
    
    return 0;
}

// Test 13: Performance test
int test_performance() {
    printf("\n--- Testing Performance ---\n");
    
    clock_t start, end;
    double cpu_time_used;
    
    start = clock();
    
    // Send multiple text messages
    for (int i = 0; i < 10; i++) {
        char message[50];
        sprintf(message, "Performance Test %d", i);
        SendText(i % 4, message, 1, 16, 5, 1, 5, 0);
        usleep(100000); // 100ms delay
    }
    
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    
    printf("Performance test completed in %.3f seconds\n", cpu_time_used);
    return 0;
}

// Main test runner
int main() {
    printf("CP5200 LED Display Library Test Suite\n");
    printf("=" * 50 "\n");
    printf("This test suite will test all major functions of the CP5200 library\n");
    printf("Make sure your CP5200 display controller is connected and configured\n");
    printf("=" * 50 "\n");
    
    // Run all tests
    test_version();
    test_debug_mode();
    test_network_setup();
    test_serial_setup();
    test_sync_time();
    test_brightness_control();
    test_text_display();
    test_picture_display();
    test_clock_display();
    test_window_splitting();
    test_communication_modes();
    test_error_handling();
    test_performance();
    
    // Print summary
    print_summary();
    
    // Return appropriate exit code
    if (tests_failed == 0) {
        printf("All tests passed! CP5200 library is working correctly.\n");
        return 0;
    } else {
        printf("Some tests failed. Please check your configuration.\n");
        return 1;
    }
}
