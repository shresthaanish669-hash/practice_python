class BankAccount:
    def __init__(self, name, account_number, balance =0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit Successfully.")
        else:
            print("Invalid Amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Amount!")
        elif amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Withdrawal Successful.")

    def check_balance(self):
        print("Balance: RS.", self.balance)

    def account_details(self):
        print("\n==ACCOUNT DETAILS==")
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

accounts = []

while True:
    print("\n===BANK ACCOUNT SYSTEM===")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Account Details")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter Your Name: ")
        account_number = int(input("Enter account number: "))
        account = BankAccount(name, account_number)
        accounts.append(account)
        print("Account Created Successfully.")

    elif choice == "2":
        account_number = int(input("Enter account number: "))
        found = False

        for account in accounts:
            if account.account_number == account_number:
                account.check_balance()
                found = True
                break

        if not found:
            print("Account not found.")

    elif choice == "3":
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        found = False

        for account in accounts:
            if account.account_number == account_number:
                account.deposit(amount)
                found = True
                break

        if not found:
                print("Account not found!")

    elif choice == "4":
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        found = False
        
        for account in accounts:
            if account.account_number == account_number:
                account.withdraw(amount)
                found = True
                break
        
        if not found:
         print("Account not found!")

    elif choice == "5":
        account_number = int(input("Enter account number: "))
        found = False
        
        for account in accounts:
            if account.account_number == account_number:
                account.account_details()
                found = True
                break
        
        if not found:
            print("Account not found!")
        
    elif choice == "6":
        print("Thank you for using banking system!")
        break

    else:
        print("Invalid Choice!")