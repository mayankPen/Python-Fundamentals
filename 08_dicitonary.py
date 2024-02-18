# dictionary contain key value pairs. Each key is separated from it's value
# by : , items are separated by comma and whole thing is enclosed within 
# curly braces.

personal_data = {
    "name"    : "mayank dubey",
    "age"     : 29,
    "skill"   : "linux and devops",
    "members" : ["Dinesh", "Bimlesh", "Mayank", "Anuj"]
}

# Adding or updating key-value pairs:

personal_data["college"] = "Truba"
print(personal_data)

# accessing value by key
age_mayank = personal_data["age"]
print(age_mayank)

# Checking if a key is in the dictionary:
if "skill" in personal_data:
    print('yes skill is there....')






# Getting a value by key with a default value if the key is not present:
get_age= personal_data.get("age",30)
get_school=personal_data.get("school","navankur")
print(get_age)
print(get_school)




# Removing a key-value pair by key
del personal_data["name"]
print(personal_data)

# Using the pop() method to remove key value pair and return a value by key:
age_returned_and_removed = personal_data.pop("age")
print(age_returned_and_removed)
print(personal_data)

# Getting all keys:
my_keys=personal_data.keys()
print(my_keys)
print(type(my_keys))

# Getting all values:
my_values = personal_data.values()
print(my_values)
print(type(my_values))


# Getting all key-value pairs as tuples:
my_items =  personal_data.items()
print(my_items)



# Copying a dictionary:
my_data = personal_data.copy()
print(my_data)


# Clearing all key-value pairs in a dictionary:
personal_data.clear()
print(personal_data)


# Updating a dictionary with key-value pairs from another dictionary:
marks = {
    "maths" : 45,
    "chemistry" : 33,
    "physics" : 35,
    "hindi" : 40
}

personal_data.update(marks)
print(personal_data)


# Iterating through keys or key-value pairs:
for key in personal_data:
    print(f"{key} =>{personal_data[key]}")

for key,value in personal_data.items():
    print(f"{key} will give {value}.")


for value in personal_data.values():
    print(value)


my_dict = {'a': 1, 'b': 2, 'c': 3}

for value in my_dict.values():
    print(value)