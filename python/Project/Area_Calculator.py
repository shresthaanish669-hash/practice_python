import math

while True:
    print("\n=== Area Calculator ===")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Exit")

    choice = input("Choose an Option: ")

    if choice == "1":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        area = length * breadth
        print("Area of rectangle is:", area)

    elif choice == "2":
        radius = float(input("Enter radius: "))
        area = 3.14 * radius ^ 2
        print("Area of circle is:", area)

    elif choice == "3":
        breadth = float(input("Enter breadth: "))
        height = float(input("Enter height: "))
        area = 0.5 * breadth * height
        print("Area of triangle is:", area)

    elif choice == "4":
        print("Thank you for using Area Calculator!")
        break

    else:
        print("Invalid Choice!")