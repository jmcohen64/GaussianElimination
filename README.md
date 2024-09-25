Gaussian Elimination
=====================
Basic algorithms are implemented in C
* Solving a linear system by Gaussian Elimination without Pivoting
* LU - decomposition "in place" where L and U are placed directly in A
* A number of useful helper functions (norms, distances, creation and destruction of matrices, random matrix generation)

Building a Python Extension
==================================
In this folder you also have examples of turning C code into Python commands.
Two ways are covered:

Building a Python Package
------------------------
The consequential file is setyp.py. To build the extension you run:

	python setup.py build
	
To install the extension you do:

	python setup.py install

Calling functions directly via cffi (C Foreign Function Interface).
-------------------------------------------------------------------
C functions are build directly into DLL (.dll) on Windows or Shared Objects.

