#try except

#calc
while 1:
        try:
            number_1 = float(input('введите первое число: '))
            operation = str(input('Выберите операцию + - * /: '))
            number_2 = float(input('введите второе число: '))
        except:
            print('пишите только числа!')
            continue
        
        if operation == '+':
            print(f'{number_1}+{number_2}={number_1+number_2}')
        elif operation == '-':
            print(f'{number_1}-{number_2}={number_1-number_2}')
        elif operation == '*':
            print(f'{number_1}*{number_2}={number_1*number_2}')
        elif operation == '/':
            print(f'{number_1}/{number_2}={number_1/number_2}')
        else:
            print('404... Пожалуйста выберите только + - * /')
    














# try:
#     number1 = '1'
#     number2 = 2

#     print(sum(number1+number2))
# except:
#     print('Какая то ошибка в коде')