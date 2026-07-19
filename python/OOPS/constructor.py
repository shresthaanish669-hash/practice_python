#Constructor
class Student:

 #default constructor 
    # def __init__(self)

#Parameterized constructor
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in Database.")

s1 = Student("Anish", 85)
print(s1.name, s1.marks)

s2 = Student("shree", 94)
print(s2.name, s2.marks)