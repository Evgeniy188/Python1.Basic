def write_str():
    with open('my_test1.txt', 'w', encoding='utf-8') as file:
        while True:
            str = input('Введите строку для записи (пустая строка - СТОП): ')
            if str == '':
                break
            file.writelines(str + '\n')


write_str()
