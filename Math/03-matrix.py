import numpy as np
import sympy as sp

# calculate the determinant of matrix a [[1,2] [4,5]] with numpy
# calculate the inverse of a with numpy
# calculate the norm of a with numpy

# create a matrix with "symbolic python" package
# calculate the row and column 0 with symbolic py
# calculate the dimension of a with symbolic py
# calculate the determinant of a with symbolic py
# calculate the inverse of a with symbolic py
# create a 4*5 matrix of 0 with symbolic py 
# create an identical matrix of 5*5 with symbolic py
# create a diagonal matrix where the main axis is "1, 2, 3, 4, 5"

matrixA = np.array([[1,2], [4,5]])
np.linalg.det(matrixA)

np.linalg.inv(matrixA)

np.linalg.norm(matrixA)

sp.Matrix([[1,2], [4,5]])

matrixA.row(0)
matrixA.col(0)

matrixA.size

matrixA.shape

matrixA.det()

matrixA.inv()

sp.zeros(4, 5)

sp.eye(5, 5)

sp.diag(1,2,3,4,5)