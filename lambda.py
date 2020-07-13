import sys


def area(radius):
    pi = 3.14
    return pi * radius * radius


# lambda = anonymous function.
# anonymous functions are functions without name ; they are not defined using "def" keyword
# lambda can take any number of arguments, but can have only one expression
# syntax = lambda <arguments>: <expression>
try:
    a = (lambda x: 3.14 * x * x)
    print("area value using lambda function: {}".format(a(10)))
except Exception as lambda_error:
    print(lambda_error)
    sys.exit(1)

# lambda implementation without try-except block
b = (lambda x, y: 3.14 * x * y)
print("area value using lambda function: {}".format(b(10,10)))

print("area value using normal function: {}".format(area(10)))
