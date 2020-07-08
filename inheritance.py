# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class or base class [being inherited from] --> Class Parents
# Child class or derived class [inherits from another class] --> Class Child(Parents)


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
        super().__init__(father, mother)
        self.child = child

    def get_child_name(self):
        print("Child Name:", self.child)

    def get_parents_info(self):
        print("Dad Name: {} \n Mom Name: {}".format(self.father, self.mother))

    # Polymorphism with inheritance
    # method overriding
    def get_location(self):
        print("{} is residing in Malaysia".format(self.child))


boy = Child("Shiva", "Parvathy", "Vinayak")
boy.get_father_name()
boy.get_mother_name()
boy.get_parents_info()
boy.get_location()

parent = Parents("shiva", "Parvathi")
parent.get_location()
