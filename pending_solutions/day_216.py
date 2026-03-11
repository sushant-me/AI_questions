"""
Create to-do list program.
"""

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

def main():
    todo = ToDoList()
    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo.remove_task(task)
        elif choice == "3":
            todo.list_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()