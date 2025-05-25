from app.car.car import Car

class Car_factory(Car):
    def __init__(self):
        self.name = name=None
        self.model = model=None
        self.storage = []

    def add(self, name=None, model=None, year=None):
        self.name = name
        self.model = model
        car = Car(name, model, year)
        self.storage.append(car)
        if name is None:
            str(input('Enter car brand: '))
        elif model is None:
            str(input('Enter car model: '))
        elif year is None:
            int(input('Enter car year: '))

    def list(self):
        for car in self.storage:
            print(f'A {car.name} {car.model}\nwas made in {car.year} year\nwith a {car._id} id\n')
    def delete(self, id=None):
        if id is None:
            int(input('Enter car id: '))
        for car in self.storage:
            if car._id == id:
                self.storage.remove(car)

factory = Car_factory()
factory.add('Koenigsegg', 'Gemera', 2023)
factory.add('Rolls-Royce', 'Cullinan', 2022)
factory.add('Chevrolet', 'Matiz', 2010)
factory.add('Tesla', 'Model S', 2022)
factory.add('BMW', 'i8', 2020)
factory.add('Audi', 'RS7 Sportback', 2021)
factory.add('Mercedes-Benz', 'G-Class', 2023)
factory.add('Toyota', 'Land Cruiser 300', 2022)
factory.add('Porsche', '911 Turbo S', 2021)
factory.add('Lamborghini', 'Urus', 2022)

