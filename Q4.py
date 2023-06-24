# Question 4
# 3 variables are created to retain the annual interest rate, number of years, and loan amount.
# All the retained values must be changed from string into float.
# Monthly interest rate is calculated by using the annual interest rate and dividing by 100 to convert into decimals and then dividing by 12, the number of months in a year.
# Monthly payment is calculated using the previously calculated monthly interest rate and multipling it with the loan amount (MIGHT BE WRONG).
# total payment is then calculated by multipling the loan amount with the number of years and also the annual interest rate in decimal form. 

annual_interest_rate = input("Enter annual interest rate: ")
no_years = input("Enter number of years: ")
loan = input("Enter loan amount: ")

annual_interest_rate = float(annual_interest_rate)
no_years = float(no_years)
loan = float(loan)

monthly_interest_rate = (annual_interest_rate / 100) / 12

monthly_payment = monthly_interest_rate * loan

total_payment = loan * no_years * (annual_interest_rate / 100)

print(monthly_interest_rate)
print(monthly_payment)
print(total_payment)
