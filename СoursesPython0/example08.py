# 1 Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год» --------------------------------------------

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