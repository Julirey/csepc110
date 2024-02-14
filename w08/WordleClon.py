# File: WordleClon.py
# Author: Julio Reyes

# Documentation: This is a basic word guessing game that selects a word, and prompts the user to input the guess.
# Depending on the things like the characters used, the order of the characters, and the number, the program will 
# output useful information to help with the guess .

# -Full version-

import random

print ()
print ("    Welcome to the word guessing game")
print ()
print ("A random word will be selected at the start of each round")
print ("This game will give you a hint of the secret word at")
print ("the beginning, and also after each guess attempt")
print ()
input ("[PRESS ENTER TO CONTINUE]")
print ()
print ("The hint is a rendering of the letters in the guess according to the following guidelines:")
print ("   - An underscore _ indicates that the letter was not present in the secret word.")
print ("   - A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.")
print ("   - An uppercase letter indicates that the letter was present at that exact spot in the secret word. ")
print ()
input ("[PRESS ENTER TO START]")
print ()
print ("      - LET'S START -")
print ()

play_again = "yes"

while play_again.lower() == "yes":

    list_of_words = ["lettuce", "ketchup", "hotdog", "mustard", "cheese", "mayonnaise", "pickle"]

    secret_word = random.choice(list_of_words)
    secret_word_letter_count = len(secret_word)

    guess = ""
    attempts = 1

    print ("Your hint is: ", end="")
    for i in range(secret_word_letter_count):
        print ("_ ", end="")
    print ()    

    guess_prompt = "What is your guess?"
    guess = (input(f"{guess_prompt} "))
    guess_letter_count = len(guess)
    print ()

    while guess_letter_count != secret_word_letter_count:
        print ("That is not the right amount of letters")
        print (f"Your guess should be {secret_word_letter_count} letters long")
        print ()
        guess = (input(f"{guess_prompt} "))
        guess_letter_count = len(guess)
        print ()

    while guess.lower() != secret_word.lower():
         print ("Your hint is: ", end="")

         for position, letter in enumerate(guess.lower()):

            if letter.lower() == secret_word.lower()[position]:
                print (f"{letter.upper()} ", end="")
            
            elif letter.lower() in secret_word.lower():
                print (f"{letter.lower()} ", end="")
            
            else:
                print ("_ ", end="")

         print ()     
         guess = (input(f"{guess_prompt} "))
         attempts = attempts + 1
         print ()

    print ("Correct!")
    print (f"Number of attempts: {attempts}")
    print ()
    play_again = input("Do you want to play again [Yes or No]? ")
    print ()
