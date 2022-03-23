#################################
#                               #
# Exercises 1 & 2 for Chapter 3 #
#                               #
#################################

###
#Fortune Cookie
#
# A program that simulates a fortune cookie. It displays one of five
# unique fortunes, at random, each time the program runs.
###
import random

fortunes = ["A child not embraced by the village will burn it down to feel its warmth.",
            "Experience is what you have left when everything else is gone.",
            "Don't pursue happiness. Create it.",
            "All things are difficult before they are easy.",
            "A ship in harbor is safe, but that's not why ships are built."]
print("\n" + random.choice(fortunes) + "\n")

###
#Coin Flip
#
# A program that flips a coin 100 times, and 
# then tells you the number of heads and tails.
###
#import random

flips = 100
heads = 0
tails= 0

for result in range(flips):
    result = (random.randrange(0, 2))
    if (result == 0):
        heads += 1
    else:
        tails += 1

print("Heads: ", heads)
print("Tails: ", tails)
