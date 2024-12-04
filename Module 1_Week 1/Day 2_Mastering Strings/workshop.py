# Strings are immutable - they don't change
name = "Allan"

# Creating strings with single and double quotes
single_quote = 'Single quotes are great'
double_quote = "So are double quotes"
print(single_quote)
print(double_quote)

# Multi-line string using triple quotes
multi_line = """This is a
string that
spans multiple lines"""
print(multi_line)

# String indexing
word = "Coding Temple"
print("\nString Indexing:")
print(word[0])
print(word[-1])
print(word[5])

# Concatenation of strings
print("\nConcatenation:")
greeting = "Why hello"
name = "George"
full_greeting = greeting + " " + name + "!"
print(full_greeting)


# Repeat strings with *
print("\nString Repetition:")
laugh = "Ha" * 3 + "!"
print(laugh)

print("-"*30)

# Finding the length of a string
phrase = "I'm not lazy, I'm on energy-saving mode."
print("\nLength of Phrase:")
length_of_phrase = len(phrase)
print(length_of_phrase)

# String slicing (substrings)
print("\nString Slicing Examples:")
string = "slice me up"
print(string[:4])
print(string[3:])
print(string[3:7])
print(string[-5:])

# Convert to uppercase and lowercase
print("\nUppercase and Lowercase:")
message = "Hello, Python!"
print(message.lower())
print(message.upper())


# Remove whitespace from start and end of a string
# check out lstrip and rstrip if you want!
print("\nstrip() removes whitespace:")
whitespace_string = "       Trim this!       "
print(whitespace_string.strip())


# Replace part of a string
print("\nReplace Example:")
text = "I love Java!"
new_text = text.replace("Java", "Python")
print(new_text)

# Split and join
print("\nSplit Example:")
sentence = "Python rocks our world"
words = sentence.split()
print(words)
print(type(words))

print(type(sentence))

print(words[0])

numbers = "12345"
print(type(numbers))
integers = int(numbers)
print(integers)
print(type(integers))




print("\nJoin Example:")
joined_sentence = ",".join(words)
print(joined_sentence)


# Check if a string starts or ends with a specific substring
print("\nStartswith and Endswith:")
filename = "super_secret_file.txt"
print(filename.startswith("my"))
print(filename.startswith("super"))
print(filename.endswith(".txt"))

# String formatting with .format()

print("\nString Formatting with .format():")
name = "Fred"
age = 99
print("My name is {} and I am {} years old.".format(name, age))


# String formatting with f-strings
print("\nString Formatting with f-strings:")
name = "Fred"
age = 99
print(f"My name is {name} and I am {age} years old.")


# More string methods: finding a substring and counting occurrences
long_text = "Python is powerful. Python is versatile. Python is everywhere!"
print("\nFind and Count Examples:")
print(long_text.find("Python"))
print(long_text.count("Python"))


# Using slicing and immutability demonstration
print("\nFixing Strings by Slicing:")
original_text = "Jython"
fixed_text = "P" + original_text[1:]
print(f"Original text: {original_text}")
print(f"Fixed text: {fixed_text}")


# title and capitalize
print("\nTitle and Capitalize:")
text = "hello world"
print(text.capitalize())
print(text.title())

    


# isdigit - Check if a string consists only of digits, 
print("\nisdigit example:")
text = "12345"
print(type(text))
print(text.isdigit())

print(isinstance(text, bool))

decision = False

print(isinstance(decision, bool))