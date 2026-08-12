tasks = []

while True:
    print("\nTo-Do-List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Tasks")
    print("4. Quit")

    choice = input("Choose an Option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")

        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet.")

    elif choice == "3":
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task removed!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to remove.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")