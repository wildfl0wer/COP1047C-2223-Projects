# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money.
# The player has a limited number of guesses. 
# If the player fails to guess in time,
# the program displays an appropriately chastising message.

import random

# sets the initial values
the_number = random.randint(1, 100)
tries = 1                              # Number of tries so far
max_tries = 6                         # Max number of tries
remaining_tries = max_tries - 1        # Number of tries left before game ends

print("\nHELLO. DO YOU WANT TO PLAY A GAME?")
print("\n\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in", max_tries, "or less guesses.\n")
print("\tOR ELSE...\n")

# User's first guess
guess = int(input("Take a guess: "))

# guessing loop
while guess != the_number:
    if (tries < max_tries):
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")

        if (remaining_tries > 1):
            print("You have", remaining_tries, "guesses left.\n")
        else:
            print("ONLY", remaining_tries, "GUESS LEFT!!!\n")

        guess = int(input("Take a guess: "))
        tries += 1
        remaining_tries -= 1

    else:
        print("\nWRONG! THE NUMBER WAS", the_number)
        print("YOU. HAVE. FAILED.")
        break

if (guess == the_number):
    print("You guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!")

input("\n\nPress the enter key to exit.")