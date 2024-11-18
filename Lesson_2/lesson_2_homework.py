#1. Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None
from os.path import split

string = 'home'
integer = 4
f = 5.3
b = True
lst = [3, 2, 1, 'Kyiv']
dct = {'age': 18, 'country': 'Ukraine', 'sex': 'male'}
tpl = (6, 8, 2)
check = None

#2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі
a = integer * f
a1 = integer + f
a2 = integer - f
a3 = f / integer
k = 2
a4 = integer ** k
a5 = integer // k
a6 = integer % k
print(a, a1, a2, a3, a4, a5, a6)

result = f > integer
print(result)

result = f < integer and b
print(result)

result = f > integer and b
print(result)

result = string == 'home' or k > 3
print(result)

print(dct['country'] == 'Ukraine')

country = 'USA'
result = dct['country'] == country or 'Kyiv' in lst
print(result)

k=9
result = k in tpl
print(result)

k=6
result = k in tpl
print(result)

print(b == check)

# 3. Використати вивчені функції Python:
#   1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str = 125
print(type(num_str))
res = str(num_str)
print(type(res))
#   2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити усі букви 'y' на '0' та 'i' на '1'.
message = 'Hi, my name is Python!'
message = message.replace('y', '0')
print(message)
message = message.replace( 'i', '1')
print(message)

#   3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за допомогою функції split(),
#   а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
split_test = 'This is a split test'
split_test = split_test.split()
print(split_test)

string_join = ' '.join(split_test)
print(string_join)

#   4. Визначити довжину рядку string_join за допомогою функції len()
print(len(string_join))

#Робота зі списками:
#   1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5
list_append = [1, 2, 3]
print(list_append)
list_append.append(4)
print(list_append)

list_append.append(5)
print(list_append)

#   2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
list_extend = [4, 5, 6]
print(list_extend)
list_extend.extend([7, 8, 9])
print(list_extend)

#    3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
result = list_extend.index(6)
print(result)

#   4. Визначити довжину списку list_append за допомогою функції len()

print(len(list_append))

#Робота зі словниками:
#   1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані,
#   які знаходяться в ключах car та where
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}

print(dict_test.get('car'), dict_test.get('where'))
print(dict_test['car'], dict_test['where'])

#   2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
keys = dict_test.keys()
print(keys)

values = dict_test.values()
print(values)

#   3. За допомогою функції items() вивести на екран пари ключ - значення
print(dict_test.items())