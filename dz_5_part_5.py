from random import randint


def create_file(f_name: str, N):
    with open(f_name, 'w') as f_write:
        for i in range(N):
            f_write.write(str(randint(-999, 999)) + ' ')


def sum_number(f_name: str):
    sum = 0
    with open(f_name, 'r') as f_read:
        for el in f_read.read().split():
            sum += int(el)
    return sum


f_name = 'my_test5.txt'
N = 100
create_file(f_name, N)
print('Сумма чисел в файле =', sum_number(f_name))
