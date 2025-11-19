#условные операторы и циклы
while True:
    color = str(input('какой цвет горит? '))
    if color == 'красный':
        print(f'горит - {color} - Остановись!')
    elif color == 'желтый':
        print(f'горит - {color} - Жди!')
    elif color == 'зеленый':
        print(f'горит - {color} - Едь!')
    else:
        print('Используй ПДД!')
    exit_ = str(input('вы уверенны что хотите выйти из игры?'))
    if exit_ == 'да':
        print('всего хорошего!')
        break
    else:
        continue



#While - работает до тех пор пока значение не станет False
# apple = 10
# box_bad = 0
# box_good = 0
# print(f'яблоки - {apple}')
# while apple !=0:
#     answer = str(input('какое яблоко? хор/плох '))
#     if answer == 'хор':
#         apple -= 1
#         box_good +=1
#         print(f'хор яблоки - {box_good}\n{apple}')
#     if answer == 'плох':
#         apple -= 1
#         box_bad +=1
#         print(f'плох яблоки - {box_bad}\n{apple}')

# print(f'хор яблоки - {box_good}\nплох яблоки - {box_bad}')





# ==, >=, <=,  != , > , <, or, and , not

# # с 20 января по 18 февраля или с 21 января по 19 февраля
# day = int(input('какой ваш день рождения? '))
# month = int(input('какой у вас месяц рождения '))
# if (month == 1 and 20 <= day <= 31) or (month == 2 and 1 <= day <= 18):
#     print('Вы водолей')
# else:
#     print("Error")




#if elif else
# color = str(input('какой цвет горит? '))
# if color == 'красный':
#     print(f'горит - {color} - Остановись!')
# elif color == 'желтый':
#     print(f'горит - {color} - Жди!')
# elif color == 'зеленый':
#     print(f'горит - {color} - Едь!')
# else:
#     print('Используй ПДД!')
