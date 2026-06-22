'''из исходного файда  выбрать хтмл коды изображений и посчитать'''


import re

with open('pazzl.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

image_tags = re.findall(r'<img[^>]+>', html_content)

print("Найденные HTML-коды изображений:")
for tag in image_tags:
    print(tag)

print(f"\nВсего найдено изображений: {len(image_tags)}")
