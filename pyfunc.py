class LinearFunction:
    """
    Represents a linear function in the form of `a * x + b`
    """
    def __init__(self, a: 'Number', b: 'Number'):
        """
        Creates a linear function with a in the form of `a * x + b`
        """
        self.slope = a
        self.yInter = b

    def infiniteSlope(self, x):
        self.__init__()

    def __repr__(self):
        sign = ("-", "+") [self.yInter > 0]
        return "{}x {} {}".format(self.slope, sign, abs(self.yInter))

    def image(self, x: 'Number'):
        return self.slope * x + self.yInter

    def preimage(self, y: 'Number'):
        return (y - self.yInter) * 1 / self.slope

    def reciprocal(self) -> 'LinearFunction':
        """
        Creates and returns the reciprocal function of self
        f(x) = ax + b
        f_r(y)= x = (y - b) / a
        x = (y - b) * (1 / a)
        x = y * (1 / a) - b * (1 / a)
        x = 1 / a * y - b / a => slope: (1 / a), yInter: - b / a
        """
        return LinearFunction(1 / self.slope, -self.yInter / self.slope)

    def intersectLinear(self, other: 'LinearFunction'):
        """
        Returns a point as a tuple where self and the other linear function intersect,
        Returns None if there's no intersection
        f(x) = o(x) => ax + b = cx + d
        ax + b = cx + d || -d
        ax + b - d = cx || -ax
        b - d = cx - ax
        b - d = x(c - a) || /(c - a)
        (b - d) / (c - a) = x
        x = (b - d) / (c - a)
        """
        denominator = (other.slope - self.slope)
        if not denominator == 0.0:
            interX = (self.yInter - other.yInter) / (other.slope - self.slope)
            return interX, self.image(interX)
        return None

    def plot(self, pyplot):
        x1, x2, _, _ = pyplot.axis()
        pyplot.plot([x1, x2], [self.image(x1), self.image(x2)], '-g')

