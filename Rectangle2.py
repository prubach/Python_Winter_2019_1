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

r1 = Rectangle()
print(r1.calc_surface())
r2 = Rectangle(5, 7)
print(r2.calc_surface())
r3 = Rectangle(a=5)
r3.a = 77
print('r3.a=' + str(r3.a))

r3.__a = 500
print('r3.__a=' + str(r3.__a))
print('orig r3.__a=' + str(r3.get_a()))
print(r3.calc_surface())

