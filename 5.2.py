'''непрограммное создание файла с последующим подсчетом слов в каждой строке, пронумерованной'''
with open('task_2.txt', 'w+') as f_2:
    string = ['Позиционные аргументы — список параметров,\n',
              'доступ к которым можно получить по индексу параметра в фигурных скобках {индекс}.\n',
              'Параметры — ключевые слова — список параметров типа ключ=значение,\n',
              ' доступ к которым можно получить с помощью ключа параметра в фигурных скобках {ключ}.\n']
    f_2.writelines(string)

x = 0

f_2 = open('task_2.txt', 'r')
for line in f_2:
    a_str = line
    a_list = a_str.split()
    len_a = len(a_list)
    x += 1
    print(f'в строке №{x} - {len_a} слов')
print('количество строк =', x)
f_2.close()
