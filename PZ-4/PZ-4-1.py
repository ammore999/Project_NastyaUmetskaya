#1. Дано вещественное число X и целое число N (> 0). Найти значение выражения X -X3/(3!) + X5/(5!) - ... + (-1)N-X2-N+1/((2-N+1)!) (N! = 12 ...N).
# Полученное число является приближенным значением функции sin в точке X.

import math

try:
    x = float(input("Введите значение x: "))
    n = int(input("Введите значение N: "))

    result = 0
    i = 1

    while i <= n:
        factorial = math.factorial(2 * i - 1)

        term = ((-1) ** (i - 1)) * (x ** (2 * i - 1)) / factorial

        result += term
        i += 1

    print ("Приближенное значение sin x:", result)

except ValueError :
    print(f"Ошибка: ")