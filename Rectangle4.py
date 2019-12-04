class Rectangle:
    num_rect = 0

    def __init__(self, a=10, b=20):
        self.set_params(a, b)
        Rectangle.num_rect += 1

    def __del__(self):
        Rectangle.num_rect -= 1
        print(self.__str__(), " destroyed")

    @classmethod
    def how_many(cls):
        return cls.num_rect

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

    def add(self, other):
        a = self.__a + other.get_a()
        b = self.__b + other.get_b()
        return Rectangle(a, b)

    def __lt__(self, other):
        self_area = self.calc_surface()
        other_area = other.calc_surface()
        return self_area < other_area

r1 = Rectangle(4, 6)
print("num rect: ", r1.how_many())
r2 = Rectangle(6, 8)
print("num rect: ", r2.how_many())
print("num rect: ", r1.how_many())
del r2
print("num rect: ", r1.how_many())

