def my_fun(x, y):
    """ Функция возведения х в степень у, где:
    х - целое положительное число
    у - целое отрицательное
    """
    # 1-й способ
    # return round(x**y, 4)
    # 2-й способ
    y = abs(y)
    result = 1
    while y > 0:
        result = result * (1 / x)
        y -= 1
    return round(result, 4)


# 3-й способ. Через рекурсию
def recursiv_fun(x, y):
    y = abs(y)
    if y == 0:
        return 1
    return (1 / x) * recursiv_fun(x, y - 1)


try:
    x = int(input('Введите действительное положительное число х: '))
    y = int(input('Введите целое отрицательное число у: '))
    if x <= 0 or y >= 0:
        raise ValueError
    print('х^у =', my_fun(x, y), '- решение через цикл while')
    print('x^y =', round(recursiv_fun(x, y), 4), '- решение через рекурсию')
except ValueError:
    print('Ошибка. Неверный ввод')
