expenses = []

while True:
    print("\n=== EXPENSES TRACKER ===")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter expenses name: ")
        amount = float(input("Enter amount: "))

        expense = {
            "name": name,
            "amount": amount
        }

        expenses.append(expense)

        print("Expenses added!")

    elif choice == "2":
        if not expenses:
            print("No expenses found!")
        else:
            print("\nYour Expenses:")

            for expense in expenses:
                print(
                    "Name:", expense["name"],
                    "| Amount: RS.", expense["amount"]
                )

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("\nTotal Expenses: RS.", total)

    elif choice == "4":
        print("GoodBye!")
        break

    else:
        print("Invalid Option!")