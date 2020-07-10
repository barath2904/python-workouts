# Polymorphism is creating an similar named entity to represent different behaviours at different scenarios
# method names are same but purposes are different for different scenarios
# polymorphism can be applicable at built-in function levels as well. "len" is a classic example
# "len" can be applied on string, list, dictionary, etc. function name is same but usage is different as per data type


class Asia:

    def __init__(self):
        self.country = "India"

    def capital(self):
        print("New Delhi is the capital of {}".format(self.country))

    def language(self):
        print("Hindi is widely spoken language in {}".format(self.country))

    def type(self):
        print("{} is a developing country".format(self.country))

    @staticmethod
    def static_method_example():
        print("method not using any attributes")


class NorthAmerica:

    def __init__(self):
        self.country = "USA"

    def capital(self):
        print("Washington, D.C. is the capital of {}".format(self.country))

    def language(self):
        print("English is the widely spoken language in {}".format(self.country))

    def type(self):
        print("{} is a developed country".format(self.country))

    @staticmethod
    def static_method_example():
        print("method not using any attributes")


countries = [Asia(), NorthAmerica()]
for country in countries:
    print("\n")
    country.capital()
    country.language()
    country.type()
    country.static_method_example()
