
'''1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Сумма элементов:
Элементы до n-1 умножены на элемент n: '''



num = ['1, 2, 3, 4, 5, -6, -7 , -8, -9, -10']

file = open("text1.txt",'w', encoding='utf-8')
file.writelines(num)
file.close()

file = open("text1.txt",'r', encoding='utf-8')
data = file.read().strip()
file.close()

numbers = []
nums = data.split(',')
for num in nums:
    numbers.append(int(num))
count = len(numbers)
total = sum(numbers)
last = numbers[-1]
new_numbers = []
for i in numbers[:-1]:
    i *= last
    new_numbers.append(i)


file = open('txt2.txt', 'w', encoding='utf-8')
file.write('Исходные данные:' + data + '\n')
file.write('Количество элементов:' + str(count) + '\n')
file.write('Сумма элементов:' + str(total) + '\n')
file.write('Элементы до n-1 умножены на элемент n: ' + str(new_numbers) + '\n')




