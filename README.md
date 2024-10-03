Gaussian Elimination
=====================
Basic algorithms are implemented in C
* Solving a linear system by Gaussian Elimination without Pivoting
* LU - decomposition "in place" where L and U are placed directly in A
* A number of useful helper functions (norms, distances, creation and destruction of matrices, random matrix generation)

IDE - Emacs
=======================
The code and Makefile will work with Emacs, given that typical
packages for C/C++ development are installed (GCC, GDB and GNU Make)

IDE - VSCode
=============
The folder .vscode contains two files, launch.json and tasks.json
which allow debugging with VSCode. Three extensions are needed. In
addition, GCC, GDB and GNU Make must be installed.

Install the following VSCode extensions:

* C/C++ by Microsoft (for code editing and IntelliSense).
* Makefile Tools (for Makefile support).
* CodeLLDB (or C/C++ Extension Pack) for GDB-based debugging support.

Also, modify the paths to GCC and GDB in the file ![.vscode/launch.json].


Disclaimer
==========
This code is very minimalistic and it is designed purely for
illustration and educational purposes. The author takes absolutely no
responsibility for damages resulting from its use.
