import math
class Shape:
    def __init__(self, a=10, b=20):
        self.set_params(a, b)

    def set_params(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def __str__(self):
        return "{0}: [{1},{2}]".format(self.__class__.__name__, self._a, self._b)

class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self._b
        #return self.get_a()*self.get_b()

class Circle(Shape):
    def __init__(self, a):
        #self.set_params(a, 0)
        super().__init__(a, 0)

    def calc_surface(self):
        return math.pi*self._a**2

    def __str__(self):
        return "{0}: [{1}]".format(self.__class__.__name__, self._a)

s = Rectangle(4, 5)
#s = Shape(4, 5)
print(s)
print(s.calc_surface())
c = Circle(5)
print(c)
print(c.calc_surface())



