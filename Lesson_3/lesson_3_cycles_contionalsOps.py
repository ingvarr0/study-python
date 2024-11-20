string = "Hello world"
#-----------------------------------------------------------------------------------------------------------------------
if 'Hello' in string:           # Виконується коли ця умова є True, якщо ні, то логіка переходить в Else автоматично
    print('Hello in string') # Hello in string
else:
    print('Hello not in string')
#-----------------------------------------------------------------------------------------------------------------------
if 'Hello' not in string:  # Виконується коли ця умова є True, якщо ні, то логіка переходить в Else автоматично
    print('Hello in string')
else:
    print('Hello not in string') # Hello not in string

#-----------------------------------------------------------------------------------------------------------------------
if 'Hello' not in string:       # У першій умові не виконалось (результат False), перейшло до elif і виконалось
    print('Hello in string')
elif 'world' in string:
    print('World in string') # World in string
else:                               # else не виконалось, бо отримали результат у попередньому блоці elif
    print('Hello not in string')
#-----------------------------------------------------------------------------------------------------------------------

a = 10
b = 20

if a >= 10 and b == 20:
    print(a+b)
else:
    print('Wrong condition')
# ------
if a == 11 and b == 20 or b < 30:  # Отримали False, False or b <30 -> False or True -> True
    print(a+b)        #30
else:
    print('Wrong condition')
# -----------------------------------------------------------------------------------------------------------------------

test_list = ['hello', 'test', 1, 2, 3]
if 'hello' in test_list and 1 in test_list:
    print('Hello 1')                            #Hello 1
elif 'test' in test_list and 4 not in test_list:
    print('Test not 4')
else:
    print('Your conditions were wrong')

# -----------------------------------------------------------------------------------------------------------------------
a = 10
b = 20
c = 'chat is active'
d = 'count of users'
print(len(c), len(d))        # 14 14

if len(c) >= b:         # 14 >= 20 -> False
    print(c)
elif len(d) <= a:       # 14 >= 10 -> False
    print(d)
else:                           # Wrong coditions, бо ні одна з умов не була виконана
    print('Wrong coditions')

# -----------------------------------------------------------------------------------------------------------------------

user_1 = {
    'name': 'Tom',
    'age': 21,
    'balance': 20000,
    'currency': 'USD',
    'status': True
}

user_2 = {
    'name': 'John',
    'age': 17,
    'balance': 5000,
    'currency': 'EUR',
    'status': False
}

user_3 = {
    #'name': 'Karine',
    'age': 30,
    'balance': 100000,
    'currency': 'UAH',
    'status': True
}

list_currency = ['USD', 'GBR', 'UAH', 'EUR']

if user_3 and user_3.get('name', None) and user_3['age'] >= 18 and user_3['status']: # Якщо Ім'я не буде, то повернемо None
# якщо об'єкт user_3 існує І в об'єкта є ім'я І об'єкту більше 18 І в об'єкта є статус
    if user_3['balance'] >= 10000 and user_3['currency'] in list_currency:
        print(f'Hello! You can create your binance accout, welcome {user_3["name"]}')
        # f (перед текстом) - рядок, дозволяє вставляти в рядок змінні
        # не можна використовувати подвійні лапки всередині подвійних лапок, а тільки одинарні або використовувати
        # КОНКАТЕНАЦІЮ \"
    elif user_3['balance'] >= 1000 and user_3['currency'] in list_currency:
        print('You need more money!')
    else:
        print('Money critical not enough')
elif not user_3.get('name', None):          # Перевірило .get('name), не знайшло ключа, повернело None - None це теж False
                                            # elif not False - повертає True і ми заходимо в цей блок
    print('Please, check your name in your account description')
elif user_3['age'] < 18:
    print('For registry binance account you have to be 18 y.o')
else:
    print('something went wrong')


#--------------------------------------------------- Цикли -------------------------------------------------------------

test_list = [1, 2, 3, 4, 5, 6]

for num in test_list: # оголошення циклу for, також оголошуємо змінну, яка буде приймати в себе кожен елемент послідовності
    #print(num+2)  # 1 2 3 4 5 6
                            # ми звертались до test_list і на кожній ітерації ми витягували з цього списку кожний елемент
    #print(num + 2)  # 3 4 5 6 7 8
    print(f'You got a {num}') # You got a 1 | You got a 2 ... You got a 6

#-----------------------------------

a = 0

while a < 10:   # об'являємо умову за якої while буде працювати
    a += 1
    print(a, '------<') # 1 2 3 4 5 6 7 8 9 10

a = 0

while a < 10:   # об'являємо умову за якої while буде працювати
    print(a, '------<') # 0 1 2 3 4 5 6 7 8 9
    a += 1

test_list = [1, 2, 3, 4, 5]
while len(test_list) < 10:
    test_list.append(3)
    print(test_list)        # на кожній ітерації додає трійку в кінець списка, доти, доки довжина списка не стала = 10


#----------------- цикли + умовні конструкції
test_list = ['test', 'python', 'code']

for s in test_list:
    #print(s,'-------<')
    if s == 'test':
        print(s)
    elif s == 'python':
        print(s)
    else:
        print(s)

a = 0
add_list = []
while len(add_list) < 100:
    print('length of the list:' , len(add_list))
    add_list.append(a)
    a += 1
    if len(add_list) == 50:
        print('You are at middle of the list')


# ----------------- складніші конструкції

user_1 = {
    'user_name': 'tester',
    'role': 'admin',
    'account_connection': True
}

user_2 = {
    'user_name': 'junior',
    'role': 'user',
    'account_connection': False
}

user_3 = {
    'user_name': 'middle',
    'role': 'pro_user',
    'account_connection': True
}


list_of_users = [user_1, user_2, user_3]

for user in list_of_users:
    print(f'Work with {user['user_name']} account')
    if not user['account_connection']: # за рахунок того, що перебираємо список, а в нього словники,
                                    # не потрібно звертатись до змінних user1,2,3, бо при передачі списку в цикл,
                                    # список сам звертається до кожної змінної і можемо універсально звертатись
                                    # до кожної з них використовуючи змінну циклу user
        count_of_tries = 10
        while count_of_tries != 0:
            if count_of_tries == 5:
                user['account_connection'] = True
                break       # Вихід із ітерації  ----- continue - пропустити ітерацію
            print('Try to connect to user account')
            count_of_tries -=1      #На кожній ітерації будемо віднімати від count_of_tries одиницю і передавати
            print(f'Count of tries left:', count_of_tries)
    elif user['role'] == 'admin':
        print(f'Hello in system', {user['user_name']})
    else:
        print('Welcome on the board')
