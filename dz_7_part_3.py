class Cell:
    def __init__(self, num: int):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        return Cell(self.num - other.num) if (self.num - other.num) > 0 else print('Вычитание клеток не возможно!')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(round(self.num / other.num))

    def __str__(self):
        return f'Число ячеек в клетке: {self.num}'

    def make_order(self, n):
        s = []
        for i in range(self.num//n):
            s.append(f"{'*' * n}")
        s.append(f"{'*' * (self.num % n)}")
        return '\n'.join(s)


cell_1 = Cell(5)
cell_2 = Cell(9)
print(Cell.__add__(cell_1, cell_2))
print(Cell.__sub__(cell_1, cell_2))
print(Cell.__sub__(cell_2, cell_1))
print(Cell.__mul__(cell_1, cell_2))
print(Cell.__truediv__(cell_2, cell_1))
print(Cell(14).make_order(4))
