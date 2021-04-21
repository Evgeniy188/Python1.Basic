from sys import argv
from itertools import cycle

'''
Скрипт выводит элементы списка, определенного заранее, в количестве заданном
'''

name, k = argv

my_list = ['a', 'b', 'c', 'd', 'e']
i = 1
try:
    for el in cycle(my_list):
        if i > int(k):
            break
        print(el)
        i += 1
except:
    print('Введены некорректные параметры.')
