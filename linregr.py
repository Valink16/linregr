from math import sqrt
from time import sleep
import pyfunc

def regress(xdata: list, ydata: list):
    """
    Returns a regressed linear function
    Calculates average slope by adding up all the slopes passing by the mean
    Caclculating the y-intercept:
    x, y, and a are known: mean.x, mean.y and the average slope
    f(x) = ax + b
    y = ax + b
    y - ax = b | We can now compute the y-intercept
    """
    mean = sum(xdata) / len(xdata), sum(ydata) / len(ydata)
    s = 0
    divider = 0
    for x, y in zip(xdata, ydata):
        if not x == mean[0]:
            divider += 1
            s += (mean[1] - y) / (mean[0] - x)

    s /= divider
    return pyfunc.LinearFunction(s, mean[1] - s * mean[0])