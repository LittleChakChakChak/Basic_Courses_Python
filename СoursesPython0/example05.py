# 1 заполнить файл текстовым значение ------------------------------------------
"""
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
    sumChar = 0
    for line in file2:
        lines += 1
        char = len(line) - 1
        sumChar += char
        print(f'В {lines} строке было {char} символов')
print(f'Всего было: {lines} строк и {sumChar} символов без пробела')
"""

# 3 прочтение файла (кол-во строк и символов в строке) ------------------------------------------
"""
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
"""
# 6 Запись предметов  ------------------------------------------

with open('files/file_6.txt', 'w') as file6:
    # сделать ввод по циклу
    # если пробел то отмена
    # если пробел в занятие то прочерк
    # по оканчанию сделать список