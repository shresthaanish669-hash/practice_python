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

