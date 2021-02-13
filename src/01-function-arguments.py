def function1(argument1, argument2):
    print(argument1, argument2)


def function2(argument1, argument2):
    print(argument1, argument2)


def function3(argument1, argument2, argument3="Good Day"):
    print(f"{argument1} {argument2}! {argument3}")


function1("hi", "hello")                      # positional argument
function2(argument2="hello", argument1="hi")  # keyword argument

# calling function3 with default parameter. if no argument is passed, it will take the default value
function3("hi", "hello", "How are you ?")
function3("hi", "hello")


# *args & **kwargs are used when number of arguments is not static during function call
def function4(*args):
    print(args)  # returns tuples
    print(sum(args))


def function5(**kwargs):
    new_list = []
    print(kwargs)  # returns dictionary
    for value in kwargs.values():
        new_list.append(value)
    print(new_list)


function4(1, 2, 3)
function4(1, 2, 3, 4)
function5(India="Delhi", China="Beijing")
function5(India="Delhi", China="Beijing", Australia="Canberra")
