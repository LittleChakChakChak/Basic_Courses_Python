import random
from itertools import count
from itertools import cycle
from functools import reduce
from math import factorial


# 1 функция расчета заработной платы сотрудника -------------------------------------------------------

def payroll(salary):
    return salary[0] * salary[1] + salary[2]


salary = [int(input('Введите зарплату в час: ')),
          int(input('Введите часы работы: ')),
          int(input('Введите премию: '))]
print(f'Зарплата: {payroll(salary)}')


# 2 Вывод большего элемента в сравнение с предыдущем -----------------------------------------------

def parsing(my_array):
    new_array = []
    for i in range(len(my_array)):
        if i == 0:
            continue
        elif my_array[i] > my_array[i - 1]:
            new_array.append(my_array[i])
    return new_array


my_array = []
i = 0
while i < 10:
    my_array.append(random.randint(0, 100))
    i += 1
print(f'Массив(список) изначально {my_array}')
print(f'Вот такой массив(список) получился{parsing(my_array)}')

# 3  Для чисел от 20 до 240 найти кратные 20 или 21 одной строкой -----------------------------------------------

print(f'{[i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]}')

# 4 Список без повторений  -----------------------------------------------
my_list = []
for i in range(10):
    my_list.append(random.randint(0, 100))
print(f'Список изначально: {my_list}')
print(f'Список без повторений: {set(my_list)}')

# 5 Список без повторений  -----------------------------------------------

my_list = []
for i in range(10):
    my_list.append(random.randrange(99, 1001, 2))
print(f'Вывод списка: {my_list}')
print(f'Вывод суммы: {reduce(lambda x, y: x + y, my_list)}')

# 6  Реализование два скрипта для циклирования списка -----------------------------------------------
# 6.1 итератор, генерирующий целые числа, начиная с указанного

begin = int(input('Введите с какого числа начинать: '))
for i in count(begin):
    print('Вывод: ', i)
    if i > 9:
        break

# 6.2 итератор, повторяющий элементы некоторого списка, определенного заранее
my_list = []
for i in range(5):
    my_list.append(random.randint(0, 15))
print(my_list)
check = 0
for i in cycle(my_list):
    check += 1
    print(i)
    if check > 20:
        break


# 7  Рекурсия и факториал -----------------------------------------------
def func():
    for fact in count(1):
        yield factorial(fact)


n = int(input('Введите факториал: '))
gen = func()
for el in gen:
    if n > 0:
        print(f'Факториал числа = {el}!')
        n -= 1
    else:
        break