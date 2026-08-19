class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        if self.available:
            status = "Available"
        else:
            status = "Borrowed"

        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)

books = []

while True:
    print("\n===Library Management System===")
    print("1.Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        book = Book(title, author)
        books.append(book)

        print("Book added successfully!")

    elif choice == "2":
        if not books:
            print("No books available.")
        else:
            print("\n===Books===")

            for book in books:
                book.display()

    elif choice == "3":
        title = input("Enter book title to search: ")
        found = False

        for book in books:
            if book.title.lower() == title.lower():
                book.display()
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "4":
        title = input("Enter book title to borrow:")
        found = False

        for book in books:
            if book.title.lower() == title.lower():
                found = True

                if book.available:
                    book.available = False
                    print("Book borrwoed successfully.")
                else:
                    print("Book is already borrowed.")
                break

        if not found:
            print("Book not found.")

    elif choice == "5":
        title = input("Enter book title to return: ")
        found = False

        for book in books:
            if not book.available:
                book.available = True
                print("Book returned successfully.")
            else:
                print("This book was not borrowed.")
            break

        if not found:
            print("Book not found.")

    elif choice == "6":
        print("Thank You for using libaray maangement system!")
        break

    else:
        print("Invalid Choice!")