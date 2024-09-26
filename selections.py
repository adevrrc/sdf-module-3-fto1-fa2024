"""
Description: A script to demonstrate selections.
Author: Damien Altenburg
Date: 2024-9-23
Usage: python selections.py
"""
age: int = 25
name: str = "Damien"

# Syntax
# if boolean_expression:
#     Statements when expression is true
if age == 25:
    print(f"The number is {age}")

print("This statement is not part of the if block.")

# Syntax
# if boolean_expression:
#     Statements when the expression is True
# else:
#     Statements when the expression is False
if age > 25:
    print("You are older.")
else:
    print("You are younger.")

# Syntax
# if boolean_expression:
#     Statements when the expression is True
# elif boolean_expression:
#     Statements when the expression is True
if age == 30:
    print("You are 30.")
elif age == 40:
    print("You are 40.")

# The following may look similar, but is different logic
if age == 30:
    print("You are 30.")

if age == 40:
    print("You are 40.")

# Syntax
# if boolean_expression:
#     Statements when the expression is True
# elif boolean_expression:
#     Statements when the expression is True
# else:
#     Statements when all expressions are False
if age >= 10:
    print("The number is 10 or higher.")
elif age != 5:
    print("Less than 10, but not 5.")
else:
    print("The number is 5.")

# Logical Operators (and, or, not)
# Syntax
# if boolean_expression operator boolean_expression:
#     Statements when the expression is True
if age >= 25 and name == "Damien":
    print("You are super cool.")

if age > 50 or name == "Damien":
    print("Still super cool.")

if not name.isalpha():
    print("Invalid name.")

# Short-circuiting
if age == 50 and name == "Damien":
    print("Age: 50, Name: Damien")

# Nested Selections
if age > 25:
    print("Age is greater than 25")

    if age == 50:
        print("You are 50.")
else:
    print("You are young.")

# Conditional Operator
# Syntax
# operand if operand else operand
# value if boolean_expression else value
age_description: str = "old" if age > 25 else "young"

print(f"You're {age_description}")

names: list[str] = ["kenny", "jon", "max", "chris", "saraya"]
name: str = "jason"

# Membership Operators
# Syntax
# value in collection_reference
# value not in collection_reference
negator: str = "" if name in names else "not "

print(f"{name.title()} is {negator}in the list.")

# Match
match name:
    case "kenny":
        message = "You are Mr. Omega"
    case "jon":
        message = "Your last name is Moxley"
    case "max":
        message = "Hello Mr. Caster"
    # "jason" or "chris"
    case "jason" | "chris":
        message = "I don't know you, but I still think you're cool."
    # default case (optional)
    case _:
        message = "Sorry, no special greeting for you."

print(message)
