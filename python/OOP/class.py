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

# #Constructor
# class Student:

#  #default constructor 
#     # def __init__(self)

# #Parameterized constructor
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print("adding new student in Database.")

# s1 = Student("Anish", 85)
# print(s1.name, s1.marks)

# s2 = Student("shree", 94)
# print(s2.name, s2.marks)

# #Class and object attributes
# class Employee:
#     company_name = "ABC Company"
#     name = "Anonymous" #class attr

#     def __init__(self, fullname, id):
#         self.name = fullname
#         self.id = id
#         print("adding new student in Database.")

# e1 = Employee("Anish", 11)
# print(e1.name, e1.id)
# print(e1.company_name)

# #Methods
# class Student:
#     college_name = "ABC College"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def welcome(self): #method
#         print("Welcome,", self.name)

#     def get_marks(self):
#         return self.marks
    
# s1 = Student("Anish", 89)
# s1.welcome()
# print(s1.get_marks())

#Static Method
class Teacher:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def hello():
        print("Hell0")

t1 = Teacher("Ram")
t1.hello()