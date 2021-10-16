# 1 Реализовать класс матрица --------------------------------------------

class Matrix:
    def __init__(self, list0, list1):
        self.list0 = list0
        self.list1 = list1
        self.nl = '\n'

    def __str__(self):
        return f"Матрицы до изменений: \n " \
               f"Первая матрица:\n{str(self.nl.join([' | '.join([str(j) for j in i]) for i in self.list0]))} \n " \
               f"Вторая матрица:\n{str(self.nl.join([' | '.join([str(j) for j in i]) for i in self.list1]))}"

    def __add__(self):
        my_math = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        for i in range(len(self.list0)):
            for j in range(len(self.list1[i])):
                my_math[i][j] = self.list0[i][j] + self.list1[i][j]

        return f"Матрица после изменений:\n" \
               f"{str(self.nl.join([' | '.join([str(j) for j in i]) for i in my_math]))}"


my_math = Matrix(
    [[31, 22, 0],
     [37, 43, 0],
     [51, 86, 0]],

    [[3, 5, 10],
     [8, 3, 5],
     [0, 0, 0]]
)
print(my_math)
print(my_math.__add__())


# 2 Реализовать проект расчета суммарного расхода ткани на производство одежды ----------------------------------------
class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_coat(self):
        return round(self.width/6.5 + 0.5)

    def get_square_suit(self):
        return round(2 * self.height + 0.3)

    @property
    def get_square_sum(self):
        return str(f'Площадь полной затраты ткани: {(self.width/6.5 + 0.5) + (2 * self.height + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)

    def __str__(self):
        return str(f'Площадь пальто: {self.get_square_coat()}')


class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)

    def __str__(self):
        return str(f'Площадь пальто: {self.get_square_suit()}')


coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
print(coat.get_square_sum)
print(suit.get_square_sum)


# 3 Реализовать программу работы с органическими клетками, состоящими из ячеек ----------------------------------------
class Cell:
    def __init__(self, number_cells):
        self.number_cells = int(number_cells)

    def __str__(self):
        return str(f'Результат операции: {self.number_cells * "*"}')

    def __add__(self, other):
        return Cell(self.number_cells + other.number_cells)

    def __sub__(self, other):
        if int(self.number_cells - other.number_cells) > 0:
            return Cell(self.number_cells - other.number_cells)
        else:
            return 'Ошибка вычитания'

    def __mul__(self, other):
        return Cell(self.number_cells * other.number_cells)

    def __truediv__(self, other):
        if int(other.number_cells) != 0:
            return Cell(self.number_cells // other.number_cells)
        else:
            return f'Ошибка деления, делимое число = 0'

    def make_order(self, cells_in_row):
        row = ''

        for i in range(int(self.number_cells / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.number_cells % cells_in_row)}'
        return f'Результат операции:\n{row}'


cell_1 = Cell(20)
cell_2 = Cell(13)
print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(7))