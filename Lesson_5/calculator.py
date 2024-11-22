def add(a , b):
    sum = a + b
    print(f'Сума чисел = {sum}')

def subtract(a, b):
    subtr = a - b
    print(f'Різниця чисел = {subtr}')

def multiply(a , b):
    mult = a * b
    print(f'Добуток чисел = {mult}')

def divide(a, b):
    if b != 0:
        div = a / b
        print(f'Ділення чисел = {div}')
    else:
        print('Ділення на нуль')
