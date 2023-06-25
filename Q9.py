# Question 9
# Create a variable for user to input the monthly saving amount.
# Create a variable the annual interest rate in decimals.
# Find the monthly interest rate.
# Define the starting balance of the account.
# Create a for loop to repeat 6 times.
# Calculate the amount gained from interest rate for the first month and then let the for loop repeat it 6 times.
# Print the final balance.

monthly_saving_amount = float(input("Enter the monthly saving amount: "))

annual_interest_rate = 0.05
monthly_interest_rate = annual_interest_rate / 12

account_value = 0

# Calculate the account value after 6 months
for month in range(6):
    account_value = account_value + monthly_saving_amount
    account_value = account_value + (account_value * monthly_interest_rate)

# Display the account value after 6 months
print("Account value after 6 months:", round(account_value, ndigits = 2)) # easier using comma then + cos won't have to change back into a string

