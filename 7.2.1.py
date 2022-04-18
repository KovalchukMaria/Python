from abc import ABC, abstractmethod

class Coat(ABC):     #не поняла, правда зачем и для чего данный метод в этой задаче
             #возможно в нем есть смысл в более объемных кодах, чтоб красивенько было
    @abstractmethod
    def __init__(self, size):
        self.size = size
    @abstractmethod
    def Consumption(self):
        return f'расход по ткани для пальто: {self.size / 6.5 + 0.5}'


class Suit:
    def __init__(self, height):
        self.height = height
    @property   #пока не вижу особой пользы, ибо просто скобочки ставить не надо при вызове метода
    def Consumption(self):
        return f'расход по ткани для костюма: {self.height * 2 + 0.3}'


class Clothes(Coat, Suit):
    def __init__(self, size, height):
        Coat.__init__(self, size)
        Suit.__init__(self, height)
    @property
    def Consumption(self):
         return f'Общий расход ткани: {(self.height * 2 + 0.3) + (self.size / 6.5 + 0.5)}'

c = Clothes(50, 2)
print(c.Consumption)
