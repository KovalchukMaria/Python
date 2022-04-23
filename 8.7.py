import MATLAB
class Complex:  # я пока не совсем поняла комплексные числа, поэтому не могу понять, почему не работает код
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
        self.com = self.a + (self.b)j

    def __add__(self, other):
        return Complex(complex(self.a, self.b) + complex(other.a, other.b))

    def __mul__(self, other):
        return Complex(complex(self.a, self.b) * complex(other.a, other.b))

c = Complex(2, 3)
d = Complex(2, 3)
print(c +d)
print(c * d)


