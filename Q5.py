# Question 5
# Create 2 variable to contain 2 values (subtotal and tip rate)
# Convert the string values into float to have decimals
# Calculate the tip and the total amount
# Print the tip and total amount calculated

tip_rate = input("Enter the tip rate: ")
subtotal = input("Enter the subtotal: ")

tip_rate = float(tip_rate)
subtotal = float(subtotal)

tip = subtotal * (tip_rate / 100)
total = subtotal + tip

print(round(tip, ndigits = 2))
print(round(total, ndigits = 2))
