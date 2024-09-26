"""
Description: A script to demonstrate file input.
Author: Damien Altenburg
Date: 2024-9-26
Usage: python file_input.py
"""
# Syntax
# open(file_path) # mode = "rt"
# open(file_path, mode)

# Modes
# - "r" Read (default) Opens for reading. Error if the file doesn't exist.
# - "a" Open for appending, creates the file if it doesn't exist.
# - "w" Open for writing, creates the file if it doesn't exist.
# - "x" Creates the specified file, returns an error it the file doesn't exist.
# - "t" Text (default)
# - "b" Binary (e.g. images)

file_path = "data.txt"

# Opens the file at the specified path and returns a reference to a
# file object. File path can be relative or absolute. Relative paths are
# evaluated from your terminal's PWD.
file = open(file_path)

print(type(file))

# Reads the whole file and returns it as a string.
data: str = file.read()

print(data)

# Won't read anything because file pointer is at the end of the file
data: str = file.readline()
print(f"Second read: {data}")

# Close the file; release the resource
file.close()

file = open(file_path)

# Reads a line of data from the file
print(file.readline())

# Reads each line of a file (from the file pointer)
for line in file:
    # rstrip() - Strips whitespace to the right of a string.
    # lstrip() - Strips whitespace to the left of a string.
    # strip() - Strips whitespace from both sides of a string.
    print(f"Read line: {line.rstrip()}")

# Close the file
file.close()

# File open error
#file = open("this-file-doesnt-exist.txt", "r")

# Read all lines into a List
with open(file_path) as file:
    # Returns a list where each element is a line from the file
    data: list[str] = file.readlines()
    print(data)

# File will be closed at this point

# Read all lines into a List where each record is a List
with open(file_path) as file:
    records: list[list] = \
        [record.rstrip().split(',') for record in file.readlines()]
    print(records)
