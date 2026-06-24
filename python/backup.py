# Basic  python code
print ("hello world!")
print("My name is anish.")
print("My age is 20.")

print("My name is anish.", "My age is 20.")

print(50)
print(50 + 50)


#Variable
x = 7
print(x)

y = float(7)
print(y)

z = int(9.9)
print(z)

name = "Anish"
age = 20
print("my name is : ", name)
print(" my age is : ", age)

a = input("Enter any number:")
print(a)

b = input("Enter your name:")
print("Hello " + b)

#arthimetic operator
a = 10
b = 2

print( a + b )
print( a - b )
print( a * b )
print( a / b )
print( a % b ) # remainder
print( a ** b ) # a^2

# relational operators 
a = 50
b = 30

print( a == b) #false
print( a != b) #true
print( a >= b) #true
print( a > b) #true
print( a <= b) #false
print( a < b) #false

#assignment oerators
num = 10 
num *= num + 20
print("num:", num)

#logical operator
a = 50
b = 10
print( not False )
print( not (a > b))

value1 = True
value2 = False
print("And operator:", value1 and value2)
print("OR operator:", value1 or value2)

#type conversion
a = int("5")
b = 5.555

print(a + b)

# str = "This is a string."
# str = 'This is a string too.'
# str = """This is also a string."""

strr = "This is a string.\n we are creating in python."
print(strr)

# Concatenation
str1 = "Hello"
str2 = "World"

print( str1 + str2 )
final_str = str1 + str2
print( final_str)

#Length of string
str3 = "Software"
print( len(str3))

#Indexing
string = "Computer"
print(string[4])

#Slicing
x = "Engineering"
print(x[1:5])
print(x[11:])

#Negative slicing
y = "Apple"
print(y[-3:-1])

#String Function
a = "I am a student"
print(a.endswith("ent"))

b = "i am a coder"
print(b.capitalize())

c = "I am learing python from youtube"
print(c.replace("youtube", "chatgpt"))

d = "Find your name."
print(d.find("your"))

e = " I am learing java and javascript  from youtube"
print(e.count("java"))

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

# while loop
i = 0
while i <= 5:
    print(i)
    i = i + 1
print("loop executed.")