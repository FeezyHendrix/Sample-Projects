"""
Project: Mega Projects List - FizzBuzz
Author: Mandeep Bhutani
Date: 01/29/2015

Problem: Write a program that prints the numbers from 1 to 100. 
For multiples of three print 'Fizz' instead of the number and for the multiples of five print 'Buzz'.
For numbers which are multiples of both three and five print 'FizzBuzz'.
"""
for number in range(1, 101):
    if number % 3 == 0 and number % 5 != 0: # If x is a multiple of 3, but not a multiple of 5.
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0: # If x is a multiple of 5, but not a multiple of 3.
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0: # If x is a multiple of both 3 and 5.
        print("FizzBuzz")
    else:
        print(number)
