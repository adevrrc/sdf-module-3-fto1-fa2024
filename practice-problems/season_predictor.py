"""
Description: 
Write a program that reads a temperature as a whole number from the keyboard 
and outputs a "probable" season (winter, spring, summer, or fall) depending 
on the temperature.

- [x] If the temperature is greater than or equal to 90, it is probably summer.
- [x] If the temperature is greater than or equal to 70 and less than 90, it is 
probably spring.
- [x] If the temperature is greater than or equal to 50 and less than 70, it is 
probably fall.
- [x] If the temperature is less than 50, it is probably winter.
- [x] If the temperature is greater than 110 or less than −5, then you should 
output that the temperature entered is outside the valid range.

1. input?

- temperature (float) - The temperature in Fahrenheit.
    - prompt: "Enter the temperature (Fahrenheit): {temperature}"

2. process?

- Refer to login in the problem.

3. output?

- "The temperature is out of range."
- "The season is probably {season}."

Author: Damien Altenburg
Date: 2024-10-1
Usage: python season_predictor.py
"""
temperature = input("Enter the temperature (Fahrenheit): ")

temperature = float(temperature)

message = ""

if temperature < -5 or temperature > 110:
    message = "The temperature is out of range."
else:
    season = ""

    # input was valid
    if temperature >= 90:
        season = "summer"
    elif temperature >= 70:
        season = "spring"
    elif temperature >= 50:
        season = "fall"
    else:
        season = "winter"

    message = f"The season is probably {season}."

print(message)
