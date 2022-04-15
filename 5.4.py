'''вывод строк файла с переводом числительных, файл прилагается'''
f_1 = open('task_5.4.txt', 'r')
f_split = []
for line in f_1:
    if line.startswith('One'):
        a = line.replace('One', 'один')
    if line.startswith('Two'):
        a = line.replace('Two', 'два')
    if line.startswith('Three'):
        a = line.replace('Three', 'три')
    if line.startswith("Four"):
        a = line.replace('Four', 'четыре')
    print(a)
f_1.close()