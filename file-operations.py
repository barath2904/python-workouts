# r for reading
# w for writing
# a for appending
# r+ for both reading and writing

f1 = open("D:\\file1.txt", "r")
v1 = f1.read()
print(v1)
f1.close()

# creating file
f2 = open("D:\\file2.txt", "w")
f2.write(v1)
f2.close()

l1 = "hi"
l2 = "hello"
l3 = "hey"
lines = [l1, l2, l3]
f3 = open("D:\\file2.txt", "a")
f3.write("\n\n")
for line in lines:
    f3.write(line)
    f3.write("\n")
f3.close()