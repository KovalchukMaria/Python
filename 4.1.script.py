'''вывод скрипта для подсчета з\п'''
from sys import argv

script_name, working_hours, rate_per_hour, premium = argv

salary = (float(working_hours) * float(rate_per_hour)) + float(premium)

print('выработка в часах - ', working_hours)
print('ставка в час - ', rate_per_hour)
print('премия - ', premium)
print('зарплата - ', salary)