# Example of Encapsulation in Pyhton

class Car:
    def __init__(self,brand,model):
        # Example of Private Variable in Class 
        self.__brand = brand
        self.model = model

    # Getter Methrod 
    
    def get_brand(self):
        print(f"Your brand car name is {self.__brand}")

harrier = Car("Tata","Harrier")
print(harrier.model)

 # print(harrier.brand) # Error 

# print(harrier.__brand) # also give an Error

harrier.get_brand()

    

