from sys import argv
from itertools import count

'''
Скрипт выводит на экран целые числа начиная с заданного в заданном количестве 
'''
try:
    name, n, k = argv
    i = 1
    for el in count(int(n)):
        if i > int(k):
            break
        print(el)
        i += 1
except:
    print('Введены некорректные параметры.')
