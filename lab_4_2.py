class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"{self.make}, {self.model}"



class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f"{self.make}, {self.model}, {self.fuel_type}"


    car = Car(make="Ford", model="mustang", fuel_type="petrol")
    print(car.get_info())