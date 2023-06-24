# Question 7
# Create 2 variable to hold the values of weight in lbs and hight in inches.
# COnvert the strings into float values.
# Convert the height into meters and weight into kg.
# Use BMI formula to calculate the BMI.
# Print out the result.

import math

Weight_lbs = input("Enter weight in lbs: ")
Height_inches = input("Enter height in inches: ")

Weight_lbs = float(Weight_lbs)
Height_inches = float(Height_inches)

Weight_kg = Weight_lbs * 0.45359237
Height_meters = Height_inches * 0.0254

BMI = Weight_kg / math.sqrt(Height_meters)

print(BMI)