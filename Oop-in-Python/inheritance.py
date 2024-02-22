class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def carDetails(self):
        print(f"Car Details is {self.brand} and {self.model}.")

class ElectricCar(Car):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery = battery
    
    def battery_Cap(self):
        print(f"Battery capacity of this car is {self.battery}.")

punch = Car("Tata","Punch")
print(punch.brand)
punch.carDetails()

tasla = ElectricCar("tasla","class s","5000KWH")
print(tasla.model)
tasla.battery_Cap()
tasla.carDetails()
    

        