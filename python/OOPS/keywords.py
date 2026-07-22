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

#class Methods
class Teacher:
    name = "Anonymous"

    #def changeName(obj, name):
    #   swlf.__class__.name = "Anish Shrestha"

    @classmethod
    def changeName(cls, name):
        cls.name = name

t1 = Teacher()
t1.changeName("AnishShrestha")
print(t1.name)
print(Teacher.name)

#property Decorator
class Student:
    def __init__(self, eng, nep, math):
        self.eng = eng
        self.nep = nep
        self.math = math

    @property
    def percentage(self):
        return str((self.eng + self.nep + self.math) / 3) + "%"

st1 = Student(99, 90, 98)
print(st1.percentage)

st1.eng = 86
print(st1.percentage)

# getter and setter method
class Employee:
    def __init__(self, name):
        self.__name = name
    
    #getter
    def get_name(self):
        return self.__name
    
    #setter
    def set__name(self, name):
        self.__name = name

e1 = Employee("Ram")
print(e1.get_name()) #Getter

e1.set__name("Sita") #Setter
print(e1.get_name())
