# Tuple is similar to list. But it is immutable.
# Data in a tuple is written using parenthesis and commas.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("count of orange", fruits.count("orange"))
print('Index value of orange', fruits.index("orange"))


# Python Dictionary is an unordered sequence of data of key-value pair form.
# It is similar to Map or hash table type.
# Dictionaries are written within curly braces in the form key:value
countries = {"India": "New Delhi", "China": "Beijing", "USA": "Washington", "Australia": "Canberra"}
print(countries["India"])

# A set is an unordered collection of items. Every element is unique (no duplicates).
# In Python sets are written with curly brackets.
a = {1, 2, 3, 3, 1, 4, 5}
print(a)
