"""
Description: Write a program that reads a file and writes a copy of the file to
             another file with line numbers inserted.
Author: Damien Altenburg
Date: 2024-10-1
Usage: python add_line_numbers_to_file.py
"""
from os import path

# Get the directory the script is saved to
script_directory = path.dirname(path.realpath(__file__))

# Use script directory to create the other project paths
data_directory = f"{script_directory}/data"
output_directory = f"{script_directory}/output"

# Open the data file
with open(f"{data_directory}/data50.txt", "r") as data_file:
    line_number = 1

    with open(f"{output_directory}/output50.txt", "w") as output_file:
        for data_line in data_file:
            output_line = f"{line_number} {data_line}"
            output_file.write(output_line)
            
            # Increment line number
            line_number += 1 
