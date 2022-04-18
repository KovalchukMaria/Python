class Cell:
    def __init__(self, nucleus):  # ввод данных исключая ошибку ввода букв или списка
        try:
            self.nucleus = int(nucleus)
        except ValueError:
            print('Ошибка ввода')

    def __add__(self, other):  # перегрузка сложения
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):  # перегрузка вычитания
        return Cell(self.nucleus - other.nucleus)
        # при полученном нуле не совсем получилось куда-либо засунуть условие

    def __mul__(self, other):  # перегрузка умножения
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):  # перегрузка деления
        try:
            return Cell(self.nucleus // other.nucleus)
        except ZeroDivisionError:  # исключение ошибки деления на ноль
            print('Деление на ноль недопустимо, введите другие параметры')

    def __str__(self):  # вывод значений, полученных выше
        return f'клетка с {self.nucleus} ядрами'

    def make_order(self, numb):  # подобие недоделанной матрицы
        self.numb = numb
        n = 1
        for el in range(1, self.nucleus + 1):
            if el <= (self.numb * n):
                el = f'{el}, '
                print(el, end="")
            else:
                n += 1
                print(el, end='')
                print('\n')


c = Cell(12)
l = Cell(12)
print(c + l)
print(l - c)
print(c * l)
print(l / c)
c.make_order(5)
