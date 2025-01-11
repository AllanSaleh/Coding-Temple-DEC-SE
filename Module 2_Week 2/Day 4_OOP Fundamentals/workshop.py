# OOP Fundamentals Lesson

# OOP is a programming paradigm that models real-world entities as objects. It provides a structure for complex programs by breaking them into smaller, reusable pieces of code.(objects)

# Basic Concepts in OOP:
'''
    - Class: A blueprint for creating objects (blueprint for a house)
    - Object: An instance of a class (the house built from the blueprint)
    - Attributes: Variables that belong to a class (or object). They define the class's properties.
    - Methods: Functions that belong to a class. They define the class's behavior.
'''

# Four Pillars of OOP:
# NOTE: This is a common interview question
'''
    1. Encapsulation: The bundling of attributes and methods that operate inside of a single class.
    2. Inheritance: Where one class (child class) inherits attributes and methods from another class (parent class). This promotes code reusability.
    3. Polymorphism: The ability of different classes to be treated as instances of the same class through a common interface. The ability to use the same method in different ways depending on the object.
    4. Abstraction: Hiding the complexity of the implementation and exposing only the necessary parts.
'''

# print("Hello everyone!")


# 1. Creating a Classes and Objects
# Creating the class(blueprint)
class MyClass:
    # constructor / dunder init
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2


    def my_method(self):
        print(f"This is our first method. Attribute1: {self.attribute1}, Attribute2: {self.attribute2}")


# Creating the Object(instance)
obj = MyClass("Allan", "Kelly")
print(obj.attribute1)
print(obj.attribute2)
obj.my_method()


# 2. Encapsulation: Implemented by defining instance variables and methods
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # Getter
    def get_salary(self):
        return self.salary
    
    # Setter
    def set_salary(self, new_salary):
        self.salary = new_salary


employee1 = Employee("Elif", 100000)
print(employee1.get_salary())
employee1.set_salary(2000000)
print(employee1.get_salary())


employee2 = Employee("Kelly", 3000000)
print(employee2.get_salary())
print(employee2.name)
employee2.set_salary(40000000)
print(employee2.get_salary())




# Inheritance: Allows a child class to acquire the properties and behaviors of a parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print('Animal does breathe air')
    
    def speak(self):
        print('Animal makes sound')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Dogs BARK!")

animal1 = Animal("Blue")
animal1.breathe()

dog1 = Dog("Bruno", "Golden Retriever")
dog1.breathe()

# Polymorphism: Allows the same method to perform different actions based on the object.
animal1.speak()
dog1.speak()

another_dog = Dog("Buffy", "Australian Shepard")

# Abstraction: Not seeing the logic that goes into functionality (EX: len(), print(), etc.)
another_dog.breathe()
print("Hello")