from app.car import car

class car_factory(car):
    def __init__(self,
        name,
        model,
        year,
        id
    ):
        self.name = name
        self.model = model
        self.year = year
        self.id = id




