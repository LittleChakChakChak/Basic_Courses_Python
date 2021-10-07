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


# 2 Реализовать класс матрица --------------------------------------------
