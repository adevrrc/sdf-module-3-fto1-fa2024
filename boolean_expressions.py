"""
Description: A script to demonstrate boolean expressions.
Author: Damien Altenburg
Date: 2024-9-23
Usage: python boolean_expressions.py
"""
age: int = 25
name: str = "Damien"

# Boolean literals
print(True)
print(False)

# Boolean variables
is_damien_cool: bool = True
print(is_damien_cool)

# Boolean Functions
print(name.isalpha())
print(name.isdigit())

# Comparison Operators (Boolean Operations)
print(age == 25)
print(age == 35)
print(age != 35)
print(age < 14)
print(age <= 25)
print(age > 25)
print(age >= 25)
