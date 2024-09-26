import ctypes

# Load the shared library
lib = ctypes.CDLL('./libgauss.so')


def lu_in_place(A):
    # Create a 2D array in Python and flatten it
    n = len(A)
    flat_array_2d = [item for row in A for item in row]

    # Convert to a ctypes array
    c_array_2d = (ctypes.c_double * len(flat_array_2d))(*flat_array_2d)

    # Define the function signature
    lib.lu_in_place.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_double))

    # Modify the array in C (e.g., add 10 to each element)
    lib.lu_in_place(n, c_array_2d)

    # Convert back to a 2D Python list
    modified_array_2d = [
        [c_array_2d[i * n + j] for j in range(n)]
        for i in range(n)
    ]
    L = [
        [modified_array_2d[i][j] for j in range(i)].append([1]).append([0 for j in range(i+1,n)])
        for i in range(n)
    ]
    return L


A = [[2.0, 3.0, -1.0],
     [4.0, 1.0, 2.0],
     [-2.0, 7.0, 2.0]];

print(lu_in_place(A))
