import os
import sys

# various exception combinations
# keywords: try, except, finally

try:
    print("Try Block")
except Exception as general_error:
    # without except block try block will throw error
    print("Exception Block. {}".format(general_error))


try:
    vowels = ['a', 'e', 'i', 'o', 'u']
    print(vowels[5])
except IndexError as index_err:
    print("Cannot print list item. Exception: {}".format(index_err))

try:
    size = os.path.getsize("class-object1.py")
    print("{} Bytes".format(size))
except FileNotFoundError as file_err:
    print("Unable to retrieve size. Exception: {}".format(file_err))

try:
    file_object = open("data.txt", "r")
    print(file_object.read())
except FileNotFoundError as no_file_err:
    print("Unable to open the file. Exception: {}".format(no_file_err))

try:
    file_object = open("../data/input/dummy.txt", "a")
    file_object.write("Hi hello")
except PermissionError as access_err:
    print("Unable to open the file. Exception: {}".format(access_err))

try:
    variable_one = "Hello Good morning"
    print(variable_two)
except NameError as name_err:
    print("Unable to retrieve variable. Exception: {}".format(name_err))
    sys.exit(1)

try:
    print(10/0)
except ZeroDivisionError as operation_err:
    print(operation_err)
finally:
    # finally block gets executed regardless of exception generation
    # optional block for try-except group
    print("division operation over")

try:
    user_input = int(input("enter a number"))
    print("received input: {}".format(user_input))
except ValueError as input_err:
    print("Unable to retrieve user input. {}".format(input_err))

# You can refer for various exceptions in python: https://docs.python.org/3/library/exceptions.html
