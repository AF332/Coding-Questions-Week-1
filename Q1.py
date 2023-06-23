# Question 1
# Have 3 variables made to store 3 values that are inputted by the user.
# Change the values being stored into float values since you want the average to have a decimal and the values being inputted by the users are defaulted as strings.
# Find the average by adding the 3 numbers together and dividing by the total number of numbers.
# Print the results.

number_1 = input("Enter a number: ")
number_2 = input("Enter a second number: ")
number_3 = input("Enter a third number: ")

Average = (float(number_1) + float(number_2) + float(number_3)) / 3

print(Average)

