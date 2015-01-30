"""
Project: Sample Project from Projects Repo - Pig Latin
Author: Mandeep Bhutani
Date: 1/29/2015

Problem:  Pig Latin is a game of alterations played on the English language game. 
To create the Pig Latin form of an English word the initial consonant sound is transposed
to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).

References: 
"""
oldword = str(raw_input("Please enter a word to be translated:"))
while not oldword.isalpha(): # Checks to make sure that the input word is a real word.
	print "Please enter a new word with alpha characters only."
	oldword = str(raw_input("Please enter a word to be translated:"))

else:
	# Prints a new word that is formed from slices of the input word.
	if oldword[0] not in 'aeiouAEIOU': # Checks input word to see if first letter is a consonant
		newword = oldword[1:len(oldword)] + oldword[0] + 'ay'
	else:
		newword = oldword + 'ay' # If the first letter is a vowel, then only the 'ay' ending is adding.
	print newword.capitalize()