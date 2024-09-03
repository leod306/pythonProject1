# Leo Dahlen
#CBIS 4210
#assignment 2.1
# 9/3/2024

# create a to do list program that allows the user to add tasks, remove tasks, and view tasks

# Task Management in a Procedural Style

# Task Management Program in Procedural Style with Inline Comments

# Global list to store tasks as dictionaries
tasks = []


# Function to add a task
def add_task():
    # Getting task details from the user
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    start_time = input("Enter start time: ")
    end_time = input("Enter end time: ")

    # Creating a dictionary to represent the task
    task = {
        "name": name,
        "description": description,
        "start_time": start_time,
        "end_time": end_time
    }

    # Adding the task dictionary to the global tasks list
    tasks.append(task)


# Function to remove a task by its name
def remove_task():
    task_name = input("Enter the name of the task to remove: ")

    # Using global to modify the global tasks list
    global tasks

    # Filtering out the task with the matching name
    tasks = [task for task in tasks if task["name"] != task_name]


# Function to view all tasks
def view_tasks():
    # If there are no tasks, inform the user
    if not tasks:
        print("No tasks available.")
        return

    # Loop through each task in the tasks list and print its details
    for task in tasks:
        print(f"\nTask: {task['name']}")
        print(f"Description: {task['description']}")
        print(f"Start Time: {task['start_time']}")
        print(f"End Time: {task['end_time']}\n")


# Main function to control the flow of the program
def main():
    while True:
        # Displaying the menu to the user
        print("\nTime Management Program")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        # Taking the user’s choice as input
        choice = input("Enter your choice: ")

        # Using if-elif structure to handle the user's choice
        if choice == '1':
            add_task()  # Call to add a task
        elif choice == '2':
            remove_task()  # Call to remove a task
        elif choice == '3':
            view_tasks()  # Call to view all tasks
        elif choice == '4':
            break  # Exit the program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid inputs


# Entry point of the program
if __name__ == "__main__":
    main()

