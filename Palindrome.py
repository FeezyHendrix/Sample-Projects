"""
Project: Sample Project from Projects Repo
Author: Mandeep Bhutani
Date: 1/30/2015

Problem: Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.

References: 
"""
def palindrome():
	givenword = str(raw_input("Please enter the word you would to have checked:"))
	while not givenword.isalpha(): # Checks to make sure all characters are alpha characters
		print "Please enter a real word."
		givenword = str(raw_input("Please enter the word you would to have checked:"))
	else:
		if givenword == givenword[::-1]: # Using an extended index to determine if the word given matches its reverse
			print "Your word is a palindrome."
		else:
			print "Your word is not a palindrome."
palindrome()