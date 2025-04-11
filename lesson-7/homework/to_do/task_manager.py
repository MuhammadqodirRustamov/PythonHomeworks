from task import Task


def data_to_text(_tasks: list[Task]):
    txt = ""
    for task in _tasks:
        txt += f"{task.task_id}, {task.title}, {task.desc}, {task.due_date}, {task.status}\n"
    return txt.strip()


def txt_to_data(data_rows):
    task_list = []
    for row in data_rows:
        _list = row.split(", ")
        task = Task(_list[0], _list[1], _list[2], _list[3], str(_list[4]).strip())
        task_list.append(task)
    return task_list


class TaskManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.__tasks: list = self.__load_tasks()

    def __load_tasks(self):

        with open(self.file_name, "w+") as file:
            data_rows = file.readlines()


        tasks_list = txt_to_data(data_rows)
        return tasks_list

    def get_task_ids(self):
        id_list = [task.task_id for task in self.__tasks]
        return id_list

    def save_tasks(self):
        data_to_txt = data_to_text(self.__tasks)
        with open(self.file_name, "w") as file:
            file.write(data_to_txt)

    def get_tasks(self, _filter):
        task_list = self.__tasks
        if _filter:
            task_list.sort(key=lambda task: task.status)
        return self.__tasks

    def add_new(self, new_task: Task):
        self.__tasks.append(new_task)

    def get_new_id(self):
        if len(self.__tasks) == 0:
            new_id = 1
        else:
            last: Task = self.__tasks[-1]
            new_id = int(last.task_id) + 1
        return new_id

    def update_task(self, updated_task: Task):
        for task in self.__tasks:
            if task.task_id == updated_task.task_id:
                if not len(updated_task.title) == 0: task.title = updated_task.title
                if not len(updated_task.desc) == 0: task.desc = updated_task.desc
                if not len(updated_task.due_date) == 0: task.due_date = updated_task.due_date
                if not len(updated_task.status) == 0: task.status = updated_task.status
                break

    def delete_task(self, task_id):
        t = None
        for task in self.__tasks:
            if task.task_id == task_id:
                t = task
                break
        old_len = len(self.__tasks)
        self.__tasks.remove(self.__tasks.index(t))
        new_len = len(self.__tasks)
        print(old_len == new_len)
