"""
Description: A script to demonstrate the while loop.
Author:
Date:
Usage: python while_loop.py
"""
new_password = "new_password"
password_confirmation = "password_confirmation"

while new_password != password_confirmation:
    new_password = input("Enter the new password: ")

    password_confirmation = input("Confirm the password: ")

    # when the password is not confirmed
    if new_password != password_confirmation:
        print("Passwords did not match. Try again.")
    else:
        print("Password updated!")
