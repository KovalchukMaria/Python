'''создадим файл'''
with open('task_5_7.txt', 'w+') as my_f:
    print('название, форма собственности, выручка, издержки', file=my_f)
    print('firm_1 OOO 10000 5030', file=my_f)
    print('firm_2 OAO 10002 12000', file=my_f)
    print('firm_3 ЗАO 10003 16050.10', file=my_f)
    print('firm_4 ЗOС 10004 1000.02', file=my_f)
    print('firm_5 ТС 10005 5000.2', file=my_f)

'''создали двухуровневый список из файла'''
with open('task_5_7.txt', 'r') as my_f:
    my_list = my_f.readlines()
    print(my_list)
    n = 1
    my_double_list = []
    margin_all = {}
    for el in my_list:
        while n < len(my_list):
            my_double_list.append(my_list[n].split())
            n += 1
        else:
            break

    ''' посчитае прибыль и содадим писок прибылей'''
    n = 0
    all = []
    for el in my_double_list:
        while n < len(my_double_list):
            a = float(my_double_list[n][2]) - float(my_double_list[n][3])
            all.append(a)
            margin = {f'{my_double_list[n][0]}': a}
            margin_all.update(margin)
            n += 1
        else:
            break

    '''средняя прибыль и список с 2мя словарями'''
    average = sum(all) / len(all)
    average_dict = {'average': f'{average}'}
    finally_list = [margin_all, average_dict]
    print(finally_list)

'''попробуем все перевести в JSON'''
import json

with open('5.7.json', 'w') as obj:
    json.dump(finally_list, obj)
    print(obj)

