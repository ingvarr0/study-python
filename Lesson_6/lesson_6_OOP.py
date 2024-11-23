class Person:           # створимо клас
    """Class for creation persons"""    # doc string
    name ='Tom' # визначимо його атрибути
    age = 18    # визначимо його атрибути
    high = 180

# У класа є вланий простір імен, в якому ми можемо визначати методи, атрибути і можна до них звертатись через . (дот нотейшн)

print(Person.name, Person.age)  # Tom 18
Person.age = 50
print(Person.name, Person.age)  # Tom 50
print(Person.__dict__)  # можна поглянути, що лежить всередині класу

person1 = Person()# Створюємо екземпляр класу
print(person1.name, person1.age, person1.high)
print(person1)    # <__main__.Person object at 0x0000022AA96A6900> - посилається на об'єкт класу Person і займає обл. пам'яті

person2 = Person()# Створюємо ще один об'єкт
print(person2.name, person2.age, person2.high)
print(person1)    # <__main__.Person object at 0x000001DF84FF6900> - посилається на об'єкт класу Person і займає обл. пам'яті

# Обидва екземпляри класу посилаються на одні й ті самі атрибути
# У класу є свій простір імен, в якому ми визначаємо методи, атрибути, коли ми створюємо об'єкт класу
# у нього є власний простір імен, але в ньому нічого не лежить, він посилається на усе, що лежить в об'єкті класу від якого\
# він був створений

# Якщо ми хочемо щось створити у namespace (неймспейсі) об'єкту класу
person1 = Person()
person1.is_animal = False
print(person1.__dict__) # виводимо неймспейс об'єкту    {'is_animal': False} - в нього є свій власний атрибут
print(Person.__dict__)  # неймспейс класу Person і побачимо, що атрибута 'is.animal' немає, але в об'єкті класу
                        # в його неймспейсі є нова властивість is.animal
person2 = Person()
print(person2.__dict__) # У неймспейсі person2 теж нема атрибута 'is_animal',бо ми від об'єкта класа нічого нового не додавали
                        # і нічого старого не видаляли
person1 = Person()
print(getattr(person1, 'name'))  # Звертається до об'єктів (як в словнику - ключ класу) атрибут можна отримати через getattr
        # якщо звертатись до неіснуючого атрибута, то буде помилка, якщо нема впевненості в існуванні атрибута, тоді
print(getattr(person1,'where_is', False))   # буде виведено False


person1.age = 59
person1.color = 'black' # Якщо намагаємось змінити неіснуючий атрибут, то воно його просто створить
print(person1.__dict__)         # {'age': 59, 'color': 'black'}

setattr(person1, 'high', 100)
print(person1.high)         # 100
print(person1.__dict__)


print(hasattr(person1,'name'))# перевірити в класі (об'єкті класу) такий атрибут    - Виводить True - такий атрибут існує
print(hasattr(person1, 'where_is')) # виводить False - такого атрибуту нема


del Person.high         #видалення атрибуту
print(Person.__dict__)  # виведення неймспейсу класу
print(hasattr(Person, 'high'))      #False

delattr(Person, 'age')
print(Person.__dict__)
print(hasattr(Person, 'age'))   #False

#Видалення неважливих чи непотрібних атрибутів чи змінних дозволяє контролювати витрати пам'яті в процесі виконання програми
# getattr - треба прочитати атрибут, зрозуміти, що в ньому знаходиться
# setattr - треба змінити на основі отриманих даних те, що знаходиться в атрибуті
# hasattr - треба переконатися, що такий атрибут існує в класі (перед видалення наприклад треба переконатись, що атрибут є)
# delattr - видалення атрибуту

print(Person.__doc__)   # Class for creation persons


#------------------------------------------------Ініціалізація об'єктів через конструктор---------------------------------

class Person:
    """Class for creation persons"""
    def __init__(self, name, age):
        self.name = name    # self - об'єкт класу в якому зберігається посилання на створений об'єкт
        self.age = age

    def print_attrs(self):
        print(f">>>>>{str(self)}<<<<<")  # >>>>><__main__.Person object at 0x0000021C5A5B6900><<<<<
        print(self.name, self.age)

person1 = Person('Tom', 18)# Екземпляр класу
print(person1)      # <__main__.Person object at 0x0000021C5A5B6900>
person1.print_attrs()   # Tom 18 - результати роботи метода (функції) print_attrs

# У момент коли ми за допомогою круглих дужок створюємо об'єкт нашого класу передаємо туди атрибути (84 рядок)
# метод __init__ їх перехоплює і за допомогою self (self - це посилання на наш об'єкт класу person1 (person1 - це об'єкт
# класу Person, який посилається на об'єкт пам'яті 0x0000021C5A5B6900) у self зберігається те ж саме посилання на об'єкт
# класу Person і на ту саму комірку пам'яті) - self необхідне для того, щоб при зверненні до створеного об'єкту класу
# інтерпретатор розумів від якого саме об'єкту ми звертаємось до методів чи атрибутів, щоб розуміти які атрибути треба
# використовувати і які методи треба використовувати

person2 = Person('Oleg', 50)# створюємо другий екземпляр
print(person2)  # <__main__.Person object at 0x0000023C4F554E10>
person2.print_attrs()   # Oleg 50 >>>>><__main__.Person object at 0x0000023C4F554E10><<<<<

# Конструктор корисний тому, що нам не треба вручну додавати атрибути класу або об'єкту, якби його не було, це все як і в
# попередніх прикладах треба було б прописувати вручну кожен раз (створювати об'єкт, щоб до його властивостей мати доступ
# - щоб при створенні об'єкту класу були унікальні властивості, треба було б прописувати все вручну тому, що вони
# посилались би на ті що зберігаються у неймспейсі класу, а це незручно і тому використовується конструктор)


class Point:
    """Class for create and set coords"""

    def __init__(self, x, y, z):    # створюємо конструктор, передамо параметри x, y, z
        self.x = x      # Ініціалізація x
        self.y = y      # Ініціалізація y
        self.z = z      # Ініціалізація z
        self.get_attrs()       #можна додати після ініцалізації
        self.check_coords()    #можна додати після ініцалізації

    def check_coords(self):     # перевірка координат, не хочемо, щоб координати були меншими за 0
        # треба перевірити всі атрибути, які є в екземплярі класу
        for attr in self.__dict__:  # self - екземпляр класу, отримуємо доступ до його неймспейсу, щоб подивитися які
                                    # в нього є атрибути
            if getattr(self, attr, False) < 0:      # метод getattr - об'єкт self, в якості атрибуту attr, до якого я отримую
                                                # доступ, якщо його не існує, то False
                print("Coord can't be less than 0")
                setattr(self, attr, 0)      # встановлювати його як нуль
            elif getattr(self, attr, False) > 100:
                print("Coord can't be more than 100")
                setattr(self, attr, 100)

        print(self.__dict__)

    def get_attrs(self):
        print(self.__dict__)    # виводити на екран всі атрибути

    def set_attrs(self, x, y, z):   # змінювати атрибути
        self.x = x
        self.y = y
        self.z = z
        self.check_coords()

# Створимо об'єкти нашого класу
coord_1 = Point(-1, 101, 50)
coord_1.get_attrs()     # {'x': -1, 'y': 101, 'z': 50}
coord_1.check_coords()  #Coord can't be less than 0 ; Coord can't be more than 100 ; {'x': 0, 'y': 100, 'z': 50}

coord_1.set_attrs(1000, 1000, -5)   # {'x': 1000, 'y': 1000, 'z': -5}
coord_1.get_attrs()                     # {'x': 1000, 'y': 1000, 'z': -5}
coord_1.check_coords()   # Coord can't be more than 100 ; Coord can't be more than 100; Coord can't be less than 0 ;
                            # {'x': 100, 'y': 100, 'z': 0}

coord_1 = Point(-1, 101, 50)
print("----------------------------")
coord_1.set_attrs(1000, 1000, -5)
# and not isinstance(self.__dict__[attr], str) перевірка на інт (тільки інт) - можна робити окрему функцію