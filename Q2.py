# Question 2
# Have a variable made to hold a value entered by the user.
# Calculate using the value entered the 6% tax and hold the value in a variable.
# Print the sales tax with 2 decimal places.

Purchase = input("Purchase Amount: ")

Sales_tax = float(Purchase) * 0.06
Sales_tax = round(Sales_tax, ndigits = 2)

print(Sales_tax)