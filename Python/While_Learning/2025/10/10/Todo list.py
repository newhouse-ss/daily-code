todo_list = []
print("Welcome to the Todo List application.")
def add_task(task, priority):
    todo_list.append({'task': task, 'priority': priority})
    print(f"{task} and {priority} are added into Todo List.")

def view_todolist():
    if not todo_list:
        print("Your todolist is empty.")
    else:
        print("These are your tasks: ")
        for index, task in enumerate(todo_list):
            print(f"The index: {index+1}, content: {task}")
    
def remove_task(task_number):
    task_number = int(task_number)
    try:
        if task_number >=1 and task_number<=len(todo_list):
            todo_list.pop(task_number-1)
            print(f'The {task_number}-th task has been removed.')
        else:
            print("The given number reach out the total number of current tasks.")
    except ValueError:
        print("Input the valid number.")

def completion(task_number):
    '''
    argus: task_number is received by input(), so it should be a string.
    '''
    task_number = int(task_number)
    try:
        if task_number-1 not in range(len(todo_list)):
            print("Invalid No.")
        elif 'completion' in todo_list[task_number-1]:
            print("Already finished.")
            return None
        else:
            todo_list[task_number-1] = f'[completion]{todo_list[task_number-1]}'
            print("completed.")

    except ValueError:
        print("Input the valid number.")

def save_to_file():
    try:
        with open('todolist', 'a') as file:
            for task in todo_list:
                file.write("\n")
                file.write(str(task))
            print("saved.")
    except FileNotFoundError:
        print("No such file.")
    except Exception as e:
        print(f'Something wrong: {e}')

def load_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                todo_list.append(line)
    except FileNotFoundError:
        print("No such file.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Complete task")
        print("5. Exit")
        print("6. Save to file")
        print("7. Load from file")

        choice = input("Input your choice: ")

        if choice == '1':
            task = input("Input the task you want: ")
            priority = input("Give the priority to this task: ")
            add_task(task, priority)
        elif choice == '2':
            view_todolist()
        elif choice == '3':
            task_number = input("Input the task number you want remove: ")
            remove_task(task_number)
        elif choice == '4':
            task_number = input('Input the task number you want to finish: ')
            completion(task_number)
        elif choice == '5':
            print("See you next time.")
            break
        elif choice == '6':
            save_to_file()
        elif choice == '7':
            file_name = input("Give the filename you want to load: ")
            load_from_file(file_name)
            print("Loading finished.")
            view_todolist()
        else:
            print('Please input the valid number.')

if __name__ == '__main__':
    main()