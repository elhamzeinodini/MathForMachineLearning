import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# feature count
n = 1000

# input
x = np.random.normal(3, 5, size=n)

# output
noise = np.random.normal(0, 3, size=n)
y = -15 * x + 20 + noise

X = np.sum(x) # an scalar
Y = np.sum(y) # an scalar

b1 = (n * np.dot(x, y) - X * Y) / (n * np.dot(x, x) - X ** 2)
b0 = (Y - b1 * X) / n


# MEAN SQUARED ERROR
def MSE_LOSS(b0, b1, x, y):
  predict = b0 + b1 * x
  loss = np.sum((predict - y) ** 2) / len(x)
  return loss

# b0 = w0 = 20, 100 numbers in range of 0 to 40
b0_vals = np.linspace(0, 40, 100)

# b1 = w1 = -15, 100 numbers in range of -30 to 0
b1_vals = np.linspace(-30, 0, 100)

# 2d array of zeros
z = np.zeros((len(b0_vals), len(b1_vals)))

for i in range(len(b0_vals)) :
  for j in range(len(b1_vals)) :
    z[i, j] = np.log(MSE_LOSS(b0_vals[i], b1_vals[j], x, y))


# a figure of "width=10" and "height=7"
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
B0, B1 = np.meshgrid(b0_vals, b1_vals)
ax.plot_surface(B0, B1, z, cmap='viridis')


ax.set_xlabel('b0')
ax.set_ylabel('b1')
ax.set_zlabel('loss')

plt.show()

# this figure shows that at (b0=w0=-20) and (b1=w1=-15) we have the lowest amount of error and from any point on this 
# figure if we try to move in direction of decreasing the error , we'll eventually get to this point (b0=w0=-20) and (b1=w1=-15) again.
