def my_func():
    try:
        a = float(input('введдите первое число'))
        b = float(input('введите второе число'))
        c = a / b
    except ZeroDivisionError:
        return None
    return c
print(my_func())
