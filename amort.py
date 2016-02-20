"""
Title: Sample Projects - Monthly Payment Calculator
Author: Mandeep Bhutani
Date: 02/18/2018
Problem: Calculate the monthly payments of a fixed term mortgage over given
Nth terms at a given interest rate. Also figure out how long it will take the
user to pay back the loan. For added complexity, add an option for users to
select the compounding interval (Monthly, Weekly, Daily, Continually).

Analysis: The  present value of annuity formula is used to solve this
problem and takes the form of: A = i * p * (1 + i)^n / (1 + i)^n - 1
Where A is the monthly payment, p is the present value of the borrowed
amount, i is the period's interest rate, and n is the total number of
payments. While the variables chosen are not pythonic, they do correspond
to the annuity formula variables.
"""
p = float(input('Enter the amount borrowed:'))
t = float(input('Enter the length of the loan (in years):'))
q = float(input('Enter the number of pay periods per year:'))
i = float(input('Enter the annual interest rate:')) / 100 / q
n = t * q
amount = (i * p * pow(1 + i, n)) / (pow(1 + i, n) - 1)
print('The monthly payment amount is ${}.' .format(round(amount, 2)))
