"""
Title: Prime Check
Author: Mandeep Bhutani
Date: 3/2/15

Description: Code determines whether or not the input number is a prime number.
"""
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
