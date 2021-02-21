# Encapsulation is a way of restricting access to methods inside a class
# As python is an interpreted language ; hence encapsulation is weak
# Encapsulation can be performed by convention, but not enforced by language
# Restriction levels: private, protected, public


class Base:

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
        print("derived protected")


d = Derived()
d.public()
print("\n\n")
# not recommended to call protected method & hence it shows warning
# private methods - we won't be able to call as python doesn't recognize
# d._protected() ---> will work, but not recommended
# d.__private()  ---> will throw error
