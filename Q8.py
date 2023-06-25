# Question 8
# Import math to mainly use the floor function so that if there is a decimal number it will always round down which is need for the rounding of the years if not it will round  to 1903 years.
# Create a variable to contain the number of minutes inserted by user.
# Find how many minutes are in a year.
# Find how many minutes are in a month.
# Convert the num ber of minutes inserted by user into float to allow calculations to be completed.
# Found out how many years there are by having the number of minutes inserted divided by the number of minutes in year.
# Find the remainder of minutes after the years are calculated by using the function modulus (%)
# Use the remainder of minutes and divide it by the number of minutes in a day to find out how many days there are.
# Print out the the years and days.

from math import *

mins = input("Enter number of minutes: ")
min_in_year = 60 * 24 * 365
min_in_day = 60 * 24

mins = float(mins)

years = mins / min_in_year

remainder = mins % min_in_year
days = remainder / min_in_day

print("There are " + str(floor(years)) + " years and " + str(floor(days)) + " days in this amount of minutes")
