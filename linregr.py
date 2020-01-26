from math import sqrt
from time import sleep
from math import inf
import pyfunc

class Regressor:
    def __init__(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata
        self.mean = (sum(xdata) / len(xdata), sum(ydata) / len(ydata))

    def regress(self, n=0.001, extremes=100): # Estimates slope with deltaError < n precision
        s1 = extremes
        s2 = -extremes
        c = (s1 + s2) / 2
        deltaC = inf
        while deltaC > n:
            e1, e2 = self.error(pyfunc.LinearFunction(s1, self.mean[1] - s1 * self.mean[0])),\
                     self.error(pyfunc.LinearFunction(s2, self.mean[1] - s2 * self.mean[0]))
            oldC = c
            if e1 < e2:
                s2 = c
                c = (s1 + c) / 2
            elif e2 < e1:
                s1 = c
                c = (s2 + c) / 2
            else:
                return c
            deltaC = abs(c - oldC)
            print(c, deltaC)
        return c

    def error(self, f: 'pyfunc.LinearFunction'):
        """
        Returns total error for f compared to data
        """
        if f.slope == 0: # If flat, we can just use the vertical distance as error
            return sum([abs(f.yInter - y) for y in self.ydata])
        perpendSlope = -1/f.slope
        error = 0
        for x, y in zip(self.xdata, self.ydata):
            fP = pyfunc.LinearFunction(perpendSlope, y - perpendSlope * x) # Perpendicular function of f
            intersectPoint = f.intersectLinear(fP)
            error += sqrt((intersectPoint[0] - x) ** 2 + (intersectPoint[1] - y) ** 2) # Pythagorean distance
        return error