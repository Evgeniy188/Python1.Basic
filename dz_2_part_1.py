my_list = [1, 2.54, 'Hello', True, [5, 6], (1, 2), {1, 2, 3}, {1: 'A', 2: 'B'}, None,
           complex(4, 5), b'text', bytearray(b'some text')]
for i, el in enumerate(my_list, 1):
    print(f'{i}-й элемент \033[4m{el}\033[0m является типом: \033[4m{type(el)}\033[0m')
