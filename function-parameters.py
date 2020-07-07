# Example of multi-line comment
"""
Two types of functions
1. Built-In Functions
2. User Defined Functions"""

# functions with/without parameters
# functions with/without return value


def function1():
    print("function without arguments")


def function2(argument1):
    print("parameterized function")
    print("passed parameter: {}".format(argument1))


def add_numbers(num1, num2):
    sum_num = num1+num2
    return sum_num


function1()
function2(10)
return_value = add_numbers(1,2)
print(return_value)
