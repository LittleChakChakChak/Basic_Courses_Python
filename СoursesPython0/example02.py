# 1  Тип в списке ----------------------------------------------

type_list = [1, 'h', 2.3, 3, 'z']
for li in type_list:
    print(f'Значение: {li} | Тип: {type(li)}')

# 2  Обмен соседий в списке ----------------------------------------------

list_num = [5, 1, 2, 3, 4, 5, 6]
print(list_num)
n = 0
if len(list_num) % 2 == 0:
    while n < len(list_num):
        ext = list_num[n]
        list_num[n] = list_num[n+1]
        list_num[n+1] = ext
        n += 2
else:
    while n < len(list_num) - 1:
        ext = list_num[n]
        list_num[n] = list_num[n+1]
        list_num[n+1] = ext
        n += 2
print(list_num)

# 3 Месяц по целому числу и какое время года -------------------------------

month = int(input('Введите месяц цифрой: '))
months = {1: 'Январь',
          2: 'Февраль',
          3: 'Март',
          4: 'Апрель',
          5: 'Май',
          6: 'Июль',
          7: 'Июнь',
          8: 'Август',
          9: 'Сентябрь',
          10: 'Октябрь',
          11: 'Ноябрь',
          12: 'Декабрь'}
seasons = ['Лето', 'Весна', 'Зима', 'Осень']
# print(months[month])
if 3 <= month <= 5:     # весна
    print(f'Месяц: {months[month]}, Время года: {seasons[1]}')
elif 6 <= month <= 8:   # лето
    print(f'Месяц: {months[month]}, Время года: {seasons[0]}')
elif 9 <= month <= 11:  # осень
    print(f'Месяц: {months[month]}, Время года: {seasons[3]}')
else:                   # зима
    print(f'Месяц: {months[month]}, Время года: {seasons[2]}')

# 4 Разделение предложения на слова -------------------------------

offer = input('Ваше предложение: ')
words = offer.split()
n = 0
while n < len(words):
    word = words[n]                     # полуаем слово для получеиня только 10 букв в дальнейшем
    print(f'{n + 1}) {word[:10]}')
    n += 1

# 5 Структура рейтинга  -------------------------------

rating = [7, 5, 3, 3, 2]
num = int(input('Введите поле рейтинга: '))
rating.append(num)
rating.sort()
rating.reverse()
print(rating)

# 6 Реализовать структуру данных «Товары»  -------------------------------

goods = []
n = 1
while input('Создадим товар? Да / Нет: ') == 'Да':
    characteristic = {"название": input('Введите название: '),
                      "цена": int(input('Введите цену: ')),
                      "количество": int(input('Введите количество на складе: ')),
                      "eд": input('Введите единицу измерения: ') + '.'}
    good = [n, characteristic]
    good = tuple(good)
    goods.append(good)
    n += 1
print(goods)
name = []
price = []
number = []
unit = []
for good in goods:
    char = good[1]
    name.append(char["название"])
    price.append(char["цена"])
    number.append(char["количество"])
    unit.append(char["eд"])
analytics = {"название": name, "цена": price, "количество": number, "ед": unit}
print(analytics)
