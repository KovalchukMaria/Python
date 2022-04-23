class Stock:  # не сильно поняла его надобность именно в этой задаче
    def __init__(self):
        print('Склад оргтехники:')


class OfficeEquipment(Stock):
    ''' внесем классовые аттрибуты '''
    def __init__(self, type_of_OE, model, price, presence, needs):
        super().__init__()
        self.type_of_OE = type_of_OE
        self.model = model
        self.price = price
        self.presence = presence
        self.needs = needs

    '''сделаем красивый вывод аттрибутов'''
    def show(self):
        print(f'модель {self.type_of_OE}а - {self.model}\n'
              f'стоимость {self.type_of_OE}а - {self.price}\n'
              f'наличие {self.type_of_OE}ов на складе - {self.presence}\n'
              f'потребность офиса в {self.type_of_OE}ах - {self.needs}\n')

    '''создадим словарь с распределение имеющейся оргтехники,
    учитывая возможность несовпадения в наличии и потребности'''
    def reception(self, kind_of_office, office_needs):
        self.value_1 = kind_of_office
        self.value_2 = office_needs
        dict_of_presence = {'вид товара': f'{self.type_of_OE}',
                            'наличие товара на складе ': f'{self.presence}',
                            'место потребности в товаре': f'{self.value_1}',
                            'передача товара по месту требования в единицах': f"{self.value_2}"}
        if int(self.value_2) > int(self.presence):
            dict_of_presence_new = {'передача товара по месту требования в единицах': 'нет необходимого количества товара'}
            dict_of_presence.update(dict_of_presence_new)
        for key, value in dict_of_presence.items():
            print(f'{key} - {value}')



'''создадим дочерние классы'''
class Printer(OfficeEquipment):
    '''сразу добавим вывод аттрибутов'''
    def __init__(self, type_of_OE, colours, model, price, presence, needs):
        super().__init__(type_of_OE, model, price, presence, needs)
        super().show()
        self.colours = colours
        print(f'тип {self.type_of_OE}а - {self.colours}')

    '''с остальными дочерними классами можно сделатьтое самое, просто скопировав эти 2 строки'''
    def reception(self, kind_of_office, office_needs):
        super().reception(kind_of_office, office_needs)


class Scanner(OfficeEquipment):
    def __init__(self, type_of_OE, size_of_sheets, model, price, presence, needs):
        super().__init__(type_of_OE, model, price, presence, needs)
        super().show()
        self.size_of_sheets = size_of_sheets
        print(f'размер листов выдачи у {self.type_of_OE}а - {self.size_of_sheets}')


class Xerox(OfficeEquipment):
    def __init__(self, type_of_OE, type, model, price, presence, needs):
        super().__init__(type_of_OE, model, price, presence, needs)
        super().show()
        self.type = type
        print(f'тип {self.type_of_OE}а - {self.type}')


p = Printer('принтер', 'черно-белый', 'hp', '3000', '10', '12')
p.reception('бухгалтерия', 45)

s = Scanner('сканер', 'а4', 'Epson', '4500', '2', '5')

x = Xerox('ксерокс', 'струйный', 'Canon', '2600', '0', '5')
