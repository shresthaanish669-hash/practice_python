#print hello world
print ("hello world!")

#Variable
x = 7
print(x)
x = float(7)
print(x)
y = int(9.9)
print(y)
a = input("Enter any number:")
print(a)
b = input("Enter your name:")
print("Hello " + b)

#Taking input from user
x = int(input("Enter any number: "))
y = int(input("Enter any number: "))
z = int(input("Enter any number: "))

a = int(x + y)
print("The sum of two number is " + str(a))

b = int(a - z)
print("The subtraction of two number is  " + str(b))

c = int(x * y)
print("The multiplication of two number is " +str(c))

d = int(x / y)
print("The Division of two number is " +str(d))

#UpperCase and LowerCase
letter = "Anish"
print(letter.upper())
print(letter.lower())
print(letter.find("i"))
print(letter.replace("i" , "s"))

#UpperCase and Lowercase taking input from user.
letter = input("Enter your name:")
print(letter.upper())
print(letter.lower())
print(letter.find("i"))
print(letter.replace("n" , "s"))

#if else condition statement
x = "Anish" 

if x == "Anish":
    print("True")

elif x == "Anis":
    print("h is missing.")

else:
    print("Enter again.")

#if else statement and taking input from user.
x: str = input("Enter Your Name:" ).lower()
print(x)

if x == "anish":
    print("Proper Name.")

elif x == "sushank":
    print("Proper Name.")

elif x == "yurish":
    print("Proper Name.")

elif x == "subin":
    print("Proper Name.")

else:
    print("Enter again.")

#ODD or Even
num = int(input("Enter any number"))
#print("Even" if num % 2 == 0 else "odd" )

if num % 2 == 0:
    print("The given number is even.")
else:
    print("The given number is odd.")

#if else statement and taking input from user.
name = input("Enter Your name: ")
if name.lower() == "anish":
    birth_year = int(input("Enter your year of birth(A.D): "))
    age = 2026 - birth_year
    print("Your age is " + str(age))

    if age < 25:
        print("You have time.")
    else:
        print("You don't have much time.")
    
else:
    print("Enter again")

#Grade Claculator
sub = input("Enter the subject:")
print("The subject is " + sub)

marks = int(input("Ener the marks between 0-100 "))

if marks >= 80:
    print("A")

elif 60 <= marks <= 79:
    print("B")

elif 40 <= marks <= 59:
    print("C")

else:
    print("F")

# if else
name = input("Enter your name:")
if name.lower() == "anish shrestha":
    birth_year = int(input("Enter your age: "))
    age = 2026 - birth_year
    print("Your current age is: " + str(age))

    Future = 10 + age
    print("Your age after 10 years is:" + str(Future))
else:
    print("Enter again.")    