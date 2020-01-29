from math import sqrt
from time import sleep
from math import inf, atan, tan
import pyfunc

class Regressor:
    def __init__(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata
        self.mean = (sum(xdata) / len(xdata), sum(ydata) / len(ydata))

    def regress(self, n=0.001, extremes=1000000000): # Estimates slope within [-extremes; extremes] with atleast n precision
        """
        Estimates ideal slope by centering on `self.mean`
        
        - Start with two 'extreme' slopes forming an angle
        - Calculate the slope with least error and switch to it's half part in the angle
        - The extreme slopes have now changed and the angle between them has been halved
        - Repeat until satisfied
        """
        s1 = extremes
        s2 = -extremes
        c = 0
        deltaC = inf
        print("Using mean: {}".format(self.mean))
        while deltaC > n:
            e1, e2 = self.error(pyfunc.LinearFunction(s1, self.mean[1] - s1 * self.mean[0])),\
                     self.error(pyfunc.LinearFunction(s2, self.mean[1] - s2 * self.mean[0]))
            print("c: {:.3f}, minError: {:.3f}".format(c, min(e1, e2)))
            if e1 < e2: # Ideal slope is in the top half
                s2 = c
            elif e2 < e1: # Ideal slope is in the bottom half
                s1 = c
            else: # The current slope is PERFECT, e1 == e2
                return c
            oldC = c
            c = bisectSlope(s1, s2)
            deltaC = abs(c - oldC)
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

def bisectSlope(a, b):
        """
        Calculates a c slope from bisecting a and b || /!\ a > b
        c = tan(beta / 2)
        a = tan(alpha + beta) => atan(a) = alpha + beta
        b = tan(alpha) => atan(b) = alpha
        beta = (alpha + beta) - alpha = atan(a) - atan(b)

        We need a calculate the slope at alpha + beta / 2
        """
        if a < b:
            raise Exception("A must be bigger than B")
        alpha = atan(b)
        beta = atan(a) - atan(b)
        return tan(alpha + beta / 2)
