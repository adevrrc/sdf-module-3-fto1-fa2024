"""
Description: A script to demonstrate the for loop.
Author:
Date:
Usage: python for_loop.py
"""

THRESHOLD = 27
temperatures = [19, 23, 24, 18, 24, 29, 35, 35, 23, 27]
number_of_temperatures_below_threshold = 0

for temperature in temperatures:
    if temperature < THRESHOLD:
        number_of_temperatures_below_threshold += 1

print(number_of_temperatures_below_threshold)

uppercase_letter_count = 0
lowercase_letter_count = 0
whitespace_character_count = 0

hockey_teams = {
    "winnipeg": "jets",
    "calgary": "flames",
    "edmonton": "oilers"
}

for key in hockey_teams:
    print(f"{key.title()} {hockey_teams[key].title()}")

for number in range(1, 11):
    print(number)
