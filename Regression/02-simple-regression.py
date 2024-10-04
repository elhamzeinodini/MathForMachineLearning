import numpy as np

n = 1000
# mean is 3, numbers cluster around the value 3
x = np.random.normal(3, 5, size=n)
# y = -15x + 20 + noise
y = -15 * x + 20 + np.random.normal(0, 3, size=n)


X = np.sum(x)
Y = np.sum(y)
b1 = (n * np.dot(x, y) - X * Y) / (n * np.dot(x, x) - X ** 2)
b0 = (Y - np.dot(b1, X)) / n

b0, b1 = round(b0, 2), round(b1, 2)
print(f"y= {b1} x + {b0}")