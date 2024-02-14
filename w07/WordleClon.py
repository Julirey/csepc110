# File: WordleClon.py
# Author: Julio Reyes

# Documentation: This is a basic word guessing game that selects a word, and prompts the user to input the guess.
# Depending on the things like the characters used, the order of the characters, and the number, the program will 
# output useful information to help with the guess .

# -Milestone version-


play_again = "yes"

print ("    Welcome to the word guessing game")
print ()
print ("- A random word has already been selected -")
print ()

while play_again.lower() == "yes":

    secret_word = "lettuce"
    guess = 0
    attempts = 1

    guess = (input("What is your guess? "))

    while guess != secret_word:
        print ("Incorrect")
        print ()
        guess = (input("What is your guess? "))
        attempts = attempts + 1

    print("Correct!")
    print()
    print(f"Number of attempts: {attempts}")
    print()
    play_again = input("Do you want to play again [Yes or No]? ")
    print()
