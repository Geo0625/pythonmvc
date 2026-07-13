class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def display_info(self):
        print(f"Car: {self.make} {self.model}")
        
my_car = Car("Toyota", "Camry")
my_car.display_info()

 