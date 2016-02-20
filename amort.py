p = float(input('Enter the amount borrowed:'))
t = float(input('Enter the length of the loan (in years):'))
q = float(input('Enter the number of pay periods per year:'))
i = float(input('Enter the annual interest rate:')) / 100 / q
n = t * q
amount = (i * p * pow(1 + i, n)) / (pow(1 + i, n) - 1)
print('The monthly payment amount is ${}.' .format(round(amount, 2)))
