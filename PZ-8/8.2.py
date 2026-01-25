#Используя словарь посчитать количество уникальных слов в заданном предложении
#«Изучаем язык Питон». Вывести на экран каждую пару «ключ:значение».

sent= "Изучаем язык питон"
words = sent.split()
uniq = {}
for word in words:
    if word in uniq:
        uniq[word]+=1
    else:
        uniq[word]=1
print(len(uniq))

for key, value in uniq.items():
    print( key, value)