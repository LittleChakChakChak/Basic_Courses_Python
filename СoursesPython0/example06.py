from time import sleep


# 1 Реализовать класс светофор --------------------------------------------
"""
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
        self.__length = length
        self.__width = width
        self.thickness = 5   # см
        self.weight = 25    # кг

    def weight_road(self):
        print(f'Масса всего дорожного покрытия: '
              f'{(self.__length * self.__width * self.thickness * self.weight)/1000} (т.)')


Road = Road(int(input('Введите длину дороги в метрах: ')), int(input('Введите ширину дороги  в метрах: ')))
Road.weight_road()

"""

# 3 Реализовать класс догора --------------------------------------------

class Worker:
    name
    surname
    position
    __income