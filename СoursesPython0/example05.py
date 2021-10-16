# 1 заполнить файл текстовым значение ------------------------------------------

file1 = open("files/file_1", "w")
while True:
    str = input('Введите что добавить в файл: ')
    if str != '':
        file1.write(f"{str} \n")
    else:
        break
file1.close()

# 2 прочтение файла (кол-во строк и символов в строке) ------------------------------------------

with open('files/file_2', 'r') as file2:
    lines = 0
    sum_char = 0
    for line in file2:
        lines += 1
        char = len(line) - 1
        sum_char += char
        print(f'В {lines} строке было {char} символов')
print(f'Всего было: {lines} строк и {sum_char} символов без пробела')

# 3 прочтение файла (кол-во строк и символов в строке) ------------------------------------------

with open('files/file_3', 'r') as file3:
    staff = {}
    sumSalary = 0
    for line in file3:
        key, value = line.split()
        staff[key] = value
        if int(value) < 20000:
            print(f'Фамилия: {key}, зарплата: {value}')
        sumSalary += int(value)
    print(f'Средняя зарплата по сотрудникам: {sumSalary / len(staff)}')
    print(f'Список всех сотрудников: {staff}')

# 4 перевод текста из файла в другой файл ------------------------------------------

with open('files/file_4', 'r') as file4:
    file4_1 = open('files/file_4_1.txt', 'w')
    rus = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
    for line in file4:
        value, key = line.split(' — ')
        file4_1.write(f'{rus[int(key[0])]} — {key[0]}\n')
    file4_1.close()
print('Переведен')

# 5 сумма из файла ------------------------------------------

with open('files/file_5', 'r') as file5:
    summer = []
    summ = 0
    summer = file5.read().split()
    for i in summer:
        summ += int(i)
print(f'Сумма чисел = {summ}')

# 6 Запись предметов  ------------------------------------------

with open('files/file_6', 'r') as file6:
    items = {}
    for line in file6:
        key, value = line.split(': ')
        time = value.split()
        if time[0] == '—':
            time1 = 0
        else:
            time1 = int(time[0].replace('(л)', ''))
        if time[1] == '—':
            time2 = 0
        else:
            time2 = int(time[1].replace('(пр)', ''))
        if time[2] == '—':
            time3 = 0
        else:
            time3 = int(time[2].replace('(лаб)', ''))
        items[key] = time1 + time2 + time3
    print(items)

# 7 Запись предметов  ------------------------------------------

with open('files/file_7', 'r') as file7:
    profit_firm = {}
    average_profit = {}
    loss_firm = {}
    count_average_profit = 0
    for line in file7:
        name_firm, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)    # получаем прибыль компании
        if profit >= 0:
            profit_firm[name_firm] = profit     # список с прибыльными компаниями
            count_average_profit += profit    # для расчета средней прибыли
        else:
            loss_firm[name_firm] = profit   # список с убыточными фирмами
    average_profit['average_profit'] = count_average_profit / len(profit_firm)    # продолжение среднего подсчета
    date_firm = [profit_firm,  average_profit, loss_firm]    # подгатавлием json
    with open('files/file_7_1.txt', 'w') as file7_1:    # записываем json
        file7_1.write(f'{date_firm}')