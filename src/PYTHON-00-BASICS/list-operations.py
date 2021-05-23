# List - Heterogeneous collection of items
# List is mutable - You can add/remove/modify elements ; Allows duplicate entries inside the list
# List index starts at 0

# List examples
empty_list = []
number_list = [0, 1, 2, 3]
word_list = ["apple", "banana", "mango", "grapes", "mango"]
mixed_list = [1, "name", "department", 10000]

# list operations

print(type(empty_list))  # returns list
print(number_list)  # prints list contents

number_list.append(4)  # appends one more item to the list (by default adds to last)
# output of number_list: [0, 1, 2, 3, 4]
word_list.insert(0, "orange")  # inserts orange as first element to the list (base on index value specified)

number_list.remove(1)  # removes the element having value as 1
# output of number_list: [0, 2, 3, 4]
number_list.pop(0)  # removes the element at index 0
# output of number_list: [2, 3, 4]

print(number_list)
print(word_list)

print(len(mixed_list))  # gives length of list
print(word_list.count("mango"))  # gives occurrences of word "mango"

number_list.reverse()  # Reverse the number list
print(number_list)

word_list.sort()  # sorts the list
print(word_list)

word_list.clear()  # empties the list
print(word_list)
print("\n")

# List unpacking
fruit1, fruit2, fruit3 = ["apple", "banana", "mango"]
print(fruit1)
print(fruit2)
print(fruit3)
