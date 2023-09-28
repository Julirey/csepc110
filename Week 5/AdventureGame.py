# File: AdventureGame.py
# Author: Julio Reyes

# Documentation: This is a basic choice-driven, text-based, adventure game, which as the description implies
# presents the user with multiple choices that affect the outcome of how the story progresses, and it is structured
# upon conditions and if-else statements.

# -Milestone version-

import time 

print ("\n        The Cave     \n")
time.sleep(2)

# Since it is a game I thought it would fit better to have the user
# decide when to continue to the next text prompt
input ("[You can press ENTER to advance text]")

input ("[Choices will be displayed in ALL CAPS]")
print ()

input ("You find yourself in a dark space, not much to be said about the view")
input ("It is cold")
input ("The ceiling is close")
input ("You try to call for help...")
input ("... and nobody responds")
print ()

input ("The sound of waterdrops splashing in the distance alerts you")
input ("You notice you are thirsty")
input ("But you don't know where you are nor how to get out")
input ("Looking to hydrate yourself might be a good idea in the mean time")
print ()

input ("You walk through the dark tunnel to reach the source of water")
input ("The ground feels hard and uneven")
input ("You are wearing a pair of hiking boots with spiky soles which prevents you from slipping")
input ("You don't remember why you know that")
print ()

input ("Upon getting closer to the water source")
input ("An impressive view surrounds you")
input ("The apparent cave welcomes you in a new chamber")
input ("Spacious and open, with rays of light coming from holes in the ceiling too high to climb to")
print ()

input ("Once your eyes adapted to the light")
input ("It is revealed to you that the water source was in fact an underground river")
input ("Originating from a waterfall, which then descents down deeper into the cave")
print ()

input ("After drinking a bit of water")
input ("The perfect chance to do something had come")

choice1 = input ("You think of either DESCENT downstream, STAY where you are and wait\nor RETURN to where you first started.\nWhat do you do? ")
print ()

if choice1.upper() == "DESCENT":
    input ("Descending appears to be the better choice")
    input ("After all, it is common knowledge that downstream rivers tend to guide you to civilization")
    input ("Or at least so used to say Bernard...")
    print ()

    input ("Another involuntary thought crossed your mind")
    input ("This time it was a person's name")
    input ("... 'Bernard'... ")
    input ("who was he?" )
    print ()

elif choice1.upper() == "STAY":
    input ("Believing people might come to find you")
    input ("You conclude that the safest option would be to stay")
    print ()
    input ("Despite your determination, this proved to be not as safe as you thought")
    input ("The hours passed")
    input ("No sign of life to be found other than the bugs on the walls")
    input ("Although thirst wasn't a concern anymore")
    input ("You didn't know how much you would last with nothing to eat")
    input ("For now you decide to fall asleep to damp the hunger")
    print ()

    input ("The sun rays that reach the dephs of the cavern shine as the morning draws closer")
    input ("The light wakes up and the first thing you notice is that the river is gone")



elif choice1.upper() == "RETURN":
    input ("For as much as you would like to satiate your thirst")
    input ("You realize this could be too convenient to be true")
    input ("Maybe some sort of allucination")
    print ()
    input ("Either way, you understand that it might be sensible to turn back on your tracks")
    input ("And discover how you ended up in this situation in the first place")
    input ("The water can wait...")

else:
    input ("It seems the tiredness has caught up to you")
    input (f"As for some reason you thought to {choice1}")
    print ()
    input ("You drink more water just in case")
    print ()
    input ("This time the water tastes different")
    input ("Your vision blurs")
    input ("The world spins")
    input ("And the ground that once supported your feet now seemed to be gone...")
    print ()

    input ("You wake up to the sight of a group of grey men surrounding you")
    input ("It seems you were poisoned")

  
    