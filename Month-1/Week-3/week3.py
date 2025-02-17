class Vehicle:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model

    def describe(self):
        return f"{self.__make} {self.__model}"


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors

    def describe(self):
        return f"{super().describe()}, Doors: {self.__num_doors}"


class Bike(Vehicle):
    def __init__(self, make, model, bike_type):
        super().__init__(make, model)
        self.__bike_type = bike_type

    def describe(self):
        return f"{super().describe()}, Type: {self.__bike_type}"


vehicles = [
    Car("BMW", "M3", 4),
    Bike("Ducati", "Monster", "Naked"),
    Vehicle("Ford", "Mustang"),
]

for vehicle in vehicles:
    print(vehicle.describe())
