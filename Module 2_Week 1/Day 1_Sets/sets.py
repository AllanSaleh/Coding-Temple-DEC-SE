"""
In Python, a set is an unordered collection of unique elements. 
It is defined using curly braces {} or the set() constructor. 

Key Characteristics of Sets:
Unique Elements: A set automatically removes duplicate elements.
Unordered: The elements in a set do not have a defined order 
    and cannot be accessed by index.
Mutable: Sets themselves can be modified (adding or removing elements), 
    but the elements in a set are immutable (e.g., numbers, strings, tuples).
    
Common uses: removing duplicates, checking memberships (emails, ips, usernames),
    tracking unique visits to a website, checking password against set of
    commonly used passwords, game inventories, etc
"""

team = set()
team.add("Alice")
team.add("Bob")
team.add("Charlie")
team.add("Diana")
team.add("Bob")

print(f"The current team: {team}")

admins = {"Charlie", "Eve", "Alice"}

print("Is Alice on the team?", "Alice" in team)
print("Is Alice an Admin?", "Alice" in admins)

# Validation of Membership or Inclusion: 
# Is my group (admins) a part of their group (team)?
# Use issubset() to ensure that a smaller collection (admins) 
# is fully satisfied by a larger collection (team).
print("Are all admins in the team?", admins.issubset(team))

# Containment or Ownership Testing
# Does my group (team) contain their group (admins)?
# Use issuperset() to confirm that one set (team) 
# includes all elements of another (admins)

print("Does the team contain all the admins?", team.issuperset(admins))

"""
Summary Analogy:
issubset(): "Do my skills meet the job requirements?"
issuperset(): "Does my toolbox contain all the tools needed for the task?"
"""

# Add a duplicate list of employees and remove duplicates using a set
employee_list = ["Alice","Bob","Eve","Frank", "Alice", "Bob"]
unique_employees = set(employee_list)
print(f"Unique employees after removing the duplicates: {unique_employees}")

# Intersection: Members who are both in the team and admins
admins_and_team_members = team.intersection(admins)
print(f"members who are both team and admin members: {admins_and_team_members}")

# Union: Combines all items from two sets into one leaving out the duplicates
all_people = team.union(admins)
print(f"all members: {all_people}")

# Difference: Admins who are not in the team
admins_not_in_team = admins.difference(team)
print(f"Admins not in the team: {admins_not_in_team}")

# Difference: Team members who are not admins
team_not_an_team = team.difference(admins)
print(f"Team that are not an admin: {team_not_an_team}")

# Symmetric Difference: Characters who are either in the team or admins, but not both
unique_to_each_group = team.symmetric_difference(admins)
print(f"People unique to either the team or admins: {unique_to_each_group}")

# Loop over the team
for member in team:
    print(member)

# Remove a member from the team
team.discard("Eve")
team.discard('Bob')
print(team)

# Frozen set example: Immutable set
tools = frozenset({"Hammer", "Wrench", "Screwdriver"})
print(f"Tools: {tools}")
# tools.add("Drill") # causes error