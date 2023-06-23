# Question 4
# 3 variables are created to retain the 

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
