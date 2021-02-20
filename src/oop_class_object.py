# OOP facilitates to have properties & behaviour bundled into an object
# create own objects that has its own methods (behaviour) & attributes (properties)
# Example: object person with properties like a name, age and behaviors such as walking, talking
# class is blueprint for objects. Multiple objects can be created with a class
# creating object from class is called instantiation
# function inside a class is called as methods
# __init__ is a special method that is called when instance of class [object] is created
# self allows access to the attributes and methods of each object in python
# class attribute is going to defined outside __init__ method
# instance attribute are defined within __init__ method


class Person:
    # class attribute
    area = "Chennai"

    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age

    def is_teenage(self):
        if 18 <= self.age <= 24:
            print("teenager")
        else:
            print("not teenager")

    def is_senior_citizen(self):
        if self.age > 60:
            print("senior citizen")
        else:
            print("not senior citizen")

    def is_indian(self, nationality):
        if nationality.lower() == "india":
            print("{} is from India".format(self.name))
        else:
            print("{} is foreigner".format(self.name))
        return nationality

    def is_tamil(self, language, nationality):
        # calling is_indian method inside current method
        person_nationality = self.is_indian(nationality)
        if language.lower() == "tamil":
            if 18 <= self.age <= 24:
                print("tamil teenager living in {0}; Nationality: {1}".format(self.area, person_nationality.upper()))
            else:
                print("other age category living in {x}; Nationality: {y}".format(x=self.area, y=person_nationality.upper()))
        else:
            print("other language person living in {}; Nationality: {}".format(self.area, person_nationality.upper()))


# object creation
person1 = Person("xxx", 18)
person2 = Person("yyy", 75)
person3 = Person("zzz", 22)
person4 = Person("abc", 25)

# printing type of object & instance attributes
print("printing info on person1 object")
print(type(person1))
print(person1.name)
print(person1.age)
print("\n")

# calling methods
print("methods calling")
person1.is_teenage()
person1.is_senior_citizen()
person2.is_teenage()
person2.is_senior_citizen()

print("\n")
person1.is_tamil("tamil", "india")
person2.is_tamil("bengali", "india")
person3.is_tamil("tamil", "singapore")
print("\n")
nationality_info = person4.is_indian("USA")
print(nationality_info + ";" + " person4 attributes: " + person4.name + " " + str(person4.age))
