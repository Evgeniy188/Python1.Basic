# # 1-й способ заполнения списка
# my_list = []
# while True:
#     my_list.append(input('Введите элемент списка (для окончания ввода оставить пустую строку): '))
#     if my_list[len(my_list)-1] == '':
#         my_list.pop()
#         break
# print(my_list)

# 2-й способ заполнения списка
my_list = input('Введите элементы списка через пробел: ').split()
print('Исходный список:\n', my_list)
my_list2 = my_list[:]
# Обмен значениями через кортежи
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

# Обмен значения через временную переменную
for i in range(0, len(my_list2) - 1, 2):
    tmp = my_list2[i]
    my_list2[i] = my_list2[i+1]
    my_list2[i+1] = tmp
print(my_list2)