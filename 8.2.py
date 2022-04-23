class My_Error(Exception):
    def __init__(self, n):
       self.n = n
user_num1 = input('Введите делимое: ')
user_num2 = input('Введите делимое: ')
try:
    num1 = int(user_num1)
    num2 = int(user_num2)
    if num2 == 0:
        raise My_Error('на ноль делить нельзя, дурачок')
    else:
        num_end = num1 / num2
except My_Error as err:
    print(err)
else:
    print(f'частное: {num_end}')