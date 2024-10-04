x = [5, 3, -1, 2, 6]
y = [14, 6, -5.5, 3.5, 18]

# X : sigma([5, 3, -1, 2, 6])
# Y : sigma([14, 6, -5.5, 3.5, 18])
# XiYi: sigma((5, 14), (3, 6), (-1, -5), ...)
# Xi2: sigma((5^2), (3^2), ...)

X, Y, XiYi, Xi2 = 0, 0, 0, 0
N = len(x)

for i in range(N):
  X = X + x[i]
  Y = Y + y[i]
  XiYi = XiYi + x[i] * y[i]
  Xi2 = Xi2 + x[i] ** 2
  
w1 = (N * XiYi - X * Y) / (N * Xi2 - X ** 2)
w0 = (Y - w1 * X) / N
# w0 must be -2, we'll get "-2.85", if the noise is added then we'll get "-2"