import math

principal = int(input("Enter pricipal amount : "))
interest = float(input("Enter interest rate : "))
years = int(input("Enter number of years : "))

# monthly interest rate
interest_rate = interest/(100 * 12)
# total number of payments
payment_num = years * 12
# calculate the monthly payment
monthly_payment = principal * \
(interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))
print(monthly_payment)

# calculate total loan amount to be paid
total_amount = monthly_payment * years * 12

sf = '''\
For a {} year mortgage loan of ${:,}
at an annual interest rate of {:.2f}%
you pay ${:.2f} monthly'''

print(sf.format(years, principal, interest, monthly_payment))
print('-'*40)
print("Total amount paid will be ${:,.2f}".format(total_amount))