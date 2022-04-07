''''сумма четных чисел от 10 до 1000'''
my_list = [el for el in range(10, 1001) if el % 2 == 0]
# через range не включчается значение последней границы, если брать до 1000
print(my_list)

from functools import reduce

summa = reduce(lambda x, y: x + y, my_list)
print(summa)