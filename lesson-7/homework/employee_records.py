import re

menu_txt = """1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit

 Enter your choice: """


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary


class EmployeeManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_new(self):
        employees = self.get_employees()
        while True:
            name = (input("Enter name: ")).strip()
            if len(name) > 0:
                break
            print("Name can not be empty")
        while True:
            position = (input("Enter position: ")).strip()
            if len(position) > 0:
                break
            print("Position can not be empty")
        while True:
            salary = (input("Enter salary: ")).strip()
            if len(salary) == 0:
                print("Salary can not be empty")
            else:
                try:
                    salary = int(salary)
                    if salary < 1:
                        print("Salary must be greater than 0")
                    else:
                        break
                except ValueError:
                    print("Salary must be in numbers only")
        emp_id = 1 if len(employees) == 0 else str(int(employees[-1].employee_id) + 1)
        new_employee = Employee(emp_id, name, position, salary)
        employees.append(new_employee)
        self.set_employees(employees)
        print("New employee added", "\n")

    def set_employees(self, new_list):
        new_content = ""
        for index, employee in enumerate(new_list):
            line = "" if index == 0 else "\n"
            line += f"{employee.employee_id} ~ "
            line += f"{employee.name} ~ "
            line += f"{employee.position} ~ "
            line += f"{employee.salary}"
            new_content += line
        with open(self.file_name, "w") as file:
            file.write(new_content)

    def get_employees(self):
        try:
            with open(self.file_name) as file:
                employees = []
                while True:
                    line = file.readline()
                    if not line:
                        break
                    attrs_list = line.split(" ~ ")
                    employee = Employee(attrs_list[0], attrs_list[1], attrs_list[2], attrs_list[3].strip(), )
                    employees.append(employee)
                return employees

        except FileNotFoundError:
            with open(self.file_name, "w") as file:
                pass
            return []

    def view_all(self):
        employees = self.get_employees()
        print()
        for employee in employees:
            print(str(employee.employee_id).center(5), end="")
            print(str(employee.name).center(25), end="")
            print(str(employee.position).center(20), end="")
            print(str(employee.salary).center(10))
        print()

    def menu_actions(self, _menu_option):
        match _menu_option:
            case 1:
                self.add_new()
            case 2:
                self.view_all()
            case 3:
                self.search_by_id()
            case 4:
                self.update_emp()
            case 5:
                self.delete()
            case 6:
                exit()

    def search_by_id(self):
        while True:
            try:
                emp_id = int(input("Enter employee ID to search for: "))
            except ValueError:
                print("Invalid ID")
            else:
                employees = self.get_employees()
                for employee in employees:
                    if employee.employee_id == str(emp_id):
                        print()
                        print(str(employee.employee_id).center(5), end="")
                        print(str(employee.name).center(25), end="")
                        print(str(employee.position).center(20), end="")
                        print(str(employee.salary).center(10), end="\n\n")
                        break
                break

    def update_emp(self):
        while True:
            try:
                emp_id = int(input("Enter employee ID to update: "))
                break
            except ValueError:
                print("Invalid ID")
        employees = self.get_employees()
        for employee in employees:
            if employee.employee_id == str(emp_id):
                name = ""
                while len(name) == 0:
                    name = input("Enter new name: ").strip()
                position = ""
                while len(position) == 0:
                    position = input("Enter new position: ").strip()
                salary = 0
                while salary < 1:
                    try:
                        salary = int(input("Enter new salary: "))
                        if salary == 0:
                            raise ValueError
                    except ValueError:
                        print('Invalid salary')
                employee.name = name
                employee.position = position
                employee.salary = str(salary)
                self.set_employees(employees)
                print("Updated employee", end="\n\n")
                break

    def delete(self):
        emp_id = 0
        while emp_id < 1:
            try:
                emp_id = int(input("Enter employee ID to be deleted: "))
            except ValueError:
                print("Invalid ID")

        employees = self.get_employees()
        for employee in employees:
            if employee.employee_id == str(emp_id):
                employees.remove(employee)
                break

        self.set_employees(employees)
        print(f"Employee with ID {emp_id} successfully deleted", end="\n\n")


employee_manager = EmployeeManager("employees.txt")
while True:
    try:
        menu_option = int(input(menu_txt))
        if menu_option > 6:
            raise ValueError
    except ValueError:
        print("Invalid menu choice\n")
    else:
        employee_manager.menu_actions(menu_option)
