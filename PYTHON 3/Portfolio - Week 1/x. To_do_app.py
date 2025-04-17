# todo_app.py

# Start with an empty list of tasks
tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("You chose to add a task.")
    elif choice == "2":
        print("You chose to view tasks.")
    elif choice == "3":
        print("You chose to delete a task.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please enter a number from 1 to 4.")
