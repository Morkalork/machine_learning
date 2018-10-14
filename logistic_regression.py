import matplotlib.pyplot as pyplot
import numpy

def logistic(x):
    return 1/(1 + numpy.exp(-x))

def main():
    x = numpy.arange(-6, 6, 0.001)
    y = logistic(x)

    pyplot.plot(x, y)
    pyplot.xlabel('x')
    pyplot.ylabel('logistic(x)')
    pyplot.show()

