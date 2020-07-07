import os
# r for reading
# w for writing
# a for appending

# creating file with content
f0 = open("D:\\file1.txt", "w")
f0.write("Hi Hello Good morning \n")
f0.write("End of File")
f0.close()

# reading an existing file
f1 = open("D:\\file1.txt", "r")
v1 = f1.read()
print(v1)
f1.close()

# creating file with content
f2 = open("D:\\file2.txt", "w")
f2.write(v1)
f2.close()

# appending lines to files
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

# file operations
print(os.getcwd())
print(os.listdir(os.getcwd()))
pathname = os.path.join("basedir", "filename")
print(pathname)

path_name = "D:/"
file_name = "sample-file-creation"
with open(os.path.join(path_name, file_name), 'w') as new_file:
    new_file.write("First Line \n")
    new_file.write("Second Line \n")
    new_file.write("continuous line1 ")
    new_file.write("continuous line2")
    new_file.write("\n")
    new_file.write("End of File")

# file & directory check
print(os.path.isdir("D:/"))
print(os.path.isfile("D:/sample-file-creation"))