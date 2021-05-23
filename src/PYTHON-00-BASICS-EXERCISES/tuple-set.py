# Tuple is similar to list. But it is immutable.
# Data in a tuple is written using parenthesis and commas.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("count of orange", fruits.count("orange"))
print('Index value of orange', fruits.index("orange"))


# A set is an unordered collection of items. Every element is unique (no duplicates).
# In Python sets are written with curly brackets.
set1 = {1, 2, 3, 3, 4, 5, 6, 7}

# convert list to set
l = [1, 1, 2]
print(set(l))

print(set1)
set1.add(10)

# remove & discard does the same thing. removes the element.
# difference is discard doesn't raise error while remove raise error if element doesn't exist in set
set1.remove(6)
set1.discard(7)
print(set1)
