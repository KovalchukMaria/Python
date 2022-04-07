
def generator():
    from math import factorial

    n = int(input('введите количество факториалов: '))
    gen = (el for el in range(1, n+1))
    for el in gen:
        print(f'факториал числа {el} = ', factorial(el))
        yield generator()



'''список факториалов чисел начиная с 1, для пользовательского ввода их количества'''
fact = generator()
print(fact)
for el in fact:
    print(el)
