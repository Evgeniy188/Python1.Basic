#### 4
n = int(input('Введите целое положительное число: '))
max = 0
while n > 0:
    num = n % 10
    if num > max:
        max = num
    n = n // 10
print(max)
