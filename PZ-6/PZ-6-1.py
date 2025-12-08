#1. Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму элементов
#списка с номерами от K до L включительно.
import random

K = int(input("введите индекс:"))
L = int(input("введите индекс:"))
lst = []

for i in range(10):
    random_int = random.randint(1, 10)
    lst.append(random_int)


sum_result = 0
for i in range(K, L + 1):
    sum_result += lst[i]
print(lst)
print("Сумма элементов списка:" , sum_result )
