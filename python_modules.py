"""
Description: A script to demonstrate python modules; math and random.
Author:
Date:
Usage: python_modules.py
"""
import math
#import random
from random import randint, choice

teams = ["jets", "flames", "oilers", "canucks", "senators", "canadians"]

number = 64

print(math.sqrt(number))

for count in range(5):
    dice_roll = randint(1, 20)
    print(dice_roll)

print(f"My favorite hockey team is {choice(teams)}.")
