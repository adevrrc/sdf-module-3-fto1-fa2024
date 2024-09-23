"""
Description: A script to demonstrate boolean expressions.
Author:
Date:
Usage: python boolean_expressions.py
"""

# Literals
print(True)
print(False)

# Java: true, false

# Variables
is_damien_here: bool = True
print(is_damien_here)
print(type(is_damien_here))

# Functions
name: str = "Damien"

print(name.isalpha())
print(name.isdigit())

is_alphabetic: bool = name.isalpha()
print(is_alphabetic)

# Operators
# Comparison Operators
age: int = 10

print(age == 25)
print(age != 25)
print(age < 35)
print(age <= 25)
print(age > 56)
print(age >= 2)
