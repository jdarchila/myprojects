# todo_app.py

FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks():
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        new_task = input("Enter your task: ")
        tasks.append(new_task)
        save_tasks()  # ✅ <--- this is what was missing!
        print(f"Task '{new_task}' added successfully.")

    elif choice == "2":
        if not tasks:
            print("\nYour to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if not tasks:
            print("Nothing to delete. Your to-do list is empty.")
        else:
            print("\nWhich task do you want to delete?")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            try:
                task_num = int(input("Enter task number: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks()  # ✅ <--- also missing!
                    print(f"Task '{removed}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please enter a number from 1 to 4.")
