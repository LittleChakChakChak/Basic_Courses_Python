# 1 Ввод ----------------------------------------------------------
a = int(input('Введите число: '))
b = str(input('Введите строку: '))
print(f'Ваше число = {a} и ваша строка = {b}')

# 2 Перевод времени ----------------------------------------------------------
time_in_sec = int(input('Введите секунды: '))
house = time_in_sec // 3600
residue = time_in_sec % 3600
minutes = residue // 60
sec = residue % 60
print(f'{house}:{minutes}:{sec}')

# 3  Странная сумма -------------------------------------------
i = int(input("Введите число: "))
s = i + int(str(i) + str(i)) + int(str(i) + str(i) + str(i))
print(f'Сумма числа = {s}')

# 4  Найти число большее в сумме  -------------------------------------------
i = int(input("Введите число: "))
ls = []
while i > 10:
    ls.append(i % 10)
    i //= 10
r = max(ls)
print(r)

# 5  Выручки и издержки   -------------------------------------------
revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    profit = revenue - costs
    print(f'Фирма в прибыле! Прибыль составляет {profit}')
    print(f'Рентабельность выручки = {profit/revenue*100}%')
    number_of_employees = int(input('Введите кол-во сотрудников: '))
    print(f'Прибыль фирмы с расчетом на одного сотрудника = {profit / number_of_employees}')
else:
    print('Фирма в убытке!')

# 6  Спортцмен и пробежки   -------------------------------------------
km = int(input('Сколько в первый день пробежал спротсмен: '))
purpose = int(input('Цель в километрах: '))
day = 1
while km <= purpose:
    km = km + (km * 0.1)
    day = day + 1
print(f'Спортсмену нужно бегать {day} дней, что бы достичь цели в {purpose} км')
