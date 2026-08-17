students = {}

while True:
    print("\n===Student Grade Manager===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Show Average")
    print("4. Check Pass/Fail")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = str(input("Enter student name: "))
        math = float(input("Enter math marks: "))
        english = float(input("Enter english marks: "))
        science = float(input("Enter science marks: "))

        students[name] = {
            "Math" : math,
            "Science": science,
             "English": english
        }
        print("Student added!")

    elif choice == "2":
        if not students:
            print("No Students Found!")
        else:
            print("\n=== Students ===")

            for name, marks in students.items():
                print("\nName:", name)
                print("Math:", marks["Math"])
                print("Science:", marks["Science"])
                print("English:", marks["English"])

    elif choice == "3":
        name = str(input("Enter Student name: "))

        if name in students:
            marks = students[name]
            average = (marks["Math"] + marks["Science"] + marks["English"]) / 3
            print("Average:", average)

        else:
            print("Student not found!")

    elif choice == "4":
        name = str(input("Enter student name: "))

        if name in students:
            marks = students[name]
            average = (marks["Math"] + marks["Science"] + marks["English"]) / 3

            if average >= 40:
                print("Average:", average)
                print("Status: Pass")
            else:
                print("Average:", average)
                print("Status: Fail")

        else:
            print("Student Not Found!")

    elif choice == "5":
        print("GoodBye!")
        break

    else: 
        print("Invalid Option!")