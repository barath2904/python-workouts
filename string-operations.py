# string operations
var1 = "hello"
var2 = "HI"
print(var1.upper())
print(var2.lower())

# string interpolation
print("hi {}".format("all"))
print("hi {0} {1}".format("hello", "all"))
print("hi {x} {y} all".format(x="hello", y="Good morning"))

string1 = 'ruby scala python java'
# Splits at space
print(string1.split())

string2 = 'hi, hello, welcome'
# Splits at ','
print(string2.split(','))
