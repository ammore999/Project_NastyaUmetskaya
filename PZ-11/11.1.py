'''1.В последовательности на n целых элементов найти среднее арифметическое
элементов первой трети.'''



import random
from functools import reduce

n = random.randint(4, 20)
print(n)

numbers = [random.randint(-20, 20) for x in range(n)]
print(numbers)

third = len(numbers)// 3
print(third)

third_half = numbers[:third]
print(third_half)

summa = reduce(lambda x, y: x+y, third_half)
print(summa)
averge = summa//third
print(averge)
