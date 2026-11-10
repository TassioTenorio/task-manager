
import os

tasks = []


def display_menu():
    os.system('cls')
    print('1. Add task')
    print('2. View tasks')
    print('3. Remove task')
    print('4. Exit')


def finish_app():
    display_subtitle('Closing application')


def display_subtitle(text):
    os.system('cls')
    line = '*' * len(text)
    print(line)
    print(text)
    print(line)
    print()


def choose_option():
    try:
        option = int(input('Choose an option: '))
    except ValueError:
        print('Error: Please enter a number!')
        return_to_main_menu()
        return

    if option < 1 or option > 4:
        invalid_option()
        return

    if option == 1:
        add_task()
    elif option == 2:
        view_tasks()
    elif option == 3:
        remove_task()
    elif option == 4:
        exit_program()


def return_to_main_menu():
    input('\nPress Enter to return to the main menu: ')
    main()


def invalid_option():
    print('Invalid option! Please choose a number between 1 and 4.')
    return_to_main_menu()


def add_task():
    display_subtitle('Adding a task')
    task = input('Enter the task: ')

    if not task.strip():
        print('Error: Task cannot be empty!')
    else:
        tasks.append(task)
        print('Task added successfully!')

    return_to_main_menu()


def view_tasks():
    display_subtitle('Task List')

    if not tasks:
        print('There are no tasks to display!')
    else:
        print('Tasks:')
        for index, task in enumerate(tasks, start=1):
            print(f'{index}. {task}')

    return_to_main_menu()


def remove_task():
    display_subtitle('Removing a task')

    if not tasks:
        print('Error: There are no tasks to remove.')
    else:
        for index, task in enumerate(tasks, start=1):
            print(f'{index}. {task}')

        try:
            task_number = int(input('Enter the task number to remove: '))
        except ValueError:
            print('Error: Please enter a number!')
            return_to_main_menu()
            return

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" removed successfully!')
        else:
            print('Invalid task number!')

    return_to_main_menu()


def exit_program():
    print('Exiting the Task Manager. Goodbye!')


def main():
    os.system('cls')
    display_menu()
    choose_option()


if __name__ == '__main__':
    main()
