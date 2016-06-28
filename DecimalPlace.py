"""
Project: Sample Project from Projects Repo
Author: Mandeep Bhutani
Date: 1/28/2015

Problem: Enter a number and have the program generate Pi up to
that many decimal places. Keep a limit to how far the program will go.
"""
import mpmath


def find_pi_decimal():
    result = int(input("Please enter how many decimal places you would like returned for Pi:"))
    mpmath.mp.dps = result
    while result > 1000:
            print("Sorry, cannot compute numbers greater than 1000.")
            result = int(input("Please enter how many decimal places you would like returned for Pi:"))
    else:
        # The result+2 slice is a trick to account for '3.', the first two characters of Pi.
        return str(mpmath.pi)[:result+2]
print(find_pi_decimal())
