#--------------------------------------------------Визначення та виклик функцій-----------------------------------------
def say_hello():    # визначення функції
    print('Hello buddy!')

def print_numbers():
    for num in range (1, 11):  # range (1, 11) - виведе від 1 до 10
                                # range(10) Функція range не виводить останнє число, яке ми об'являємо, виведе 9, але 10 - ні
        print(f"Current number is: {num}")


say_hello() #Hello buddy!
print(print_numbers())

#---------------------------------------------------------Параметри функцій--------------------------------------------
def say_hello(username, age):    # задамо параметр username - параметри повинні мати інформативне ім'я (не a, b, c)
    print(f'Hello {username}, welcome to the club, buddy')
    print(f'Your age is {age}, you are so beautiful!')
    print('-------------------------------------------')

def print_numbers(start, stop):
    for num in range (start, stop):
        print(f"Current number is: {num}")
    print('-------------------------------------------')


user_data = {
    'Dima': 25,
    'Sara': 34,
    'Tom': 11
}
list_of_ranges = [(1, 10), (2, 9), (0, 100)]

#for name, age in user_data.items():
 #   say_hello(name, age)

for start_pos, stop_pos in list_of_ranges:  # за рахунок того, що ми в якості об'єкта ітерації використовуємо список,
                                        # ми його відкриваємо і у кожну зі змінних start_pos та stop_pos, потрапляє окремий
                                        # кортеж: 1 у start_pos та 10 у stop_pos
    print_numbers(start_pos, stop_pos)


#   Іменовані параметри:

def check_connection(username, count_tries, priority):  # у цій ф-ції будемо перевіряти підключення до акаунту
    if priority > 10:   # якщо priority > 10 - це пріоритетний юзер, ми використовуємо к-ть спроб, яка задана при передачі
        finish = 5
        for attempt in range(1, count_tries + 1):
            if attempt == finish:
                print('Connection was successful')
                break
            print(f'Attempt: {attempt} to connect to {username}')

    elif priority >= 5 and priority < 10:
        finish = 3
        for attempt in range(1, 6):
            if attempt == finish:
                print('Connection was successful')
            print(f'Attempt: {attempt} to connect to {username}')

    else:
        print("Your username has so low priority")


check_connection(count_tries = 10, username = 'Oleg', priority= 100)

#-------------------------------------------- Робота з модулями---------------------------------------------------------

import my_module

my_module.hello('Alex')

# Вбудовані модулі

import turtle

def drawSquare(size, color):
    turtle.speed(1)
    turtle.color(color)
    turtle.begin_fill()
    def move(len):
        turtle.forward(len)
        turtle.left(90)

    for _ in range(4): #  _ означає, що воно присвоїть сюди результати із range,
                    # але ми не будемо її використовувати (змінна не потрібна)
        move(size)
    turtle.end_fill()


drawSquare(100,'red')

turtle.goto(200, 200)
drawSquare(200, 'blue')



