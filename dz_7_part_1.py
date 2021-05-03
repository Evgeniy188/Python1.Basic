class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            for k in self.matrix[i]:
                s = s + str(k) + ' '
            s = s + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            print('Матрицы не одинаковые по размеру! Сложение не возможно!')
            return -1
        else:
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    print('Матрицы не одинаковые по размеру! Сложение не возможно!')
                    return -1
        sum_matrix = [[0 for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                sum_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(sum_matrix)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_3 = Matrix([[1, 2, 3], [4, 5, 6]])
print(Matrix.__add__(matrix_1, matrix_2))
print(Matrix.__add__(matrix_1, matrix_3))
print(Matrix.__add__(matrix_3, matrix_1))
