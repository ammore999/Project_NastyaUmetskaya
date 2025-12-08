#2. Дан целочисленный список размера N. Найти количество различных элементов в
#данном списке.
import random

lst = []
N =10
for i in range(N):
    random_int = random.randint(1, 100)
    lst.append(random_int)



print("Список:", lst)

number = len(set(lst))
print("Количество различных элементов:", number)
