def my_func():
    print('нажмите enter без ввода для завершения программы')
    add = True
    my_int = []
    my_list_1 = []
    a = 0
    s_1 = 0
    while add:
        my_str = input('введите числа через пробел для подсчета суммы: ')

        if not my_str:
            break

        my_list = list(my_str.split())
        my_list_1.extend(my_list)
        for el in my_list:
            x = int(my_list_1[a])
            my_int.append(x)
            a = a + 1
        s_1 = sum(my_int)
        print(s_1)
    if not my_str:
        exit()

    return s_1

print(my_func())
