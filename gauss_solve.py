#----------------------------------------------------------------
# File:     gauss_solve.py
#----------------------------------------------------------------
#
# Author:   Marek Rychlik (rychlik@arizona.edu)
# Date:     Thu Sep 26 10:38:32 2024
# Copying:  (C) Marek Rychlik, 2020. All rights reserved.
# 
#----------------------------------------------------------------
# A Python wrapper module around the C library libgauss.so

import ctypes

gauss_library_path = './libgauss.so'

def unpack(A):
    """ Extract L and U parts from A, fill with 0's and 1's """
    n = len(A)
    L = [[A[i][j] for j in range(i)] + [1] + [0 for j in range(i+1, n)]
         for i in range(n)]

    U = [[0 for j in range(i)] + [A[i][j] for j in range(i, n)]
         for i in range(n)]

    return L, U

def lu_c(A):
    """ Accepts a list of lists A of floats and
    it returns (L, U) - the LU-decomposition as a tuple.
    """
    # Load the shared library
    lib = ctypes.CDLL(gauss_library_path)

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

    # Extract L and U parts from A, fill with 0's and 1's
    return unpack(modified_array_2d)

def lu_python(A):
    n = len(A)
    for k in range(n):
        for i in range(k,n):
            for j in range(k):
                A[k][i] -= A[k][j] * A[j][i]
        for i in range(k+1, n):
            for j in range(k):
                A[i][k] -= A[i][j] * A[j][k]
            A[i][k] /= A[k][k]

    return unpack(A)


def lu(A, use_c=False):
    if use_c:
        return lu_c(A)
    else:
        return lu_python(A)

def plu(A, use_c = False):
    n = len(A)
    P,L,U = [],[],[]
    for i in range(n):
        P.append([])
        L.append([])
        U.append([])
        for j in range(n):
            if i ==j:
                P[i].append(1)
            else:
                P[i].append(0)
            L[i].append(0)
            U[i].append(A[i][j])

    #print(U,L,P)
    #for i in range(5):
    #rint('test')
    
    for col in range(n-1):
        #print('here')
        p = abs(U[col][col])
        rmax = col
        row = col + 1
        while row < n:
            #find max element in the column and swap
            q = abs(U[row][col])
            if p < q:
                p = q
                a, b = U[rmax], P[rmax]
                U[rmax], P[rmax] = U[row], P[row]
                U[row], P[row] = a, b
                for i in range(col):
                    c = L[rmax][i]
                    L[rmax][i] = L[row][i]
                    L[row][i] = c
            row += 1
        
        r = col + 1
        while r < n:
            L[r][col] = U[r][col]/U[col][col]
            c = col
            while c < n:
                U[r][c] -= L[r][col]*U[col][c]
                c+=1
            r +=1


            
        #print('update:',U,L,P)

    for i in range(n):
        #print(27)
        L[i][i] = 1            
                
    return P,L,U

if __name__ == "__main__":

    def get_A():
        """ Make a test matrix """
        A = [[2.0, 3.0, -1.0],
             [4.0, 1.0, 2.0],
             [-1.0, 7.0, 2.0]]
        return A

    A = get_A()
    """
    L, U = lu(A, use_c = False)
    print(L)
    print(U)

    # Must re-initialize A as it was destroyed
    A = get_A()

    L, U = lu(A, use_c=True)
    print(L)
    print(U)
    """  
    P, L, U = plu(A, use_c = False)
    print(P,L,U)
    
