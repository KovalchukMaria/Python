'''код для подсчета общего расхода ткани без декоратора и абстрактных классов'''
class Coat:     #расчеты под пальто
    def __init__(self, size):
        self.size = size
        print(f'расход по ткани для пальто: {self.size / 6.5 + 0.5}')


class Suit:    #расчеты под костюм
    def __init__(self, height):
        self.height = height
        print(f'расход по ткани для костюма: {self.height * 2 + 0.3}')


class Clothes(Coat, Suit):    #объединение инитов, через перегрузку
    def __init__(self, size, height):
        Coat.__init__(self, size)
        Suit.__init__(self, height)
        print(f'Общий расход ткани: {(self.height * 2 + 0.3) + (self.size / 6.5 + 0.5)}')


c = Clothes(50, 1.7)

