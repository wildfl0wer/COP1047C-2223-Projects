"""
PSEUDOCODE:

-First guess: 100/2
--Yes or no?
--If no, proceed through the guessing loop.
--If yes, skip loop, print message, and end program.

While no continue Guessing Loop:
(Guessing Loop is inspired by bindary search.
The guess being searched for is in a list
that is generated each time after a guess is
incorrect with the range determined by the 
previous guess and user input.)

-Higher or lower?
--If higher:
        list_start = guess + 1
        step = int(((list_end - 1) - list_start) / 2)
        if (step == 0):
            step = 1
        list = range(list_start, list_end, step)
        middle = int(len(list) / 2)
        guess = (list[middle])
--Else:
        list_end = guess
        step = int((list_end - list_start) / 2)
        if (step == 0):
            step = 1
        list = range(list_start, list_end, step)
        middle = int(len(list) / 2)
        guess = (list[middle])
--Yes or No?
--If no, continue through the guessing loop. 
--If yes, break out of loop, print message, and end program.
"""

# Guess Your Number
#
# The user picks a random number between 1 and 100
# The computer tries to guess it and and asks
# the user if the guess is too high, too low
# or right on the money.


# sets the initial values
start = 1                # Start of range of numbers to guess from
end = 100                # End of range of numbers to guess from
list_start = start       # Start of list program guesses from
list_end = end + 1       # End of list program guesses from
guess = int(end / 2)     # Program's guess
tries = 1                # Number of tries so far
has_forgotten = False    # Flags if used forgets their number

print("\nHello... You don't know me... but I want to play a game.")
print("\n\tWelcome to 'Guess Your Number'!")
print("\nThink of a number between {} and {}.".format(start, end))
print("And I'll  try to guess it!\n")

# Program's first guess
print("Is your number {}?".format(guess))
reply = input("Press 'y' for yes or 'n' for no. ")

# Guessing loop
while (reply != 'y'):
    print("\nIs your number higher or lower?")
    position = input("Press 'h' for higher or 'l' for lower. ")

    if (position == 'h'):
        list_start = guess + 1
        step = int(((list_end - 1) - list_start) / 2)
        if (step == 0):
            step = 1
        list = range(list_start, list_end, step)
        middle = int(len(list) / 2)
        guess = (list[middle])

    else:
        list_end = guess
        step = int((list_end - list_start) / 2)
        if (step == 0):
            step = 1
        list = range(list_start, list_end, step)
        middle = int(len(list) / 2)
        guess = (list[middle])

    tries += 1
    print("\nIs your number {}?".format(guess))
    reply = input("Press 'y' for yes or 'n' for no. ")

    if (((guess == list_start) or (guess == list_end)) and (reply == 'n')):
        has_forgotten = True
        break

if (has_forgotten == True):
    print("\n\nAre you sure?\nI think you forgot your number!")

if (has_forgotten != True):
    print("\nI guessed it! Your number was {}!".format(guess))
    if (tries == 1):
        print("And it only took me", tries, "try!")
    else:
        print("And it only took me", tries, "tries!")

input("\n\nPress the enter key to exit.")
