# Question 3
# Create a variable to hold 3 values.
# Once 3 numbers are inputted with commas inbetween, a split function is needed to get the individual numbers
# The numbers are then needed to be changed from string to float values
# Average is calculated
# Average printed

numbers = input("Enter in three numbers separated by commas: ")
numbers = numbers.split(",")

numbers[0] = float(numbers[0])
numbers[1] = float(numbers[1])
numbers[-1] = float(numbers[2])

Average = (numbers[0] + numbers[1] + numbers[2]) / 3

print(Average)

