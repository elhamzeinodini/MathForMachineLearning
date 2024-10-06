import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 1000
noise = np.random.normal(0, 3, size=n)
x = np.random.normal(3, 5, size=n)
y = -15 * x + 20 + noise

X = np.sum(x)
Y = np.sum(y)
b1 = (n * np.dot(x, y) - Y * X) / (n * np.dot(x, x) - X ** 2)
b0 = (Y - b1 * X) / n
b0, b1 = round(b0, 2), round(b1, 2)
print(f"b0 = {b0} x + {b1}")

def MSE_Loss(b0, b1, x, y):
    predict = b0 + b1 * x
    loss = np.sum((predict - y) ** 2) / len(x)
    return loss

# y = -15 x + 20
# w0 = b0 = 20
b0_vals = np.linspace(0, 40, 100)

# w1 = b1 = -15
b1_vals = np.linspace(-30, 0, 100)

# 2D array of zeros
z = np.zeros((len(b0_vals), len(b1_vals)))

# Populate the z array with MSE loss values
for i in range(len(b0_vals)):
    for j in range(len(b1_vals)):
        # Logarithm is for better displaying the data
        z[i, j] = np.log(MSE_Loss(b0_vals[i], b1_vals[j], x, y))

# Plotting the surface
# a figure with 10 inches width and 20 inches height
fig = plt.figure(figsize=(10, 20))
ax = fig.add_subplot(111, projection='3d')
B0, B1 = np.meshgrid(b0_vals, b1_vals)
ax.plot_surface(B0, B1, z, cmap='viridis')

ax.set_xlabel('b0')
ax.set_ylabel('b1')
ax.set_zlabel('Loss')

plt.show()
