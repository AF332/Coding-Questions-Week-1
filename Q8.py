# Question 8

from math import *

mins = input("Enter number of minutes: ")
min_in_year = 60 * 24 * 365
min_in_day = 60 * 24

mins = float(mins)

years = mins / min_in_year

remainder = mins % min_in_year
days = remainder / min_in_day

print("There are " + str(floor(years)) + " years and " + str(round(days)) + " days in this amount of minutes")
