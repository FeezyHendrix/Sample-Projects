"""
Project: Mega Project List - Pig Latin
Author: Mandeep Bhutani
Date: 1/29/2015

Problem:  Pig Latin is a game of alterations played on the English language game. 
To create the Pig Latin form of an English word the initial consonant sound is transposed
to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).
"""
word = str(input("Please enter a word to be translated: "))

while not word.isalpha():
    word = str(input("Please enter a new word with alpha characters only: "))

if word[0] not in 'aeiouAEIOU':  # Checks input word to see if first letter is a consonant
    pig_latin_word = word[1:len(word)] + word[0] + 'ay'
else:
    pig_latin_word = word + 'ay'  # If the first letter is a vowel, then only the 'ay' ending is adding.

print(pig_latin_word.capitalize())
