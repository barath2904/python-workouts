from functools import reduce


def multiply(multiply_argument):
    return multiply_argument*10


def filtering(filter_argument):
    if (filter_argument % 2) != 0:
        return True
    else:
        return False


# Higher order functions are functions that take another function as argument

# map() syntax= map(function, iterator object)
# map() returns map object
number_list = [1, 2, 3, 4, 5]
multiply_object = map(lambda x: x * 10, number_list)
print("map object: {}".format(multiply_object))
lambda_multiply = list(multiply_object)
normal_multiply = list(map(multiply, number_list))
print("multiply result using lambda function: {}".format(lambda_multiply))
print("multiply result using normal function: {}".format(normal_multiply))
fruits = ["apple", "mango"]
up_fruits = list(map(str.upper, fruits))
print("fruits in lower case: {}".format(fruits))
print("fruits in upper case: {}".format(up_fruits))

# filter() filters given sequence with help of passed function that evaluates the condition to be true or not
# filter() syntax= filter(function returning Boolean, iterator object)
# filter() returns filter object
print("\n")
filter_list = [5, 10, 15, 20, 25, 30, 35]
odd_object = filter(lambda x: (x % 2 != 0), filter_list)
print("filter object: {}".format(odd_object))
odd_filtered = list(odd_object)
print("filtered list using lambda function: {}".format(odd_filtered))
normal_filtering = list(filter(filtering, filter_list))
print("filtered list using normal function: {}".format(normal_filtering))

# reduce function used a mathematical technique called folding
# folding reduces list of items to single/cumulative item
# reduce() syntax= filter(function, iterator object, <optional initializer>)
reduce_numbers = [10, 20, 30, 40]
added_value = reduce((lambda x, y: x+y), reduce_numbers)
# reduce logic
# 0  + 10 = 10
# 10 + 20 = 30
# 30 + 30 = 60
# 60 + 40 = 100
added_value_with_initializer = reduce((lambda x, y: x+y), reduce_numbers, 10)
# reduce logic
# 10 + 10 = 20
# 20 + 20 = 40
# 40 + 30 = 70
# 70 + 40 = 110
print("\n")
print("reduce result type 1: {}".format(added_value))
print("reduce result type 2: {}".format(added_value_with_initializer))

# finding min & max using reduce function
maximum_number = reduce((lambda a, b: a if a > b else b), reduce_numbers)
minimum_number = reduce((lambda a, b: a if a < b else b), reduce_numbers)
print("minimum: {}, maximum: {}".format(minimum_number,maximum_number))
