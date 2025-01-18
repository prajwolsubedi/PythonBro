#Composition = The composed object directly owns it's components,
# which cannot exist independently
# "owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}"

#Here in composition if we delete these two car objects then the above horsepower and
# wheel class will not exist independently whereas in aggregation even if we didn't
# create any objects of library the book class will exist independently

car = Car("Ford", "Mustang", horse_power=500, wheel_size=18)
print(car.display_car())