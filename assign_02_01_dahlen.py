# Leo Dahlen
#CBIS 4210
#assignment 2.1
#8/31/2024

# create a to do list program that allows the user to add tasks, remove tasks, and view tasks

class Task:
    def __init__(self, name, description, start_time, end_time):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Task: {self.name}\nDescription: {self.description}\nStart Time: {self.start_time}\nEnd Time: {self.end_time}\n"

class TimeManagement:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def view_tasks(self):
        for task in self.tasks:
            print(task)

def main():
    tm = TimeManagement()

    while True:
        print("\nTime Management Program")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            start_time = input("Enter start time: ")
            end_time = input("Enter end time: ")
            task = Task(name, description, start_time, end_time)
            tm.add_task(task)
        elif choice == '2':
            task_name = input("Enter the name of the task to remove: ")
            tm.remove_task(task_name)
        elif choice == '3':
            tm.view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()