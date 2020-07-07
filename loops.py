# for loop example
# list iteration
fruits = ["apple", "grapes", "mango"]

for fruit in fruits:
    if fruit == "apple":
        print("a starting fruit")
    else:
        print("other fruits")

for index in range(len(fruits)):
    print(range(len(fruits)))
    print(index)
    print(fruits[index])

for index_num, index_val in enumerate(fruits):
    print("index is {} and value is {}".format(index_num, index_val))


# In python, while loop is used to execute a block of statements repeatedly until a given a condition is satisfied.
# And when the condition becomes false, the line immediately after the loop in program is executed.
num = 0
while num < 3:
    num += 1
    print("Hi" + " " + str(num))
