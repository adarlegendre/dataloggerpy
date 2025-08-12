cmake_minimum_required(VERSION 3.10)
project(CP5200_Library)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Set build type if not specified
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Compiler flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2 -Wall -Wextra -D_GNU_SOURCE")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -O0")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -O3 -DNDEBUG")

# Platform-specific settings
if(UNIX AND NOT APPLE)
    # Linux-specific settings
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
    
    # Check if we're on Raspberry Pi
    if(EXISTS "/proc/cpuinfo")
        file(READ "/proc/cpuinfo" CPUINFO)
        if(CPUINFO MATCHES "Raspberry Pi")
            message(STATUS "Detected Raspberry Pi - optimizing build")
            set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native -mtune=native")
        endif()
    endif()
endif()

# Include directories
include_directories(${CMAKE_SOURCE_DIR})

# Create the CP5200 library
add_library(cp5200 STATIC cp5200/cp5200.cpp)
add_library(cp5200_shared SHARED cp5200/cp5200.cpp)

# Set library properties
set_target_properties(cp5200 PROPERTIES
    OUTPUT_NAME cp5200
    VERSION 3.0.0
    SOVERSION 3
)

set_target_properties(cp5200_shared PROPERTIES
    OUTPUT_NAME cp5200
    VERSION 3.0.0
    SOVERSION 3
)

# Create the example executable
add_executable(simple_example simple_example.cpp)
target_link_libraries(simple_example cp5200)

# Create a test executable
add_executable(test_cp5200 test_cp5200.cpp)
target_link_libraries(test_cp5200 cp5200)

# Installation
install(TARGETS cp5200 cp5200_shared
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)

install(FILES cp5200/cp5200.h
    DESTINATION include
)

# Print installation information
message(STATUS "")
message(STATUS "Installation targets:")
message(STATUS "  make install    - Install to system directories")
message(STATUS "  sudo make install - Install to system directories (requires sudo)")
message(STATUS "")
message(STATUS "Installation locations:")
message(STATUS "  Libraries: ${CMAKE_INSTALL_PREFIX}/lib")
message(STATUS "  Headers:  ${CMAKE_INSTALL_PREFIX}/include")
message(STATUS "  Binaries: ${CMAKE_INSTALL_PREFIX}/bin")

# Create pkg-config file
configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cp5200.pc.in"
    "${CMAKE_CURRENT_BINARY_DIR}/cp5200.pc"
    @ONLY
)

install(FILES "${CMAKE_CURRENT_BINARY_DIR}/cp5200.pc"
    DESTINATION lib/pkgconfig
)

# Print configuration summary
message(STATUS "")
message(STATUS "CP5200 Library Configuration:")
message(STATUS "  Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "  C++ compiler: ${CMAKE_CXX_COMPILER}")
message(STATUS "  C++ flags: ${CMAKE_CXX_FLAGS}")
message(STATUS "  Install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "")
