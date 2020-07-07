import os
import datetime

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

# current date & datetime
datetime_object = datetime.datetime.now()
print(datetime_object)

date_object = datetime.date.today()
print(date_object)

# date object of today's date
today = datetime.date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)