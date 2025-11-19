import re
import os

# Определяем путь к файлу, где лежит main.py
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'main.txt')
file_path2 = os.path.join(current_dir, 'emails.txt')
file_path3 = os.path.join(current_dir, 'phones.txt')
# Чтение файла
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Поиск email адресов (исправлена ошибка точки перед text)
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
phones = re.findall(r'\+996\d{9}', text)
names = re.findall(r'Имя:\s*([^,]+)', text)
#print(phones)
print(names)

#Запись найденных номеров в новый файл
with open(file_path3, 'w', encoding='utf-8') as f:
    for phone in phones:
        f.write(phone + '\n')


# Запись найденных адресов в новый файл
with open(file_path2, 'w', encoding='utf-8') as f:
    for email in emails:
        f.write(email + '\n')

#print(emails)
