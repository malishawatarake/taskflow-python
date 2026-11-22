
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available!")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ").strip()

        if task:
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()

        if tasks:
            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
