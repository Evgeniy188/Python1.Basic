def my_fun(a, b, c):
    if c <= a and c <= b:
        return a + b
    elif b <= a:
        return a + c
    else:
        return b + c


print(my_fun(3, 1, 2))
