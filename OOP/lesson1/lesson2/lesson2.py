class Animal:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def pets(self, bark):
        return f'Это животное может лаять? {bark}'

    def __str__(self):
        return f'Цвет - {self.color}\nВес - {self.weight} кг'


class Cat(Animal):
    def __init__(self, color, weight, name):
        Animal.__init__(self, color, weight)  # вызываем напрямую Animal
        self.name = name

    def __str__(self):
        return Animal.__str__(self) + f'\nИмя - {self.name}'


class Dog(Animal):
    def __init__(self, color, weight, age):
        Animal.__init__(self, color, weight)
        self.age = age

    def __str__(self):
        return Animal.__str__(self) + f'\nВозраст - {self.age}'


class CatDog(Cat, Dog):
    def __init__(self, color, weight, name, age):
        Cat.__init__(self, color, weight, name)
        Dog.__init__(self, color, weight, age)

    def __str__(self):
        return f'{Cat.__str__(self)}\n{Dog.__str__(self)}'


# Проверим
catdog = CatDog(color='серый', weight=4, name='Мурзик', age=3)
print(catdog.pets(bark=True))
print(catdog)
