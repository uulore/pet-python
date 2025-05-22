from app.car.car import Car
class car_factory(Car):
    def __init__(self):
        self.name = name=None
        self.model = model=None
        self.storage = []

    def add(self, name, model, year):
        self.name = name
        self.model = model
        car = Car(name, model, year)
        self.storage.append(car)

    def list(self):
        for car in self.storage:
            print(f'A {car.name} {car.model}\nwas made in {car.year} year\nwith a {car._id} id\n')
    def delete(self, id):
        for car in self.storage:
            if car._id == id:
                self.storage.remove(car)


