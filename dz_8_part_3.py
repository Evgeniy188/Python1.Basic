def is_float(s: str):
    try:
        float(s)
        return True
    except ValueError:
        return False


class MyOwn(Exception):
    def __init__(self):
        self.txt = 'Неверный ввод, введите число!'


my_list = []
while True:
    num = input('Введите число: ')
    if num == 'stop':
        break
    try:
        if num.isdigit() or is_float(num):
            my_list.append(num)
        else:
            raise MyOwn
    except MyOwn as err:
        print(err.txt)

print(my_list)
