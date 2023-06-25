# Question 10
# Create a variable that contains the number inserted by the user.
# Convert the number into an integer for the calculation.
# Extract the hundreds digit using floor division.
# Extract the tens digit using modulus first then floor divison.
# Extract the ones digit using modulus.
# Sum all the digits together.
# Print the sum

number = input("Enter a number between 0 and 999: ")
number = int(number)

first_number = number // 100  
second_number = (number % 100) // 10  
third_number = number % 10  

sum = first_number + second_number + third_number

print("First number:", first_number)
print("Second number:", second_number)
print("Third number:", third_number)
print("Sum:", sum)