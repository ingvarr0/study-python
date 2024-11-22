def calculate_average(numbers):
#numbers = [1, 2, 3, 4, 5, 5, 12, 6, 10]
    res = 0
    for i in numbers:
        res += i
    #print(res)
    average = res / len(numbers)
    print(f'Ваш список: {numbers}')
    print(f'Середнє арифметичне списку дорівнює {average}')


def find_max(numbers):
    max_ind = 0 # перший елемент є максимальним
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[max_ind]:
            max_ind = i

    max_number = numbers[max_ind]
    print(f"Найбільше число у списку: {max_number}")