import numpy as numpy
from sklearn import linear_model
import matplotlib.pyplot as plt

# original data set
x = [1, 2, 3]
print(len(x))
y = [1, 2.5, 3.5]
print(len(y))
plt.scatter(x, y)

# slope for 1 is 0.5
# slope for 2 is 1.0
# slope for 3 is 1.5
slope = [0.5, 1.5, 1]


def multipy_matrix(features, theta):
    mutated = []
    for i in range(len(x)):
        mutated.append(features[i] * theta)
        #     1*0.5=1.5,2*0.5=1.0,3*0.5=1.5
    print(mutated)
    return mutated


# calculate hypothesis value
for i in range(len(slope)):
    multipy_matrix(x, slope[i])

plt.show()
