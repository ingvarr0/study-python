#                                            **Завдання 1: Створення класу і об'єктів**
from inspect import ClassFoundException


class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def get_attr(self):
        print(self.__dict__)

    def make_sound(self):
            if self.species == 'cow':
                print(f'{self.species} makes sound : Moo')
            elif self.species == 'cat':
                print(f'{self.species} makes sound : meow')
            elif self.species == 'dog':
                print(f'{self.species} makes sound : a bark')
            elif self.species == 'chiken':
                print(f'{self.species} makes sound : peep')
            else:
                print('Введіть іншу тварину')

Animal1 = Animal('Alex', 'cat', 3)
Animal1.get_attr()
Animal1.make_sound()

Animal2 = Animal('Doris', 'cow', 9)
Animal2.get_attr()
Animal2.make_sound()


#                                               **Завдання 2: Робота з об'єктами**

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        s = self.height * self.width
        print(f'Площа прямокутника дорівнює: {s}')

rect1 = Rectangle(12, 14)
rect1.calculate_area()

rect2 = Rectangle(2, 8)
rect2.calculate_area()

