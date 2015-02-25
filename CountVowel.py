"""
Title: Projects Repo - Count Vowels
Author: Mandeep Bhutani
Date: 1/31/2015
Problem: Enter a string and the program counts
the number of vowels in the text.
"""
result = str(raw_input("Please enter text in order to \
    count the number of vowels:"))
total = 0
for x in result:
    if x in "AEIOUaeiou":  # Python allows for the iteration of
        # strings using the word 'in'.
        total += 1  # For each vowel found, add 1 to the total.
if total > 1:  # In order to print correct grammer,
            # prints a sentence based on the number of vowels.
    print "There were %s vowels found in your text." % total
else:
    print "There was %s vowel found in your text." % total
