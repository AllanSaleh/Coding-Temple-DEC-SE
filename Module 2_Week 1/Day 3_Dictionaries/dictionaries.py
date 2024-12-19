# Python Dictionaries
# A dictionary in Python is a collection of key-value pairs.
# Each key is associated with a value, and both the keys and values 
# can be of any data type. (By convention, keys are usually strings)


# alist = [1,2,58,6,8]

name = "Allan"
age = 99
has_car = False
occupation = "Instructor"

person2_name = "Matthew"
person2_age = 25
person2_has_car = True


# person = ["allan", 99, False]
# print(person[2])
print(f"Person {name} is {person2_age} years old. He is a {occupation}")

person = {
    "name": "Allan",
    "age" : 99,
    "has_car": False,
    "occupation": "Instructor"
}

person2 = {
    "name": "Ferdinand",
    "age" : 26,
    "has_car": True,
    "occupation": "Software Engineer"
}

print(f"Person {person['name']} is {person["age"]} years old. He is a {person["occupation"]}")
print(f"Person {person2['name']} is {person2["age"]} years old. He is a {person2["occupation"]}")



team = {
    #key      #value
    "Alice": "Leader",
    "Ben": "Engineer",
    "Diana": "Support"
}

# Accessing a value by key
print(f"Alice's role: {team["Alice"]}")
# print(f"Grace's role: {team["Grace"]}")

# Using .get() to safely access keys
print(f"Ben's role: {team.get("Ben")}")
print(f"Grace's role: {team.get("Grace")}")
print(f"Grace's role: {team.get("Grace", "Not in the team")}")

# Adding a new member
team["Hannah"] = "Coordinator"
print(team)

# Removing a member using .pop()
removed = team.pop("Ben")
print("Removed Ben: ",removed)
print(team)

# Removing a member using del
del team["Diana"]
print(team)

# Modifying an element in a dictionary
team["Alice"] = "Manager"
print(team)


# .keys(), .values(), and .items()
print("Members (keys): ", team.keys())
print("Roles (values): ", team.values())
print("Members and roles (items): ",team.items())

# Looping through the dictionary
for key in team.keys():
    print(key)

for member, role in team.items():
    print(f"{member} is a {role}")

for key in team:
    print(key, team[key])

# Nested dictionaries
organization = {
    "Team": team,
    "Departments": {
        "HR": "Human Resources",
        "SE": "Software Engineering",
        "CS": "Cyber Security"
    },
    "Students":["Osvaldo", "Matthew", "William"]
}

# Accessing nested dictionaries
print("SE stands for ", organization["Departments"]["SE"])
print("The third students is",organization["Students"][2])

# Modifying a nested dictionary
organization["Departments"]["CS"] = "Computer Science"

# Adding to a nested dictionary
organization["Departments"]["BE"] = "BackEnd"

input_dep = input("Which department do you want to update?")
input_update = input("What do you want update it to?")

organization["Departments"][input_dep] = input_update

print(organization)

# List of dictionaries
departments = [
    {"Name": "Engineering", "Head": "Alice", "Focus": "Product Development"},
    {"Name": "Marketing", "Head": "Diana", "Focus": "Brand Strategy"},
    {"Name": "Operations", "Head": "Charlie", "Focus": "Process Optimization"},
]

# Accessing data in a list of dictionaries
print("Head of Operations", departments[0]["Head"])
print("Focus for the 3rd department ", departments[2]["Focus"])