# Initialize an empty list to store tasks
tasks = []

# Function to display tasks
def show_tasks():
    if not tasks:
        print("No tasks available!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to delete a task
def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Exiting the To-Do List app. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")