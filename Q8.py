# Question 8
# Create a variable to contain the number of minutes inserted by user.
# Find how many minutes are in a year.
# Find how many minutes are in a month.
# Convert the number of minutes inserted by user into int to allow calculations to be completed.
# Found out how many years there are by having the number of minutes inserted divided by the number of minutes in year. Use floor division to make sure it's rounded down.
# Find the remainder of minutes after the years are calculated by using the function modulus (%)
# Use the remainder of minutes and divide it by the number of minutes in a day to find out how many days there are. Use floor division to make sure it's rounded down.
# Print out the the years and days.

mins = input("Enter number of minutes: ")
min_in_year = 60 * 24 * 365
min_in_day = 60 * 24

mins = int(mins)

years = mins // min_in_year

remainder = mins % min_in_year
days = remainder // min_in_day

print("There are " + str(years) + " years and " + str(days) + " days in this amount of minutes")
