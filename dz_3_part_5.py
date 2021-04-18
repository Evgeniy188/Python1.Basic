def my_fun():
    def sum_fun():
        sum_list = input('Введите числа через пробел или q для окончания: ').split()
        nonlocal result
        for el in sum_list:
            if el != 'q':
                try:
                    result += float(el)
                except:
                    print('Ошибка ввода. Введите число!')
                    break
            else:
                return result
        print('Сумма чисел на данный момент: ', result, '\nПродолжаем...')
        sum_fun()
        return result

    result = 0
    sum_fun()
    return result


print('Сумма чисел =', my_fun())
