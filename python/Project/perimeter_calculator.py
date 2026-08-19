import math

while True:
    print("\n===Perimeter Calculator===")
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Circle")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        perimeter = 2 *(length + breadth)

        print("Perimeter of rectangle is ", perimeter)

    elif choice == "2":
        length = float(input("Enter length: "))
        perimeter = 4 * length

        print("Perimeter of square is ", perimeter)

    elif choice == "3":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        height = float(input("Enter height: "))
        perimeter = length + breadth + height

        print("Perimeter of triangle is ", perimeter)

    elif choice == "4":
        radius = float(input("Enter radius: "))
        perimeter = 2 * 3.14 * radius

        print("Perimeter of circle is ", perimeter)

    elif choice == "5":
        print("Thank you for using Area Calculator!")
        break


    else:
        print("Invalid Choice!")