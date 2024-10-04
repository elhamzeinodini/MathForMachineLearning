import matplotlib.pyplot as plt
import numpy as np

# create [3, 4] as a
# what is the type of vector "a"
# what is the length of the array "a"
# what is the first element of the array "a"
# what is the second element of the array "a"
# what is the third element of the array "a"
# create [6, 7] as b
# calculate a + b, a - b and a * b
# calculate ([3, 4] * [6, 7] = 46) or the dot product of a and b
# calculate (2 * a)
# calculate (4 * 5)
# calculate the norm of vector a
# plot vector a

vectorA = np.array([3, 4])

vectorAType = type(vectorA)
print(vectorAType)

vectorALength = len(vectorA)
print(vectorALength)

print(vectorA[0])

print(vectorA[1])

print(vectorA[2])

vectorB = np.array([6, 7])

sum = vectorA + vectorB
minus = vectorA - vectorB

# both results in [18, 28]
multiplyA = vectorA * vectorB
multiplyB = np.multiply(vectorA, vectorB)

# 46
dotProduct = np.dot(vectorA, vectorB)

scalarToVectorMultiplication = np.dot(2, vectorA)

# 4 * 5 = 20
4 * 5
np.dot(4, 5)

# 3 ** 2 + 4 ** 2 = 25
normOfVectorA = np.linalg.norm(vectorA)


# plotting
plt.quiver(vectorA[0], vectorA[1], scale_units='xy', scale=1, angles='xy', color="red")
plt.text(vectorA[0], vectorA[1], r'$\vec{u}$', size=25, color="green")
plt.xlim(0, 10)
plt.ylim(0, 10)

