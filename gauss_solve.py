import ctypes

# Load the shared library
lib = ctypes.CDLL('./libgauss.so')

A = [
    [2, 3, -1],
    [4, 1, 2],
    [-2, 7, 2]
];

# def lu_in_place(A):
# Create a 2D array in Python and flatten it
n = len(A)
flat_array_2d = [item for row in A for item in row]

# Convert to a ctypes array
c_array_2d = (ctypes.c_int * len(flat_array_2d))(*flat_array_2d)

# Define the function signature
lib.lu_in_place.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))

# Modify the array in C (e.g., add 10 to each element)
lib.lu_in_place(n, c_array_2d)

# Convert back to a 2D Python list
modified_array_2d = [
    [c_array_2d[i * n + j] for j in range(cols)]
    for i in range(n)
]
    
