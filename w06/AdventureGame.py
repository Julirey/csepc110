# File: AdventureGame.py
# Author: Julio Reyes

# Documentation: This is a basic choice-driven, text-based, adventure game, which as the description implies
# presents the user with multiple choices that affect the outcome of how the story progresses, and it is structured
# upon conditions and if-else statements.

# -Full version-

import time 

print ("\n        The Cave     \n")
time.sleep(1)

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
print ()

choice1 = input ("You think of either DESCENT downstream, STAY where you are and wait\nWhat do you do? ")
print ()

if choice1.upper() == "DESCENT":
    input ("Descending appears to be the better choice")
    input ("After all, it is common knowledge that downstream rivers tend to guide you to civilization")
    print ()
    input ("Or at least so used to say Bernard...")
    print ()

    input ("Another involuntary thought had crossed your mind")
    input ("This time it was a person's name")
    input ("... 'Bernard'... ")
    input ("Who was he?" )
    print ()

    input ("As you descended further down the tunnel")
    input ("A new dilemma presented itself")
    input ("The pathway divided into two separate paths")
    print ()

    # Defining this point as a function allows me to run it again in case the user inputs an invalid choice
    def choicepoint1a():
        choice1a = input ("Where do you want to go, LEFT or RIGHT?\n")
        print ()

        if choice1a.upper() == "LEFT":
            input ("You decide to take the path on the left")
            input ("There's is not much change to be said about the tunnel")
            input ("The flow of water is still at you feet")
            input ("And if anything")
            input ("The tunnel only seems to be getting longer")
            print ()

            input ("After a few minutes of walking")
            input ("The echo of your steps starts get louder")
            input ("You are getting closer to something")
            print ()

            input ("As you are thinking this")
            input ("You fail to realize that the path ahead was going to end")
            input ("All that there was left after that was a unprecedented fall")
            input ("One that would have no end")
            print ()

            input ("After taking your last possible step on the path")
            print ()
            input ("You fell")
            print ()

            input ("Panicked and confused")
            input ("You started screaming in fear")
            input ("Cool air rushed to your face as you fell")
            print ()

            input ("Even surrounded by nothing but darkness")
            input ("The instinct of closing your eyes took over")
            input ("You wanted for this to end")
            input ("You wished to be somewhere else")
            input ("You needed help")
            print ()

            input ("'EVAN!'")
            print ()

            input ("A voice called your name")
            input ("In desbelief you opened your eyes")
            input ("And you saw a light")
            input ("Brighter than anything you've ever seen in your life")
            print()

            input ("'EVAN! GRAB MY HAND!")
            print ()

            input ("As the voice said that, a hand appeared in front of you")
            print ()
            input ("The moment has come Evan")
            print ()
            input ("Will you let him help you this time?")
            input ("Or will it become another one of your regrets")
            print ()

            choice1a1 = input ("GRAB his hand or CLOSE your eyes")
            print ()

            if choice1a1.upper() == "GRAB":
                input ("You grabbed his hand")
                input ("It was warm")
                input ("And its grasp was gentle")
                print ()

                input ("It felt save")
                print ()

                input ("A moment later")
                input ("You were back in your house")
                input ("You were in bed")
                input ("You heard your wife calling you to come eat breakfast")
                print ()

                input ("The Cave was a dream")
                print ()
                print ("     The End")

            elif choice1a1.upper() == "CLOSE": 
                input ("You closed your eyes")
                input ("These were your last moments")
                input ("There was no reason to bother yourself with allucinations")
                input ("A part of you already knew it was meant to be")
                input ("So why fight it?")
                input ("Why not just let yourself live it")
                print ()

                input ("Goodbye")
                print ()

                print ("     The End\n")

            else :
                input ("You failed to act in time")
                input ("Nor did you have any time left anyways")
                print ()
                input ("Perhaps typing better would bring you a better ending")

        elif choice1a.upper () == "RIGHT":
            input ("You decide to take the path on the right")
            input ("The path showed some differences")
            input ("Now it seemed to be going a little bit up")
            input ("And there was no more water on your feet")
            print ()

            input ("Slowly the path started to become more of a ramp")
            input ("Your legs grow tired as you climb")
            input ("But it was ok")
            print ()

            input ("You could see an exit")
            print ()

            input ("Tired")
            input ("Feeling pain on your hands and legs")
            input ("You finally managed to get out of the cave")
            print ()

            input ("The air was fresh")
            input ("The sky was clear")
            input ("And you've never felt better in your life")
            print ()

            input ("As you wonder how you are going to get back to civilization")
            input ("You see a helicopter in the distance")
            input ("Thinking of a way to call its attention")
            print ()
            
            def choicepoint1a2():
                choice1a2 = input ("Do you believe climbing a TREE or making a FLAG would be better?\n")
                print ()

                if choice1a2.upper() == "TREE":
                    input ("Climbing a tree should make yourself as visible as possible")
                    input ("You start climbing with the little energy you got left")
                    input ("Almost there, you are only a few branches from the top")
                    print()

                    input ("You slipped")
                    print ()

                    input ("As you fell, it was enough time for you to flip over an face the ground")
                    input ("You realized the height was too great")
                    input ("And that you were definately going to land on your head")
                    print ()

                    input ("This was it")
                    print ()

                    input ("This was the end")
                    print ()

                    print ("     The Cave\n")

                elif choice1a2.upper() == "FLAG":
                    input ("Making a flag would call a lot of attention")
                    input ("You rip your T-shirt and wrap it around a stick")
                    input ("You start to wave it as hard as you can")
                    print ()

                    input ("After a few minutes of intense effort") 
                    input ("A miracle happens")
                    print ()

                    input ("The helicopter started coming to your direction")
                    input ("And the lights were pointing to you")
                    print ()

                    input ("They had noticed you")
                    print ()

                    input ("You were saved")
                    print()

                    input ("     The End\n")


                else :
                    print ("No, that is not a good idea")
                    choicepoint1a2()

            choicepoint1a2()


        else :
            print ("It is only possible to go either LEFT or RIGHT")
            choicepoint1a()  
            
    choicepoint1a()        

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
    print ()

    input ("A new thing appeared in its place")
    input ("A staircase that led to what seemed to be a tomb")
    input ("There was some text on top of it")

    def choicepoint1b():
        choice1b = input ("You debated whether you should READ it or just BREAK the tomb open\n")
        print ()

        if choice1b.upper == "READ":
            input ("As you decipher the letters")
            input ("It appears to be some kind of puzzle")
            input ("In short, it tells you that the tomb has two openings")
            print ()

            input ("One leads to fortune")
            input ("The other leads to death")
            print ()

            input ("The part that explains which one is which has been damaged so you can't read it")
            input ("But you can see that each side has different drawings")
            print ()

            def choicepoint1b1():
                choice1b1 = input ("Do you open the tomb from the MOON side or the SUN side?\n")

                if choice1b1.upper() == "MOON":
                    input ("You chose eto open the Moon side")
                    input ("To your surprise")
                    input ("This side contained jewels and fortune")
                    input ("Worth so much you can't think of ways to spend it")
                    print ()

                    input ("You found the treasure")
                    print ()

                    input ("You conquered The Cave")
                    print ()

                    print ("     The End")

                elif choice1b1.upper == "SUN":
                    input ("You chose to open the Sun side")
                    input ("Inmediately after opening it")
                    input ("A swarm of spiders started crawling out of it")
                    print ()

                    input ("You were too slow to react and one already managed to bite you")
                    input ("It paralyzed you instantly")
                    print ()

                    input ("This was the end of your journey")
                    print ()

                    print ("     The Cave")

                else : 
                    input ("That is not a valid option")
                    choicepoint1b1()
            choicepoint1b1()
            
        elif choice1b.upper == "BREAK":
            input ("You decide to break the tomb")
            input ("But to do that you first need a tool")

            def choicepoint1b2():
                choice1b2 = input ("What do you use a ROCK, a STICK, or your BOOTS?\n")
                print ()

                if choice1b2.upper() == "ROCK":
                    input ("You chose to use a rock")
                    input ("Nothing much happened")
                    input ("The rock broke and now you are too tired to try anything else")
                    input ("Without any water left you face dehydration")
                    print ()

                    input ("You don't know how much time you have left")
                    input ("An yet, you still believe that if you had a little more time")
                    input ("You could have achieved something great")
                    print ()

                    print ("     The Cave")

                elif choice1b2.upper() == "STICK": 
                    input ("You chose to use a stick")
                    input ("You look for a side that has a dent")
                    input ("You insert the stick and use it as a lever to pry open the tomb")
                    print ()

                    input ("The tomb was opened")
                    input ("And inside was something you could have never imagined")
                    print ()

                    input ("There was statues of golden spiders")
                    input ("But something was weird about them")
                    print ()

                    input ("They could move")
                    print ()

                    input ("Against all logic, you had found what was probably")
                    input ("A mystic legend")
                    input ("Something straight out of a movie")
                    print ()

                    input ("And that's were it dawns on you")
                    input ("This is the reason you came to this cave")
                    input ("To prove the acient legend")
                    input ("You had completed your promise")
                    print ()

                    input ("     The End")

                elif choice1b2.upper() == "BOOTS":
                    input ("You chose to use your boots")
                    input ("You hurt your legs and now it seems it is impossible to do anything")
                    print ()

                    input ("As your finals thoughts come,")
                    input ("You wish you at least had the opportunity to try more things")

                    print ("     The Cave")

                else :
                    input ("I don't think that would be as effective")
                    choicepoint1b2()
            
            choicepoint1b2()
        else :
            input ("I wouldn't take that option")
            choicepoint1b()

    choicepoint1b()

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

    input ("You wake up to the sight of a group of men surrounding you")
    input ("The amount of light pouring down to your face makes it hard to see")
    input ("Sunrays rest upon your skin giving you warmth")
    input ("You slowly realize that you are not in a cave anymore")
    print ()

    input ("It seems you were poisoned...")
    input ("But these men around you didn't cause it")
    input ("In fact, it appears they are the ones that got you out")
    input ("They brought you food, a change of clothes")
    print()

    input ("One of them was holding what looked to be a picture")
    input ("It showed 2 people in it")
    input ("You recognized the first person")
    input ("It was a friend, you can't seem to remember his name")
    input ("The second picture showed a face you would never forget")
    print ()
    input ("It was You")
    print ()
    input ("As your confusion started to set in")
    input ("A man dressed in sharp clothes approaches you")
    input ("He says-")
    print ()

    input ("'Welcome back, Evan'")
    input ("'We had been searching you for 2 weeks now'")
    input ("'We thought we would never find you...'")
    input ("'But I believed,'") 
    input ("'I believed that you wouldn't give up'")
    input ("'You had to be somewhere'")
    input ("'I'm glad I found you")
    print ()
    input ("'We can go home now'")
    print ()
    input ("'You are safe'")
    print ()
    print ("     The End\n")
    time.sleep(1)
    print ("'... but where's Bernard?'")
    time.sleep(1)
    print ()
    print ("     The End?\n")
  
    