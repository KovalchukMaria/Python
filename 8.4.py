class Stock:
    def __init__(self):
        print('Склад оргтехники')


class Office_Equipment(Stock):
    def __init__(self, type_of_OE, model, price, presence, needs):
        super().__init__()
        self.type_of_OE = type_of_OE
        self.model = model
        self.price = price
        self.presence = presence
        self.needs = needs

    def show(self):
        print(f'модель {self.type_of_OE}а - {self.model}\n'
              f'стоимость {self.type_of_OE}а - {self.price}\n'
              f'наличие {self.type_of_OE}ов на складе - {self.presence}\n'
              f'потребность офиса в {self.type_of_OE}ах - {self.needs}\n')


class Printer(Office_Equipment):
    def __init__(self, type_of_OE, colours, model, price, presence, needs):
        super().__init__(type_of_OE, model, price, presence, needs)
        super().show()
        self.colours = colours
        print(f'тип {self.type_of_OE}а - {self.colours}')


class Scanner(Office_Equipment):
    def __init__(self, type_of_OE, size_of_sheets, model, price, presence, needs):
        super().__init__(type_of_OE, model, price, presence, needs)
        super().show()
        self.size_of_sheets = size_of_sheets
        print(f'размер листов выдачи у {self.type_of_OE}а - {self.size_of_sheets}')


class Xerox(Office_Equipment):
    def __init__(self, type_of_OE, type, model, price, presence, needs):
        super().__init__(type_of_OE, model, price, presence, needs)
        super().show()
        self.type = type
        print(f'тип {self.type_of_OE}а - {self.type}')


p = Printer('принтер', 'черно-белый', 'hp', '3000', '10', '12')
s = Scanner('сканер', 'а4', 'Epson', '4500', '2', '5')
x = Xerox('ксерокс', 'струйный', 'Canon', '2600', '0', '5')
