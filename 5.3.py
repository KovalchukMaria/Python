''''создаем файл и вносим данные'''
oklad1 = open('task5.3.txt', 'w+')
print('петров 25000.5', file=oklad1)
print('петрова 288000.3', file=oklad1)
print('кукушка 450.3', file=oklad1)
print('соловей 4567', file=oklad1)
print('рыбак 45873.284', file=oklad1)
print('улитин 25', file=oklad1)
print('копытина 3854', file=oklad1)
print('кулыгин 187058', file=oklad1)
print('капустина 1358498', file=oklad1)
print('копеечка 1', file=oklad1)
print('сковородко 3546', file=oklad1)
print('ивановых 54867.54', file=oklad1)
print('ли 4567', file=oklad1)
oklad1.close()

''''введем переменные'''
salary = []
salary_split = []
salary_float = []

oklad = open('task5.3.txt', 'r')

'''создаем список, разделенный на фамилии и оклады'''
salary.append(oklad.read())
n = 0
for el in salary:
    salary_split = salary[n].split()
    n += 1

'''посчтиаем средний оклад через сумму и создание списка окладов'''
i = 1
for el in salary_split:
    while i < len(salary_split):
        salary_float.append(float(salary_split[i]))
        i += 2
s_1 = sum(salary_float)
medium_sal = s_1 / len(salary_split)
print('средний оклад сотрудников: ', medium_sal)

''''выведе сотрудников, у которых оклад > 20'000'''
i = 1
for el in salary_split:
    while i < len(salary_split):
        if float(salary_split[i]) > 20000:
            print(f'сотрудник {salary_split[i - 1]} получает оклад в размере: {salary_split[i]}')
        i += 2

oklad.close()
