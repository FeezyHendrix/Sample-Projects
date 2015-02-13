"""
Title: Projects Repo - Coin Flip
Author: Mandeep Bhutani
Date: 2/13/2015
Problem: Simulate a coin flip. 
"""
import random # Module that will choose between heads or tails

count_heads = 0
count_tails = 0

while True: # While command loops until user no longer wishes to continue

    guess = random.choice([0,1]) # Chooses between 0 and 1
    play = str(raw_input("Would you like to flip a coin? Yes or No?"))

    if play.lower() != "yes":
        break

    if guess == 0:
        count_heads += 1
        print "Heads"
    else:
        count_tails += 1
        print "Tails"
    print "The coin has flipped %s Heads and %s Tails." % (count_heads, count_tails)
