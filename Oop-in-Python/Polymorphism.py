class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fuel_capacity(self):
        print(f"Postol & diesel")

class ElectricCar(Car):
    def __init__(self):
        def __init__(self,brand,model,battery):
            super().__init__(brand,model)
            self.battery = battery


    def fuel_capacity(self):
        print(f"battery Capacity is {self.battery}.") 

safari = Car("Tata","Safari")
safari.fuel_capacity()

tasla = ElectricCar("Tasla","S Class","7000KWH")