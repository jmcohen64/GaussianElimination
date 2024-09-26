#----------------------------------------------------------------
# File:     gauss_solve.py
#----------------------------------------------------------------
#
# Author:   Marek Rychlik (rychlik@arizona.edu)
# Date:     Thu Sep 26 10:38:32 2024
# Copying:  (C) Marek Rychlik, 2020. All rights reserved.
# 
#----------------------------------------------------------------
# A Python wrapper around the C library libgauss.so

import ctypes

# Load the shared library
lib = ctypes.CDLL('./libgauss.so')


def lu(A):
    """ Accepts a list of lists A of floats and
    it returns (L, U) - the LU-decomposition as a tuple.
    """
    # Create a 2D array in Python and flatten it
    n = len(A)
    flat_array_2d = [item for row in A for item in row]

    # Convert to a ctypes array
    c_array_2d = (ctypes.c_double * len(flat_array_2d))(*flat_array_2d)

    # Define the function signature
    lib.lu_in_place.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_double))

    # Modify the array in C (e.g., add 10 to each element)
    lib.lu_in_place(n, c_array_2d)

    # Convert back to a 2D Python list of lists
    modified_array_2d = [
        [c_array_2d[i * n + j] for j in range(n)]
        for i in range(n)
    ]

    # Extract L and U parts from A
    L = [
        [[modified_array_2d[i][j] for j in range(i)] + [1] + [0 for j in range(i+1,n)]]
        for i in range(n)
    ]
    U = [
        [ 0 for j in range(i) ] + [ modified_array_2d[i][j] for j in range(i, n) ]
        for i in range(n)
    ]

    return L, U


if __name__ == "__main__":

    A = [[2.0, 3.0, -1.0],
         [4.0, 1.0, 2.0],
         [-2.0, 7.0, 2.0]];

    L, U = lu(A)
    print(L)
    print(U)
