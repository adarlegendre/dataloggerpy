# 🐍 CP5200 Python Builder for Raspberry Pi

## **Overview**

This is a **pure Python implementation** of the CP5200 library builder that automatically:
- ✅ Detects Raspberry Pi environment
- ✅ Compiles CP5200 library for ARM architecture  
- ✅ Sets proper file permissions
- ✅ Places libraries in all locations where test scripts expect them
- ✅ Verifies everything works automatically

## **🚀 Quick Start**

### **Step 1: Navigate to SDK Directory**
```bash
cd cp5200Original
```

### **Step 2: Run the Python Builder**
```bash
python3 build_cp5200_python.py
```

### **Step 3: Test Your Library**
```bash
cd ..
python3 test_czech_plates_unified.py
```

## **🔧 What the Python Builder Does**

### **1. Environment Detection**
- Automatically detects if running on Raspberry Pi
- Shows system information (platform, architecture, Python version)
- Applies ARM-specific optimizations

### **2. Prerequisites Check**
- Verifies `g++`, `ar`, and `ranlib` are available
- Suggests installation commands if tools are missing
- Ensures build environment is ready

### **3. Source File Validation**
- Checks if `cp5200.cpp` and `cp5200.h` exist
- Shows file sizes and validates source integrity
- Ensures all required files are present

### **4. Compilation Process**
- Creates clean build directory
- Compiles with ARM-specific flags (`-march=native`, `-mtune=native`)
- Uses C++11 standard with position-independent code (`-fPIC`)
- Shows detailed compilation output

### **5. Library Creation**
- Creates static library (`.a`) using `ar` and `ranlib`
- Creates shared library (`.so`) for better Python compatibility
- Handles both library types automatically

### **6. Permission Management**
- Sets proper read permissions for all users
- Ensures libraries are accessible by Python scripts
- Handles permission errors gracefully

### **7. Automatic Library Placement**
The builder places libraries in **multiple strategic locations**:

| Priority | Location | Purpose |
|----------|----------|---------|
| **Highest** | `./cp5200Original/` | Current SDK directory |
| **High** | `./` (root project) | Main project directory |
| **Medium** | `./cp5200Original/dist/Release/GNU-Linux/` | Original dist structure |
| **Optional** | `/usr/local/lib/` | System-wide access |

### **8. Verification & Testing**
- Verifies libraries are discoverable in all locations
- Tests library loading with Python ctypes
- Confirms everything works before completion

## **📁 File Structure After Building**

```
dataloggerpy/
├── libcp5200.so          ← Builder places here automatically
├── libcp5200.a           ← Builder places here automatically
├── cp5200Original/
│   ├── libcp5200.so      ← Builder places here automatically
│   ├── libcp5200.a       ← Builder places here automatically
│   ├── build_raspberry_pi/  ← Build artifacts
│   └── dist/Release/GNU-Linux/
│       ├── libcp5200.so  ← Builder places here automatically
│       └── libcp5200.a   ← Builder places here automatically
└── test_czech_plates_unified.py
```

## **🎯 Why This Approach is Superior**

### **✅ Advantages of Python Builder**
- **Cross-platform compatible** (works on any system with Python)
- **Better error handling** with detailed error messages
- **Automatic permission management** 
- **Intelligent file placement** in multiple locations
- **Built-in verification** that libraries actually work
- **No shell script dependencies** or bash-specific syntax

### **✅ Perfect Integration**
- **Zero manual file moving** required
- **Test scripts find libraries automatically**
- **Multiple fallback locations** ensure reliability
- **Permission issues resolved automatically**

## **🔍 Troubleshooting**

### **Common Issues & Solutions**

#### **1. Missing Build Tools**
```bash
# Install required tools
sudo apt update
sudo apt install build-essential
```

#### **2. Permission Denied**
```bash
# The Python builder handles this automatically
# If manual fix needed:
chmod +r libcp5200.*
```

#### **3. Library Not Found**
```bash
# Verify libraries were placed correctly
ls -la libcp5200.*
ls -la cp5200Original/libcp5200.*
```

#### **4. Architecture Mismatch**
```bash
# Check your architecture
uname -m
# Should show: armv7l or aarch64 for Raspberry Pi
```

## **🚀 Advanced Usage**

### **Custom Build Options**
The Python builder automatically detects your environment, but you can modify the source if needed:

```python
# In build_cp5200_python.py, modify these lines:
compile_cmd = [
    'g++', '-c', '-O2', '-std=c++11', '-fPIC',
    '-march=native', '-mtune=native',  # ← ARM optimization
    '-D__ARM_ARCH',                    # ← ARM define
    '-I', str(self.current_dir),
    str(self.source_files['cpp']),
    '-o', str(self.build_dir / 'cp5200.o')
]
```

### **Adding Custom Compiler Flags**
```python
# Add custom flags like:
compile_cmd.extend(['-Wall', '-Wextra', '-DDEBUG'])
```

## **📋 Complete Workflow**

1. **Copy files to Raspberry Pi**
2. **Navigate to SDK directory**: `cd cp5200Original`
3. **Run Python builder**: `python3 build_cp5200_python.py`
4. **Wait for completion** (shows progress and results)
5. **Go to root directory**: `cd ..`
6. **Run test**: `python3 test_czech_plates_unified.py`
7. **Enjoy automatic library discovery!**

## **🎉 Result**

After running the Python builder:
- ✅ **Libraries compiled for ARM architecture**
- ✅ **Proper permissions set automatically**
- ✅ **Files placed in all necessary locations**
- ✅ **Test scripts work without modification**
- ✅ **Zero manual configuration required**

The Python builder gives you a **professional-grade build system** that handles everything automatically, just like the bash script but with better error handling, cross-platform compatibility, and intelligent file management!
