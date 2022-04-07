'''рандомный список с выводом чисел, которые больше предыдущего'''
import random

original_list = [0]
new_list = []
n = 0
m = 0

for el in original_list:
    original_list.append(random.randint(0, 200))
    n += 1
    if n > 10:
        break
print('исходный список :', original_list)

i = 0
i +=1

new_list = [original_list[i] for i in range(0, len(original_list)) if original_list[i - 1] < original_list[i]]

print('новый список:', new_list)
