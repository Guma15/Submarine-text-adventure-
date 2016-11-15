#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is the main file for the text adventure. It contains all the rooms, items
objects and everything else that makes the game function. The game is accessed
from the Adventure.py file.
"""

import random

def bridge(command):
    """
    the bridge room and its command responses.
    """
    
    if command == "west":
        print(">You went west through the door."
              "\n>You are now in the lower corridor."
              "\n>There is a ladder to the north that leads to the upper corridor."
              "\n>To the west is the door to the Engine room."
              "\n>To the east is the door to the bridge.")

    elif command == "east":
        print(">To the east is the bridge window showing the outside ocean."
              "\n>It is currently pitch black, however you can see some bioluminescent"
              " creatures in the distant."
              "\n>Nothing else of interest is in this direction.")
        
    elif command == "north":
        print(">To the north you see the Captain looking out the window smoking a pipe."
              "\n>The captain is probably wondering when you will deliver the results."
              "\n>Nothing else of interest is in this direction.")
        
    elif command == "south":
        print(">To the south is a desk with a few drawers and piles of papers on top."
              "\n>On the wall is a map of the pacific ocean."
              "\n>Nothing else of interst is in this direction.")
        
    elif command == "inspect":
        print(">You inspect the bridge."
              "\n>In the south area of the room is a desk."
              "\n>The captain is the standing in the north area of the room."
              "\n>In the east area of the room is main window, showing the ocean."
              "\n>In the west area of the room is the door to the lower corridor.")
        
    elif command == "clue":
        print("Try opening the desk.")
        
    elif command == "open":
        print(">You open the first drawer."
              "\n>There's a manual for the engine here. It might be useful!"
              "\n>You pick up the manual.")
    
    elif command == "move":
        print(">I don't see the point in moving that, besides it looks heavy.")
        
    elif command == "use":
        print(">You sit down at the desk pretending to do paper work."
              "\n>The captain gives you a dissaproving look."
              "\n>You stop using the desk and get back to getting the report.")
        
    elif command == "turn":
        print(">You try to turn the desk."
              "\n>The captain is giving you a dissaproving look."
              "\n>You turn back the desk as it was.")
        
    elif command == "desk":
        print(">The desk is made of wood."
              "\n>There are a few drawers."
              "\n>Maybe there's something intersting in them?"
              "\n>There are piles of papers on top of the desk.")
        
    elif command == "final":
        print(">You walk up to the captain with the lab results."
              "\n>The captain looks pleased."
              "\n>He takes a little while reading through the results."
              "\n>He then says: Good job! The results is telling us that there's a"
              " greater source of the material located at the bottom of the Marianna"
              " Trench."
              "\n>Set a heading for the trench! We're going deeper!")
        print("\n\n***This is all for this adventure, you have finished the game!***"
              "\n\n>Press any key to end the game.")
        input()
       
        
        
def corridorOne(command):
    """
    the lower corridor room and its command responses.
    """
    
    if command == "west":
        print(">You went west through the door."
              "\n>You are now in the engine room."
              "\n>The engine for the submarine is taking up most of the north" 
              "end of the room."
              "\n>There's a control panel at the south end of the room."
              "\n>To the east is the door to the lower corridor.")
        
    elif command == "east":
        print(">You went east through the door."
              "\n>You are now on the bridge."
              "\n>The captain is waiting in the north area of the room."
              "\n>To the west is the door to the lower corridor.")
        
    elif command == "north":
        print("You went up the ladder."
              "\n>You are now in the upper corridor."
              "\n>To the north is the door to the lab."
              "\n>To the east is the door to the meeting room."
              "\n>To the west is the door to the living quarters"
              "\n>To the south is the ladder down to the lower corridor.")
        
    elif command == "south":
        print("There's nothing of interest here.")
        
    elif command == "inspect":
        print(">You are in the lower corridor."
              "\n>There is a ladder to the north that leads to the upper corridor."
              "\n>To the west is the door to the Engine room."
              "\n>To the east is the door to the bridge.")
        
    elif command == "clue":
        print("Get a wrench to open the hatch.")
        
    elif command == "open":
        print(">You try to open the hatch."
              "\n>It wont budge!"
              "\n>I don't think I can open it with my bare hands."
              "\n>I think I need some kind of tool.")
        
    elif command == "move":
        print(">I don't think I can move this.")
        
    elif command == "use":
        print(">How would I use a hatch? Besides opening it.")
        
    elif command == "turn":
        print(">There's nothing I can turn here")
        
    elif command == "hatch":
        print(">You look at the hatch."
              "\n>It looks very sturdy, the screw handle seem to be missing."
              "\n>I would probably need somekind of tool to open it.")


def engine(command):
    """
    The engine room and its command responses.
    """
    
    if command == "west":
        print(">You try to go west."
              "\n>There's a steam cloud blocking the way."
              "\n>The steam is leaking out of a pipe connected to the engine.")
        
    elif command == "east":
        print(">You went east through the door."
              "\n>You are now in the lower corridor."
              "\n>There is a ladder to the north that leads to the upper corridor."
              "\n>To the west is the door to the Engine room."
              "\n>To the east is the door to the bridge.")
        
    elif command == "north":
        print(">To the north is the engine for the submarine."
              "\n>You've heard that there have been a few problems with it recently."
              "\n>The control panel for the engine is behind you in the south end.")
        
    elif command == "south":
        print("To the south is the control panel for the engine."
              "\n>Control panel seem to be old and well used."
              "\n>There are three valves on the panel that seem important.")
        
    elif command == "panel":
        print(">You approach the control panel at the south end of the room.")
        theResult = False
        theResult = valveGame()
        return theResult
        
    elif command == "inspect":
        print(">You inspect the engine room."
              "\n>The engine for the submarine is taking up most of the north end of the room."
              "\n>There's a control panel at the south end of the room."
              "\n>To the east is the door to the lower corridor.")
        
    elif command == "clue":
        print(">Use the manual from the bridge.")
        
    elif command == "use":
        print(">There doesn't seem to be anything I can use on the engine.")
        
    elif command == "open":
        print(">I don't think I should do that. I might break something.")
        
    elif command == "move":
        print(">I don't think I can move this.")
        
    elif command == "turn":
        print(">I don't think I can turn this.")
        
    elif command == "engine":
        print(">You look at the engine."
              "\n>The engine looks pretty complicated. yet old.")
        
    elif command == "control":
        print(">You look at the control panel."
              "\n>It looks very basic. It has three valves on it.")
        
#Valve puzzle for engine room.
def valveGame():
    """
    Valve game
    """
    valveTurns = 0
    valveOne = 0
    valveTwo = 0
    valveThree = 0
    
    print(">The control panel have three valves on it that seem to control the steam output.")
    while True:
        print(">There's valve 1, valve 2 and valve 3.\n"
              "\n***Input exit to quit.***\n")
        valveInput = str(input("Which valve should I turn?\n-->"))
        valveTurns = valveTurns + 1
        
        if valveInput == "exit":
            print(">You leave the control panel for now.")
            break
        
        elif valveInput == "turn valve 1" or valveInput == "1":
            print("\n>You turn valve 1")
            valveOne = valveOne + 1
            
        elif valveInput == "turn valve 2" or valveInput == "2":
            print("\n>You turn valve 2")
            valveTwo = valveTwo + 1
            
        elif valveInput == "turn valve 3" or valveInput == "3":
            print("\n>You turn valve 3")
            valveThree = valveThree + 1
            
        else:
            print(">What do you mean \"" + str(valveInput) + "\". I need to turn"
                  " the valves.")
            valveTurns = valveTurns - 1
            
        if valveOne == 2 and valveTwo == 1 and valveThree == 1:
            print(">The engine behind you makes a calming sound as if it stabalized."
                  "\n>The pipe that was giving off steam resides revealing a wrench"
                  " on the floor in the west end of the room.")
            return True
        
        if valveTurns >= 4:
            print(">The engine behind you makes a fizzing sound and all the valves"
                  " reset its positions."
                  "\n>I don't think that was the right combination.")
            valveOne = 0
            valveThree = 0
            valveTwo = 0
            valveTurns = 0
        
    
def corridorTwo(command):
    """
    The upper corridor and all command responses.
    """
    
    if command == "west":
        print(">You go through the door to the west."
              "\n>You are now in the living quarters."
              "\n>To the west is a small window and a few bunkbeds."
              "\n>To the south is another set of bunk beds."
              "\n>To the north is a table and some chairs. There's also a young"
              " blond girl sitting on one of the chairs. It's Lily!")
        
    elif command == "east":
        print(">You try to go through the door to the east to the meeting room."
              "\n>The door seem to be locked with a key."
              "\n>Maybe there's a key somewhere else?")
        
    elif command == "north":
        print(">You try to go through the door to the north to the lab."
              "\n>The door is locked and seem to require a keycode to open."
              "\n>What was the keycode again? Maybe it's written down somewhere?")
        
    elif command == "south":
        print(">You went south down the ladder."
              "\n>You are now in the lower corridor."
              "\n>There is a ladder to the north that leads to the upper corridor."
              "\n>To the west is the door to the Engine room."
              "\n>To the east is the door to the bridge.")
        
    elif command == "inspect":
        print(">You are in the upper corridor."
              "\n>To the north is the door to the lab."
              "\n>There's a keypad next to the lab door."
              "\n>To the east is the door to the meeting room."
              "\n>There's a keyhole on the door to the meeting room."
              "\n>To the west is the door to the living quarters"
              "\n>To the south is the ladder down to the lower corridor.")
        
    elif command == "clue":
        print("Get the key to the west. When you have the code use the keypad")
        
    elif command == "keypad":
        print(">You approach the keypad to the lab door.")
        theResult = False
        theResult = keypadGame()
        return theResult
        
    elif command == "keyhole":
        print(">You use the key and unlock the door to the meeting room.")
        
    elif command == "move":
        print(">I can't move that.")

    elif command == "turn":
        print(">I can't turn that.")
        
    elif command == "open":
        print(">I can't open that.")
        
    elif command == "keypadTwo":
        print(">You look at the keypad."
              "\n>It is a basic number keypad.")
        
    elif command == "keyholeTwo":
        print(">You look at the keyhole."
              "\n>Not too interesting, but where's the key?")
        
def keypadGame():
    """
    Keypad game function
    """
    
    while True:
        try:
            keypadInput = int(input(">I need to input four numbers:\n"
                                    "***1111 to exit***\n-->"))
            
            if len(str(keypadInput)) != 4:
                print("That was not four numbers!")
            else:
                if keypadInput == 2131:
                    print(">Correct!"
                          "\n>The door to the lab unlocks.\n")
                    return True
                    
                elif keypadInput == 1111:
                    print(">You leave the keypad be for now.\n")
                    return False
                    
                else:
                    print(">Incorrect passcode!\n")
                
        except ValueError:
            print(">That's not a number! How did that happen?")  

def living(command):
    """
    The living quarters room and command responses.
    """
    
    if command == "west":
        print(">To the west is a small window and a few more bunkbeds"
              "\n>You can see some glowing jellyfish passing by the window."
              "\n>One of the bunkbeds here is your."
              "\n>Nothing of interest seem to be here.")
        
    elif command == "east":
        print(">You went through the east door."
              "\n>You are now in the upper corridor."
              "\n>To the north is the door to the lab."
              "\n>To the east is the door to the meeting room."
              "\n>To the west is the door to the living quarters"
              "\n>To the south is the ladder down to the lower corridor.")
        
    elif command == "north":
        print(">To the north there are two chairs and a table."
              "\n>They are usually used by the crew when playing card games."
              "\n>Lily, a orphaned blond haired girl that is currently traveling"
              " with the crew for various reasons." 
              "\n>She is very fond of playing games.")
        
        while True:
            inputPanel = str(input("Would you like to talk to her?.\n--->"))
            if inputPanel == "yes" or inputPanel == "y":
                riddleGame()
                break
                    
            elif inputPanel == "no" or inputPanel == "n":
                print(">You leave and move on.")
                break
                    
            else:
                print("What do you mean \"" + str(inputPanel) + "\"")
        
    elif command == "south":
        print("To the south there are just a few bunkbeds used by the crew."
              "\n>Nothing of interest seem to be here.")
        
    elif command == "inspect":
        print(">You inspect the living quarters."
              "\n>To the west is a small window and a few bunkbeds."
              "\n>To the south is another set of bunk beds."
              "\n>To the east is the door to the upper corridor."
              "\n>To the north is a table and some chairs. There's also a young"
              " blond girl sitting on one of the chairs. It's Lily! "
              "\n>Maybe she knows something?")
        
    elif command == "clue":
        print("Go to Lily")
        
    elif command == "use":
        print(">I don't think this is the right time to sleep.")
        
    elif command == "open":
        print(">How would I even open a bed?")
        
    elif command == "move":
        print(">The bed is attached to the wall, I can't move it")
    
    elif command == "turn":
        print(">I can't turn this, it is attached to the wall.")
        
    elif command == "bed":
        print(">You look at the bed."
              "\n>The bed looks comfy.")
    
        
def riddleGame():
    """
    The riddle game.
    """
    print(">You approach Lily."
          "\n>She looks at you and says: Hey first-mate anything on your mind?"
          " Maybe your are looking for this?"
          "\n>Lily holds up a silver key."
          "\n>Lily says: It's the key for the meeting room. You can have it if"
          " you can solve this riddle. Okay? Here I go!"
          "\n>'I remain calm and cool among turmult and fury.'"
          "\n>'I hide treasures and creature you could hardly fathom'"
          "\n>'I will crush those I welcome in deeply.'"
          "\n>'I am dark yet beatiful. What am I?'"
          "\n1) A dragon\n2) A Pirate \n3) The ocean\n")
    
    while True:
        try:
            inputRiddle = int(input("What do you think?\n-->"))
            
                    
            if inputRiddle == 3:
                print(">Lily says: That's right! The ocean! Here you go. "
                      "\n>Lily gives you the key to the meeting room."
                      "\n>Lily says: See you later first-mate!"
                      "\n>You leave with the key.")
                break
            else:
                print(">Lily says: That's not quite correct. Try again!")
                
        except ValueError:
            print("That's not a number")
    
def meeting(command):
    """
    the meeting room and all of its respone commands.
    """
    
    if command == "west":
        print(">You went through the west door."
              "\n>You are now in the upper corridor."
              "\n>To the north is the door to the lab."
              "\n>To the east is the door to the meeting room."
              "\n>To the west is the door to the living quarters"
              "\n>To the south is the ladder down to the lower corridor.")
        
    elif command == "east":
        print(">To the east is a big window showing the dark ocean."
              "\n>You see nothing interesting outside.")
        
    elif command == "north":
        print(">To the north is the meeting table."
              "\n>This is where the crew gather up for meals as well as "
              " bigger meetings."
              "\n>Today no one seems to be here.")
        
    elif command == "south":
        print(">To the south is a table with a strange puzzle box on it."
              "\n>On the box there is something inscribed."
              "\n>It says: 'codes and secrets inside'."
              "\n>Maybe the code for the lab is inside this box?")
        
    elif command == "inspect":
        print(">You are in the meeting room."
              "\n>To the north is a meeting table with several chairs"
              "\n>To the south is a table with a box on it."
              "\n>To the east is a big window showing the darkness" 
              " of the ocean."
              "\n>To the west is the door to the upper corridor."
              "\n>The box on the table seem interesting.")
        
    elif command == "clue":
        print(">Turn the box, then use it.")
        
    elif command == "turn":
        print(">You turn the box, revealing a small touchscreen on the otherside."
              "\n>The screen displays a play button with the text 'Guess the number'"
              " written out above it."
              "\n>Maybe I need to play this game to unlock its contents?")
        
    elif command == "use":
        print(">You use the box by touching the play button."
              "\n>The game starts up.")
        guessGame()
        print(">You notice the box unlocked.")
        
    elif command == "open":
        print(">You try to open the box."
              "\n>It wont budge, maybe I need to do something to unlock it first?")
        
    elif command == "move":
        print(">I don't see the point in moving the box.")
        
    elif command == "box":
        print(">You look at the box."
              "\n>It seems to have something on the backside.")

def guessGame():
    """
    The guessing game
    """
    
    while True:
        guesses = 0
        number = random.randint(1, 100)
        print(">I am thinking of a number between 1 and 100, guess it!")
    
        while guesses < 6:
            try:
                guess = int(input(">Take a guess.\n--->"))
            except ValueError:
                print("That's not a number!")
            
            guesses = guesses + 1
    
            if guess < number:
                print(">Think bigger!")
            
            elif guess > number:
                print(">Think smaller!")
                
            elif guess == number:
                break
                
        if guess == number:
            print(">CORRECT! Good job . "
                  "You guessed it in " + str(guesses) + " tries.")
            break
    
        if guess != number:
            print(">HA!" 
                  "The number you should have guessed was " + str(number))
            print(">Try again!")
            
        
def lab(command):
    """
    The lab room and the command responses.
    """
    
    if command == "west":
        print(">To the west is some uninteresting lab equipment."
              "\n>Nothing else of interest is here.")
        
    elif command == "east":
        print(">To the east is a desk with a computer on it."
              "\n>The computer should have the research results on it."
              "\n>Now to access it.")
        
    elif command == "north":
        print(">To the north is the display case with the material sample."
              "\n>The material looks like an orange crystal. It is giving off "
              "a reddish glow."
              "\n>I should probably leave it alone."
              "\n>Nothing else of interest is here.")
        
    elif command == "south":
        print(">You went through the south door."
              "\n>You are now in the upper corridor."
              "\n>To the north is the door to the lab."
              "\n>To the east is the door to the meeting room."
              "\n>To the west is the door to the living quarters"
              "\n>To the south is the ladder down to the lower corridor.")
        
    elif command == "inspect":
        print("You are finally inside the lab."
              "\n>To the south is the door to the upper corridor."
              "\n>To the east is a desk with a computer on it."
              "\n>To the west is some uninterseting lab equipment."
              "\n>To the north is the strange material sample inside"
              " a display case"
              "\n>Maybe the computer could print out the results?")
        
    elif command == "clue":
        print("Use the computer.")
        
    elif command == "use":
        print(">You start using the computer.")
        computerGame()
        
    elif command == "move":
        print(">I should probably not try to move the computer.")
        
    elif command == "turn":
        print(">I should probably not try to turn the computer.")
        
    elif command == "open":
        print(">I should probably not try to move the computer.")
        
    elif command == "computer":
        print(">You look at the computer."
              "\n>It looks pretty expensive."
              "\n>It should have the lab results on it.")
        
def computerGame():
    """
    The computer puzzle.
    """
    nextPress = 0
    
    
    print(">The computer displays a wall of text with three buttons below it."
          "\n>The buttons are: 'Next' , 'Previous' and 'Print'")
    
    while True:
        inputButton = str(input("\n1)Next\n2)Previous\n3)Print\n"
                                "Which button should I press?\n-->"))
        
        if inputButton == "3":
            if nextPress == 2:
                print(">You press the print button."
                      "\n>The page prints out. You take the printed research results."
                      "\n>Now to deliver it to the captain!")
                break
            else:
                print(">This is not the right page. "
                      "\n>You should keep looking.")
            
        elif inputButton == "1":
            print(">You press the 'Next' button."
                  "\n>The page changes.")
            nextPress = nextPress + 1
            if nextPress == 1:
                print(">The display show a little bit of text with the headline:"
                      "\n>'Fish and Fishsticks: a delicious combination'"
                      "\n>That doesn't seem quite right.")
                
            elif nextPress == 2:
                print(">The display shows a wall of text with the headline:"
                      "\n>'Research sample, lab results'"
                      "\n>This seems to be it, now to print it out.")
                
            elif nextPress == 3:
                print(">The display shows a wall of text with the headline:"
                      "\n>'The mysteries of the sea'"
                      "\n>This doesn't seem to be quite it.")
            else:
                print(">There are no more pages than this."
                      "\n>Maybe I should go to one of the previous pages.")
                nextPress = nextPress - 1
                
        elif inputButton == "2":
            print(">You press the 'Previous' button.")
            nextPress = nextPress - 1
            if nextPress <= 0:
                print(">There are no previous pages."
                      "\n>I should go to the next page.")
                nextPress = 0
            
            elif nextPress == 1:
                print(">The display show a little bit of text with the headline:"
                      "\n>'Fish and Fishsticks: a delicious combination'"
                      "\n>That doesn't seem quite right.")
                
            elif nextPress == 2:
                print(">The display shows a wall of text with the headline:"
                      "\n>'Research sample, test results'"
                      "\n>This seems to be it, now to print it out.")
                
            elif nextPress == 3:
                print(">The display shows a wall of text with the headline:"
                      "\n>'The mysteries of the sea'"
                      "\n>This doesn't seem to be quite it.")
            else:
                print(">There are not more pages than this."
                      "\n>Maybe I should go to one of the previous pages.")
                nextPress = nextPress - 1
           
        else:
            print("What do you mean '" + inputButton + "'. You should press 1,2 or 3.")
    

def gameStart():
    """
    game main method.
    """
    Gameover = True
    
    #Rooms
    roomBridge = True
    roomCorridorOne = False
    roomCorridorTwo = False
    roomEngine = False
    roomLiving = False
    roomMeeting = False
    roomLab = False
    
    #Items
    itEngineManual = False
    itWrench = False
    itKey = False
    itLabResult = False
    
    #Objects
    objDesk = False
    objHatch = False
    objEngine = False
    objKeypad = False
    objKeyhole = False
    objBoxTurn = False
    objBox = False
    
    print(">You are the first-mate at a submarine that is researching a strange "
          "material that have been found around Marianna Trench in the pacific ocean." 
          "\n> You have just been asked by the captain to go get the research " 
          "results from a collected sample of the material. It is however in the "
          "on board research lab. Go get it!")

    while Gameover:
        
        inputCommand = str(input("What should I do next.\n--->"))
        
        #Other commands.
        if inputCommand == "h" or inputCommand == "help":
            print("""The control commands are as following:

        help - shows this help message.
        exit - exit program. (Progress will be reset.
                
        e, east - Your character goes east, if possible.
        w, west - Your character goes west if possible.
        n, north - Your character goes north if possible.
        s, south - Your character goes south if possible.
                
        Note: that if there is an item or character in the direction you go to
        your character will automatically interact with it.
                
        i, inspect - describes the room you are in and all objects of interest.
        c, clue - gives a clue about the room your character is in.
        <object> - describes an object.
        use <object> - uses an object is available.
        move <object> - moves an object if possible.
        open <object> - opens an object if possible.
        turn <object> - turns an object if possible.
            """)
        
        elif inputCommand == "exit":
            print("Exiting program")
            input()
            break
            
        #Item commands.
        elif itWrench and inputCommand == "wrench":
            print(">You look at the wrench. It looks well used.")
            
        elif itEngineManual and inputCommand == "manual":
            print(">You look at the engine manual."
                  "\n>The titles says 'Submarine engine 101'"
                  "\n>There's some instructions written inside."
                  "\n>To lower the steam, turn valve 1 twice, turn valve 2 once"
                  " and valve 3 once.")
            
        elif itKey and inputCommand == "key":
            print(">You look at the key."
                  "\n>It is shiny.")
            
        elif itLabResult and inputCommand == "result":
            print(">You look at the lab results."
                  "\n>It is just a bunch of numbers and texts.")
        
        #The bridge room and all the rooms.
        elif roomBridge and inputCommand != None:
            if inputCommand == "e" or inputCommand == "east":
                bridge("east")
                
            elif inputCommand == "w" or inputCommand == "west":
                bridge("west")
                roomBridge = False
                roomCorridorOne = True
                
            elif inputCommand == "n" or inputCommand == "north":
                if itLabResult == False:
                    bridge("north")
                else:
                    bridge("final")
                    break
                
            elif inputCommand == "s" or inputCommand == "south":
                bridge("south")
                
            elif inputCommand == "i" or inputCommand == "inspect":
                bridge("inspect")
                if objDesk == False:
                    print("There's a desk in the south end of the room")
                else:
                    print("That's the desk you got the engine manual from.")
                
            elif inputCommand == "c" or inputCommand == "clue":
                bridge("clue")
                
            elif inputCommand == "Open desk" or inputCommand == "open desk":
                bridge("open")
                objDesk = True
                itEngineManual = True
                
            elif inputCommand == "Move desk" or inputCommand == "move desk":
                bridge("move")
                
            elif inputCommand == "Use desk" or inputCommand == "use desk":
                bridge("use")
                
            elif inputCommand == "Turn desk" or inputCommand == "turn desk":
                bridge("turn")
                
            elif inputCommand == "desk":
                bridge("desk")
                
            else:
                print("What do you mean \"" + str(inputCommand) + "\"")
        
        #The lower corridor room and all commands.
        elif roomCorridorOne and inputCommand != None:
            if inputCommand == "e" or inputCommand == "east":
                corridorOne("east")
                roomCorridorOne = False
                roomBridge = True
 
            elif inputCommand == "w" or inputCommand == "west":
                corridorOne("west")
                roomCorridorOne = False
                roomEngine = True
                
            elif inputCommand == "n" or inputCommand == "north":
                if objHatch == True:
                    corridorOne("north")
                    roomCorridorOne = False
                    roomCorridorTwo = True
                else:
                    print(">I can't go up the ladder to the upper corridor."
                          "\n>There's a sealed hatch blocking the way")
                
            elif inputCommand == "s" or inputCommand == "south":
                corridorOne("south") 
 
            elif inputCommand == "i" or inputCommand == "inspect":
                corridorOne("inspect")
                if objHatch == False:
                    print("There's a sealed hatch blocking the way to the upper corridor.")
                else:
                    print("The hatch that blocked the way to the upper corridor is wide open.")
                    
            elif inputCommand == "c" or inputCommand == "clue":
                corridorOne("clue")
                
            elif inputCommand == "use wrench" or inputCommand == "open hatch":
                if itWrench == False:
                    corridorOne("open")
                else:
                    if objHatch == False and itWrench == True:
                        print(">You force open the hatch with the wrench you got from"
                              " the engine room."
                              "\n>The hatch slam open, and clear the path up to the "
                              "upper corridor.")
                        objHatch = True
                    else:
                        print(">The hatch is already open.")
                        
            elif inputCommand == "Move hatch" or inputCommand == "move hatch":
                corridorOne("move")
                
            elif inputCommand == "Use hatch" or inputCommand == "use hatch":
                corridorOne("use")
                
            elif inputCommand == "Turn hatch" or inputCommand == "turn hatch":
                corridorOne("turn")
                
            elif inputCommand == "hatch":
                corridorOne("hatch")
                
            else:
                print("What do you mean \"" + str(inputCommand) + "\"")
                
                
        #The engine room and all the commands.        
        elif roomEngine and inputCommand != None:
            if inputCommand == "e" or inputCommand == "east":
                engine("east")
                roomEngine = False
                roomCorridorOne = True
                    
            elif inputCommand == "w" or inputCommand == "west":
                if itWrench:
                    print(">There's nothing else of interst here.")
                elif objEngine:
                    print(">You go to the now steam free west end of room."
                          "\n>There's a wrench on the floor. You pick it up."
                          "\n>This might be useful!")
                    itWrench = True
                else:
                    engine("west")
                    
            elif inputCommand == "n" or inputCommand == "north":
                engine("north")
                    
            elif inputCommand == "s" or inputCommand == "south":
                    
                if objEngine:
                    print(">You approach the control panel."
                          "\n>There doesn't seem to be anything of interest here.")
                else:
                    objEngine = engine("south")
                    
            elif inputCommand == "i" or inputCommand == "inspect":
                engine("inspect")
                    
            elif inputCommand == "c" or inputCommand == "clue":
                if objEngine:
                    print("Get the wrench to the west.")
                else:
                    engine("clue")
                    
            elif inputCommand == "use control panel":
                    
                if objEngine:
                    print(">You approach the control panel."
                          "\n>There doesn't seem to be anything else you can do here.")
                       
                else:
                    objEngine = engine("panel")
                    
            elif inputCommand == "use engine":
                engine("use")
                    
            elif inputCommand == "move control panel" or inputCommand == "move engine":
                engine("move")
                    
            elif inputCommand == "open engine" or inputCommand == "open control panel":
                engine("open")
                    
            elif inputCommand == "turn engine" or inputCommand == "turn control panel":
                engine("turn")
                    
            elif inputCommand == "engine":
                engine("engine")
                    
            elif inputCommand == "control panel":
                engine("control")
                    
            else:
                print("What do you mean \"" + str(inputCommand) + "\"")
        
        #The upper corridor room and all the commands.
        elif roomCorridorTwo and inputCommand != None:
            if inputCommand == "e" or inputCommand == "east":
                if objKeyhole == False:
                    corridorTwo("east")
                else:
                    print(">You go through the door to the east."
                          "\n>You enter the meeting room."
                          "\n>To the north is a meeting table with several chairs"
                          "\n>To the south is a table with a box on it."
                          "\n>To the east is a big window showing the darknesss" 
                          " of the ocean."
                          "\n>To the west is the door to the upper corridor.")
                    roomCorridorTwo = False
                    roomMeeting = True
                    
            elif inputCommand == "w" or inputCommand == "west":
                corridorTwo("west")
                roomCorridorTwo = False
                roomLiving = True
                    
            elif inputCommand == "s" or inputCommand == "south":
                corridorTwo("south")
                roomCorridorTwo = False
                roomCorridorOne = True
                    
            elif inputCommand == "n" or inputCommand == "north":
                if objKeypad == False:
                    corridorTwo("north")
                else:
                    print("You go through the door to the north."
                          "\n>You are now inside the lab."
                          "\n>To the south is the door to the upper corridor."
                          "\n>To the east is a desk with a computer on it."
                          "\n>To the west is some uninterseting lab equipment."
                          "\n>To the north is the strange material sample inside"
                          "a display case")
                    roomCorridorTwo = False
                    roomLab = True
                    
            elif inputCommand == "i" or inputCommand == "inspect":
                corridorTwo("inspect")
                    
            elif inputCommand == "c" or inputCommand == "clue":
                corridorTwo("clue")
                    
            elif inputCommand == "Use keypad" or inputCommand == "use keypad":
                objKeypad = corridorTwo("keypad")
                    
            elif inputCommand == "use keyhole":
                print(">I can't use that")
                    
            elif inputCommand == "Use key" or inputCommand == "use key":
                if itKey == True:
                    corridorTwo("keyhole")
                    objKeyhole = True
                else:
                    print(">You don't have a key.")
                    
            elif inputCommand == "move keypad" or inputCommand == "move keyhole":
                corridorTwo("move")
                    
            elif inputCommand == "turn keypad" or inputCommand == "turn keyhole":
                corridorTwo("turn")
                    
            elif inputCommand == "open keypad" or inputCommand == "open keyhole":
                corridorTwo("open")
                    
            elif inputCommand == "keypad":
                corridorTwo("keypadTwo")
                    
            elif inputCommand == "keyhole":
                corridorTwo("keyholeTwo")
                    
            else:
                print("What do you mean \"" + str(inputCommand) + "\"")
        
        #The living quarters room and all the commands.
        elif roomLiving and inputCommand != None:
            if inputCommand == "e" or inputCommand == "east":
                living("east")
                roomLiving = False
                roomCorridorTwo = True
                    
            elif inputCommand == "w" or inputCommand == "west":
                living("west")
                    
            elif inputCommand == "s" or inputCommand == "south":
                living("south")
                    
            elif inputCommand == "n" or inputCommand == "north":
                if itKey == True:
                    print(">Lily seems satisfied."
                          "\n>You decide to move on.")
                else:
                    living("north")
                    itKey = True
                    
            elif inputCommand == "i" or inputCommand == "inspect":
                living("inspect")
                    
            elif inputCommand == "c" or inputCommand == "clue":
                living("clue")
                    
            elif inputCommand == "use bed" or inputCommand == "use bunkbed":
                living("use")
                    
            elif inputCommand == "move bed" or inputCommand == "move bunkbed":
                living("move")
                    
            elif inputCommand == "turn bed" or inputCommand == "turn bunkbed":
                living("turn")
                    
            elif inputCommand == "open bed" or inputCommand == "open bunkbed":
                living("open")
                    
            elif inputCommand == "bed":
                living("bed")
                    
            else:
                print("What do you mean \"" + str(inputCommand) + "\"")
        
        #The meeting room and all the commands.
        elif roomMeeting and inputCommand != None:
            if inputCommand == "e" or inputCommand == "east":
                meeting("east")
                    
            elif inputCommand == "w" or inputCommand == "west":
                meeting("west")
                roomMeeting = False
                roomCorridorTwo = True  
                    
            elif inputCommand == "s" or inputCommand == "south":
                meeting("south")
                    
            elif inputCommand == "n" or inputCommand == "north":
                meeting("north")
                    
            elif inputCommand == "i" or inputCommand == "inspect":
                meeting("inspect")
                    
            elif inputCommand == "c" or inputCommand == "clue":
                meeting("clue")
                    
            elif inputCommand == "Use box" or inputCommand == "use box":
                if objBoxTurn == False:
                    print(">There doesn't seem to be any visible way to open it."
                          "\n>Maybe if I turn it?")
                else:
                    if objBox == True:
                        print(">No point using the box again, it is already "
                              "open.")
                    else:
                        meeting("use")
                        objBox = True
                    
            elif inputCommand == "Move box" or inputCommand == "move box":
                meeting("move")
                    
            elif inputCommand == "Turn box" or inputCommand == "turn box":
                meeting("turn")
                objBoxTurn = True
                    
            elif inputCommand == "Open box" or inputCommand == "open box":
                if objBox == False:
                    meeting("open")
                else:
                    print(">You open the box revealing a paper."
                          "\n>Something is written on the paper."
                          "\n>It says: 'Lab code: 3121 don't forget it!'"
                          "\n>You leave the paper in the box and close it.")
                
            elif inputCommand == "box":
                meeting("box")
                    
            else:
                print("What do you mean \"" + str(inputCommand) + "\"")
        
        #The Lab room and all the commands.
        elif roomLab and inputCommand != None:
            if inputCommand == "e" or inputCommand == "east":
                lab("east")
                    
            elif inputCommand == "w" or inputCommand == "west":
                lab("west")
                    
            elif inputCommand == "s" or inputCommand == "south":
                lab("south")
                roomLab = False
                roomCorridorTwo = True
                    
            elif inputCommand == "n" or inputCommand == "north":
                lab("north")
                    
            elif inputCommand == "i" or inputCommand == "inspect":
                lab("inspect")
                    
            elif inputCommand == "c" or inputCommand == "clue":
                lab("clue")
                    
            elif inputCommand == "Use computer" or inputCommand == "use computer":
                lab("use")
                itLabResult = True
                    
            elif inputCommand == "Move computer" or inputCommand == "move computer":
                lab("move")
                    
            elif inputCommand == "Turn computer" or inputCommand == "turn computer":
                lab("turn")
                    
            elif inputCommand == "Open computer" or inputCommand == "open computer":
                lab("open")
                    
            elif inputCommand == "computer":
                lab("computer")
                    
            else:
                print("What do you mean \"" + str(inputCommand) + "\"")
            

