# 1 заполнить файл текстовым значение ------------------------------------------

file1 = open("files/file_1", "w")
while True:
    str = input('Введите что добавить в файл: ')
    if str != '':
        file1.write(f"{str} \n")
    else:
        break
file1.close()

"""
# 2 прочтение файла (кол-во строк и символов в строке) ------------------------------------------

with open('files/file_2', 'r') as file2:
    lines = 0
    sumChar = 0
    for line in file2:
        lines += 1
        char = len(line) - 1
        sumChar += char
        print(f'В {lines} строке было {char} символов')
    file2.close()
print(f'Всего было: {lines} строк и {sumChar} символов без пробела')
"""
""""
# 3 прочтение файла (кол-во строк и символов в строке) ------------------------------------------
with open('files/file_3', 'r') as file3:
    lines = 0
    employee = []
    staff = []
    for line in file3:
        lines += 1
        employee = line.split()
        staff = employee.append()


    file3.close()
print(staff)