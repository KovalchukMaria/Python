def my_func(arg_1, arg_2, arg_3):
    return arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)


arg_1 = float(input('введите первый аргумент'))
arg_2 = float(input('введите второй аргумент'))
arg_3 = float(input('введите третий аргумент'))

print(my_func(arg_1, arg_2, arg_3))
