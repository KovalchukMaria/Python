import numpy as np


class Matrix:
    def __init__(self, matri):
        self.matri = matri

    def __str__(self):
        return f' - {np.array(self.matri)}'

    def __add__(self, other):
        return Matrix(np.array(self.matri) + np.array(other.matri))


m = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
n = Matrix([[3, 2, 1], [3, 2, 1], [3, 2, 1]])
print(m)
print(n)
print(m + n)
