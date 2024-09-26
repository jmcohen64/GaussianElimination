import ctypes

# Load the shared library
lib = ctypes.CDLL('./libgauss.so')


def gauss_solve(A, b):
    # Create a 2D array in Python and flatten it
    rows, cols = 3, 3
    array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat_array_2d = [item for row in array_2d for item in row]

    # Convert to a ctypes array
    c_array_2d = (ctypes.c_int * len(flat_array_2d))(*flat_array_2d)

    # Define the function signature
    lib.modify_2d_array.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int)

    # Modify the array in C (e.g., add 10 to each element)
    lib.modify_2d_array(c_array_2d, rows, cols, 10)

    # Convert back to a 2D Python list
    modified_array_2d = [
        [c_array_2d[i * cols + j] for j in range(cols)]
        for i in range(rows)
    ]
    
