class Collage:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def studentDetails(self):
        print(f"Student Details is {self.fname} {self.lname}.")

student01 = Collage("Jack","Rones")
print(student01.fname) 
print(student01.lname)
student01.studentDetails()



