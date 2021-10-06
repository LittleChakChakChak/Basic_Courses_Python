from time import sleep


# 1 Реализовать класс светофор --------------------------------------------

class TrafficLight:
    __private_color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{self.__private_color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            else:
                sleep(10)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()


# 2 Реализовать класс догора --------------------------------------------

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.thickness = 5  # см
        self.weight = 25  # кг

    def weight_road(self):
        print(f'Масса всего дорожного покрытия: '
              f'{(self._length * self._width * self.thickness * self.weight) / 1000} (т.)')


Road = Road(int(input('Введите длину дороги в метрах: ')), int(input('Введите ширину дороги  в метрах: ')))
Road.weight_road()


# 3 Реализовать класс догора --------------------------------------------

class Worker:
    def __init__(self, name, sur_name, position, wage, bonus):
        self.name = name
        self.sur_name = sur_name
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, sur_name, position, wage, bonus):
        super().__init__(name, sur_name, position, wage, bonus)

    def get_full_name(self):
        return self.sur_name + ' ' + self.name

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


employee = Position('Иван', 'Иванов', 'Программист', 70000, 30000)
print(employee.get_full_name())
print(employee.position)
print(employee.get_total_income())


# 4 Реализовать класс автомобиль --------------------------------------------

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехала'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction):
        return f'Автомобиль {self.name} повернула на {direction}'

    def show_speed(self):
        return f'Автомобиль {self.name} едет со скорость : {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Автомобиль {self.name} едет со скорость : {self.speed} \n ' \
                   f'Привышение скорости на {self.speed - 60}'
        else:
            return f'Автомобиль {self.name} едет со скорость : {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Автомобиль {self.name} едет со скорость : {self.speed} \n ' \
                   f'Привышение скорости на {self.speed - 40}'
        else:
            return f'Автомобиль {self.name} едет со скорость : {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


porshe = SportCar(100, 'Red', 'Porshe', False)
opel = TownCar(65, 'Yellow', 'Opel', False)
lada = WorkCar(39, 'White', 'Lada', False)
bmw = PoliceCar(110, 'Black', 'BMW', True)

print(porshe.go())
print(porshe.turn('Лево'))
print(porshe.turn('Право'))
print(porshe.show_speed())
print(porshe.stop())
print('---------------------------------------------------')
print(opel.go())
print(opel.turn('Лево'))
print(opel.turn('Разворот'))
print(opel.show_speed())
print(opel.stop())
print('---------------------------------------------------')
print(lada.go())
print(lada.turn('Лево'))
print(lada.turn('Лево'))
print(lada.show_speed())
print(f'Автомобиль {lada.name} принадлежит полиции? {lada.is_police}')
print(lada.stop())
print('---------------------------------------------------')
print(bmw.go())
print(bmw.turn('Лево'))
print(bmw.turn('Право'))
print(bmw.show_speed())
print(f'Автомобиль {bmw.name} принадлежит полиции? {bmw.is_police}')
print(bmw.stop())


# 5 Реализовать класс канцелярская принадлежность --------------------------------------------

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбрана {self.title}, запуск отриcовки ручкой'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбрана {self.title}, запуск отриcовки карандашом'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбрана {self.title}, запуск отриcовки маркером'


pen = Pen('ручка')
print(pen.draw())
print('---------------------------------------------------')
pencil = Pencil('карандаш')
print(pencil.draw())
print('---------------------------------------------------')
handle = Handle('маркер')
print(handle.draw())
print('---------------------------------------------------')