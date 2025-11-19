#структура данных list tuple dict
#списки - несколько данных в 1 переменной

# индексация всегда начинается с 0
data_type = ['hello', 3.12, 'world', 33, True]

#create 
#append - добавление в конец списка нового элемента
data_type.append('Ivan')
#insert - добавляет элемент перед другим элементом указывается индекс
data_type.insert(1, False)

#удаление
data_type.remove(3.12)
del data_type[2]
#Изменение
data_type[0] = 'world'


print(data_type)



