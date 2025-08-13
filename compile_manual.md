# 🍓 Manual Compilation for Raspberry Pi

## **Quick Fix for "Invalid ELF Header" Error**

The error occurs because the existing library was compiled for a different architecture (likely x86_64) but you're running on Raspberry Pi (ARM).

## **🔧 Solution: Recompile on Raspberry Pi**

### **Step 1: On Your Raspberry Pi, Navigate to the SDK Directory**
```bash
cd cp5200Original
```

### **Step 2: Create a Build Directory**
```bash
mkdir -p build_raspberry_pi
cd build_raspberry_pi
```

### **Step 3: Compile for ARM Architecture**
```bash
# Compile the source file for ARM
g++ -c -O2 -std=c++11 -fPIC \
    -march=native \
    -mtune=native \
    -I../ \
    ../cp5200.cpp \
    -o cp5200.o
```

### **Step 4: Create the Library**
```bash
# Create static library (.a)
ar rcs libcp5200.a cp5200.o
ranlib libcp5200.a

# Create shared library (.so) - recommended for Python
g++ -shared -fPIC -o libcp5200.so cp5200.o
```

### **Step 5: Copy Libraries to Parent Directory**
```bash
cp libcp5200.* ../
cd ..
```

### **Step 6: Test the New Library**
```bash
python3 ../test_czech_plates_unified.py
```

## **🚀 One-Command Solution**

If you have the build script:
```bash
chmod +x build_for_raspberry_pi.sh
./build_for_raspberry_pi.sh
```

## **🔍 Why This Happens**

1. **Architecture Mismatch**: x86_64 vs ARM
2. **Cross-Platform Issues**: Windows/Linux x86 → Raspberry Pi ARM
3. **Library Format**: Different binary formats between architectures

## **✅ Expected Result**

After recompiling, you should see:
- `libcp5200.a` (static library for ARM)
- `libcp5200.so` (shared library for ARM)
- No more "invalid ELF header" errors

## **📋 Verification**

Check the new library works:
```bash
# Test library loading
python3 -c "import ctypes; lib = ctypes.CDLL('./libcp5200.so'); print('✓ Library loaded successfully')"
```

## **🎯 Alternative: Use Shared Library**

The `.so` file is often more reliable than `.a` files for Python ctypes:
- More compatible across systems
- Better error handling
- Standard for dynamic linking

## **🆘 If Still Having Issues**

1. **Check architecture**: `uname -m` (should show `armv7l` or `aarch64`)
2. **Verify compiler**: `g++ --version`
3. **Check dependencies**: `ldd libcp5200.so`
4. **Rebuild from scratch**: Delete build directory and start over

This should resolve your "invalid ELF header" error!
