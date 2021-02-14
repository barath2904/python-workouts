total = 1000
city = input("enter the city name:").lower()

# simple if-else block
if total == 100:
    print("total:100")
else:
    print("total is not 100")

# nested if-elif-else block
if city == "bangalore":
    print(city.upper())
    if total == 100:
        print("total:100")
    elif total < 100:
        print("total less than 100")
    else:
        print("total greater than 100")
else:
    print("city provided is not bangalore")
