#ООП - Объектно оринтированное программирование
#Наследование от матери к ребенку - > 
class Person:
    #Создание атрибутов
    def __init__(self, name, age, hair, height, education):
        self.n = name
        self.a = age
        self.h = hair
        self.h = height
        self.e = education
    
    def programming(self, language):
        return f'{self.n} может программировать на {language}'

    
    #Метод для вывода атрибутов в консоли
    def __str__(self):
        return f'Имя-{self.n}\nВозраст-{self.a}\nВолосы-{self.h}\nРост-{self.h}\nОбразование-{self.e}'
    
person_1 = Person(name='Ivan', age=18, hair='brown', height=1.90, education=False)
person_2 = Person(name='Ymyt', age=18, hair='white', height=2.0, education=False)

print(person_1)
print(person_1.programming('Java'))
print('-'*20)
print(person_2)
print(person_2.programming('PHP'))
print('-'*20)

class Teacher(Person):
    def __init__(self, name, age, hair, height, education, skills, iq):
        super().__init__(name, age, hair, height, education)
        self.sk = skills
        self.iq = iq

    def __str__(self):
        return super().__str__()+f'\nОпыт-{self.sk}\nIQ-{self.iq}'
    

person_3 = Teacher(name='Sam', age=21, hair='yellow', height=1.89, education=True, skills='MiddleDev', iq=150)
print(person_3)
print(person_3.programming('JavaScript'))


class Student(Teacher):
    def __init__(self, name, age, hair, height, education, skills, iq):
        super().__init__(name, age, hair, height, education, skills, iq)
        
    # точно так же
    