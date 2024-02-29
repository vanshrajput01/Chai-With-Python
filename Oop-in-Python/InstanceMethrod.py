class Person:
    def __init__(self,fname,lname,a):
        self.firstname = fname
        self.lastname = lname
        self.age = a

    # instance Methrod
    def printname(self):
        return f'My name is {self.firstname} {self.lastname}.'
    
# creating object of Person Class
p1 = Person("Uncle","Tom",56)
print(p1.firstname)
