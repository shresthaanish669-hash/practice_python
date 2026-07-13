# class Student:
#     name = "Anish"
#     roll_no = 3
#     semester = 4

# S1 = Student()
# print(S1.name)
# print(S1.roll_no)

# class Car:
#     color ="Black"
#     model = "BMW M5"

# C1 = Car()
# print(C1.model)

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