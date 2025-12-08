#1. Дана строка. Если она представляет собой запись целого числа, то вывести 1, если вещественного (с дробной частью) — вывести 2;
# если строку нельзя преобразовать в число, то вывести 0. Считать, что дробная часть вещественного числа отделяется
#от его целой части десятичной точкой «.».

def check_number_type(s):
    try:
        float_value = float(s)

        if float_value.is_integer():
            return 1
        else:
            return 2
    except ValueError:
        return 0

test_strings = input('Введите ')
test = test_strings.split()
for test_str in test:
    result = check_number_type(test_str)
    print(test_str , "=", result)

