# string operations
var1 = "hello"
var2 = "HI"
print(var1.upper())
print(var2.lower())

# string interpolation : process for substituting values of variables into placeholders in a string
print("hi {}".format("all"))
print("hi {0} {1}".format("hello", "all"))
print("hi {x} {y} all".format(x="hello", y="Good morning"))
print("\n")

# f-strings - available in python version >= 3.6
# this way of string interpolation method is known as literal string interpolation
print(f"Good morning. {var2.capitalize()} {var1}")

string1 = 'ruby scala python java'
# Splits at space
print(string1.split())

string2 = 'hi, hello, welcome'
# Splits at ','
x = string2.split(',')

print(len(string2))
print(x)
print(len(x))
