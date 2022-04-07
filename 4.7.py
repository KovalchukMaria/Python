def generator(x):
    from math import factorial

    gen = (el for el in range(1, x + 1))
    for el in gen:
        print(f'факториал числа {el} = ', factorial(el))
        yield generator(x)



'''список факториалов чисел от 1 до х(ввести число)'''
fact = generator(x)
print(fact)
for el in fact:
    print(el)
