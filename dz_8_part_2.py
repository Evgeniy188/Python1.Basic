class MyOwn(Exception):
    def __init__(self):
        self.txt = 'Деление на 0 !!!'


try:
    a = int(input('Введите числитель: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise MyOwn
    print(a / b)
except ValueError:
    print('Введите число!')
except MyOwn as err:
    print(err.txt)
