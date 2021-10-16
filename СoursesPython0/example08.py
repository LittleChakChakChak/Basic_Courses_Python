# 1 Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год» --------------------------------------------

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
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

class CheckingNumbers:
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


my_list = CheckingNumbers()
print(my_list.checking())


# 4-5-6 Создание проект "Склад ортехники" --------------------------------------------
class OfficeEquipmentWarehouse:
    _warehouses = {}
    _in_price = {}
    _time_price = {}

    def __init__(self, our_division):
        self._our_division = our_division

    def acceptance(self):  # Пополняем наш склад
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

    def translation(self):  # Перевод товара на другой склад
        flag_name = True
        flag_quantity = True
        in_our_division = input('В какое подразделение: ')
        name = input('Переводимый товар: ')
        for products in self._warehouses[self._our_division]:  # пробегаемся по складу нашего подразделения
            if products == name:  # ищем товар
                quantity = int(input('Кол-во перевода товара: '))
                flag_name = False
                our_quantity = (self._warehouses[self._our_division])[name]  # смотрим количество в нашем подразделении
                if our_quantity >= quantity:  # проверяем кол-во
                    # списываем с нашего подразделения
                    self._warehouses[self._our_division].update({name: our_quantity - quantity})
                    # добавляем в новое подразделение
                    self._time_price[name] = quantity
                    self._warehouses.update({in_our_division: self._time_price})
                    flag_quantity = False
        if flag_name:
            return 'Не найден товар'
        elif flag_quantity:
            return 'На складе нет такого количества'
        else:
            print(f'Склад списания: {self._warehouses[self._our_division]}')
            print(f'Склад перевода: {self._warehouses[in_our_division]}')


class EquipmentWarehouse:
    def __init__(self, name, connection_type, price):
        self.name = name
        self.connection_type = connection_type
        self.price = price


class Printer(EquipmentWarehouse):
    def __init__(self, color_printing, print_speed, printer_type, name, connection_type, price):
        self.color_printing = color_printing
        self.print_speed = print_speed
        self.printer_type = printer_type
        super().__init__(name, connection_type, price)

    def __str__(self):
        return f'Вы ввели устройство: \n' \
               f'Название устройства - {self.name} \n' \
               f'Подключение устройства - {self.connection_type} \n' \
               f'Цена - {self.price} руб.\n' \
               f'Цвет печати - {self.color_printing} \n' \
               f'Скорость печати - {self.print_speed} сек.\n' \
               f'Тип принтера - {self.printer_type} \n'


class Scanner(EquipmentWarehouse):
    def __init__(self, scanner_speed, scanner_size, name, connection_type, price):
        self.scanner_speed = scanner_speed
        self.scanner_size = scanner_size
        super().__init__(name, connection_type, price)

    def __str__(self):
        return f'Вы ввели устройство: \n' \
               f'Название устройства - {self.name} \n' \
               f'Подключение устройства - {self.connection_type} \n' \
               f'Цена - {self.price} руб.\n' \
               f'Скорость сканеровки - {self.scanner_speed} сек.\n' \
               f'Ширина сканера - {self.scanner_size} см * см\n'


class Xerox(EquipmentWarehouse):
    def __init__(self, size, name, connection_type, price):
        self.size = size
        super().__init__(name, connection_type, price)

    def __str__(self):
        return f'Вы ввели устройство: \n' \
               f'Название устройства - {self.name} \n' \
               f'Подключение устройства - {self.connection_type} \n' \
               f'Цена - {self.price} руб.\n' \
               f'Размер - {self.size} см * см\n'


printer_1 = Printer('black', 5, 'лазерный', 'HP', 'bluetooth', 15000)
print(printer_1)
print('--------------------------------------------------------')

scanner_1 = Scanner(4, '60 * 25', 'Samsung', 'USB', 10000)
print(scanner_1)
print('--------------------------------------------------------')

xerox_1 = Xerox('5000 * 4500', 'Xerox', 'wi-fi', 55000)
print(xerox_1)
print('--------------------------------------------------------')

my_warehouse = OfficeEquipmentWarehouse('Москва')
print(my_warehouse.acceptance())  # Пополняем наш склад
print(my_warehouse.translation())  # Перевод товара на другой склад


# 7 Создание проект Операции с комплексными числами --------------------------------------------
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):  # сложение
        # (a + b * i) + (c + d * i) = (a + c) + (b + d) * i
        return f' Вывод суммы: \n' \
               f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):  # умножение
        # (a + b * i) * (c + d * i) = (a * c − b * d) + (a * d + b * c) * i
        return f' Вывод произедения: \n' \
               f'z = {self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a} * i'

    def __str__(self):
        return f'{self.a} + {self.b} * i'


z1 = ComplexNumber(2, -5)
z2 = ComplexNumber(4, 3)
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
