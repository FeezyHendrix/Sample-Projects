"""
Title: Prime Check
Author: Mandeep Bhutani
Date: 3/2/15

Description: Code determines whether or not the input number is a prime number.
"""
from math import sqrt


def is_prime(n):
    for x in range(2, int(sqrt(n))):
        if n % x == 0:
            return False
    else:
        return True
