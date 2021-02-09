# string operations
var1 = "hello"
var2 = "HI hi"

print(var1.upper())
print(var2.lower())

# string interpolation : process for substituting values of variables into placeholders in a string
print("hi {}".format("all"))
print("hi {0} {1}".format("hello", "all"))
print("hi {x} {y} all".format(x="hello", y="Good morning"))
print("\n")

# f-strings - available in python version >= 3.6
# this way of string interpolation method is known as literal string interpolation
# capitalize will change only first character of the string
print(f"Good morning. {var2.capitalize()} {var1}")

string1 = 'ruby scala python java'
# Splits at space
print(string1.split())

string2 = 'hi, hello, welcome'
# Splits at ','
x = string2.split(',')
# removing extra spaces around items in list
# edge case handling => check if element is string
x = [i.strip() if isinstance(i, str) else i for i in x]

print(len(string2))
print(x)
print(len(x))

swap_ex = "gOOD mORNING"
print(swap_ex.swapcase())

# join split string
join_x = "-".join(x)
print(join_x)

print("*"*25)
y = ["hello ", 2, " morning"]
# list comprehension
z1 = [i.strip() for i in y if isinstance(i, str)]
z2 = [i.strip() if isinstance(i, str) else i for i in y]
print(z1)
print(z2)
print("*"*25)
