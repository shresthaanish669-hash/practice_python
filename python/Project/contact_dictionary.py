contacts = {}

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")  

    choice = input("Choose an option:")

    if choice == "1":
        name = str(input("Enter Name: "))
        phone = int(input("Enter Number: "))

        contacts[name] = phone
        print("Contact added!")

    elif choice == "2":
        if not contacts:
            print("No contacts found!")
        else:
            print("\nYour Contacts:")

            for name, phone in contacts.items():
              print("Name: ", name)
              print("Phone: ", phone)

    elif choice == "3":
        name = str(input("Enter the name to search: "))

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name])
        else:
            print("Contact not found!")

    elif choice == "4":
        name = str(input("Enter the name to delete: "))

        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif choice == "5":
        print("GoodBye!")
        break
    else:
        print("Invalid Option!")