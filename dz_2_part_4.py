my_list_input = input('Введите строку: ').split()
for i, el in enumerate(my_list_input, 1):
    print(f'{i}. {el[:10]}')
