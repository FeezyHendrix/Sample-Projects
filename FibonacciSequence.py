"""
Project: Sample Project from Projects Repo - Fibonacci Sequence
Author: Mandeep Bhutani
Date: 1/28/2015

Problem: Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

References: http://en.wikipedia.org/wiki/Fibonacci_number
"""
a, b = 0, 1 # Setting the beginning of the Fibonnaci sequence to 0,1.
total = []
while a <= int(raw_input("Please enter how many terms you would like:")
    if a % 2 == 0: 
    	a, b = b, a+b  # Once a = 0 is added to the total, the variables' values are changed to find the next number in the series.
print total