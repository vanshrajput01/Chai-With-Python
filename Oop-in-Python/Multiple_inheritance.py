class Person:
    def __init__(self,fn,ln,gender,age):
        self.fname = fn
        self.lname = ln
        self.gender = gender
        self.age = age
    
    def walk(self,step):
        print(f"Person Walked {step} in a day.")
    
class Student:
    def __init__(self,sid,grade):
        self.studentid = sid
        self.grade = grade

    
    def printname(self):
        print(f"My name is {self.fname} {self.lname}.")
    
class Teacher(Person,Student):
    def __init__(self, tid,subject,fn, ln, gender, age,sid,grade):
        self.teacher_id = tid
        self.subject = subject
        Person.__init__(self,fn, ln, gender, age)
        Student.__init__(self,sid,grade)
        
    
    def year_of_exp(self,year):
        print(f"{self.fname} have more than {year}+ Exp.")
    
t1 = Teacher(301,"Math","Maine","Jone","Female",34,101,"B")
t1.walk(20)
# t1.grade error
t1.year_of_exp(10)
t1.printname()
print(t1.grade)


