import random

count_heads = 0
count_tails = 0

while True:
    guess = random.choice([0,1])
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
