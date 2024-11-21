#-----------------------------------------------Списки------------------------------------------------------------------

a = [1, 2, 3, 4, 5] # 0 1 2 3 4 - індекси спочатку, а якщо з кінця, то -5 -4 -3 -2 -1
b = ['apple', 'banana', 'cherry']

print(a[0], a[1], a[-1]) # виводимо перший, другий та останній елемент - 1 2 5
print(b[1])              # виводимо другий елемент - banana

print(a[1:4])  # [2, 3, 4] з першого по 4 елемент, тобто з індекса ОДИН до ТРЕТЬОГО (не включаючи четвертий)
print(a[::2])  # [1, 3, 5] береться ввесь список з кроком 2
print(b[::2])  # 'apple', 'cherry'] перший і третій елемент

print(a[::-1])  # [[5, 4, 3, 2, 1]] перевернути список і взяти всі елементи з кінця - береться повний список і крок -1
print(b[::-1])  # ['cherry', 'banana', 'apple'] крок -1, тобто список буде йти -1 -2 -3 -4 -5

#------------------------------------------Методи Списків------------------------------------------------------------------
a = [1, 2, 3, 4, 5] # 0 1 2 3 4 - індекси спочатку, а якщо з кінця, то -5 -4 -3 -2 -1
b = ['apple', 'banana', 'cherry']

a.append(6)            #додає елемент в кінець
b.append('tomato')     #додає елемент в кінець
print(a, b) # [1, 2, 3, 4, 5, 6] ['apple', 'banana', 'cherry', 'tomato']

a.insert(3, 7.4)       # Третім індексом стане True [1, 2, 3, 7.4, 4, 5, 6]
b.insert(3, "bottle")   # Третім індексом стане 'bottle'['apple', 'banana', 'cherry', 'bottle', 'tomato']
print(a)
print(b)

a.remove(7.4)           # Видалило зі списку 7.4
b.remove('bottle')      # Видалило зі списку 'bottle'
print(a,b)


last_elem_1 = a.pop()   # Видаляє і повертає останній елемент списку і присвоюється змінній
print(a)
last_elem_2 = b.pop()   # Видаляє і повертає останній елемент списку
print(b)
print(last_elem_1,last_elem_2)  # 6 tomato отримуємо елементи, які видалили

# видалимо конкретну позицію - перший елемент
first_elem_1 = a.pop(0)
first_elem_2 = b.pop(0)
print(first_elem_1, first_elem_2) # 1 apple

print(a.index(3), b.index('banana')) # 1 0 - бачимо, що трійка - це другий елемент, бо одиниця була видалена
                                     # 'banana' - це перший елемент, бо 'apple' було видалено

a.extend([5,5,5])                           # розширимо список трьома п'ятірками
b.extend(['cherry', 'banana', 'banana'])    # розширимо список двома 'banana' і 'cherry'
print(a.count(5), b.count('banana'), b.count('cherry')) # порахуємо кількість п'ятірок, кількість 'banana' та 'cherry' - 4 3 2
print(a, b)                             # [2, 3, 4, 5, 5, 5, 5] ['banana', 'cherry', 'cherry', 'banana', 'banana']


a.sort()    # Відсортувало в порядку зростання
b.sort()    # Відсортувало в порядку зростання
print(a, b) # [2, 3, 4, 5, 5, 5, 5] ['banana', 'banana', 'banana', 'cherry', 'cherry']

a.sort(reverse = True)    # можемо розвернути сортування
b.sort(reverse = True)    # можемо розвернути сортування
print(a, b) # [5, 5, 5, 5, 4, 3, 2] ['cherry', 'cherry', 'banana', 'banana', 'banana']

a.reverse()
b.reverse()
print(a, b)
#-----------------------------------------------Кортежі------------------------------------------------------------------

a = (1, 2, 3, 4, 5,)
print(a[0], a[1], a[2])     # 1 2 3
print(a[:2], a[-2:]) # (1, 2) (4, 5) вивести на екран перші два елемента та останні два елемента

#a[0] = 10 # TypeError: 'tuple' object does not support item assignment
a = (1, 2, 3, 4, 5, 5, 4)
print(a.count(5), a.count(4))   #   2 2      -    кількість 5 і 4
print(a.index(4))               #  Індекс 4 - перше входження (знаходить перше число і далі не рахує)

#-----------------------------------------------Словники------------------------------------------------------------------

test_dict = {'user': 'Oleg', 'age': 21, 'country': 'Poland'}

print(test_dict['user'], test_dict['age'], test_dict.get('country'))        # Oleg 21 Poland
#print(test_dict['animal'])      # Виникне помилка - ключа не існує
print(test_dict.get('animal', 'key not found'))     #key not found

test_dict['age'] = 30
print(test_dict['age'])

test_dict['animal'] = 'cat' # створюємо нову пару ключ - значення
print(test_dict['animal'])

animal = test_dict.pop('animal')    # видаляємо пару ключ-значення  'animal'
print(test_dict)        # {'user': 'Oleg', 'age': 30, 'country': 'Poland'}  У словнику пара ключ-значення відсутня
print(animal)         # cat        У змінній animal буде значення cat

# ------------------------------------------------Методи словника------------------------------------------------------

test_dict = {'user': 'Oleg', 'age': 21, 'country': 'Poland'}
test_dict.clear()
print(test_dict)

test_dict = {'user': 'Oleg', 'age': 21, 'country': 'Poland'}
copy_test_dict = test_dict.copy()
test_dict.clear()
print(test_dict)
print(copy_test_dict)

for key, value in copy_test_dict.items():       # .items щоб розпакувати словник
    print(f'Key: {key}, Value: {value}')

wrong_key = copy_test_dict.pop('currency', 'Key not found')     # Не знайшло значення ключа і повернуло дефолтне значення
                                                                # яке присвоїлось у змінну
print(wrong_key)    # Key not found

dict_update = {'new role': 'admin', 'salary': 10000}
copy_test_dict.update(dict_update)
print(copy_test_dict)

