ranking_list = [7, 5, 3, 3, 2]
print('Существующий рейтинг:\n', ranking_list)
n = int(input('Введите новый элемент: '))

if n > ranking_list[0]:
    ranking_list.insert(0, n)
elif n <= ranking_list[len(ranking_list) - 1]:
    ranking_list.append(n)
else:
    for i in range(0, len(ranking_list) - 1, 1):
        if ranking_list[i] == n and ranking_list[i + 1] != n:
            ranking_list.insert(i + 1, n)
            break
print('Новый рейтинг:\n', ranking_list)
