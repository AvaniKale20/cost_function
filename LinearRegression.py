import numpy as numpy
import matplotlib.pyplot as plt

x = numpy.array([1, 2, 3, 4, 5])
print(x.shape)
y = numpy.array([2, 3, 4, 4, 4])
print(y.shape)
plt.scatter(x, y)
# plt.show()

m = (y.dot(x) - y.mean() * x.sum()) / (x.dot(x) - x.mean() * x.sum())
print(m)
c = (y.mean() * x.dot(x) - x.mean() * y.dot(x)) / (x.dot(x) - x.mean() * x.sum())
print(c)

y_hat = m * x + c
print("The value of y_hat", y_hat)
plt.scatter(x, y)
plt.scatter(x, y_hat)

error = y - y_hat
print("sun of square of residual", error)
ssm = y - y.mean()
print("sun of square of wrt mean",ssm)

R2=1-(error.dot(error))/(ssm.dot(ssm))
print(R2)
plt.show()
