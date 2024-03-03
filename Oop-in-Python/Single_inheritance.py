class Person:
    def __init__(self,fn,ln,gender,age):
        self.fname = fn
        self.lname = ln
        self.gender = gender
        self.age = age
    
    def walk(self,step):
        print(f"Person Walked {step} in a day.")
    
class Student(Person):
    def __init__(self,sid,grade,fn, ln, gender, age):
        self.studentid = sid
        self.grade = grade
        super().__init__(fn, ln, gender, age)
    
    def printname(self):
        print(f"Student name is {self.fname} {self.lname}.")

s1 = Student(101,"A","Jackey","Chain","Male",67)
print(s1.lname)
print(s1.fname)
s1.walk(30)
s1.printname()
    