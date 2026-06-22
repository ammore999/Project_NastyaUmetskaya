'''2. Из предложенного текстового файла (text18-19.txt) вывести на экран его содержимое,
количество символов, принадлежащих к группе букв. Сформировать новый файл, в
который поместить текст в стихотворной форме предварительно заменив символы верхнего
регистра на нижний.'''



file = open("poem.txt", "w", encoding="utf-8")
file.write("Изведал враг в тот день немало,\n"
          "Что значит русский бой удалый,\n"
          "Наш рукопашный бой!..\n"
          "Земля тряслась — как наши груди,\n"
          "Смешались в кучу кони, люди,\n"
          "И залпы тысячи орудий\n"
          "Слились в протяжный вой…")
file.close()


file = open("poem.txt", "r", encoding="utf-8")
text = file.read()
file.close()

print("Содержимое файла:")
print(text)


letter_count = 0
for char in text:
    if char.isalpha():
        letter_count += 1

print("Количество символов, принадлежащих к группе букв:", letter_count)

lower_text = text.lower()

new_file = open("poem_lower.txt", "w", encoding="utf-8")
new_file.write(lower_text)
new_file.close()


