import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: Task file is invalid.")
    return []

tasks = load_tasks()

def save_tasks():
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = input("Enter a task: ").strip()

    if task:
        tasks.append({"name": task, "completed": False})
        save_tasks()
        print("Task added.")
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{number}. {task['name']} [{status}]")

def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks()
            print("Task completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print(f"Deleted: {removed['name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def main():
    while True:
        print("\nTASK TRACKER")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
