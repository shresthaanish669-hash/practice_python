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
print(list(student.keys()))# typecasting changing dict into tuples
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