# Завдання 1: Робота з функціями
import calculator

a = int(input('Уведіть перше число:'))
b = int(input('Уведіть друге число:'))
operator = input('Впишіть потрібну операцію (додавання, віднімання, множення або ділення) або (+, - , *, /)')

if operator == 'додавання' or operator == '+':
    calculator.add(a, b)
elif operator == 'віднімання' or operator == '-':
    calculator.subtract(a, b)
elif operator == 'множення' or operator == '*':
    calculator.multiply(a, b)
elif operator == 'ділення' or operator == '/':
    calculator.divide(a, b)
else:
    print('Неправильно введена операція')

# Завдання 2: Створення та імпорт власних модулів

import utilities

nums = [1, 2, 3, 4, 5, 5, 12, 6, 11]
utilities.calculate_average(nums)

utilities.find_max(nums)

