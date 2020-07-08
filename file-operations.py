import os
import sys

print("version of python: ", sys.version)

# r for reading
# w for writing
# a for appending

# creating file with content
f0 = open("D:\\file1.txt", "w")
print("opening a new file file1.txt & writing contents to it")
f0.write("Hi Hello Good morning \n")
f0.write("End of File")
f0.close()

# reading an existing file
f1 = open("D:\\file1.txt", "r")
print("Reading file1.txt")
v1 = f1.read()
print(v1)
f1.close()

# creating file with content
f2 = open("D:\\file2.txt", "w")
print("writing the contents of file1.txt to file2.txt")
f2.write(v1)
f2.close()

# appending lines to files
l1 = "hi"
l2 = "hello"
l3 = "hey"
lines = [l1, l2, l3]
f3 = open("D:\\file2.txt", "a")
print("Appending content to file2.txt")
f3.write("\n\n")
for line in lines:
    f3.write(line)
    f3.write("\n")
f3.close()

# file operations
# getting current working directory
dir_loc = os.getcwd()
print(dir_loc)
print(os.listdir(dir_loc))
pathname = os.path.join(dir_loc, "sample.txt")
print(pathname)

path_name = "D:/"
file_name = "sample-file-creation.txt"
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
