class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self) -> str:
        return f'<Car {self.make} {self.model}>'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car): # tells you whether the variable that you git is a instance of Car
            raise NotImplementedError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can onlyu add `Car` objects')
        self.cars.append(car)


ford = Garage()
ford.add_car('Fiesta')
print(len(ford))

