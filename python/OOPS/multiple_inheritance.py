#Multiple Inheritance
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

#Pratice multiple inheritance
class Fruits:
    varFruits = "Banana"

class Animal:
    varAnimal = "Monkey"

class Statement(Fruits,Animal):
    varStatement = "Monkey eats Banana."

c1 = Statement()

print(c1.varAnimal)
print(c1.varFruits)
print(c1.varStatement)