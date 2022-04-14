class Worker:
    name = 'Igor'
    surname = 'Ivanov'
    position = 'manager'
    income = {'wage': 20000, 'bonus': 500}

class Position(Worker):
    def get_full_name(self):
        s = self.name + self.surname
        print(f'Полное имя сотрудника: {s}')
    def get_total_income(self):
        sal = self.income.get('wage') + self.income.get('bonus')
        print(f'Полная зарплата сотрудника сотавляет: {sal}')

'''как ни искала, не поняла откуда None выводится, по идее может от get'''

exp = Position()
print(exp.get_full_name())
print(exp.get_total_income())
