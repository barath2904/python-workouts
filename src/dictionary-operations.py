# Python Dictionary is an unordered sequence of data of key-value pair form.
# It is similar to Map or hash table type.
# Dictionaries are written within curly braces in the form key:value
# Mutable data type

countries = {"India": "Delhi", "China": "Beijing", "USA": "Washington", "Australia": "Canberra"}
print(countries)

# adding entry
countries["UK"] = "London"
print(countries)

# adding/updating entry
countries.update({"India": "New Delhi", "France": "Paris"})
print(countries)

# Retrieving values from Dictionary
# print(countries["unknown_country"]) will return KeyError
print(countries.get("unknown_country"))  # will return None if Key not found
print(countries.get("unknown_country", "NA"))  # will return default value if key not found

# iteration with dictionary
country_list = []
country_capital_list = []
country_capital_dic = {}
for country_name in countries.keys():
    country_list.append(country_name)
for country_capital in countries.values():
    country_capital_list.append(country_capital)
for country, capital in countries.items():
    country_capital_dic[country] = capital

print(country_list)
print(country_capital_list)
print(country_capital_dic)
