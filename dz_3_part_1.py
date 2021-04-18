def fun_division(a=input('Введите числитель: '), b=input('Введите делитель: ')):
    try:
        return round(float(a) / float(b), 4)
    except ZeroDivisionError:
        return 'Ошибка. Деление на ноль.'
    except ValueError:
        return 'Ошибка. Введите число'


print(fun_division())
