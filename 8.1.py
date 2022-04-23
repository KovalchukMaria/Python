class Data:
    def __init__(self):
        self.user_date = input('введите дату в формате дд-мм-гггг: ')
    @classmethod
    def numb(cls, user_date):
        a, b, c = user_date.split('-')
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            print(a, b, c)
        except ValueError:
            print('невравильный формат ввода')
    @staticmethod   #виду того, что нет доступак методам, нужно копировать
    def validation(user_date):
        a, b, c = user_date.split('-')
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            print(a, b, c)
        except ValueError:
            print('невравильный формат ввода')
        if a < 1 or a > 31:
            print('неправильный ввод числа')
        if b < 1 or b > 12:
            print('неправильный ввод месяца')
        if c > 9999 or c < 0:
            print('неправильный ввод года')
d = Data()
Data.numb('04-05-789')
Data.validation('04-98-894')

