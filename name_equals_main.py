# 1. What is __name__?
# - Every Python file (module) has a built‑in variable called __name__.
# - When you run a file directly, Python sets __name__ = "__main__".
# - When you import the file as a module, Python sets __name__ to the module’s name (the filename without .py)

# 2. Why Use if __name__ == "__main__":?
# It’s a control guard that lets you separate:
# - Code that should run only when the file is executed directly (like tests, demos, or scripts).
# - Code that should NOT run when the file is imported (like helper functions, classes, constants).

def square(x):
    return x**2

print("This will always run")

if __name__ == "__main__":
    # This block runs only if executed directly
    print("Running as a script")
    print(square(5))

# “__name__ is a special variable in Python. When a file is run directly, __name__ is set to '__main__'. 
# When it’s imported, __name__ is set to the module’s name. 
# The if __name__ == "__main__": idiom is used to ensure certain code runs only when the file is executed directly, 
# not when imported.”

# mymath.py

def square(x):
    """Return the square of a number."""
    return x**2

def cube(x):
    """Return the cube of a number."""
    return x**3

# This block will only run if the file is executed directly
if __name__ == "__main__":
    print("Running mymath as a script...")
    print("Square of 5:", square(5))
    print("Cube of 3:", cube(3))

# Running mymath as a script...
# Square of 5: 25
# Cube of 3: 27

# main.py
# import mymath

# print("Using mymath as a module")
# print(mymath.square(10))

# This will NOT print the 'Running mymath as a script...' part
# Using mymath as a module
# 100

# - You can reuse functions (square, cube) in other files without triggering the test/demo code.
# - The __main__ block acts like a self‑test harness or entry point.
# - This is the Pythonic way to write reusable modules that can also be executed standalone.

# “if __name__ == "__main__": lets a Python file act both as a reusable module and as a standalone script. 
# The block under it runs only when executed directly, not when imported.”


# What it is
# - __init__ is the constructor method in Python classes.
# - It’s automatically called when you create a new object from a class.
# - Its main job: initialize the object’s state (i.e., set up attributes).

class Student:
    def __init__(self, name, age):
        # initialize attributes
        self.name = name
        self.age = age

# Creating an object automatically calls __init__
s1 = Student("Sayan", 25)
print(s1.name, s1.age)   # Sayan 25

# - __init__ is not the object creator (that’s __new__), but the initializer.
# - It ensures each object starts with the right data.
# - You can give it default values:

class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

# Why It’s Useful
# - Encapsulates setup logic in one place.
# - Makes objects self‑contained and ready to use immediately.
# - Supports different initializations via parameters

# “The __init__ method in Python is the constructor. 
# It runs automatically when an object is created, and its main use is to initialize the object’s attributes. 
# It doesn’t create the object—that’s __new__—but it ensures the object starts in a valid state.”

# - Public: accessible everywhere (default).
# - Protected: prefix with _ (convention: “don’t touch unless subclass”).
# - Private: prefix with __ (name mangling makes it harder to access directly)


# 🧩 What is Name Mangling?
# - In Python, when you define an attribute with two leading underscores (e.g., __pin), 
# the interpreter automatically changes its name internally to avoid accidental access or overriding in subclasses.
# - This process is called name mangling.
# - The attribute __pin inside a class BankAccount becomes _BankAccount__pin under the hood.

# Why does Python do this?
# - To prevent accidental collisions between subclass attributes and parent class attributes.
# - To discourage direct access to variables meant to be private.
# - It’s not true “privacy” (like in Java/C++), but a soft barrier.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private (name mangled)

acct = BankAccount(1000)

# print(acct.__balance)          # ❌ AttributeError
print(acct._BankAccount__balance)  # ✅ Works (name mangled form)

# - Name mangling doesn’t make attributes truly private.
# - It just makes them harder to access accidentally.
# - You can still access them if you know the mangled name, but that’s considered bad practice.

# “Name mangling in Python is the automatic transformation of identifiers with double leading underscores. 
# For example, __var inside class MyClass becomes _MyClass__var. 
# This prevents accidental name clashes in subclasses and discourages direct access to private attributes.”

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism in action
for animal in [Dog(), Cat()]:
    print(animal.speak())

# method overriding

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r**2

class Square(Shape):
    def __init__(self, s):
        self.s = s
    def area(self):
        return self.s**2

shapes = [Circle(3), Square(4)]
for s in shapes:
    print(s.area())

# Duck Typing in Python

class Duck:
    def quack(self): return "Quack!"

class Person:
    def quack(self): return "I can quack like a duck!"

def make_it_quack(obj):
    print(obj.quack())

make_it_quack(Duck())     # Quack!
make_it_quack(Person())   # I can quack like a duck!

# Class Methods
# - Defined with the @classmethod decorator.
# - First argument is cls (the class itself, not the instance).
# - Can access and modify class state (class variables).
# - Often used as alternative constructors or for operations that affect the whole 

class Employee:
    company = "TCS"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Sayan")
print(e1.company)  # TCS

Employee.change_company("Infosys")
print(e1.company)  # Infosys (class variable changed for all)

# - Defined with the @staticmethod decorator.
# - No self or cls parameter.
# - Behaves like a regular function, but lives inside the class for logical grouping.
# - Cannot access or modify class/instance state.
# - Used for utility/helper functions related to the class.

class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

print(MathUtils.add(5, 7))  # 12

# Instance Methods (for contrast)
# - Regular methods (no decorator).
# - First argument is self (the instance).
# - Can access/modify both instance variables and class variables.

class Employee:
    company = "TCS"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, int(salary))   # alternative constructor

    @staticmethod
    def is_high_salary(salary):
        return salary > 50000

# Alternative constructor
e2 = Employee.from_string("Sayan-60000")
print(e2.name, e2.salary)  # Sayan 60000

# Static method usage
print(Employee.is_high_salary(e2.salary))  # True


# “Instance methods work with object data. 
# Class methods work with the class itself and are often used as alternative constructors. 
# Static methods don’t access class or instance data—they’re just utility functions grouped inside the class for 
# logical organization.”