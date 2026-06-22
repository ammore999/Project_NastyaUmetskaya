'''В матрице найти среднее арифметическое элементов последних двух столбцов'''



import random
size = int(input('введите размер матрицы'))
matrix = [[random.randint(-10,10) for _ in range(size)] for _ in range(size)]

for row in matrix:
    print(row)
last_two_colums = []
for row in matrix:
    last_two_colums.append(row[-2:])
print(last_two_colums)

num_rows=len(matrix)
print(num_rows)

col1_sum=sum(row[0] for row in last_two_colums)
col2_sum=sum(row[1] for row in last_two_colums)

col1_averge = col1_sum/num_rows
col2_averge = col2_sum/num_rows
print('сред ареф для предпоследнего столбца',col1_averge)
print('сред ареф для последнего столбца',col2_averge)