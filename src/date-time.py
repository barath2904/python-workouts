import datetime

# current date & datetime
datetime_object = datetime.datetime.now()
print(datetime_object)
print(datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f"))
# specific formats
print(datetime_object.strftime("%Y/%m/%d"))
print(datetime_object.strftime("%Y|%m|%d"))


print(datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f"))

date_object = datetime.date.today()
print(date_object)

# date object of today's date
today = datetime.date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
