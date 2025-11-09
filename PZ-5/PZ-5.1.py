#1. Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр и т. д.
# Через сколько таких действий получится нуль?
def count_steps_to_zero(n):
    steps = 0
    while n > 0:
        digit_sum = 0
        temp = n

        while temp > 0:
            digit_sum += temp % 10
            temp //= 10

        n -= digit_sum

        steps += 1
    return steps

number = int(input("Введите число: "))
result = count_steps_to_zero(number)
print("колличесво шагов:", result)