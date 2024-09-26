"""
Description: A script to demonstrate file output.
Author: Damien Altenburg
Date: 2024-9-26
Usage: python file_output.py
"""
file_path: str = "grades.txt"
grades: list[int] = [85, 34, 67, 78, 89, 99, 21, 45, 64, 88, 92]

# Write to a file then close the file
with open(file_path, "w") as file:
    file.write(str(grades[0]))

# Write to file using List
with open(file_path, "w") as file:
    for grade in grades:
        # Writes without a line ending
        #file.write(str(grade))

        # Write with line ending
        file.write(f"{grade}\n")

# Append to a file
with open(file_path, "a") as file:
    for grade in [66, 77, 88]:
        file.write(f"{grade}\n")
