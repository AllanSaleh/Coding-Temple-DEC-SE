# Python Syntax
# camelCase, snake_case, PascalCase, UPPER_CASE
firstName = "Allan"
first_name = "Allan"
FirstName = "Allan" # used only for classes
FIRST_NAME = "Allan" # used only for constants (values never changes)

# Python Conditionals (if, elif, else)
# falsy values
# empty sequences and collections (lists, tuples, strings, dictionaries, sets), zero in every numeric type, None, and False

temp = 85

if temp:
    print('temp defined')
else:
    print('temp undefined')

# comparison operators
# <, <=, >, >=, ==, !=
if (temp >= 90):
    print('Its pretty steamy outside, do not wear black!')
elif temp > 75:
    print("It's a nice day")
elif temp == 65:
    print('The temp is 65 exactly')
else:
    print('Its cold outside, consider layering up!')


# logical AND & OR
# nested if & input function

username = 'allana'
password = 'lakers'

# if(first_name == 'Allan' and username == 'allana'):
#    decision = input('Are you the Lead Instructor, Allan Ahmed? (yes or no)\n').lower()
#    if decision == 'yes':
#         password_attempt = input("What is the password?\n")
#         if password_attempt == 'lakers':
#             print('Access Granted: Hello ' + username)
#         else:
#             print('Incorrect password, try again')
#    else:
#         print("Hello, student!")
# else:
#     print("Hello, student!")


# Python Lists: Stores multiple values in a single variable
students = ["Mitchell", "Robbie", "Elif", "Jeni"]

# indexing
print(students[0])


# slicing (start(includes): stop(excludes): step)
print(students[1::2])


# add to list
students.append("Dustin")

# remove from list using .pop(0), .remove('student 1'), del, .clear()
students.pop(1) # .pop(2) removes index value

students.remove("Jeni") # removes the value itself

del students[0] # deletes the index defined

students.clear() # clears all values in a list

print(students)

# membership checks with "in" & "not in"
languages = ['python', 'javascript', 'c++']

if 'python' not in languages:
    print('Language is Not in the program')
else:
    print('Language is apart of the curriculum')