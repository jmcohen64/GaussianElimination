import ctypes

# Load the shared library
lib = ctypes.CDLL('./libfoo.so')

# Define the function signature
lib.foo_add.argtypes = (ctypes.c_int, ctypes.c_int)
lib.foo_add.restype = ctypes.c_int

# Call the function
result = lib.foo_add(5, 7)
print(result)  # Outputs: 12
