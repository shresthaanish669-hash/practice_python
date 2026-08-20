while True:
    print("\n===Temerature Converter===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        celsius = float(input("Enter temperature in celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print("Fahrenheit: ", fahrenheit)

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("Celsius: ", celsius)

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")