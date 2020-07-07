user_input = input("Enter an input value:")
print(type(user_input))
# input function always returns a string
print(user_input.isdigit())
# strip function removes leading & trailing spaces if any
if user_input.isdigit():
    numeric_input = int(user_input.strip())
    print(numeric_input)
    print(type(numeric_input))
else:
    print("enter a valid value; Example: 123")
