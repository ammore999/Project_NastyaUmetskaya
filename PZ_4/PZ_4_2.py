#2. Дано целое число N (> 0). Найти сумму 1N + 2N-1 + ... + N1.
try:
    n = int(input("Введите значение N: "))
    
    summa = 0
    i = 1
    while i <= n:
        summa += i ** (n - i + 1)
        i += 1

    print("Сумма:", summa)

except ValueError :
    print("Ошибка")