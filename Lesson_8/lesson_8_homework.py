# Завдання 1: Інкапсуляція
class User:
    '''Class User'''
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self. __password = password

    def get_user_data(self):
        print(self.__dict__)
        print(self.__name, self.__email, self.__password)

    def set_user_data(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

user_1 = User('Ihor', 'ihor.qwerty@gmail.com', "13f31")
user_1.get_user_data()
user_1.set_user_data('Oleg', '123Oleg@ukr.net', '123f21')
user_1.get_user_data()

# Завдання 2: Абстракція
from abc import ABC, abstractclassmethod
import math
import matplotlib


class Shape(ABC):
    """Class Shape"""

    @abstractclassmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        s = math.pi * (self.r ** 2)
        print(f'Площа кола з радіусом {self.r}: {s}')

class Rectangle(Shape):

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def calculate_area(self):
        s = self.side_a * self.side_b
        print(f'Площа прямокутника зі сторонами {self.side_a} та {self.side_b}: {s}')

class Triangle(Shape):

    def __init__(self, sideline, height):
        self.sideline = sideline
        self.height = height

    def calculate_area(self):
        s = 1/2 * self.sideline * self.height
        print(f'Площа трикутника зі стороною {self.sideline} та висотою {self.height}: {s}')

circle = Circle(4)
circle.calculate_area()

rectangle = Rectangle(5, 3)
rectangle.calculate_area()

triangle = Triangle(6, 2)
triangle.calculate_area()



#                                   Завдання 3: Користування інкапсуляцією та абстракцією у реальному коді
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def make_sound(self):
        pass

    def get_name(self):
        return self._name

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def show_animals(self):
        for animal in self._animals:
            print(f"{animal.get_name()} says: ", end="")
            animal.make_sound()

zoo = Zoo()
dog = Dog("Buddy")
cat = Cat("Whiskers")

zoo.add_animal(dog)
zoo.add_animal(cat)

zoo.show_animals()


# Клас Animal є абстрактним класом з абстрактним методом make_sound() і захищеним атрибутом _name.
# Класи Dog та Cat успадковують клас Animal і надають власні реалізації методу make_sound().
# Клас Zoo інкапсулює список тварин і надає методи для додавання тварин до зоопарку та відображення звуків, які вони видають.
# Інкапсуляція забезпечує приховування деталей реалізації класів, дозволяючи взаємодіяти з ними лише через визначені методи.
# Атрибут _name в класі Animal є захищеним, що вказує на те, що він не повинен бути змінений напряму зовнішнім кодом.
# Замість цього надається метод get_name(), який забезпечує контрольований доступ до значення атрибута.
# У класі Zoo атрибут _animals також захищений, і його зміну чи доступ до нього можна здійснити лише через методи add_animal() та show_animals().
# Клас Zoo приховує внутрішню структуру списку тварин (_animals).
# Замість безпосереднього доступу до списку, можна використовувати методи, що гарантують правильну поведінку програми.
# Інкапсуляція захищає внутрішні дані від випадкових помилок і зберігає консистентність стану об'єктів.
#
# Клас Animal є абстрактним (ABC) і визначає шаблон для всіх підкласів, що наслідуються від нього.
# Метод make_sound() є абстрактним і змушує підкласи (Dog, Cat) реалізувати власну версію цього методу.
# Це забезпечує єдиний інтерфейс для різних видів тварин.
# Клас Zoo працює з об'єктами класу Animal або його підкласів, абстрагуючись від деталей конкретних реалізацій (наприклад, звуку, який видає тварина).
# У методі show_animals() він однаково взаємодіє з об'єктами Dog і Cat.
# Завдяки абстракції і наслідуванню, можна викликати метод make_sound() для будь-якої тварини без потреби знати,
# до якого конкретного класу вона належить. Це спрощує масштабування програми.
# Абстракція дозволяє створювати гнучкий і розширюваний код. Якщо потрібно додати новий тип тварини (наприклад, Bird),
# достатньо реалізувати новий підклас Animal і визначити метод make_sound().
#
# Код структурований у вигляді класів із чітко визначеними методами і відповідальністю, що робить його легким для читання
# та розуміння.
#
# Загальні методи (наприклад, get_name()) визначаються в базовому класі Animal і повторно використовуються у підкласах.
#
# Окремо можна тестувати Zoo, Dog, Cat, що знижує ризик помилок при зміні або додаванні нового функціоналу.











