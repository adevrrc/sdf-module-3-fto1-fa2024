"""
Description: A script to demonstrate python modules; math and random.
Author: Damien Altenburg
Date: 2024-9-26
Usage: python_modules.py
"""
# Import entire module
import math
#import random

# Import functions
from random import choice, randint, random, shuffle, uniform

teams: list[str] = [
    "jets",
    "flames",
    "oilers",
    "canucks",
    "senators",
    "canadians"
]

# Math Functions
# Returns square root of the specified value
print(math.sqrt(64))

# Rounds up to the nearest integer
print(math.ceil(1.4))

# Rounds down to the nearest integer 
print(math.floor(1.4))

radius: float = 3.4
print(f"Area: {math.pi * pow(radius, 2):.2f}")

# random Module Functions
# Random value between 0 and 1
random_number = random()
print(random_number)

# Random integer
random_number = randint(3, 9)
print(random_number)

# Random float value
random_number = uniform(3.0, 9.0)
print(random_number)

# Return a random value from the specified collection
random_team = choice(teams)
print(random_team)

# Reorder element values in a random order
shuffle(teams)
print(teams)
