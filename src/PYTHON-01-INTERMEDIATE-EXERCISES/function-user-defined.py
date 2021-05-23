# Example of multi-line comment
"""
Two types of functions
1. Built-In Functions
2. User Defined Functions
"""

# functions with/without argument
# functions with/without return value

constant_value = 100


def function1():
    print("function without arguments")


def function2(argument1):
    function_variable = 10
    print(F"constant value: {constant_value}")
    print(F"scope of this is with in this function only. Value: {function_variable}")
    print("parameterized function or function with arguments")
    print("argument/parameter: {}".format(argument1))
    print(F"sum : {constant_value + function_variable + argument1}")


def add_numbers(num1, num2):
    print("function with argument & return value")
    sum_val = num1 + num2
    return sum_val


# calling statements for the defined functions
function1()
function2(1000)
function2(2000)
function2(3000)
c1 = add_numbers(1, 2)
c2 = add_numbers(10, 20)

if c1 > 10:
    print("sum greater than 10")
else:
    print("sum is less than 10")
