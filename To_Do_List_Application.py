# To-Do List Application

# Create an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

# Function to display all tasks
def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks in the list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Main program loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Exiting the application. Goodbye. Have a Goodday!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
