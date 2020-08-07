# for loop example
# list iteration
fruits = ["apple", "grapes", "mango"]

for fruit in fruits:
    if fruit == "apple":
        print("a starting fruit")
    else:
        print("other fruits")

new_fruits = []
for index in range(0,3):
    print(range(len(fruits)))
    # printing the index
    print(index)
    # printing value corresponding to the index
    print(fruits[index])
    new_fruits.append(fruits[index])

# break - operation to break the loop

print(new_fruits)

for index_num, index_val in enumerate(fruits):
    print("index is {} and value is {}".format(index_num, index_val))


# In python, while loop is used to execute a block of statements repeatedly until a given a condition is satisfied.
# And when the condition becomes false, the line immediately after the loop in program is executed.
# num = 0
# while num < 25:
#     num += 1  # num = num + 1
#     print("Hi" + " " + str(num))
