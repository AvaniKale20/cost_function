import numpy as numpy

x = numpy.array([5])
y = numpy.array([10])


def costFunction(x, y):
    print(numpy.sum(x - y) / len(x))
    # return numpy.sum(x - y) / len(x)


costFunction(x, y)

