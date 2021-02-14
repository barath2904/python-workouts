# Python Dictionary is an unordered sequence of data of key-value pair form.
# It is similar to Map or hash table type.
# Dictionaries are written within curly braces in the form key:value
# Mutable data type

countries = {"India": "Delhi", "China": "Beijing", "USA": "Washington", "Australia": "Canberra"}
print(countries)

# adding entry
countries["UK"] = "London"
print(countries)

# key values are case-sensitive
# retrieving values
print(countries["India"])
print(countries["Australia"])

# adding/updating entry
countries.update({"India": "New Delhi", "France": "Paris"})
print(countries)

# Retrieving values from Dictionary
# print(countries["unknown_country"]) will return KeyError
print(countries.get("unknown_country"))  # will return None if Key not found
print(countries.get("unknown_country", "NA"))  # will return default value if key not found

# print keys & values separately
print(countries.keys())
print(countries.values())
print(countries.items())
