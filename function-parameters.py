# Example of multi-line comment
"""
Two types of functions
1. Built-In Functions
2. User Defined Functions
"""

# functions with/without parameters
# functions with/without return value


def function1():
    print("function without arguments")


def function2(argument1):
    print("parameterized function")
    print("passed parameter: {}".format(argument1))


def add_numbers(num1, num2):
    sum_num = num1+num2
    print(sum_num)
    return sum_num


# calling statements for the defined functions
function1()
function2(10)
c1 = add_numbers(1,2)
c2 = add_numbers(10,20)
function2(20)
function2(30)

if c1 > 10:
    print("sum greater than 10")
else:
    print("sum is less than 10")
