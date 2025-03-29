from turtle import update

file_name = "employees.txt"
menu_txt = """1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
 Enter from menu options: 
"""


def get_records():
    with open(file_name, "r+") as file:
        records = []
        for record_str in file.read().split("\n"):
            record = record_str.split(", ")
            records.append(record)
        return records


def set_records(records):
    records_str = ""
    for index, record in enumerate(records):
        record_str = "" if index == 0 else "\n"
        for i, data in enumerate(record):
            if i != 0:
                record_str += ", "
            record_str += str(data)
        records_str += record_str
    with open(file_name, "w+") as file:
        file.write(records_str)


def add_new():
    records = get_records()
    emp_id = 1 if len(records) == 0 else int(records[-1][0]) + 1
    name = input("Enter employee name: ").strip()
    position = input("Enter employee position: ").strip()
    salary = input("Enter employee salary: ").strip()
    new_record = [emp_id, name, position, salary]
    records.append(new_record)
    set_records(records)
    print("------------------------------------------------")
    print(f"New employee successfully added".center(50))
    print("------------------------------------------------")


def view_all():
    records = get_records()
    print("  N  |  ID  |          Name          |     Position     |    Salary    ")
    print("---------------------------------------------------------------------")
    for i, record in enumerate(records):
        print("{0} {1} {2} {3} {4}".format(str(i + 1).center(5), record[0].center(6), record[1].ljust(24),
                                           record[2].center(
                                               18), record[3].center(14)))
    if len(records) == 0:
        print("No employee records".center(73))
    print("")


def delete():
    records = get_records()
    emp_id = input("Enter employee id to be deleted: ")
    for record in records:
        if record[0] == emp_id:
            records.remove(record)
            set_records(records)
            print("------------------------------------------------")
            print(f"Employee with id {emp_id} successfully deleted".center(50))
            print("------------------------------------------------")
            return
    print("------------------------------------------------")
    print(f"Employee with id {emp_id} not found".center(50))
    print("------------------------------------------------")


def search_by_id():
    records = get_records()
    emp_id = input("Enter employee id: ")
    for record in records:
        if record[0] == emp_id:
            print("  ID  |          Name          |     Position     |    Salary    ")
            print("---------------------------------------------------------------------")
            print(" " + record[0].center(6) + " " + record[1].ljust(24) + " " + record[2].center(
                18) + " " + record[3].center(14))
            return
    print("------------------------------------------------")
    print(f"Employee with id {emp_id} not found".center(50))
    print("------------------------------------------------")


def update_emp():
    records = get_records()
    emp_id = input("Enter id of the employee to be updated: ")
    for record in records:
        if record[0] == emp_id:
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = input("Enter employee salary: ")
            new_record = [record[0], name.strip(), position.strip(), salary.strip()]
            records[records.index(record)] = new_record
            set_records(records)
            print("------------------------------------------------")
            print(f"Employee record updated".center(50))
            print("------------------------------------------------")
            return
    print("------------------------------------------------")
    print(f"Employee with id {emp_id} not found".center(50))
    print("------------------------------------------------")


def menu_actions(_menu_option):
    match _menu_option:
        case 1:
            add_new()
        case 2:
            view_all()
        case 3:
            search_by_id()
        case 4:
            update_emp()
        case 5:
            delete()
        case 6:
            exit()


while True:
    try:
        menu_option = int(input(menu_txt))
        if menu_option > 6:
            raise ValueError
    except ValueError:
        print("-------------------------------")
        print("   Enter valid menu number")
        print("-------------------------------")
    else:
        menu_actions(menu_option)
