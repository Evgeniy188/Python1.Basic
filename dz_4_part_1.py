from sys import argv

try:
    name, production, rate, award = argv
    salary = float(production) * float(rate) + float(award)
    print('Заработная плата сотруднкиа =', round(salary, 2))
except:
    print('Вы ввели неверные значения.')
