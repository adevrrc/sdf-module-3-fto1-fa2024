"""
Description: A script to demonstrate list comprehensions.
Author: Damien Altenburg
Date: 2024-9-26
Usage: list_comprehensions.py
"""
squares: list[int] = [number ** 2 for number in range(1, 11)]
print(squares)

names: list[str] = ["kenny", "eric", "kyle", "stan", "butters", "clyde"]

odd_names: list[str] = [name.title() for name in names if len(name) % 2 != 0]
print(odd_names)
