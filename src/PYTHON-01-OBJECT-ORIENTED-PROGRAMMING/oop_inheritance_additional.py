class Employee:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def parse_employee(cls, employee_data):
        pass


class Technology(Employee):
    def __init__(self, first_name, last_name, age, skill):
        super().__init__(first_name, last_name, age)
        self.skill = skill
        self.department = Technology.__name__

    def print_info(self):
        print(F"{self.first_name} {self.last_name} belongs to {self.department} division & proficient in {self.skill}")


class HR(Employee):
    def __init__(self, first_name, last_name, age, speciality):
        super().__init__(first_name, last_name, age)
        self.speciality = speciality
        self.department = HR.__name__


class Supervisor(Employee):
    def __init__(self, first_name, last_name, age, employees=None):
        super().__init__(first_name, last_name, age)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
        else:
            print("Employee already tagged")

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print("Employee not available")

    def list_employees(self):
        for employee in self.employees:
            if "skill" in dir(employee):
                speciality = employee.skill
            else:
                speciality = employee.speciality
            print(F"Manager: {self.first_name} {self.last_name}; "
                  F"Employee: {employee.first_name} {employee.last_name}; "
                  F"Speciality: {speciality}; "
                  F"Department: {employee.department}")


emp1 = Technology("Michael", "Clarke", 28, "Python")
emp2 = Technology("Sara", "Johnson", 26, "ReactJS")
emp3 = HR("Alan", "Simon", 30, "Recruitment")
emp1.print_info()

manager1 = Supervisor("James", "Davis", 35, [emp1])
manager1.list_employees()
manager2 = Supervisor("Tim", "Connors", 32)
manager2.add_employee(emp2)
manager2.add_employee(emp3)
manager2.list_employees()
