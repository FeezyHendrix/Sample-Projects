"""
Title: Sample Projects - Monthly Payment Calculator
Author: Mandeep
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
import pandas as pd


class Amortization(object):

    def __init__(self, name='Loan'):
        self.name = name
        self.p = float(input('Enter the amount borrowed:'))
        self.t = float(input('Enter the length of the loan (in years):'))
        self.q = float(input('Enter the number of pay periods per year:'))
        self.i = float(input('Enter the annual interest rate:')) / 100 / self.q
        self.n = int(self.t * self.q)

    def present_value(self):
        return self.p

    def number_of_payments(self):
        return self.n

    def interest_rate(self):
        return self.i

    def monthly_payment(self):
        amount = (self.i * self.p * pow(1 + self.i, self.n)) / (pow(1 + self.i, self.n) - 1)
        return round(amount, 2)

    def beginning_balances(self):
        balance = []
        beginning_balance = self.p
        for _ in range(0, self.n):
            balance.append(round(beginning_balance, 2))
            beginning_balance -= self.monthly_payment() - (beginning_balance * self.i)
        return balance

    def interest_payments(self):
        return [round(bal * self.i, 2) for bal in self.beginning_balances()]
    
    def principal_payments(self):
        return [round(self.monthly_payment() - i_pay, 2) for i_pay in self.interest_payments()]

    def ending_balances(self):
        return [round((bal - pri), 2) for bal, pri in zip(self.beginning_balances(), self.principal_payments())]

    def schedule(self):
        df = pd.DataFrame.from_items([('Beginning Balance', self.beginning_balances()),
                                      ('Monthly Payment', self.monthly_payment()),
                                      ('Principal', self.principal_payments()),
                                      ('Interest', self.interest_payments()),
                                      ('Ending Balance', self.ending_beginning_balances())])
        df.index = df.index + 1
        return df
