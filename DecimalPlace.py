"""
Project: Sample Project from Projects Repo
Author: Mandeep Bhutani
Date: 1/28/2015

Problem: Enter a number and have the program generate PI up to
that many decimal places.
Keep a limit to how far the program will go.

References: https://docs.python.org/2/library/decimal.html
"""
import math  # Importing this module will give access math.pi
import decimal  # Importing this module will give access to decimal(),
# a optimized replacement of float()


def findnum():
    result = int(raw_input("Please enter how many decimal places you would like returned for Pi:"))
    while result > 50:
            print "Sorry, cannot compute numbers greater than 50."
            # The code below lets the user enter another number.
            result = int(raw_input("Please enter how many decimal places you would like returned for Pi:"))
    # The str() function turns math.pi into a string from a float.
    # The brackets indicate an index slice in order to return the
    # exact number of decimals that the user entered.
    # The result+2 is a trick to account for '3.', the first two characters.
    else:
        return str(decimal.Decimal(math.pi))[0:result+2]
print findnum()
