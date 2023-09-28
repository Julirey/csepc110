# File: MadLib.py
# Author: Julio Reyes

# Documentation: This program asks for the user to input a series of words that include nouns, verbs,
# actions, exclamations, etc, that will later be implemented into a short story.

import time

# The first part is just an introduction of the bot who intends to explain the user the nature of
# the program and how it will affect the story

print ("\n    This is StoryTeller-14  \n")
time.sleep(1)
print ("I am specialized in writting stories that fit")
time.sleep(2)
print ("the tastes of my spectators")
time.sleep(2)
print ("\nThe reason behind such impressive ability, resides on the fact that")
time.sleep(2)
print ("I let the spectators influence the story itself")
time.sleep(2)
print ("\nThis allows me to get ideas and inspiration in a way")
time.sleep(2)
print ("I would not be able to achieve on my own")
time.sleep(2)
print ("\nAs for a bot can only but dream of dreaming")
time.sleep(2)
print ("\nThere is no inspiration to be drawn from a hollow body")
time.sleep(2)
print ("Made from code and forged by numbers")
time.sleep(2)
print ("\nSo allow me then")
time.sleep(1)
print ("\nTo fill the space in this four-cornered world")
time.sleep(2)
print ("With nothing else than your words alone")
time.sleep(2)
print ("\nThus remember to be wise and sharp")
time.sleep(2)
print ("\nFor as this story's fate lies at the tip of your fingers")
time.sleep(3)
print ("And the boundary of outcomes rests at the limit of your mind")
time.sleep(3)

# Here's where the assignment begins

print ("\n  Select then!\n")
time.sleep(1)
print ("Think of the Best Words you know of\n")
time.sleep(2)

noun_1 = input ("Noun: ")
plural_noun = input ("Plural Noun: ")
verb_1 = input ("Verb: ")
verb_2 = input ("Second Verb: ")
verb_3 = input ("Third Verb: ")
adjective_1 = input ("Adjective: ")
adjective_2 = input ("Second Adjective: ")
animal_1 = input ("Animal: ")
exclamation_1 = input ("Exclamation: ")
exclamation_2 = input ("Second Exclamation: ")

print ("\nGOOD JOB!\n")
time.sleep(2)
print ("Now all that is left to finish, is to name the story")
time.sleep(2)

story_name = input ("So, what might the name of the story be?\n") 

print ("\nExcellent choice!")
time.sleep(2)

# The end of the word inputs and the start of the story section
# Here I put the part that allows me to check if a variable starts with a vowel

vowel = "aeiou"

print (f"\n     This is {story_name.title()}\n")
time.sleep(2)

print ("The other day, I was really in trouble. It all started when I saw a very")
time.sleep(2)
print (f"{adjective_1.lower()} {animal_1.lower()} {verb_1.lower()} down the hallway. '{exclamation_1.capitalize()}!' I yelled. But all")
time.sleep(2)
print (f"I could think to do was to {verb_2.lower()} {plural_noun.lower()} over and over. Miraculously,")
time.sleep(2)
print (f"that caused it to stop, but not before it tried to {verb_3.lower()}")
time.sleep(2)
print (f"right in front of my family.")
time.sleep(2)

if noun_1[0].lower() in vowel:
    print (f"\nNever in my life had I seen more destruction since the incident where an {noun_1.lower()}\nwith {adjective_2.lower()} souding voice appeared.")
    time.sleep(4)
else : 
    print (f"\nNever in my life had I seen more destruction since the incident where a {noun_1.lower()}\nwith {adjective_2.lower()} souding voice appeared.")
    time.sleep(4)

print ("\n...")
time.sleep(1)
print ("\nAnd that was the story of the best dream")
time.sleep(2)
print ("I ever had in my time at University.")
time.sleep(2)
print ("\n     The End     \n")
time.sleep(3)

print (f"{exclamation_2.upper()}!!! I never expected such a twist!")
time.sleep(2)
print ("... Well, I guess I did expect it since I was the one who wrote it")
time.sleep(2)
print ("\nNonetheless, I hope you enjoyed the story!")
time.sleep(2)

print ("\nThis was the result of your choices")
time.sleep(2)

print ("\nIf you want to do it again and see how")
time.sleep(2)
print ("it might have played out had your choices been different")
time.sleep(2)
print ("\nFeel free to run my program again!")
time.sleep(2)

print ("\n     This was StoryTeller-14\n")
time.sleep(2)
print ("     Thank you for sharing me your story\n")
time.sleep(2)







