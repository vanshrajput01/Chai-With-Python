class Car:
    def __init__(self,brand,model,color,price,odometer = 0):
        self.brandname = brand
        self.modelname = model
        self.carColor = color
        self.price = price
        self.odometer = odometer
    
    def car_details(self):
        print(f"Car model is {self.modelname} , barnd is {self.brandname} ,color is {self.carColor} and price is {self.price}.")

class EletricCar(Car):
    def __init__(self,batterty_capa,brand,model,color,price):
        self.batteryCapacity = batterty_capa
        super().__init__(brand,model,color,price)

    def batterty_power(self):
        print(f"This Eletric Car battery capacity is {self.batteryCapacity}.")
    
    def update_odometer(self,kms):
        if kms >= self.odometer:
            self.odometer = kms
            return self.odometer
        else:
            return self.odometer
    
e1 = EletricCar("300kmh","Tata","Punch","Red","30L")  
e1.update_odometer(10)
print(e1.odometer)
 
        

    


