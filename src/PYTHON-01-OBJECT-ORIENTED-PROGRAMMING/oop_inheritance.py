# Inheritance allows us to define a class that inherits all the methods and attributes (properties) from another class.
# Parent class or base class [being inherited from] --> Class Parents
# Child class or derived class [inherits from another class] --> Class Child(Parents)
# Inheritance benefits with code reuse, extensibility & readability
# Types of Inheritance - Single, Multiple, Multilevel, Hierarchical, Hybrid
# Single Inheritance: Derived class inherits from single base class
# Multiple Inheritance: Derived class inherits from multiple base class
# Multilevel Inheritance: Base - Intermediate - Derived --> Intermediate is base class for Derived.
# Hierarchical Inheritance: More than one derived class created from single base class
# Hybrid: Implemented mix of above mentioned inheritance


class Parents:

    def __init__(self, father, mother):
        self.father = father
        self.mother = mother

    def get_father_name(self):
        print("Father Name:" + self.father)

    def get_mother_name(self):
        print("Mother Name:" + self.mother)

    def get_location(self):
        print("{} and {} are residing in India".format(self.father, self.mother))


class Child(Parents):

    def __init__(self, father, mother, child):
        Parents.__init__(self, father, mother)
        # super().__init__(father, mother)
        self.child = child

    def get_child_name(self):
        print("Child Name:", self.child)

    def get_parents_info(self):
        print("Dad Name: {} \nMom Name: {}".format(self.father, self.mother))

    # Polymorphism with inheritance
    # method overriding
    def get_location(self):
        print("{} is residing in Malaysia".format(self.child))

# calls are being made from oop_import_module.py program
