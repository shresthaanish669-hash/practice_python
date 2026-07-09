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

#if else statement
age = 21

if(age >= 18):
    print("you are egible for license.")
    
Age = 12

if(Age >= 18):
    print("you can vote.")
else:
    print("you cannot vote.")

#Trafficlight using if else statement
light = "green"

if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Look")
else:
    print("Light is broken.")    

#Grade Calculator
marks = int(input("Enter student marks:"))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("Grade of the studen: ", grade)  

#nesting
age = 34
if(age >= 18):
    if(age >= 80):
        print("Cannot drive.")
    else:
        print("Can drive.")
else:
    print("Cannot drive.")

#Listing
marks = [94.5, 45.55,55,79]
print(marks)
print(type(marks))
print(len(marks))
print(marks[1])
print(marks[3])

student = ["Anish", 97, 19, "Kathmandu"]
print(student[0])
student[0] = "shree"
print(student)


#List slicing
num = [33, 45, 67, 98,199]
print(num[1:4])
print(num[ :2])
print(num[1: ])
print(num[-3:-1])


#List Method
list =[2, 3, 4, 5, 1]

#list.append(6)
#list.sort()
#list.sort(reverse=True)
#list.reverse()
#list.insert(0,7)
#list.remove(1)
#list.pop(1)
print(list)

#Tuples
tup = (2, 3, 1, 5, 3, 2, 11)

print(type(tup))
print(tup[0])
print(tup[1])
print(tup[ : 2]) #slicing

print(tup.index(1)) #Method
print(tup.count(3)) #Method

tups = ("hello",)
print(tups)
print(type(tups))

#Dictionaries
info ={

    "Key" : "value",
    "name" : "anishshrestha",
    "Age" : 20,
    "is adult" : "True",
    "learning" : "Coding",
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dict", "set"),
}

"""
info["surname"] = "shrestha"
null_dict = {}
null_dict["name"] = "shree"
print(null_dict)
"""

print(type(info))
print(info["name"])
print(info["Age"])
print(info["subjects"]) 
print(info)


#nested dictionary
student = {
    "name" : "Anish Shrestha",
    "subjects" : {
        "english" : 90,
        "math" : 85,
        "science" : 90,
    }
}

"""
print(student["subjects"]["math"])
print(student.keys()) #method
print(student.values()) #method
print(student.items()) #method
print(list(student.keys()))# typecasting changing dictionay into tuples
print(student.get("name)) #method

new_dict = {"city" : "kathmandu", "age": 20}
student.update(new_dict) #method


pairs = list(student.items()) 
print(pairs[0])

print(student.get("name2")) # no error -> none

print("before")
print(student["name2"]) # return error
print("after")

"""
print(student)

#Sets
collection = {1, 2, 3, 4, 4 ,5, "Hello World"}
print(collection.pop())

#collection = {} #empty dictionary
#collection = set() # empty set


deal = set()

deal.add(1)
deal.add(2)
deal.add("Pokharar")
deal.add((1, 2, 3)) #method
deal.remove((1,2, 3)) #method
deal.clear() #method

print(deal)

set1 = {1, 2 ,3, 3 ,4}
set2 = {4, 2, 5}

print(set1.union(set2))
print(set1.intersection(set2))

# while loop
i = 0
while i <= 5:
    print(i)
    i = i + 1
print("loop executed.")

count = 1
while count <= 5 :
    print("Hello", count)
    count += 1

#print number from 1 to 10
i = 1
while i<= 10 :
    print(i)
    i += 1
print("Loop Ended")

# #Break
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("End of loop")

#Continue
i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1 

#For loops
nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

fruits = ["Apple", "Banana", "Grapes"]

for val in fruits:
    print(val)
 
#tuples using in for loop
tup = (1, 2, 3, 4, 5)

for num in tup:
    print(num)

#string using in for loop
str = "AnishShrestha" 

for char in str:
    print(char) 

#For loop with else
str = "Aeroplane in Mars"

for char in str:
    print(char)
else:
    print("False")

#searching element i for loop
str = "Engineer"

for char in str:
    if(char == 'e'):
     print("e found")
     break
    print(char)

print("END")

num = [1, 3, 5, 6, 7, 8, 9]

for el in num:
   print(el)

#range
seq = range(5)

for i in seq:
    print(i)

#range(stop)
for x in range(5): 
    print(x)

#range(start, stop)
for y in range(2, 10): 
    print(y)

#range(start, stop, step)
for z in range(2, 10, 2): 
     print(z)

#odd even in range
for odd in range(1, 50, 2):
    print(odd)

for even in range(2, 50, 2):
    print(even)

#pass statement
for i in range(5):
    pass
if i > 5:
    pass
print("Use for for future code.")

#function definition
def calc_sum(a, b): #parameter
    return a + b
sum = calc_sum(1234, 2345) #function call; arguments
print(sum)

#without parameter and return value
def intro():
    print("Hello")

output = intro()
intro()
intro()
intro()
print(output) # it doesn't have return value so, it shows none.

#average of 3 number
def calc_avg(a, b, c):
    sum = (a + b + c)
    avg = sum / 3
    print(avg)
    return avg

calc_avg(23, 45, 65)

#Default parameter
def cal_prod(a=5, b=3):
    print(a * b)
    return a * b

cal_prod()

#recursive function
num = int(input("Enter number:"))
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

# show(num)

#factorial using recursive
num = int(input("Enter number:"))
def fact(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num * fact(num-1)
    
print(fact(num))

#File I/O BASIC
f = open("D:\practice_python\python\File_IO\demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

# reading a file
f = open("D:\practice_python\python\File_IO\demo.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

#to create file
f = open("sample.txt", "w")
f = open("sample.txt", "a")
f.close()

# writing to a file
#f = open("D:\practice_python\python\File_IO\demo.txt", "w") # to write
f = open("D:\practice_python\python\File_IO\demo.txt", "a") # to append
f.write("\n I takes time to learn.")
f.close()

#to overwrite from the starting
f = open("D:\practice_python\python\File_IO\demo.txt", "r+")
f.write("Hey")
print(f.read()) # to read the file after overwrite
f.close()

#with syntax
with open("D:\practice_python\python\File_IO\demo.txt", "r") as f:
    data = f.read()
    print(data)

#deleteing a file
import os
os.remove("sample.txt")

