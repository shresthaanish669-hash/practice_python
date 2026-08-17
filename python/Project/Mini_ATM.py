account = {
    "name": "AnishShrestha",
    "balance": 150000,
    "pin": "1010",
    "type": "saving account"
}
print("=== Welcome to the ASTON ATM ===")

attempts = 3
while attempts > 0:

    pin = input("\nEnter Your Pin: ")
    if pin == account["pin"]:
        print("\nPIN accepted.")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("\nYour card has been blocked.")
    print("Please contact your bank.")

else:
    print("\n================================")
    print(" Welcome", account["name"])
    print("================================")

    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Cash Deposit")
        print("3. Cash Withdrawal")
        print("4. Account Details")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("YOUR BALANCE IS: RS.", account["balance"])

        elif choice == "2":
            amount = float(input("Enter Your Amount: "))

            if amount > 0:
                account["balance"] = account["balance"] + amount
                print("Cash deposited successfully.")
                print("NEW BALANCE: RS.", account["balance"])
            else:
                print("Invalid amount!")

        elif choice == "3":
            amount = float(input("Enter Your Amount: "))

            if amount <= 0:
                print("Invalid Amount!")
            elif amount > account["balance"]:
                print("Insufficient Balance!")
            else:
                account["balance"] = account["balance"] - amount
                print("Collect Your Cash.")
                print("NEW BALANCE: RS.", account["balance"])

        elif choice == "4":
            print("\nAccount Name:", account["name"])
            print("Account Balance: RS.", account["balance"])
            print("Account Type:", account["type"])

        elif choice == "5":
            print("THANK YOU!")
            print("Have a nice day!")
            break

        else:
            print("Invalid Option!")