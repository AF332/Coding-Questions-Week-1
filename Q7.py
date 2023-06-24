# Question 7
# Create 2 variable to hold the values of weight in lbs and hight in inches.
# COnvert the strings into float values.
# Convert the height into meters and weight into kg.
# Use BMI formula to calculate the BMI.
# Print out the result.

Weight_lbs = input("Enter weight in lbs: ")
Height_inches = input("Enter height in inches: ")

Weight_lbs = float(Weight_lbs)
Height_inches = float(Height_inches)

Weight_kg = Weight_lbs * (1 / 0.45359237)
Height_meters = Height_inches * (1 / 0.0254)

BMI = Weight_kg / sqrt(Height_meters)

print(BMI)