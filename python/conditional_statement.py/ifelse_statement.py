age = 21

if(age >= 18):
    print("you are egible for license.")

light = "green"

if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Look")
else:
    print("Light is broken.")    

Age = 12

if(Age >= 18):
    print("you can vote.")
else:
    print("you cannot vote.")

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