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
        Person.__init__(self,fn, ln, gender, age)
    
    def printname(self):
        print(f"Student name is {self.fname} {self.lname}.")

class Teacher(Student):
    pass

t1 = Teacher(101,"c","Geeni","Golde","Female",45)
t1.printname()
t1.walk(80)
        

