from random import randint
from app.services.get_id import get_id

class Car:
    __max_speed = 220
    def __init__(self,
        name = str,
        model = str,
        year = int
    ):
        self.name = name
        self.model = model
        self.year = year
        self._id = get_id()

    def speed_up(self, imt=5):
        self.max_speed += int

    def max_speed(self):
        speed = randint(0, self.__max_speed)
        return speed