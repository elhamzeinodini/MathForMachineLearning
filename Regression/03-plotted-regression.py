import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets


# Simulating Data
n = 1000
x = np.random.normal(3, 5, size=n)
y = -15 * x + 20 + np.random.normal(0, 3, size=n)


X = np.sum(x)
Y = np.sum(y)
b1 = (n * np.dot(x,y) - Y*X)/(n*np.dot(x,x)-X**2)
b0 = (Y-b1*X)/n
b1, b0 = round(b1, 2), round(b0, 2)
print(f"y = {b1} x + {b0}")


def MSE_loss(b0, b1, x, y):
    pred = b0 + b1 * x
    loss = np.sum((pred - y) ** 2) / len(y)
    return loss

# Generate a grid of b0 and b1 values around the real b0=20 and b1=-15
b0_vals = np.linspace(0, 40, 100)
b1_vals = np.linspace(-30,0, 100)


# The logarithm function is applied to the MSE value. Since MSE values are typically positive (** 2),
# taking the logarithm helps transform the scale, making it easier to visualize differences,
# especially when MSE values span a wide range (for example, very large or very small values).
Z = np.zeros((len(b0_vals),len(b1_vals)))
for i in range(len(b0_vals)):
    for j in range(len(b1_vals)):
        Z[i, j] = np.log(MSE_loss(b0_vals[i], b1_vals[j], x, y))


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
B0, B1 = np.meshgrid(b0_vals, b1_vals)
ax.plot_surface(B0, B1, Z, cmap='viridis')

# Adding labels
ax.set_xlabel('b0')
ax.set_ylabel('b1')
ax.set_zlabel('Loss')
plt.show()