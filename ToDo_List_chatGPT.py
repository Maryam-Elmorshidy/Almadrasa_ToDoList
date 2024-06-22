def print_intro():
    print("\n\n----------------------------------------------------------")
    print("ToDo List")
    print("----------------------------------------------------------\n")

def display_menu():
    return input("What do you want to do? (add, view, remove, exit)\n ==> ").lower().strip()

def add_task(tasks):
    additional_task = input("Add new task: ").strip()
    if additional_task:
        tasks.append(additional_task)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")
    print("----------------------------------------\n")

def view_tasks(tasks):
    if tasks:
        print("My tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("There are no tasks.")
    print("----------------------------------------\n")

def remove_task(tasks):
    if tasks:
        del_task = input("Enter the task to delete: ").strip()
        if del_task in tasks:
            tasks.remove(del_task)
            print("Task removed successfully.")
        else:
            print(f"Task '{del_task}' does not exist.")
    else:
        print("There are no tasks.")
    print("----------------------------------------\n")

def main():
    tasks = []
    print_intro()

    while True:
        task = display_menu()
        print("----------------------------------------\n")

        if task == "add":
            add_task(tasks)
        elif task == "view":
            view_tasks(tasks)
        elif task == "remove":
            remove_task(tasks)
        elif task == "exit":
            print("Exiting the ToDo List application.")
            break
        else:
            print("Invalid option. Please try again.")
            print("----------------------------------------\n")

if __name__ == "__main__":
    main()
