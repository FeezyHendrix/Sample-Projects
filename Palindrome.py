"""
Project: Projects Repo - Check if Palindrome
Author: Mandeep Bhutani
Date: 1/30/2015

Problem: Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like “racecar”.

References: https://docs.python.org/2.3/whatsnew/section-slices.html
"""
def palindrome():
	givenword = str(raw_input("Please enter the word you would like to have checked:"))
	while not givenword.isalpha(): # Checks to make sure all characters are alpha characters
		print "Please enter a real word."
		givenword = str(raw_input("Please enter the word you would like to have checked:"))
	else:
		if givenword == givenword[::-1]: # An extended index slice determines if the word given matches its reverse
			print "Your word is a palindrome."
		else:
			print "Your word is not a palindrome."
palindrome()
