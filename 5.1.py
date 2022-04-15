'''созд файл, ввести пользователем данные построчно, завершая пустой строкой'''
with open('task1.txt', 'w+') as file_1:
    x = True
    while x:
        x = input('введите строки в файл: ')
        print(x, file=file_1)

with open('task1.txt', 'r') as file_1:
    for line in file_1:
        print(line)
