list_2 = (list(input("введите строку или список через запятую")))
list_3 = list_2.copy()
print(type(list_2))
z = len(list_2)
n = 0
m = 1
for el in list_2:
    while n < z - 1:
        list_2.insert(n, list_3[m])
        list_2.pop(n + 2)
        n += 2
        m += 2
print(list_2)

