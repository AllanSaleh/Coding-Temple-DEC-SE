"""
Tuples
-Ordered: The elements in a tuple maintain their position and can be accessed using indices.
-Immutable: You cannot change, add, or remove items in a tuple after it is created.
-Heterogeneous: Tuples can contain a mix of data types.
-Defined by Parentheses: Tuples are typically created using () or the tuple() constructor.
-Memory efficient: Tuples are more memory efficient than lists
-Read only integrity: once they've been created the data can't change
-Common uses: fixed coordiantes on a map, sensitive data from databases that should not change
"""

# Creating a tuple with names
names = ("Alice", "Bob", "Charlie", "Dana")


# Single element tuple (requires a trailing comma)
leader = ("Alice",)
print(f"Team Leader: {leader}", type(leader))

# Empty tuple
empty_group = ()
print(type(empty_group))

# Using the tuple() constructor
gifts = tuple(["Notebook", "Pen", "Laptop"])
print(gifts, type(gifts))

# Accessing tuple elements
print(f"The second name is:",names[1])

# Slicing tuples
print(f"First three members of the team:{names[:3]}")
print(f"Last three members of the team:{names[-3:]}")


# Looping over tuples
for name in names:
    print(name)
    
# Tuples are immutable; attempting to change an element raises an error
try:
    names[0] = "Allan"
except TypeError as e:
    print(f"Cannot modify tuple: {e}")
    

# Reassigning a tuple
# names = ("Allan","Robbie","Mitchell", "Matthew", "Kelly","Ferdinand")
# print(names)


# Tuple packing and unpacking
# Great for csv (comma separated values) files
tools = "Hammer", "Screwdriver", "Wrench", "Drill"
print(tools,type(tools))
tool1, secondary_tool, tool3, main_tool = tools

print(f"Unpacking tools: tool1: {tool1} | secondary_tool: {secondary_tool} | tool3: {tool3} | main: {main_tool}")


# Extended unpacking
first, *middle, last = tools
print(first)
print(middle)
print(last)

names = ("Allan","Robbie","Mitchell", "Matthew","Ferdinand", "Kelly", "Matthew")
first_name, second, third, *rest_of_name, last_person = names
print(f"first: {first_name}, second: {second}, third: {third}, the rest of the tuple in a var: {rest_of_name}, last_person: {last_person}")

# Using _ as a placeholder in unpacking
_, _, third_person, *_ = names
print(third_person)

# Unpacking and packing with functions/parameters/arguments
def introduce_member(name, role, location):
    print(f"{name}, the {role}, is from {location}")

member1 = ("Alice", "Leader", "New York")
member2 = ("Ben", "Engineer", "San Francisco")

# introduce_member(member1[0], member1[1], member1[2])
print(*member1)
introduce_member(*member1)


def list_roles(*members):
    print(members)
    for name, role, _ in members:
        print(f"{name}: {role}")

list_roles(member1, member2)

# Tuple methods: count() and index()
print(f"Count of Bob in team: {names.count('Matthew')}")
print(f"Index of 'Kelly' in tuple:{names.index("Kelly")}")
