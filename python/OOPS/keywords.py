#Static Method
class Teacher:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def hello():
        print("Hell0")

t1 = Teacher("Ram")
t1.hello()

#static keywords
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))

#del Keywords
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Anish")
s2 = Student("Ram")

print("Student 1:", s1.name)
print("Student 2:", s2.name)

#deleting the s2 object
del s2
print("S2 has been deleted.")

print("Student 1:", s1.name)
