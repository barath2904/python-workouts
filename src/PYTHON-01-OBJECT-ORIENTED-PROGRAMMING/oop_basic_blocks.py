# Object Oriented Programming (OOP) is a programming paradigm associated with concepts of Class & Object
# Class is a blueprint of any entity that defines certain properties & functions (behaviour)
# Class allows you logically group the data (Attributes) & functions (Methods) in a way to reuse

# Creating object from class is called instantiation & functions inside a class is called as methods
# In general, methods is like any other usual function that does some action except that it is associated with an object
# Class is blueprint for objects. Multiple objects can be created with a class
# Classes are essentially user defined data types

# OOP facilitates to have properties & behaviour bundled into an object
# objects that has its own attributes (properties) & methods (behaviour)
# Example: object person with properties like a name, age and behaviors such as walking, talking

# __init__ is a special method that is called when instance of class (object) is created.
# __init__ is similar to constructor that used to initialize state of an object
# self represents instance of a class. It allows us access to the attributes and methods of the class.
# There are 2 types of attributes -> class attribute & instance attribute
# class attributes are defined outside __init__ method while instance attributes are defined within __init__ method.
# There are 3 types of methods -> regular methods, class methods & static methods
# Regular methods automatically takes instance (self) a first argument.
# Class method is bound to class rather than object. Hence instance creation is not required
# static method is similar to normal except that it is logically connected to the class
# class methods & static methods are denoted using decorators: @classmethod & @staticmethod respectively

# Four Principles of OOP : Inheritance, Encapsulation, Abstraction & Polymorphism

class Employee:
    # class attribute/variables
    company = "Microsoft"

    def __init__(self, name, salary):
        # instance attributes/variables
        self.first_name = name
        self.salary = salary

    def calculate_salary(self):
        total_salary = 12 * self.salary
        print(F"{self.first_name} earns Rs.{total_salary} per year at {self.company}")

    @classmethod
    def modify_company(cls, company_name):
        # cls -> class Employee
        cls.company = company_name

    @classmethod
    def parse_employee(cls, employee_data):
        first_name, salary = employee_data.split("-")
        return cls(first_name, int(salary))

    @staticmethod
    def emp_category(category):
        if category == "FTE":
            print("Long Term Employee")
        elif category == "C2C":
            print("Short Term Employee")
        else:
            print(F"{category} is undefined")


# object creation
emp1 = Employee("Ram", 100000)
emp1.calculate_salary()

# self represents instance of a class
emp2 = Employee("Sam", 100000)
Employee.calculate_salary(emp2)

print("\n")
# changing the class variable
Employee.company = "Amazon"
emp1.calculate_salary()
emp2.calculate_salary()
print("\n")
# changing the class variable for a specific instance
emp2.company = "Google"
emp2.calculate_salary()
emp1.calculate_salary()

# changing the class variable value without object creation
Employee.modify_company("Facebook")

# class methods can be used as alternative constructor
emp_data = "Michael-200000"
emp3 = Employee.parse_employee(emp_data)
emp3.calculate_salary()
emp3.emp_category("FTE")
