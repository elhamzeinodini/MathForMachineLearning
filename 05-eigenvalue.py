# it's "ai.guhn.va.lyoo" !
import sympy as sp
import numpy as np

# with numpy

a = np.array([[1,4], [3,2]])
L, V = np.linalg.eig(a)
formattedV = np.around(V, decimals = 1)


# with sympy

a = sp.Matrix([[1,2,3], [0,3,0], [0,0,1]])
a.eigenvals()
# {3: 1, 1: 2} , means we have a 3 and 2 of 1s
a.eigenvects()


# SVD decomposition

A = np.array([[3,1,1], [-1,3,1]])
AATranspose = np.dot(A, A.T)
L, V = np.linalg.eig(AATranspose)
U, S, Vt = np.linalg.svd(A)
U = np.around(U, decimals = 1)
S = np.around(S, decimals = 1)
Vt = np.around(Vt, decimals = 1)
