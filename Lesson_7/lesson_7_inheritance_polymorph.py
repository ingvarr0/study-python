class A:
    ''''Class A'''
    name_a = 'Class A is parent'
    is_main_class = True

    def print_hello(self):
        print('Hello from A')

class B(A):
    """Class B"""
    name_b = 'class B is child'
    is_main_class = False
    def print_hello(self):
        print('Hello from B')

class C(B):
    """Class C"""
    pass

test_ex = C()
#test_ex.    #бачимо, що маємо доступ до name_a, name_b та is_main class. Як це працює? Коли ми хочемо викликати метод або
# звернутись до якоїсь властивості інтерпретатор шукає його в нашому класі від якого ми викликаємо це, від якого створений
# екземпляр класу, якщо такої властивості немає в цьому класі, воно йде на рівень нижче, шукає в класі B і якщо воно там є
# воно його викличе, в нашому випадку такого немає і воно йде ще на рівень нижче і шукає його в класі A і знаходячи, повертає
# результат до виклику
print(test_ex.name_a)   # Class A is parent
print(test_ex.name_b)   # class B is child
print(test_ex.is_main_class)    # Пише False, бо знайшло цю властивість у класі B і повернуло його у виклик
#print(test_ex.)      # У Python усі класи неявно унаслідували свої властивості від базового класу, коли створюється клас
                    # тобто коли пишемо class A , ми неявно наслідуємось від класу object, тобто class A(oject) в класі
                    # object є всі інші властивості

test_ex.print_hello()

#-----------------------------------------------------------------------------------------------------------------------
class Vehicle:
    '''It's a base class for Vehicles'''
    def __init__(self, type, color, left_of_life = 100):
        self.type = type
        self.color = color
        self.left_of_life = left_of_life
    def move(self):
        print('Your vehicle is moving')

    def fix(self):
        if self.left_of_life <= 50:
            print(f'{self.type} need to fix')
        else:
            print(f'Your {self.type} is good')
# створили базовий клас визначили в ньому метод __init__, наші атрибути класу і метод move



class Car(Vehicle):
    '''Class Car'''
    def __init__(self, type, color, left_of_life, cost = 0):
        super().__init__(type, color, left_of_life)
        self.cost = cost

    def move(self):
        print(f"{self.color} {self.type} is driving")
        print(f'Cost of this car: {self.cost}')
# визначили клас car, унаслідували його від класу Vehicle і також в ньому визначили метод __init__


class Bicycle(Vehicle):
    '''Class bicycle'''

    def __init__(self, type, color, left_of_life, count_of_wheels):
        super().__init__(type, color, left_of_life)
        self.count_of_wheels = count_of_wheels

    def move(self):
        print("You are so fast")


car_1 = Car('car', 'black', 70, 10000)   # екземпляр класу Car
car_1.move()
car_1.fix()

bicycle_1 = Bicycle('road_bicycle', 'blue', 30, 2000)
bicycle_1.move()
bicycle_1.fix()

# Цих методів fix ми не бачимо в класі Car та класі Bicycle, але знову ж таки отримали доступ до них у
# нашому батьківському класі. Якщо ми хочемо перевизначити його в цих класах, то ми можемо його викликати так само як і move

# ----------------------------------------------Поліморфізм-----------------------------------------------------------

class Counter:
    '''Count of something'''

    def __init__(self, count_obj, type_obj, max_elements):
        self.count_obj = count_obj
        self.type_obj = type_obj
        self.max_elements = max_elements

    def counter(self):
        print(f'Type of object: {self.type_obj}')       # виводить тип об'єкту
        if isinstance(self.count_obj, (list, dict, str, tuple)):   # перевірило чи тим об'єкту знаходиться у вказаних типах
            count = len(self.count_obj)
            if count > self.max_elements:
                print('Count elements of your object more than need')
                print(f'More on {count - self.max_elements}')
            else:
                print(f'Count of elements: {count}')
        else:
            print("Your object must be iterable")

    def get_attr(self):
        print(self.__dict__)

    # Метод зміни атрибута
    def set_attr(self, attr, value):              # передаємо назву атрибута - attr, передаємо його значення - value
        if hasattr(self, attr):     # перевірка чи є такий атрибут взагалі, в цьому класі
            setattr(self, attr, value)    # у разі якщо верхня умова True змінюємо атрибут (сетимо)
        else:
            print('Check your attrs')


class List_elements(Counter):
    ''''Class for list elements'''
    def __init__(self, count_obj, type_obj, max_elements):
        super().__init__(count_obj, type_obj, max_elements)
        pass

    def counter(self):
        super().counter()

    print("Operation was ended")

    def get_attr(self):
        super().get_attr()
        print('Operation was ended')

list_ex = List_elements([1, 2, 3, 4], 'list', 10)
list_ex.counter()
list_ex.get_attr()

list_ex.set_attr('count_obj', [1, 2, 3, 4, 5, 6])


# -----------------------------------Єдиний інтерфейс в базовому класі -----------------------------------------------
class BaseInterface:
    '''Base class'''
    def __init__(self):
       pass

    def get_attrs(self):
        pass

    def print_model(self):
        pass

    def count_of_price(self):
        pass

    def call_to_support(self):
        pass

class SiteInterface(BaseInterface):
    ''' Interface of our site'''

    def __init__(self, number, model, price):
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self):
        print(f'Model of site: {self.model}')


    def count_of_price(self):
        print(f'Count of site price: {self.price ** 2}')

    def call_to_support(self):
        print(f'Number of support is {self.number}')
        print(f"You can call from 8am to 7pm")

class AppInterface(BaseInterface):
    ''' Interface of our application'''

    def __init__(self, number, model, price):
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self):
        print(f'Model of application: {self.model}')


    def count_of_price(self):
        print(f'Count of application price: {self.price ** 2}')

    def call_to_support(self):
        print(f'Number of support is {self.number}')
        print(f"You can call from 8am to 7pm")


site_user = SiteInterface(12345, 'shop', 1000)
app_user = AppInterface(322324, 'android', 5000)

for user in (site_user, app_user):
    user.print_model()
    user.count_of_price()
    user.call_to_support()
    print("------------------")