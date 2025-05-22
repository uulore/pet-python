from random import randint


class Car:
    __max_speed = 220
    def __init__(self,
        name = str,
        model = str,
    ):
        self.name = name
        self.model = model

    def speed_up(self, imt=5):
        self.max_speed += int

    def max_speed(self):
        speed = randint(0, self.__max_speed)
        return speed