'''генерация целых чисел, начиная с указанного'''
from itertools import count

x = int(input('введите число, с которого должна начинаться последовательнось: '))
for el in count(x):
    if el > 10:
        break
    else:
        print(el, end='')

'''повторение введенного списка 15 раз'''
from itertools import cycle

your_list = input('введите список')
n = 0
for el in cycle(your_list):
    if n > 15:
        break
    else:
        n += 1
        print(el, end='')
