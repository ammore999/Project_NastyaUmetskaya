'''Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
последних сроках и столбцах матрицы Matr2 произвольного размера.'''

import random
size = int(input('введите размер матрицы'))
Matr2 = [[random.randint(-10,10) for _ in range(size)] for _ in range(size)]

for row in Matr2:
    print(row)
Matr1=[row[1:-1] for row in Matr2[1:-1]]

print('Матрица Matr1:')
for row in Matr1:
    print(row)