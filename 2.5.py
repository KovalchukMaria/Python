my_list = [8, 8, 7, 7, 7, 5, 2]
print(my_list)
my_list_copy = my_list.copy()
a = int(input('number'))
n = 1
for el in my_list_copy:
    if a > my_list_copy[0]:
        my_list.insert(0, a)
        break
    if a > my_list_copy[n]:
        n = n - 1
        my_list.insert(n, a)
        break
    if a == my_list[-1]:
        my_list.insert(-1, a)
        break
    if a < my_list[-1]:
        my_list.append(a)
        break
    else:
        n = n + 1
print(my_list)
