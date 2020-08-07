# for loop example

# list iteration
fruits = ["apple", "grapes", "mango"]
for fruit in fruits:
    if fruit == "apple":
        print(True)
    else:
        print(False)

# Ternary operator (conditional expression) inside iteration
for fruit in fruits:
    bool_value = True if fruit == "mango" else False
    print(bool_value)

new_fruits = []
for index in range(0, 3):
    print(index, fruits[index])  # printing the index & its corresponding value
    new_fruits.append(fruits[index])

print("\n")
print(new_fruits)
for index_num, index_val in enumerate(new_fruits):
    print("index is {} and value is {}".format(index_num, index_val))

# iteration with dictionary
countries = {"India": "Delhi", "China": "Beijing", "USA": "Washington", "Australia": "Canberra"}
print("\n")
country_list = []
country_capital_list = []
country_capital_dic = {}
for country_name in countries.keys():
    country_list.append(country_name)
for country_capital in countries.values():
    country_capital_list.append(country_capital)
for country, capital in countries.items():
    country_capital_dic[country] = capital

print(country_list)
print(country_capital_list)
print(country_capital_dic)
print("\n")

# break - operation to break any loop
# In python, while loop is used to execute a block of statements repeatedly until a given a condition is satisfied.
# And when the condition becomes false, the line immediately after the loop in program is executed.
num = 0
while num < 5:
    num += 1  # num = num + 1
    print("Hi" + " " + str(num))
