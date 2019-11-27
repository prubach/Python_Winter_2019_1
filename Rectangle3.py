class Rectangle:
    def __init__(self, a=10, b=20):
        self.set_params(a, b)

    def set_params(self, a, b):
        self.__a = a
        self.__b = b

    def calc_surface(self):
        return self.__a*self.__b

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def __str__(self):
        return "Rect: {0} by {1}".format(self.__a, self.__b)

    def __add__(self, other):
        a = self.__a + other.get_a()
        b = self.__b + other.get_b()
        return Rectangle(a, b)

    def __lt__(self, other):
        self_area = self.calc_surface()
        other_area = other.calc_surface()
        return self_area < other_area

r1 = Rectangle(4, 6)
r2 = Rectangle(6, 8)
r = r1 + r2
print(r)
print(r2<r1)