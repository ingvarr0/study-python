### Умовні конструкції:
# 1. **Перевірка паролю:**

password_set = "password123"
#password_check = input('Уведіть пароль:')       #\n символ перенесення рядка

password_check = "password1234"
#password_check = "password123"
if password_check == password_set:
    print('Ви увійшли в систему')
else:
    print('Неправильний пароль')

# 2. **Визначення днів тижня:**

# 1 спосіб
day = 1

if day > 7 or day < 1:
    print('Error, try again')
else:
    if day == 1:
        print(f'День {day} - Понеділок')
    elif day == 2:
        print(f'День {day} - Вівторок')
    elif day == 3:
        print(f'День {day} - Середа')
    elif day == 4:
        print(f'День {day} - Четвер')
    elif day == 5:
        print(f"День {day} - П'ятниця")
    elif day == 6:
        print(f'День {day} - Субота')
    elif day == 7:
        print(f'День {day} - Неділя')

# 2й спосіб
days= {
    1: "Понеділок",
    2: "Вівторок",
    3: "Середа",
    4: "Четвер",
    5: "П'ятниця",
    6: "Субота",
    7: "Неділя"
}

day = 7

if day < 1 or day > 7:
    print('Error, try again')
else:
    print(f'Цей день - {days[day]}')

                                                                ### Цикли:

#1. **Таблиця множення:**
  # Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.

mult_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = 8
for i in mult_table:
    res = number * i
    print(f" {number} * {i} = {res}" )

#2. **Сума чисел:**
   #Завдання: Визначте список чисел і обчисліть їх суму.

number_list = [6, 2, 4, 1, 10, 3]
result = 0
for num in number_list:
    result += num   # result = result + num
print(result)

#3. **Факторіал числа:**
  # Завдання: Обчисліть факторіал заданого числа.

num = 6 # 8!
factor = 1
if num < 0:
    print("Не існує факторіала для від'ємних значень")
elif num == 0:
    print(f'Факторіал числа дорівнює {factor}')
else:
    x = 1
    while x <= num:
        factor *= x   # factor = factor * x
        x += 1
    print(factor)


#4. **Парні числа:**
   #Завдання: Виведіть всі парні числа від 1 до 50.
x = 1
while x <= 50:
    if x % 2 == 0:
        print(x)
    x += 1

#5. **Пошук простих чисел:**
   #Завдання: Знайдіть всі прості числа в заданому діапазоні.

for num in range(2, 51):    # Цикл перебирає всі числа від 2 до 50
    for i in range(2, num): # Вкладений цикл перевіряє, чи ділиться число на будь-яке число в діапазоні від 2 до num-1.
        if num % i == 0:
            break           # Якщо знайдено дільник (number % i == 0), цикл завершується (break).
    else:                   # Якщо не знайдено жодного дільника, виконується блок else вкладеного циклу, і число виводиться.
        print(num)

