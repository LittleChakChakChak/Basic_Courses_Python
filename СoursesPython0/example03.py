# 1  Функция деления предусмотреть деление на ноль ----------------------------------------------

def division(a, b):
    print(a / b)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a == 0 or b == 0:
    print('a = 0 или b = 0, не надо так!')
else:
    division(a, b)


# 2  Данные пользователя  ----------------------------------------------

def user_info(data_user):
    print(f' Имя Фамилия: {data_user["firstName"] + " " + data_user["lastName"]};/n'
          f' Дата рожденияЖ {data_user["dateBirth"]};/n'
          f' Город проживания: {data_user["city"]};/n'
          f' Контактные данные: {data_user["email"]}, {data_user["phone"]}.')


data_user = {'lastName': input('Введите фамилию: '),
             'firstName': input('Введите имя:'),
             'dateBirth': input('Введите дату рождения: '),
             'city': input('Введите город: '),
             'email': input('Введите почту: '),
             'phone': input('Введите телефон: ')}

user_info(data_user)


# 3  Функция принимающая архументы и сумирует наибольшие два аргумента  ----------------------------------------------

def my_func(a, b, c):
    m1 = max(a, b, c)
    if m1 == a:
        m2 = max(b, c)
    elif m1 == b:
        m2 = max(a, c)
    else:
        m2 = max(a, b)
    print(m1 + m2)


my_func(int(input('Введите первое число: ')),
        int(input('Введите второе число: ')),
        int(input('Введите третье число: ')))


# 4  Возводим число в отрицательную степень (без использование функций)  ----------------------------------------------

def my_func(x, y):
    num = 1
    while y < 0:
        num *= x
        y += 1
    print(1 / num)


my_func(int(input('Введите возводимое число в степень: ')),
        int(input('Введите отрицательную степень: ')))


# 5  Вводим числа и сумируем их пока не будет введен спицыальный символ 's'  ------------------------------------------

def sumer():
    n = ''
    num = 0
    while n != 's':
        numbers = input('Введите числа через пробел: ')
        for n in numbers:
            if n == ' ':
                continue
            elif n == 's':
                break
            else:
                num += int(n)
        print(f'Сумма чисел = {num}')
    print(f'В конечном итоге сумма = {num}')


sumer()


# 6  Первую букву слова изменять на заглавную  ----------------------------------------------

def int_func(offer):
    new_words = []
    words = offer.split()
    for word in words:
        new_word = word.replace(word[0], word[0].upper(), 1)
        new_words.append(new_word)
    return new_words


offer = input('Введите предложение с из маленьких букв: ')
print(f'Измененное предложение: {int_func(offer)}')
