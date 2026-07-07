# #For loops
nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

fruits = ["Apple", "Banana", "Grapes"]

for val in fruits:
    print(val)
 
tup = (1, 2, 3, 4, 5)

for num in tup:
    print(num)

str = "AnishShrestha" 

for char in str:
    print(char) 

#For loop with else
str = "Aeroplane in Mars"

for char in str:
    print(char)
else:
    print("False")

#searching element in for loop
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