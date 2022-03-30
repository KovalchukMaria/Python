my_dict_1 = {}
a_1 = input('введите название товара')
b_1 = input('введите цена вышеупомянутого товара')
c_1 = input('введите количество вышеупомянутого товара')
d_1 = input('введите единицу измерения вышеупомянутого товара')
my_dict_1.update({'название': a_1, 'цена': b_1, 'количество': c_1, 'ед': d_1})
my_tuple_1 = (1, my_dict_1)
print(my_tuple_1)

my_dict_2 = {}
a_2 = input('введите название товара')
b_2 = input('введите цена вышеупомянутого товара')
c_2 = input('введите количество вышеупомянутого товара')
d_2 = input('введите единицу измерения вышеупомянутого товара')
my_dict_2.update({'название': a_2, 'цена': b_2, 'количество': c_2, 'ед': d_2})
my_tuple_2 = (2, my_dict_2)
print(my_tuple_2)

my_dict_3 = {}
a_3 = input('введите название товара')
b_3 = input('введите цена вышеупомянутого товара')
c_3 = input('введите количество вышеупомянутого товара')
d_3 = input('введите единицу измерения вышеупомянутого товара')
my_dict_3.update({'название': a_3, 'цена': b_3, 'количество': c_3, 'ед': d_3})
my_tuple_3 = (3, my_dict_3)
print(my_tuple_3)

list_name = []
a = my_dict_1.get('название')
aa = my_dict_2.get('название')
aaa = my_dict_3.get('название')
list_name.append(a)
list_name.append(aa)
list_name.append(aaa)

list_price = []
b = my_dict_1.get('цена')
bb = my_dict_2.get('цена')
bbb = my_dict_3.get('цена')
list_price.append(b)
list_price.append(bb)
list_price.append(bbb)

list_number = []
c = my_dict_1.get('количество')
cc = my_dict_2.get('количество')
ccc = my_dict_3.get('количество')
list_number.append(c)
list_number.append(cc)
list_number.append(ccc)

list_unit = []
d = my_dict_1.get('ед')
dd = my_dict_2.get('ед')
ddd = my_dict_3.get('ед')
list_unit.append(d)
list_unit.append(dd)
list_unit.append(ddd)

new_dict = {'название': list_name, 'цена': list_price, 'количество': list_number, 'ед': list_unit}
print(new_dict)
'''может нужно было информацию доставать через кортежи, объединенные в список, но у меня не получилось'''
my_list = []
my_list.append(my_tuple_1)
my_list.append(my_tuple_2)
my_list.append(my_tuple_3)
print(my_list)