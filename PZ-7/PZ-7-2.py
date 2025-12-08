#2. Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами (одним или
# несколькими). Преобразовать каждое слово в строке, заменив в нем все предыдущие вхождения его последней буквы на символ
#«.» (точка). Например, слово «МИНИМУМ» надо преобразовать в «.ИНИ.УМ».
#Количество пробелов между словами не изменять
def process_string(s):
    words = s.split()
    processed_words = []

    for word in words:
        last_char = word[-1]
        without_last = word[:-1]
        replaced = without_last.replace(last_char, '.')
        new_word = replaced + last_char
        processed_words.append(new_word)

    return ' '.join(processed_words)

input_string = "МИНИМУМ АБББАКХАДА АХХХХ"
result = process_string(input_string)
print("Исходная строка:", input_string)
print("Результат:     ", result)