class Person:
    # Class Variable
    hair_color = "black"
    def __init__(self,fname,lname,gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender
    
# Creating Object of Class

p1 = Person("Jack","Pearo","male")
p2 = Person("Jackey","chain","male")
p3 = Person("raso","mile","Female")
print(p1.hair_color)
print(p2.hair_color)
print(p3.hair_color)
    
