from scipy.linalg import solve
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


# create "x^2 + 3x + y" equation with sympy
# solve (x - y = -1, 3x + y = 9) with sympy
# solve (x - y = -1, 3x + y = 9) with numpy
# solve (x - y = -1, 3x + y = 9) with scipy
# plot (x - y = -1, 3x + y = 9)

x, y = sp.symbols('x, y')
x ** 2 + 3 * x + y

eq1 = sp.Eq((x - y), -1)
eq2 = sp.Eq((3 ** x + y), 9)
sp.solve((eq1, eq2), (x, y))

# X = A^-1 * b
matrixA = np.array([[1, -1], [3, 1]])
b = np.array([-1, 9])
AInv = np.linalg.inv(matrixA)
X = np.dot(AInv, b)
# or
X = np.solve(matrixA, b)

solve(matrixA, b)

# create 10 numbers from -5 to 5
x = np.linspace(-5, 5, 10)
y1 = x + 1
y2 = 9 - 3 * x

plt.plot(x, y1)
plt.plot(x, y2)

# the answer is : [2, 3]
plt.axvline(x = 2, color="green")
plt.axhline(y = 3, color="red", linestyle="--")

plt.xlabel('x')
plt.ylabel('y')