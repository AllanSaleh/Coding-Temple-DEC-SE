# Python File Handling Lesson

# Python provides built-in functions to easily read, write, and manipulate files.

'''
    Reading Files:
    "read()" - Reads the entire content of the file
    "readline()" - Reads a single line
    "readlines()" - Reads all lines and returns a list
    
    Common Modes:
    "r" - Read (default)
    "w" - Write (overwrites the file)
    "a" - Append (adds to the file)
    "x" - Create (creates a new file, raises error if the file exists)
    "b" - Binary (used for binary files like images)
    "t" - Text (default)
'''

# 1. Open and read a .txt file
# NOTE: open() returns a file object.
file = open('workshop.txt', 'r')
print(file)
content = file.read()
print(content)
file.close()

# 2. Writing to a .txt file
# write(): writes a string to the file
file = open('workshop.txt', 'w')
file.write("I am writing to the txt file from Python")
# writelines(): writes a list of strings
file.writelines(['\nstudent 1: Robbie\n','student 2: Mitchell\n','student 3: Kassie\n', 'student 4: Marc\n'])
file.close()


# 3. Appending to Files: Add content to an existing file
file = open('workshop.txt', 'a')
file.write('I am Allan the Instructor')
file.close()


# opening a file with the "with" statement: good practice and recommended way of opening files because it automatically closes the file
print(30*"*")
with open('workshop.txt', 'r') as file:
    content = file.read()
    print(content)


try:
    with open('class.txt', 'x') as file:
        file.write('This is a new file created with "x" mode')
except FileExistsError:
    print('File already exists!')

print("This is a sentence")


# Python Modules Lesson: allows you to structure your code and reuse it in other programs. Its just a .py file containing python code (functions, classes, or variables)

# 1. Importing a module
import re

from math import pi as pie
print(pie)

# 2. Creating your own Module
import modules.mymodule as mymodule
mymodule.greet("Allan")

# Importing Specific Functions
from modules.mymodule import loop_students
loop_students(['Timothy',"Osvaldo","Elif","Dustin"])

# Using "as" to Rename a Module or Function
import math as m
print(m.pi)

from math import sqrt as square_root
print(int(square_root(16)))

# use the "." for nested imports
from modules.python_modules.anotherone import loop_students as loop
loop(['Timothy',"Osvaldo","Elif","Dustin"])

# 3. Built-in and Third-Party Modules: Python has a large set of built-in modules (like "os", "sys", "datetime"). You can also install third-party modules using "pip or pip3"
import requests
import pyfiglet

text = "Hello, World!"

ascii_art = pyfiglet.figlet_format(text)

print(ascii_art)