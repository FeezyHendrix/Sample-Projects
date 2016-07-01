"""
Project: Mega Projects List - Reverse a String
Author: Mandeep Bhutani
Date: 01/29/2015

Problem: Enter a string and the program will reverse it and print it out.
"""

word = str(input("Please enter the string you would like to reverse:"))
reversed_word = word[::-1] # This is an extended slice in the format of [start:stop:step]. The -1 step 
# reverses the order of its assignment.
print(reversed_word)
