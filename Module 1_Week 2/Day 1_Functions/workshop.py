
def greet(name):
    """
    This function greets a person
    """
    print("Hello "+ name)
    print("Welcome to Coding Temple!")

greet("Mitchell")
greet("Dustin")


"""
Docstrings - explanations of functions
    1. What the function does
    2. The received parameters and data types
    3. What is returned and the data type
"""


jedi_name = "Luke Skywalker"
jedi_rank = "Jedi Knight"
force_power = 100

def attack(target, weapon = "lightsaber"):
    """
    Perform an attack on a target with a specified weapon.

    Parameters:
    target (str): The target being attacked.
    weapon (str): The weapon being used. Defaults to "lightsaber".
    
    Returns:
    str: The action of the attack.
    """

    jedi_name = "Obi Wan Kenobi"
    return f"{jedi_name} attacks {target} with a {weapon}"

print(attack("Darth Vader"))

print(f"the global variable jedi_name {jedi_name} was not affected")



# def sum(num1, num2):
#     return num1+num2


# def display_result(number_to_display):
#     print(f"The result is {number_to_display}")

# result = sum(5,6)

# display_result(result)

# [1,2,3,4,5,6]
# (1,2,3,4,5,6) #tuple



def add_force_power(*points):
    """
    Adds points to the Jedi's force power.

    Parameters:
    *points (int): Multiple point values to be added.
        - The * means it can accept however many arguments passed in
        - Values are placed in a tuple (immutable list)
    Returns:
    int: The new total points.
    """
    total_power = sum(points)
    global force_power # uses the global force_power var, not a local one
    force_power += total_power
    return force_power


print(f"Jedi's force power after battle: {add_force_power(50, 75, 25, 12, 6, 100, 25)}")
print(f"The global var force_power was changed to {force_power}")

# tuple1 = (12,5,9,9)