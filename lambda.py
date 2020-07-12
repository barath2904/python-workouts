def area(r):
    pi = 3.14
    return pi * r * r


# lambda = anonymous function.
# anonymous functions are functions without name ; they are not defined using "def" keyword
# lambda can take any number of arguments, but can have only one expression
# syntax = lambda <arguments>: <expression>
a = (lambda x: 3.14 * x * x)
print("area value using lambda function: {}".format(a(10)))
print("area value using normal function: {}".format(area(10)))
