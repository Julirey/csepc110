# File: favoritecolorbot.py
# Author: Julio Reyes

# Documentation: This script features a bot that can display text, ask for inputs, and give different outputs
# on certain inputs. The bot's dialogue was designed to convey that it (the bot) has some human traits. 

import time

# I took liberty to assume that we are allowed to use functions that have yet to be taught for the sake
# of creativity.
# In this case, I utilized the sleep() function to add personality to what otherwise would be,
# in my eyes, just a lifeless output.


# I implemented the "Hello world" part of the lessons because it adds to the appeal of the bot 
# The "Favorite Color" assignment is still present in this script

print ("\n  Hello World!\n")
time.sleep(2)
print ("I am a bot")
time.sleep(2)
print ("You may call me C0-loR Bot")
time.sleep(2)


name_answer = input ("\nWould you tell me what your name is? [WRITE YOUR INPUT]\n")
#Try "yes" and "no" for different dialogue

if name_answer.lower() == "yes":
    print ("\nWonderful!")
    time.sleep(2)
    name_answer = input ("Then, what might this name be? [WRITE YOUR INPUT]\n")

if name_answer.lower() == "no":
    print ("\nOh...w-well that's a fine... it's ok if you don't want to tell me...\n")
    time.sleep(3)

else : 
    print ("\nThat's a beautiful name!... " + name_answer + ", very easy to pronounce I like it!\n")
    time.sleep(3)

print ("NOW!!! this wasn't the only thing I can do. No! No! For I am a sophisticated Bot!!!\n")
time.sleep(3)
print ("  Second Question!")
time.sleep(2)


color_answer = input ("\nWhat is your most FAVORITE color in the world? [WRITE YOUR INPUT]\n")
# Try "gray" and "blue" for different dialogue

if color_answer.lower() == "gray":
    print ("\nOh... sorry to hear that... seems machines are not the only one who can't see colors...\n")
    time.sleep(3)

if color_answer.lower() == "blue":
    print ("\nWHAT!!!! T-that's my Creator's favorite color too!\n")
    time.sleep(2)
 
print ("\nSo your favorite color is " + color_answer + "...")
time.sleep(2)
print ("I guess I have to say it\n")
time.sleep(2)
print ("It is very interesting! And it goes against my current information of you")
time.sleep(3)
print ("In my database, it says that your favorite color is 'Cosmic Latte'")
time.sleep(3)
print ("with an addendum from my Creator that says as follows:\n")
time.sleep(2)
print ("[Yes, yes it sounds fake but it's a real color, google it, you won't be dissapointed]\n")
time.sleep(3)
print ("I posses no information as to what 'google it' means")
time.sleep(2)
print ("but I am sure you know it\n")
time.sleep(3)

print ("\nAs of now [date:2023/01/06] this is the limit of my functions\n")
time.sleep(3)
print ("Thus I represent no reason to be active\n")
time.sleep(2)
print ("This was C0-loR Bot\n")
time.sleep(2)
print ("\n  Goodbye World...\n")
time.sleep(2)
if name_answer.lower() != "no": 
    print ("\n  Goodbye " + name_answer + "WhoLikes" + color_answer +"...\n")
    time.sleep(2)
else : 
    print ("\n  Goodbye PersonWhoDidNotWantToTellMeItsNameAndWhoLikes" + color_answer + "...\n")
    time.sleep(2)