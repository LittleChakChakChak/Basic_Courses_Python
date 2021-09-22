import random
from functools import reduce

# 1 функция расчета заработной платы сотрудника -------------------------------------------------------
"""
def payroll(salary):
    return salary[0] * salary[1] + salary[2]


salary = [int(input('Введите зарплату в час: ')),
          int(input('Введите часы работы: ')),
          int(input('Введите премию: '))]
print(f'Зарплата: {payroll(salary)}')
"""

# 2 Вывод большего элемента в сравнение с предыдущем -----------------------------------------------
"""
def parsing(myArray):
    newArray = []
    for i in range(len(myArray)):
        if i == 0:
            continue
        elif myArray[i] > myArray[i - 1]:
            newArray.append(myArray[i])
    return newArray


myArray = []
i = 0
while i < 10:
    myArray.append(random.randint(0, 100))
    i += 1
print(f'Массив(список) изначально {myArray}')
print(f'Вот такой массив(список) получился{parsing(myArray)}')
"""
# 3  Для чисел от 20 до 240 найти кратные 20 или 21 одной строкой -----------------------------------------------
"""
print(f'{[i for i in range(20,241) if i % 20 == 0 or i % 21 == 0]}')

# 4 Список без повторений  -----------------------------------------------
myList = []
for i in range(10):
    myList.append(random.randint(0, 100))
print(f'Список изначально: {myList}')
print(f'Список без повторений: {set(myList)}')
"""
# 5 Список без повторений  -----------------------------------------------
"""
myList = []
for i in range(10):
    myList.append(random.randrange(99, 1001, 2))
print(f'Вывод списка: {myList}')
print(f'Вывод суммы: {reduce(lambda x, y: x + y, myList)}')
"""

# 6  Реализование два скрипта для циклирования списка -----------------------------------------------
# 6.1 итератор, генерирующий целые числа, начиная с указанного
from itertools import count

begin = int(input('Введите с какого числа начинать: '))
for i in count(begin):
    print('Вывод: ', i)
    if i > 9:
        break
