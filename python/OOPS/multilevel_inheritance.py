class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)   # Call Person's constructor
        self.roll = roll

    def display_roll(self):
        print("Roll No:", self.roll)

class College_Student(Student):
    def __init__(self, name, roll, college):
        super().__init__(name, roll)   # Call Student's constructor
        self.college = college

    def display_college(self):
        print("College:", self.college)

s = College_Student("Anish", 1, "Xavier International College")

s.display_name()
s.display_roll()
s.display_college()