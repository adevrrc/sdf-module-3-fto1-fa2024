"""
Description: A script to demonstrate selections.
Author:
Date:
Usage: python selections.py
"""

age: int = 125
name: str = "David"

if age == 25:
    print("You are at the perfect age.")

print("This is not part of the if block.")

if age > 25:
    print("You are a boomer.")
else:
    print("You are super cool.")


if name == "Damien":
    print("You are super cool.")
elif age < 100:
    print("You are probably still alive.")
elif name == "David":
    print("Hello David")

    print("asdf")

    thing: int = 4

    print(thing * 8)
else:
    print("None of the conditions were met.")

if name == "Damien":
    print("You are super cool.")
elif age < 100:
    print("You are probably still alive.")

if name == "Damien":
    print("You are super cool.")

if age < 100:
    print("You are probably still alive.")

# Match
# Syntax
# match expression(variable):
#     case value:
#          statements
#     case value:
#          statements

age = 77

match age:
    case 5:
        print("You are in kindergarten this year.")
    case 6:
        print("You are in grade school now.")
    case 13:
        print("You will be starting junior high.")
    case 15:
        print("You made it to high school.")
    case _:
        print("You are likely not in school.")

# Logical Operators

age = 23
name = "David"

if age >= 25 or name == "Damien" or name == "David":
    print("Damien you are old.")

# str.isalpha() True, False

if not name.isalpha():
    print("Invalid name.")

if age < 20:
    print("You might be a teenager.")

    if name == "Damien":
        print("You play rugby.")
    elif name == "David":
        print("You are on the chess team.")
else:
    print("You are old.")

# Conditional Operator
# Syntax: operand(value) if operand(boolean_express) else operand(value)

# Java: boolean_exp ? true_value : false_value

name = "Jason"

length_description = "long" if len(name) > 6 else "short"

print(f"{name} your name is {length_description}.")

# Membership Operator

names = ["Damien", "James", "Kirk", "Lars"]

if name not in names:
    print("You were not found in this group.")
else:
    print("You are part of the group.")
