#### 5

proceed = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
profit = proceed - costs
if profit > 0:
    rent = profit/proceed
    emp = int(input('Введите количество сотрудников: '))
    pr_1 = profit/emp
    print(f'Фирма работает с прибылью. Рентабильность {rent:.2f}. Прибыль на 1 сотрудника - {pr_1:.2f}')
elif profit < 0:
    print('Фирма работает в убыток.')
else:
    print('Фирма работает в 0.')