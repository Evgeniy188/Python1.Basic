class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a + self.b * other.b * (-1), self.a * other.b + self.b * other.a)

c1 = Complex(3, 5)
c2 = Complex(2, 3)
print(c1 + c2)
print(c1 * c2)
