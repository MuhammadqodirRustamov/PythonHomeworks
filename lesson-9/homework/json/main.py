import json

json_text = """[
    {"id": 1, "task": "Do laundry", "completed": false, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": true, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": false, "priority": 1}
]"""

json_file_name = "tasks.json"
csv_file_name = "tasks.csv"

with open(json_file_name, "w+") as file:
    file.write(json_text)

with open(json_file_name, "r") as file:
    tasks_list = json.load(file)


# class Task:
#     def __init__(self, task_id, task, completed, priority):
#         self.task_id = task_id
#         self.task = task
#         self.completed = completed
#         self.priority = priority
#
#
# for task in task_list:
#     task_id = task["id"]
#     task = task["task"]
#     completed = task["completed"]
#     priority = task["priority"]
#     task_

def total_number(_tasks_list: list):
    return len(_tasks_list)


def completed(tasks_list: list):
    count = 0
    for task in tasks_list:
        if task["completed"]:
            count += 1
    return count


def average_priority(_tasks_list: list):
    pr_list = []
    for task in _tasks_list:
        pr_list.append(int(task["priority"]))
    return sum(pr_list) / len(pr_list)


total = total_number(tasks_list)
completed_tasks = completed(tasks_list)
pending_tasks = total - completed_tasks
average_prior = average_priority(tasks_list)

print(f"Total number: {total}")
print(f"Completed tasks: {completed_tasks}")
print(f"Pending tasks: {pending_tasks}")
print(f"Average priority: {average_prior}")

print()
def to_csv(_tasks_list: list):
    csv_text = "ID,Task,Completed,Priority\n"
    for task in _tasks_list:
        new_line = ""
        new_line += f"{task["id"]},"
        new_line += f"{task["task"]},"
        new_line += f"{task["completed"]},"
        new_line += f"{task["priority"]}\n"
        csv_text += new_line
    csv_text.strip()
    print(csv_text)
    with open(csv_file_name, "w+") as file:
        file.write(csv_text)


to_csv(tasks_list)
