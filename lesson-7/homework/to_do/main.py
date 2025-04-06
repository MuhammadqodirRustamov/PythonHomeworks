from task_manager import TaskManager
from menu import menu_actions
from menu import menu_text

file_name = "tasks.csv"
task_manager = TaskManager(file_name)

print("Welcome to the To-Do Application!")
while True:
    choice = input(menu_text)

    # Check for valid input
    try:
        choice = int(choice)
        if choice not in range(1, 8):
            raise ValueError
    except ValueError:
        print("Invalid menu choice")

    else:
        # Exit the menu
        if choice == 7:
            break

        # Executing corresponding menu action
        menu_actions(task_manager, choice)

    # Printing extra line after each action
    print()
