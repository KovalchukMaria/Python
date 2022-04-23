class Numb_Error(Exception):
    def __init__(self, x):
        self.x = x


"""проверим все ли вводимые данные являются числами"""
my_list = []
while True:  # бесконечный цикл
    user = input('введите число: ')
    try:
        user = int(user) or str(user)  # вот тут проблема
        if not isinstance(user, int):  # не смогла придумать как обойти хорошо
            raise Numb_Error("вы ввели не число")
        else:
            my_list.append(int(user))
    except Numb_Error as er:  # почему-то не выводися сообщение. п.н.:отметила проблемное место
        print(er)
    except:  # завершение программы
        if user == 'stop':
            print(my_list)
            break
