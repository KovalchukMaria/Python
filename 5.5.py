with open('task_5.5.txt', 'w+') as file_5_5:
    file_5_5.write(input('Введите числа через пробел: '))

with open('task_5.5.txt', 'r') as file_5_5:
    content = file_5_5.read()
    content_list = content.split()
    summa = sum(int(el) for el in content_list)
    print(summa)