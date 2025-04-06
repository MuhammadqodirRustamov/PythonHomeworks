menu_text = """1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Exit
Enter your choice: """

from task import Task
from task_manager import TaskManager


def enter_non_empty_data(name, is_integer=False):
    data = ""
    while len(str(data)) == 0:
        data = input(f"Enter {name}: ")
        if len(data) == 0:
            print(f"{name.capitalize()} can not be blank")
        elif is_integer:
            try:
                data = int(data)
            except ValueError:
                print(f"{str(name).capitalize()} can only be integer")
                data = ""
    return data


def add_new_task(_task_manager: TaskManager):
    task_id = _task_manager.get_new_id()
    title = enter_non_empty_data("title")
    desc = enter_non_empty_data("task description")
    due_date = input("Enter due date YYYY-MM-DD (optional): ")
    status = enter_non_empty_data("status")
    new_task = Task(task_id, title, desc, due_date, status)
    _task_manager.add_new(new_task)
    print("New task added")


def view_all(_task_manager: TaskManager, _filter=False):
    tasks = _task_manager.get_tasks(_filter)
    if len(tasks) == 0:
        print(" No tasks added yet")
    for task in tasks:
        print(f"{task.task_id}".center(5), end=" ")
        print(f"{task.title}", end="  ")
        print(f"{task.due_date}", end="  ")
        print(f"{task.status}")
        print(f"     {task.desc}")


def enter_task_id(_task_manager):
    id_list = _task_manager.get_task_ids()
    task_id = -1
    first_time = True
    while task_id not in id_list:
        if not first_time:
            print(f"Task with id {task_id} not found")
        task_id = enter_non_empty_data("task ID", True)
        first_time = False
    return task_id


def update_task(_task_manager: TaskManager):
    task_id = enter_task_id(_task_manager)
    title = input("Enter task title(optional): ")
    desc = input("Enter task description(optional): ")
    due_date = input("Enter task title(optional): ")
    status = input("Enter task title(optional): ")
    updated_task = Task(task_id, title, desc, due_date, status)
    _task_manager.update_task(updated_task)
    print("Task updated")


def delete(_task_manager: TaskManager):
    task_id = enter_task_id(_task_manager)
    _task_manager.delete_task(task_id)
    print("Task deleted")


def filter_by_status(_task_manager):
    view_all(_task_manager, True)


def save_tasks(_task_manager:TaskManager):
    _task_manager.save_tasks()
    print("Tasks saved")


def menu_actions(_task_manager, _choice):
    match _choice:
        case 1:
            add_new_task(_task_manager)
        case 2:
            view_all(_task_manager)
        case 3:
            update_task(_task_manager)
        case 4:
            delete(_task_manager)
        case 5:
            filter_by_status(_task_manager)
        case 6:
            save_tasks(_task_manager)
