#Name = "Tom1"
#_name__41 = "Tom"
#print(Name, _name__41)
#---------------------------------
#user_email = 'example@gmail.com' #under_score
#userEmail = 'example@gmail.com' #camelCase
#print(user_email, userEmail)
#---------------------------------
name = 'John'
print(name)

name = 'Tom'
print(name)
#---------------------------------
num_1 = 100
num_2 = 10
num_3 = num_1 + num_2
print(num_3)

num_3 = num_1 - num_2
print(num_3)

num_3 = num_1 * num_2
print(num_3)

num_3 = num_1 / num_2
print(num_3)
#---------------------------------
num_1 = 7
num_2 = 2

num_3 = num_1 / num_2
num_4 = num_1 // num_2 # Цілочисельне ділення - скільки цілих цисел поміщається в іншому числі
print(num_3, num_4)

#---------------------------------
num_1 = 5
num_2 = 2

num_3 = num_1 ** num_2 # (Піднесення до степеня): одне число в степені іншого
print(num_3)
#---------------------------------
num_1 = 7
num_2 = 2

num_3 = num_1 % num_2 # Залишок від ділення
print(num_3)

#---------------------------------
num_1 = 10
num_2 = 5

num_3 = num_1 == num_2 # рівно
print(num_3)

#---------------------------------
num_1 = 10
num_2 = 5

num_3 = num_1 != num_2 # не рівно
print(num_3)

#---------------------------------
num_1 = 10
num_2 = 5

num_3 = num_1 < num_2 # менше
print(num_3)

#---------------------------------
num_1 = 10
num_2 = 5

num_3 = num_1 > num_2 # більше
print(num_3)

#---------------------------------
num = 10
name = 'Tom'

result = num > 5 and name == 'Tom'
print(result)

#---------------------------------
num = 10
name = 'Tom'

result = num < 5 or name == 'Tom'
print(result)

#---------------------------------
num = 10
name = 'Tom'

message = 'Tom got some money'
print(name in message) # True

name = 'John'
message = 'You won!'
print(name not in message) #True

#---------------------------------
age = 50
name = 'Ira'
animal = 'cat'

print(age == 50 and 'I' in name and animal != 'dog') # True всі умови виконано
print(age == 50 and 'I' in name or animal != 'dog') #True - оператор виконується послідовно, перші два оператори дають True
#True or animal != 'dog'

#---------------------------------#---------------------------------#---------------------------------

num_1 = 5
print(type(num_1)) #<class 'int'>

num_2 = 3.14
print(type(num_2)) #<class 'float'>

string = 'hello'
print(type(string)) #<class 'str'>

check = True
print(type(check)) #<class 'bool'>

lst = [1, 2, 3]
print(type(lst)) #<class 'list'>

lst = ['my', 'name', 'is', 'Tom']
print(type(lst)) #<class 'list'>

tpl = (1, 2, 3)
print(type(tpl)) #<class 'tuple'>

dct = {'name': 'John', 'age' : 23}
print(type(dct)) #<class 'dict'>

set_ex = {1, 2, 3}
print(type(set_ex)) # <class 'set'>

print(type(None)) # <class 'NoneType'>

class Person:
    pass

a = Person()
print(type(a)) #<class '__main__.Person'> посилання на наш клас


#---------------------------------#---------------------------------#---------------------------------

lst = [1, 2, 3, 4, 5]
dct = {'name': 'Tom', 'age': 5}
name = 'Tom'
tpl = ('n', 'a', 'g')

result = dct['age'] in lst # Чи є вік Тома в списку (ключ 'age')
print(result) #True

result = dct['age'] in lst and dct['name'] in tpl # Чи є вік Тома в списку (ключ 'age') І чи є ім'я Тома в tpl (ключ 'name')
print(result) #False

print(dct['name'] == name) #True (перевірка чи ключ 'name' дорівнює змінній name і те і те посилається на Tom)
print(dct['name'] == name and dct['age'] in lst) #True

                                                    # Вбудовані функції

num_1 = '1'
print(type(num_1)) #<class 'str'>
num_1 = int(num_1)
print(type(num_1)) #<class 'int'>
print(num_1) # 1
num_1 = float(num_1)
print(type(num_1)) #<class 'float'>
print(num_1) #1.0

#--------------------------------- Функції для рядків

string = 'hello world!'
print(len(string))              # 12
string = string.upper()         # Перехід у верхній регістр всіх символів
print(string)                   # HELLO WORLD!
string = string.lower()         # Перехід у нижній регістр всіх символів
print(string)                   # hello world!
string = string.capitalize()    # тільки перша буква у верхньому регістрі
print(string)                   # Hello world!

string = string.replace('!', '.') # Перше значення - що ми хочемо замінити, а друге - те на що ми хочемо замінити
print(string)                                 # Hello world.
string = string.split()                       # приймає значення, символ по якому будемо розбивати (розбивається по пробілу)
print(string)                                 # ['Hello', 'world.'] - отримали список із двох значень
string = 'hello world!'
string = string.split('o')                    # розбиваємо по 'o'
print(string)                                 # ['hell', ' w', 'rld!']

string = 'hello world!'
string = string.split('w')                    # розбиваємо по 'w'
print(string)                                 # ['hello ', 'orld!']

string = 'w'.join(string)                     # Передається параметр об'єднання (об'єднується по 'w')
print(string)                                 # hello world! - зробили зі списку рядок

string = string.count('o')                    # Порахувати кількість елементів
print(string)                                 # 2

string = 1                                    # Змінна string з типом даних int
string = str(string)                          # змінюємо тип даних
print(type(string))                           # <class 'str'>


#--------------------------------- Функції для списків та кортежів
base_list = [1, 2, 3]
print(len(base_list))           # 3 - кількість значень в списку - три значення
base_list.append(4)             # додає значення в кінець списка
print(base_list)                # [1, 2, 3, 4]

base_list.extend([5, 6, 7])     # розширюємо список іншим списком
print(base_list)                # [1, 2, 3, 4, 5, 6, 7]

print(base_list.index(4))       # 3 - Вивести індекс ЗНАЧЕННЯ 4, тобто ЗНАЧЕННЯ 4 знаходиться на ТРЕТІЙ позиції

#--------------------------------- Функції для словників
base_dict = {'name': 'Tom', 'age': 40, 'height': 180}
print(base_dict.keys())      # dict_keys(['name', 'age', 'height']) - Всі ключі словника
print(base_dict.values())    # dict_values(['Tom', 40, 180]) - Всі значення ключів словника

print(base_dict.items())     # dict_items([('name', 'Tom'), ('age', 40), ('height', 180)])
                             # Пари ключ-значення у формі кортежів, щоб потім, наприклад, присвоїти якимось змінним

print(base_dict['name'])     # Можемо звертатись до ключів через дужки і лапки і отримаємо ключ Tom
print(base_dict.get('name')) # Tom - перевага його над прямим зверненням до ключа, бо якщо ми передаємо неіснуючий ключ
print(base_dict.get('is_animal', 'No')) # То буде виведено значення 'No', в пошуках ключа 'is_animal' ми його не знайшли
                                        # і у разі відсутності повернули 'No' , якщо звертатись до словника у вигляді
                                        # ['is_animal'] , то отримаємо помилку відсутності ключа