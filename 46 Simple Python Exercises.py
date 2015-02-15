"""
Title: 46 Simple Python Exercises
Author: Mandeep Bhutani
Date: 2/14/2015

Description: A collection of exercises taken from
http://www.ling.gu.se/~lager/python_exercises.html
"""

# Define a function max that takes two arguments and
# returns the maximum of the two.


def max_func(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "They are equal."


# Define a function max_of_three that returns the
# maximum of three arguments.


def max_of_three(x, y, z):
    some_max = x
    if y > x:
        some_max = y
    elif z > y:
        some_max = z
    return some_max


# Write a function that takes a character (i.e. a string of length 1)
# and returns True if it is a vowel, False otherwise.

def vowel_finder(x):
    if str(x) in "aeiouAEIOU":
        return True
    else:
        return False


# Write a function translate() that will translate a text into
# robber's language. That is, double every consonant and place an
# occurrence of "o" in between. For example, translate("this is fun")
# should return the string "tothohisos isos fofunon".

def translate(string):
    new_string = ""
    consonants = "bcdfghjklmnpqrstvwxyz"
    for letters in string:
        if letters in consonants:
            new_string += letters + "o" + letters
        else:
            new_string += letters
    return new_string


# Define a function multiply() that multiplies all the numbers
# in a list of numbers. For example, multiply([1, 2, 3, 4]) should return 24.

def multiply(some_list):
    new_list = 1
    for x in some_list:
        new_list *= x
    return new_list


# Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am test") should return the string "tset ma I".

def reverse(words):
    new_words = words[::-1]
    return new_words


# Define a function is_palindrome() that recognizes palindromes.
# For example, is_palindrome("radar") should return True.

def is_palindrome(word):
    new_word = word[::-1]
    if new_word == word:
        return True
    else:
        return False


# Define a function overlapping() that takes two lists and returns
# True if they have at least one member in common, False otherwise.

def overlapping(first, second):
    if [x for x in first if x in second]:
        return True
    else:
        return False


# Write a function find_longest_word() that takes a list of words
# and returns the length of the longest one.

def find_longest_word(a_list):
    new_list = []
    for words in a_list:
        new_list.append(len(words))
    return max(new_list)


# Write a function filter_long_words() that takes a list of words and an
# integer n and returns the list of words that are longer than n.

def filter_long_words(the_list, n):
    if find_longest_word(the_list) > n:
        return find_longest_word(the_list)


# Write a version of a palindrome recognizer that also accepts phrase
# palindromes such as "Was it a rat I saw?",

def isit_palindrome(the_string):
    import string
    new_string = the_string.replace(" ", "")
    newer_string = new_string.translate(None, string.punctuation).lower()
    newest_string = newer_string[::-1]
    if newest_string == newer_string:
        return True
    else:
        return False


# A pangram is a sentence that contains all the letters of the English alphabet
# at least once, for example: "The quick brown fox jumps over the lazy dog."
# Write a function to check a sentence to see if it is a pangram.

def pangram(input_sentence):
    consonants = "abcdefghijklmnopqrstuvwxyz"
    sentence = input_sentence.lower()
    new_sentence = ""
    for char in set(sentence):
        if char in consonants:
            new_sentence += char
    newer_sentence = "".join(sorted(new_sentence))
    if newer_sentence == consonants:
        return True
    else:
        return False


#  Write a Python program capable of generating all the verses of the song,
# "99 Bottles of Beer"

def bottles(n):
    while n > 0:
        print "There are %s bottles of beer on the wall, \
        %s bottles of beer." % (n, n)
        print "Take one down, pass it around %s bottles \
        of beer on the wall." % (n - 1)
        n -= 1
