import numpy as np

# create a multidimensional array (matrix) of a with values : [[1,2,3] [4,5,6]]
# what is the dimension of the matrix (2 * 3) here
# number of elements in the matrix
# first row of the matrix
# first column of the matrix
# element in row 0, column 0
# elements in row 0, and 1
# elements in row 1 to 2, all columns
# declare a new matrix b: [[1,2,3], [4,5,6], [7,8,9]] , get row 0 and 1 and column 0
# calculate the sum of all elements in the matrix b
# calculate the column sum of elements in 
# calculate the row sum of elements in 
# multiply 2 to [1 2][3 4] and save it to b
# calculate the sum and minus of matrix a and b, element by element
# calculate the multiplication of matrix a and b, where it is not element by element and is row 1 by column 1, ...
# calculate the transpose of matrix a
# calculate the transpose transpose of matrix a
# are matrix a and b equal
# calculate the sum of elements in the main axis

matrixA = np.array([[1,2,3], [4,5,6]])

matrixA.shape

matrixA.size

matrixA[0]

matrixA[:,0]

matrixA[0][0]

matrixA[0:2, :]
# or
matrixA[:2]

matrixB = np.array([[1,2,3], [4,5,6], [7,8,9]])
matrixB[0:2, :1]

matrixB.sum()

# row
matrixB.sum(axis = 1)

# column
matrixB.sum(axis = 0)

matrixC = np.array([1,2], [3,4])
b = np.dot(2, matrixC)

elementByElementSum = matrixA + matrixB

elementByElementMinus = matrixA - matrixB

elementByElementMultiply = matrixA * matrixB

matrixMultiplication = np.dot(matrixA, matrixB)

matrixA.T

matrixA.T.T

matrixA == matrixB

np.trace(matrixA)