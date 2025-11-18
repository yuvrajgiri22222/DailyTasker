tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks added yet.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == "3":
        task_no = int(input("Enter task number to remove: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")