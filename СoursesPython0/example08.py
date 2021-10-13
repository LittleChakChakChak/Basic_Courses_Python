# 1 Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год» --------------------------------------------
"""
class Date:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        my_date = day_month_year.split('-')
        return f'День: {int(my_date[0])}, Месяц: {int(my_date[1])}, Год: {int(my_date[2])}'

    @staticmethod
    def checking(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year > 0:
                    return 'Дата верная!'
                else:
                    return 'Неправильно введен год'
            else:
               return 'Неправильно введен месяц'
        else:
            return 'Неправильно введен день'

    def __str__(self):
        return self.extract(self.day_month_year)

date = Date('10-10-2021')
print(date.extract('10-11-2021'))
print(date.checking(10, 9, 2020))
print(date)


# 2 Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на нуль. --------------------------------------------

class Division:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    @staticmethod
    def divisor_zero(number_1, number_2):
        try:
            return number_1 / number_2
        except:
            return 'Дление на ноль!'


my_division = Division(2, 0)
print(my_division.divisor_zero(2, 2))


# 3 Создайте собственный класс-исключение,
# который должен проверять содержимое списка на наличие только чисел. --------------------------------------------

class Checking_numbers:
    def __init__(self):
        self.list_numbers = []

    def checking(self):
        while True:
            try:
                value = int(input('Введите число, которое добавиться в список: '))
                self.list_numbers.append(value)
                print(f'Ваш список: {self.list_numbers}')
            except:
                value_str = input('Вы ввели букву, если хотите закончить введите stop: ')
                if value_str == 'stop':
                    return f'Вы остановились \n' \
                           f'Ваш итоговый список: {self.list_numbers}'
                else:
                    self.list_numbers.append(int(value_str))
                    print(f'Ваш список: {self.list_numbers}')

my_list = Checking_numbers()
print(my_list.checking())
"""

# 4-5-6 Создание класса ортехники --------------------------------------------
class OfficeEquipmentWarehouse:
    _warehouses = {}
    _in_price = {}
    _time_price = {}

    def __init__(self, our_division):
        self._our_division = our_division

    def acceptance(self):
        nl = '\n'
        while True:
            name = input('Введите название устройства: ')
            if name != 'стоп':
                quantity = input('Введите количество на складе: ')
                self._in_price[name] = int(quantity)
            else:
                break
        print('{:<20} {:<15}'.format('Название', 'Кол-во'))
        for name, quantity in self._in_price.items():
            print('{:<20} {:<15}'.format(name, quantity))
        self._warehouses[self._our_division] = self._in_price
        print(self._warehouses)

    def translation(self):
        in_our_division = input('В какое подразделение: ')
        name = input('Переводимый товар: ')
        for products, availability in self._in_price.items():            # пробегаемся по складу нашего подразделения
            if products == name:                                         # ищем товар
                quantity = int(input('Кол-во перевода товара: '))
                if availability >= quantity:                           # проверяем кол-во
                    self._in_price[name] = self._in_price[name] - quantity
                    self._time_price[name] = quantity
                    self._warehouses[in_our_division] = self._time_price
        print(f'Склад списания: {self._warehouses[self._our_division]}')
        print(f'Склад перевода: {self._warehouses[in_our_division]}')


class EquipmentWarehouse:
    def __init__(self, name, color, connection_type, price):
        self.name = name
        self.color = color
        self.connection_type = connection_type
        self.price = price


class Printer(EquipmentWarehouse):
    def __init__(self, color_printing, print_speed, printer_type):
        self.color_printing = color_printing
        self.print_speed = print_speed
        self.printer_type = printer_type

class Scanner(EquipmentWarehouse):
    def __init__(self, scanner_speed, scanner_size):
        self.scanner_speed = scanner_speed
        self.scanner_size = scanner_size

class Xerox(Printer, Scanner):
    def __init__(self, size):
        self.size = size

test = OfficeEquipmentWarehouse('Москва')
print(test.acceptance())
print(test.translation())