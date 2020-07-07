user_input = input("Enter an input value:")
print(type(user_input))
# input function always returns a string
print(user_input.isdigit())
# strip function removes leading & trailing spaces if any
numeric_input = int(user_input.strip())
print(numeric_input)