# Інкапсуляція

class Card:
    """Class Card for users card"""

    def __init__(self, card_number, balance):
        if self.__check_attribute_type(card_number, str):
            self._card_number = card_number      # _card_number - протектед (protected)
        if self.__check_attribute_type(balance, float):
            self.__balance = balance        # __balance - прайвет (private)

# Реалізація гетеру
    def get_card_data(self):        #визначимо метод повернення даних
        return self.__dict__

#Реалізація сетеру
    def set_card_data(self, attr, value):
        if self.__check_attribute_type(attr, str):
            self.__dict__[attr] = value
            return {attr: self.__dict__[attr]}
        else:
            return 'Attribute must be string type'

# Реалізація приватний метод check для перевірки типів даних, які передаються при створенні об'єкта класа
    def __check_attribute_type(self, attr, should_be):
        if type(attr) == should_be:
            return True
        else:
            raise TypeError(f'Attribute must be {should_be}')


user_card_1 = Card("4145 3454 6787 9043", 1000.0)

print(user_card_1.__dict__)     # {'_card_number': '4145 3454 6787 9043', '_Card__balance': 1000}
# спробуємо отримати доступ до атрибуту ззовні
#print(user_card_1.__balance)    # AttributeError: 'Card' object has no attribute '__balance'
# Коли ми пишемо два підкреслювання (__) ми кажемо, що ця властивість буде приватною і ми не зможемо отримати до неї доступ
# ззовні, але можна отримати доступ шляхом print(user_card_1._Card__balance) - ми зможемо отримати до нього доступ, але
# цього робити не варто. Зазвичай прайветом (private) позначаються властивості, які взагалі не треба чіпати і вони мають
# дуже важливу роль, яка впливає на критичний функціонал програми
print(user_card_1.get_card_data())

print(user_card_1.set_card_data('card_number', "4145 0000 6787 9043"))  # {'card_number': '4145 0000 6787 9043'}
print(user_card_1.set_card_data('balance', 100))        # {'balance': 100}


# -------------------------------------------------- Абстракція--------------------------------------------------------

from abc import ABC, abstractclassmethod


class Car(ABC):

    def __init__(self, mark, cost):
        self.mark = mark
        self.cost = cost

    @abstractclassmethod # декоратор
    def car_preview(self):
        pass

# класи, які будуть оголошуватись далі, які будуть наслідуватись від класу car повинні реалізовувати метод car_preview
# якщо вони цього не зроблять, то вони будуть вважатися абстрактними
# декоратор каже які методи є абстрактними у абстрактному класі

class Toyota(Car):
    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")

class Mersedes(Car):
    def car_preview(self):
        print(f"car {self.mark} costs {self.cost}")

class BMW(Car):
    pass

toyota = Toyota("offroad", 1000)
toyota.car_preview()
mersedes = Mersedes('crossover', 5000)
mersedes.car_preview()
#bmw = BMW('city_type', 4000)
#bmw.car_preview()       # TypeError: Can't instantiate abstract class BMW without an implementation
                            # for abstract method 'car_preview' - це означає, що ми повинні реалізовувати в наших класах
                            # метод car_preview, якщо було б п'ять чи десять, всі треба було реалізувати, бо це
                            # специфікація за якою ми повинні чітко слідувати


class Animal(ABC):
    @abstractclassmethod
    def move(self):
        pass

    @abstractclassmethod
    def eat(self):
        pass

class Cat(Animal):
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def move(self):
        print(f'Cat with {self.color} color moves to ahead')

    def eat(self):
        print(f'Cat ate this food {self.age} years')

class Dog(Animal):
    def __init__(self, distance, food_type):
        self.distance = distance
        self.food_type = food_type

    def move(self):
        print(f'Dog walked {self.distance} km')

    def eat(self):
        print(f'Dog ate this food {self.food_type} today')


class AnimalType(Animal):
    pass

class Bird(AnimalType):

    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'Bird {self.name} flyes')

    def eat(self):
        print(f'Bird {self.name} ate two days ago')

# У нас є клас Animal з двома абстрактними методами move та eat. У нас є клас Cat, який реалізує в собі ці два методи
# клас Dog, який так само в собі реалізує ці два методи, клас AnimalType, який просто наслідуваний, але не реалізує нічого
# і клас Bird, який унаслідуваний від класу AnimalType
# По логіці, якби ми викликали якісь методи від класу AnimalType, то повинна була б випасти помилка, але цього не буде
#Чому? Тому, що якщо цей клас AnimalType не реалізує методи move та eat він також вважається абстрактним і за рахунок того,
# що він унаслідував всі властивості з класу Animal, все що є в класі, то ніякої помилки не буде, але якщо ми будемо
# працювати напряму з цим класом, то помилки будуть падати

cat = Cat('red', 7)
cat.move()
cat.eat()

dog = Dog(10, 'meat')
dog.move()
dog.eat()

bird = Bird('Lusy')
bird.move()
bird.eat()

# animal_type = AnimalType()        animal_type = AnimalType()
                                    # TypeError: Can't instantiate abstract class AnimalType without an implementation
                                    # for abstract methods 'eat', 'move'
# animal_type.move()
# animal_type.eat()

# Помилка, бо в цьому класі не реалізовано потрібні методи
# Корисно у великих компаніях, при професійній розробці, оскільки за рахунок цього, ви можете структурувати свій код
# створювати абстрактні класи для того, щоб в якихось модулях мати змогу використовувати цю специфікацію за рахунок якої
# ви матимете структурований код, ваші співробітники/колеги матимуть розуміння що ви хочете бачити, якщо вони вносять
# правки в ваші модулі або ваші файли і не втручатися в логіку вашого коду зі своїми методами, які не реалізовані, які
# ви не хочете бачити при роботі з вашим абстрактним класом

# за рахунок інкапсуляції можете обмежувати доступ до вашого коду або вказувати на те, що не треба чіпати
# а за рахунок абстракції чітко структурувати та вказувати розробникам як варто працювати з вашим кодом, щоб все гарно
# виглядало та працювало як треба