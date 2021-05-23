# Encapsulation is a way of restricting access to methods inside a class
# As python is an interpreted language ; hence encapsulation is weak
# Encapsulation can be performed by convention, but not enforced by language
# Restriction levels: private, protected, public


class Base:
    def __init__(self):
        self.amount = 100
        self._amount = 200
        self.__amount = 300

    def print_amount(self):
        print(self.amount)
        print(self._amount)
        print(self.__amount)

    def set_amount(self, amount1, amount2, amount3):
        self.amount, self._amount, self.__amount = amount1, amount2, amount3

    def __private(self):
        print("private value in Base")

    def _protected(self):
        print("protected value in Base")

    def public(self):
        print("public value in Base")
        self.__private()


class Derived(Base):

    def __private(self):
        print("derived private")

    def _protected(self):
        self.__private()
        print("derived protected")


b = Base()
b.print_amount()
print("")
b.amount = 150
# protected & private attributes can't be changed
b.__amount = 250
b.__amount = 350
b.print_amount()
# protected & private attributes can be changed via setter method
print("")
b.set_amount(150, 250, 350)
b.print_amount()

print("")
d = Derived()
# d.public()
print("")
# not recommended to call protected method & hence it shows warning
# private methods - we won't be able to call as python doesn't recognize
# d._protected()  # ---> will work, but not
# d.__private()   # ---> will throw error

# print(dir(d))  # --> prints attributes & methods of object
# d.__private() can be called as d._Base_private() --> Name Mangling
# Name mangling: Double underscore prefix causes python interpreter to rewrite attribute & method names
d._Base__private()  # ---> still accessible ; Remember Encapsulation is not enforced
