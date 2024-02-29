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

# punch = Car("Tata","Punch")
# print(punch.brand)
# punch.carDetails()

# tasla = ElectricCar("tasla","class s","5000KWH")
# print(tasla.model)
# tasla.battery_Cap()
# tasla.carDetails()
        
# Other Example based on inheritance in python

class Animal:
    def speak(self):
        pass
    
class Cat(Animal):
    def speak(self):
        return "Meow Meow"

class Dog(Animal):
    def speak(self):
        return "Boo Boo"



cat = Cat()
print(cat.speak())

dog  = Dog()
print(dog.speak())

# Shapes Hierarchy

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width * self.height)

rectangle = Rectangle(4,5)
print(rectangle.area())
print(rectangle.perimeter())

# Employee Hierarchy:

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    

class Manager(Employee):
    def __init__(self, name, age, salary,exp_year):
        super().__init__(name, age, salary)
        self.exp_year = exp_year

class Engineer(Employee):
    def __init__(self, name, age, salary,stream):
        super().__init__(name, age, salary)
        self.stream = stream
    
class Intern(Employee):
    def __init__(self, name, age, salary,durationTime):
        super().__init__(name, age, salary)
        self.durationTime = durationTime

manager = Manager("Jack",56,90000,"10+")
print(manager.salary)

eng = Engineer("maggi",27,500000,"Full Stack dev")
print(eng.stream)

intren01 = Intern("Rocks",20,6000,"6 Months")
print(intren01.durationTime)

class ModifiedCar(Car):
    pass
        
        

city = ModifiedCar("Honda","City")
print(city.model)









    

        