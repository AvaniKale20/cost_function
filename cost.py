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


# mutiply the original X values by the theta
# to produce hypothesis values for each X
def multipy_matrix(features, theta):
    mutated = []
    for i in range(len(x)):
        mutated.append(features[i] * theta)
        #     1*0.5=1.5,2*0.5=1.0,3*0.5=1.5
    print(mutated)
    plt.plot(mutated, y)
    return mutated


# calculate cost by looping each sample
# subtract hyp(x) from y
# square the result
# sum them all together
def calculate_cost(training_set, Y, h):
    total = 0
    for i in range(training_set):
        error_squared = (Y[i] - h[i]) ** 2
        # print(error_squared)
        total = total + error_squared

    return total * (1 / (2 * training_set))


# calculate hypothesis value
for i in range(len(slope)):
    hypothesis_value = multipy_matrix(x, slope[i])
    calculate_cost(len(x), y, hypothesis_value)

plt.show()
