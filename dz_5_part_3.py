def average_salary(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        sum, n = 0, 0
        emp_list = []
        for line in file:
            salary = float(line.split()[1])
            n += 1
            sum = (sum + salary) / n
            if salary < 20000:
                emp_list.append(line.split()[0])
        return round(sum, 4), emp_list


file_name = 'text_3.txt'
aver_sal, emp_list_lower_20k = average_salary(file_name)
print('Средняя зарплата сотавляет:', aver_sal)
print('Список сотрудников с з/п ниже 20к:')
[print(i, end=' ') for i in emp_list_lower_20k]
