# #dict - словари 

# #key - value

# student = {
#     'name': 'Sam',
#     'age': 21,
#     True : 'education',
#     183: 'height',
#     False:True,
#     'number': ['0312', '2345']
# }

# student['number'].append('qwerrt')

# #добавление
# student.update(kuznetsov=1234)

# #изменение
# student.update(age=22)

# #удаление
# del student['name']

# #Преобразование пар ключ и значение
# for key, value in student.items():
#     print(f'{key} - {value}')

# # print(student)
flags = {
    'ru': {'red blue', 'white'},
    'kg': {'red yellow', 'red'},
    'ua': {'red blue', 'red', 'blue'},
    'uk': {'yellow', 'blue'},
    'kz': {'blue yellow', 'blue'}
}

while True:
    color1 = input('enter the color of a country flag:')
    found = False
    for country, flag in flags.items():
        if color1 in flag:
            print(country)
            found = True
    if not found:
        print('not found')



