"""
Title: Mega Projects List - Count Vowels
Author: Mandeep Bhutani
Date: 01/31/2015
Problem: Enter a string and the program counts
the number of vowels in the text.
"""
result = str(input("Please enter text in order to count the number of vowels:"))

total = 0

for letter in result:
    if letter in "AEIOUaeiou":
        total += 1

if total > 1:  # In order to print correct grammer, prints a sentence based on the number of vowels.
    print("There were {} vowels found in your text." .format(total))
else:
    print("There was {} vowel found in your text." .format(total))
