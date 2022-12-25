"""
1. Напишіть клас для роботи з матрицями. Клас повинен створювати об'єкт матриць з вкладених списків, виводити матриці
на друк, виконувати операції додавання, віднімання, множення на число, множення на матрицю, транспонування. Передбачте
можливість приведення матриць для операцій додавання і віднімання, та обробку виключних ситуацій для операції множення
матриці на матрицю.
"""

import random


def create_matrix(x, y):
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(0, 100))
    return Matrix(array)


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += " ".join([str(x) for x in row]) + "\n"
        return result

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матриці мають різні розміри")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матриці мають різні розміри")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.matrix[i][j] * other)
                result.append(row)
            return Matrix(result)
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Несумісні розміри матриць для множення.")
            result = []
            for i in range(self.rows):
                row = []
                for j in range(other.cols):
                    sum = 0
                    for k in range(self.cols):
                        sum += self.matrix[i][k] * other.matrix[k][j]
                    row.append(sum)
                result.append(row)
            return Matrix(result)

    def transpose(self):
        result = []
        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append(self.matrix[j][i])
            result.append(row)
        return Matrix(result)


x = random.randint(2, 5)
y = random.randint(2, 5)
rmult = random.randint(1, 100)

matrix1 = create_matrix(x, y)
print(f"Сгенерована матриця 1 ({x}x{y}):\n{matrix1}")
matrix2 = create_matrix(x, y)
print(f"Сгенерована матриця 2 ({x}x{y}):\n{matrix2}")


res = matrix1 + matrix2
print(f"Результат сумми матриць:\n{res}")

res = matrix1 - matrix2
print(f"Результат різниці матриць:\n{res}")

res = matrix1 * rmult
print(f"Результат множення матриці 1 на число {rmult}:\n{res}")

res = matrix2 * rmult
print(f"Результат множення матриці 2 на число {rmult}:\n{res}")

res = matrix1 * matrix2
print(f"Результат множення матриць:\n{res}")

res = matrix1.transpose()
print(f"Результат транспонування матриці 1:\n{res}")