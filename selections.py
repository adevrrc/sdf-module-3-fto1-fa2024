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
