import os

print(os.getcwd())
print(os.listdir(os.getcwd()))
pathname = os.path.join("data", "filename")
print(pathname)


import datetime
datetime_object = datetime.datetime.now()
print(datetime_object)

date_object = datetime.date.today()
print(date_object)

from datetime import date
# date object of today's date
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)