"""
Project: Sample Project from Projects Repo - Reverse a String
Author: Mandeep Bhutani
Date: 1/29/2015

Problem: Enter a string and the program will reverse it and print it out.

References: https://docs.python.org/2.3/whatsnew/section-slices.html
"""

oldstring = str(raw_input("Please enter the string you would like to reverse:"))
newstring = oldstring[::-1] # This is an extended slice in the format of [start:stop:step]. The -1 step 
# reverses the order of its assignment.
print newstring