my_string = input('введите строку через пробел')
print(my_string.split())
my_string_1 = my_string.split()
for ind, el in enumerate(my_string_1, 1):
    print(ind, el[:10])