seasons = {'z': 'winter', 's': 'summer', 'sp': 'spring', 'a': 'autumn'}
key = int(input('введите месяц в виде целого числа'))
if key <= 2 or key == 12:
    print(seasons.get('z'))
elif key > 2 and key < 6:
    print(seasons.get('sp'))
elif key > 5 and key < 9:
    print(seasons.get('s'))
elif key > 8 and key < 12:
    print(seasons.get('a'))
else:
    print('данного месяца не существует')
