"""
Project: Mega Projects List - Check if Palindrome
Author: Mandeep Bhutani
Date: 01/30/2015

Problem: Checks if the string entered by the user is a palindrome.
References: https://docs.python.org/2.3/whatsnew/section-slices.html
"""


def palindrome():
    word = str(input("Please enter the word you would like to have checked: "))
    while not word.isalpha():
        print("Please enter a real word.")
        word = str(input("Please enter the word you would like to have checked: "))
    if word == word[::-1]: # An extended index slice determines if the word given matches its reverse.
        return "Your word is a palindrome."
    else:
        return "Your word is not a palindrome."

print(palindrome())
