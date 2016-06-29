"""
Project: Find Pi to the Nth Digit - Mega Projects List
Author: Mandeep Bhutani
Date: 1/28/2015

Problem: Enter a number and have the program generate Pi up to
that many decimal places. Keep a limit to how far the program will go.

Analysis: The use of the bailey-borwein-plouffe formula allows for the quick
calculation of Pi to the nth digit. The user is constrained to 10,000 decimal
places of Pi as required by the problem.

References: https://en.wikipedia.org/wiki/Bailey-Borwein-Plouffe_formula
"""
from decimal import Decimal, getcontext


def bailey_borwein_plouffe(precision):
    """The precision argument is an integer that defines the length of Pi."""
    getcontext().prec = precision
    formula = sum(1 / Decimal(16) ** k * (Decimal(4) / (8 * k + 1) -
                                          Decimal(2) / (8 * k + 4) -
                                          Decimal(1) / (8 * k + 5) -
                                          Decimal(1) / (8 * k + 6))
                  for k in range(precision))
    return formula


def find_pi_decimals():
    decimal_places = int(input("Please enter how many decimal places you would like returned for Pi: "))
    while decimal_places > 1000:
            print("Sorry, cannot compute fractional part greater than 1,000.")
            decimal_places = int(input("Please enter how many decimal places you would like returned for Pi: "))
    # By adding 1 to decimal_places we account for '3', the integer part of Pi.
    return bailey_borwein_plouffe(decimal_places + 1)

print(find_pi_decimals())
