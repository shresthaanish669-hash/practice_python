""" QS NO:1
WAP to input 2 numbers and print their sum.
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
sum = (x + y)
print("sum of two number = ",sum)
 """

""" QS NO:2
WAP to input number and find square and print its area.
side = float(input("Enter a number : "))
print(side * side)
"""

""" QS NO:3
WAP to take input 2 floating point and find its average.
a = float(input("Enter first num:"))
b = float(input("Enter second num:"))
print("avg:", (a + b)/2)
"""

""" QS NO:4
WAP to input 2 int num a and b, print True if a is greater and False if not.
num1 = int(input("Enter a num:"))
num2 = int(input("Enter a num:"))
print(num1 >= num2)
"""

""" QS NO:5
WAP to input user's first name and its length.
name = input("Enter your name:")
print("The length of your name is", len(name))
"""

""" QS NO:6
WAP to find the occurance of '$' in a string.
tr = "$The coder$ is$ back$."
print("The count of dollor is:", str.count("$"))
"""

""" QS NO:7
WAP to check if a number entered by the user is odd or even.
num = int(input("Enter a number:"))
if(num == 2):
    print("The given number is even.", num)
else:
    print("The given number is odd.", num)

#Alternative method
num = int(input("Enter a number:"))

rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")
"""

""" QS NO:8
WAP to find the greatest of 3 numbers entered by the user.
a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
c = int(input("Enter third num: "))

if( a > b and a > c ):
    print("The first number is greater.")
elif( b > c and b > a ):
    print("The second number is greater number.")
else:
    print("The third number is greatest number.")
"""

""" QS NO:9
WAP to check if a number is a multiple of 7 or not.
if(x % 7 == 0):
    print("Multiple of 7")
else: 
    print("not a multiple of 7")
"""

"""  QS NO:10
WAP to ask user to enter names of their 3 favorite mavies and store them in list.
movies = []
flim1 = str(input("Enter 1st movie."))
flim2 = str(input("Enter 2nd movie."))
flim3 = str(input("Enter 3rd movie."))

movies.append(flim1)
movies.append(flim2)
movies.append(flim3)

print(movies)
"""

""" QS NO:11
WAP to check if list contains a palindrome of elements.
list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("is palindrome.")
else:
    print("is not palindrome.")
"""

""" QS NO:12
WAP to count the number of students with the "A" grade in the following tuple.
grade = ["C", "D", "A", "D", "A", "B", "B", "C"]
grade.sort()
print(grade)
"""

""" QS NO:13
Store a following words meanings in python dictionary.
Also present how many classroom are needed by all students for the given subjects.

dictionary = {
    "Cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}
print(dictionary)

subjects= {
    "python", "java", "c++", "python",
    "javascript", "java", "python", "c++", "c"
}
print(len(subjects))
"""

""" QS NO:14
WAP to enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary & add one by one. use subject name as key & marks as value.
marks = {}

x = int(input("Enter the marks of math: "))
marks.update({"math": x})

y = int(input("Enter the marks of science:"))
marks.update({"science": y})

z = int(input("Enter the marks of Physics:"))
marks.update({"physics": z})

print(marks)
"""

""" QS NO:15
Figure out a way to store 9 & 9.0 as seperate values in the set.
values = {
    ("float", 9.0),
    ("int", 9),
}
print(values)
"""

""" QS NO:16
WAP to print numbers from 1 to 100.
num = 1
while num <= 100 :
    print(num)
    num += 1

print("Program Executed")
"""

""" QS NO:17
WAP to print numbers from 100 to 1.
count = 100
while count >= 1 :
    print(count)
    count -= 1

print("Program Executed.")
"""

"""QS NO:18
WAP to print the multiplication table of a number n.
n = int(input("Enter a number:"))

i = 1
while i <= 10:
    print(n*i)
    i += 1
"""

"""QS NO:19
Print the elements of the following list using loops.
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] #traverse

idx = 0
while idx < len(num):
    print(num[idx]) #num[0], num[1], num[2]....
    idx += 1 
"""

"""QS NO:20
Search for a number x in this tuple using loops.
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
 
x = 36

i = 0 #initialization
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
        break
    else:
        print("Finding..")
    i += 1

print("end of loop..")
"""

"""QS NO:21
print the elements of the following list using a loop and search for 
a number x in this tuples using loop.
num = [1, 4, 9, 25, 36, 45, 55,60, 81, 100]
x = 60

idx = 0
for el in num:
    if(el == x):
     print("number found at idx", idx)
     break
    idx += 1 
"""

""" QS NO:22
print numbers from 1 to 25
for num in range(1, 26):
    print(num)
"""

""" QS NO:23
print numbers from 25 to 1.
for num in range(25, 0, -1):
    print(num)
"""

"""QS NO:24
print the multiplication table of a number n.
n = int(input("Enter number:"))

for multi in range(1, 11):
    print(n * multi)
"""

"""QS NO:25 
WAP to find the sum of first n numbers.(using for)
num = int(input("Enter number:"))

sum = 0
for i in range(1, num+1):
    sum += i

print("total sum=", sum)
"""

"""QS NO:26
WAP to find the sum of first n numbers.(using while)
num = int(input("Enter number:"))

sum = 0
i = 1
while i <= num:
    sum += i
    i += 1

print("total sum=", sum)
"""

"""QS NO:27
WAP to find the factorial of fist n numbers.(using while loop)
num = int(input("Enter number:"))

fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1

print("total factorial=", fact)
"""

"""QS NO:28
WAP to find the factorial of fist n numbers.(using for loop)
num = int(input("Enter number:"))

fact = 1

for i in range(1, num+1):
    fact *= i

print("Factorial =", fact)
"""

"""QS NO:29
WAP to print the length of a list.(using function)
cities = ["Kathmandu", "Pokhara", "Gorkha"]
fruits = ["Apple", "Banana", "Orange"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(fruits)
"""

"""QS NO:30
WAP to print the elements of a list in a single line.(using function)
heros = ["Spider-man", "Black panther", "Iron man", "Thor"]

def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(heros)
"""

"""QS NO:31
WAP to find the factorial on n.
n = int(input("Enter number:"))

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
      fact *= i
    print(fact)

calc_fact(n)
"""

"""QS NO:32
WAP to convert USD to NPR.
ruppee = int(input("Enter number:"))
def converter(usd_val):
    npr_val = usd_val * 151
    print(usd_val, "USD =", npr_val, "NPR")
converter(ruppee)  
"""
