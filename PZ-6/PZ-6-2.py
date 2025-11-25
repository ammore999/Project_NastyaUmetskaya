#2. Дан целочисленный список размера N. Найти количество различных элементов в
#данном списке.
import random

N = 10
lst = [random.randint(1, 20) for _ in range(N)]
print("Список:", lst)

number = len(set(lst))
print("Количество различных элементов:", number)
