""" First Question
WAP to input 2 numbers and print their sum.
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
sum = (x + y)
print("sum of two number = ",sum)
 """

""" Second Question
WAP to input number and find square and print its area.
side = float(input("Enter a number : "))
print(side * side)
"""

""" Third Question
WAP to take input 2 floating point and find its average.
a = float(input("Enter first num:"))
b = float(input("Enter second num:"))
print("avg:", (a + b)/2)
"""

""" Fourth Question
WAP to input 2 int num a and b, print True if a is greater and False if not.
num1 = int(input("Enter a num:"))
num2 = int(input("Enter a num:"))
print(num1 >= num2)
"""

""" Fifth Question
WAP to input user's first name and its length.
name = input("Enter your name:")
print("The length of your name is", len(name))
"""

""" Sixth Question
WAP to find the occurance of '$' in a string.
tr = "$The coder$ is$ back$."
print("The count of dollor is:", str.count("$"))
"""

""" seventh Question
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

""" Eight Question
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

""" Ninth Question
WAP to check if a number is a multiple of 7 or not.
if(x % 7 == 0):
    print("Multiple of 7")
else: 
    print("not a multiple of 7")
"""

""" Tenth Question
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

""" Eleventh Question
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

"""Twelev Question
WAP to count the number of students with the "A" grade in the following tuple.
grade = ["C", "D", "A", "D", "A", "B", "B", "C"]
grade.sort()
print(grade)
"""
