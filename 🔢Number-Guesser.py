#IMPORTS
import math
from random import randrange

#DEFINING VARIABLES
Database = {
    "Gamemode": "",
    "PossibleNumbers": [],
    "PotentialNumbers": [],
    "Count": 0,
    "GuessedNumber": ""
}

#CODE

##Asks the player to choose a gamemode and saves it to the database
def GamemodeChooser():
    GamemodeInput = input(">> Type \"s\" to choose Smart guesser, \"r\" to choose the Random guesser and \"m\" to choose the Mixed guesser: ")
    if GamemodeInput.lower() == "s" or GamemodeInput.lower() == "r" or GamemodeInput.lower() == "m":
        Database["Gamemode"] = GamemodeInput.lower()
    else:
        print("")
        print("Invalid input: Choose a valid option")
        GamemodeChooser()

##Asks the player the range, makes a list of all possible numbers and saves it to the database
def RangeHandler():
    RangeInput = input(">> Type the highest number(inclusive) till which you will guess: ")
    try:
        RangeInput = int(RangeInput)
        if RangeInput >= 10:
            for number in range(1,(RangeInput + 1)):
                Database["PossibleNumbers"].append(number)
        else:
            print("Invalid input: The range can be 10 minimum.")
            RangeHandler()
    except:
        print("Invalid Input: The range can not be anthing else than an integer")
        RangeHandler()

##Creates a list of potential numbers from the 3 algorithms and saves it to the database
def PotentialNumbersCreator():
    Database["PotentialNumbers"].clear()
    if bool(len(Database["PossibleNumbers"]) > 2) is True:
        if Database["Gamemode"] == "m":
            if (Database["Count"] % 2) == 1:
                PotentialNumberLength = math.floor(len(Database["PossibleNumbers"]) / 2)
            else:
                PotentialNumberLength = randrange(len(Database["PossibleNumbers"]))
        elif Database["Gamemode"] == "s":
            PotentialNumberLength = math.floor(len(Database["PossibleNumbers"]) / 2)
        elif Database["Gamemode"] == "r":
            PotentialNumberLength = randrange(len(Database["PossibleNumbers"]))
        if PotentialNumberLength == Database["PossibleNumbers"][0]:
            PotentialNumberLength = Database["PossibleNumbers"][1]
        elif PotentialNumberLength == Database["PossibleNumbers"][-1]:
            PotentialNumberLength = Database["PossibleNumbers"][-2]
        PNCcounter = 0
        while bool(len(Database["PotentialNumbers"]) < PotentialNumberLength) is True:
            Database["PotentialNumbers"].append(Database["PossibleNumbers"][PNCcounter])
            PNCcounter = PNCcounter + 1
    else:
        Database["PotentialNumbers"].append(Database["PossibleNumbers"][0])
    
##Sends the win message, resets the database and starts a new game
def WinHandler():
    print("The number is " + str(Database["GuessedNumber"]) + " and was guessed in " + str(Database["Count"]) + " Queries")
    print("\n\n\n")
    Database["PotentialNumbers"] = []
    Database["PossibleNumbers"] = []
    Database["Count"] = 0
    Game()

##Asks the player if their number is higher than or lower than the number guessed by the computer, updates the possible numbers, calls itself recursively if not guessed or calls the winhandler functon if guessed
def Guess():
    if bool(Database["Count"] != 1) is True and bool((len(Database["PossibleNumbers"])) >> 1):
        print("I am guessing the number is between " + str(Database["PossibleNumbers"][0]) + " and " + str(Database["PossibleNumbers"][-1]) )
    Database["Count"] = Database["Count"] + 1
    if len(Database["PossibleNumbers"]) != 1:
        PotentialNumbersCreator()
        Command =  input(">> Type \"h\" if your number is higher than, \"l\" if your number is lower than and \"e\" if your number is equal to " + str(Database["PotentialNumbers"][-1]) + ": ")
        print("")
        if Command == "h":
            LastElementPossibleNumbers = Database["PossibleNumbers"][-1]
            LastElementPotentialNumbers = Database["PotentialNumbers"][-1]
            if LastElementPotentialNumbers == LastElementPossibleNumbers:
                print("Invalid input: There is no number higher than " + str(LastElementPossibleNumbers) + "!")
                Guess()
            else:
                Database["PossibleNumbers"] = [x for x in Database["PossibleNumbers"] if x not in Database["PotentialNumbers"]]
                Guess()
        elif Command == "l":
            FirstElementPossibleNumbers = Database["PossibleNumbers"][0]
            FirstElementPotentialNumbers = Database["PotentialNumbers"][-1]
            if FirstElementPotentialNumbers == FirstElementPossibleNumbers:
                print("Invalid input: There is no number lower than " + str(FirstElementPossibleNumbers) + "!")
                Guess()
            else:
                Database["PossibleNumbers"] = Database["PotentialNumbers"][:-1]
                Guess()
        elif Command == "e":
            Database["GuessedNumber"] = Database["PotentialNumbers"][-1]
            WinHandler()
        else:
            print("Invalid input: Type \"h\" if your number is higher than, \"l\" if your number is lower than and \"e\" if your number is equal to " + str(Database["PotentialNumbers"][-1]) + ": ")
            Guess()
    else:
        Database["GuessedNumber"] = Database["PossibleNumbers"][-1]
        WinHandler()

##The game function. Starts a game when called
def Game():
    print("Welcome to the number guessing game made by Crystallyen.")
    print("""
    How to Play:
    To play this game first choose a number and say if it is above or below my number from which I will try to guess it!
    There are 3 algorithms for guessing the number:
    
        [s] Smart guesser
            It tries to guess the number by finding the middle of the possible numbers. 
            It may not be fast but it is the most consistent.

        [r] Random guesser
            It tries to guess the number by asking a random number from the possible numbers.
            This alogoritm may be fast at guessing the number but is not consistent.

        [m] Mixed guesser
            It tries to guess a number by switching between the smart guesser algorithm and the random guesser algorithm every query.
            This algorith may be faster than Smart guesser alone. It is more consistent than Random guesser alone.

        All of these algorithms will not guess a number that is at the either the lowest possible number or the highest possible numbers unless if there are only 2 possible numbers.
        """)
    GamemodeChooser()
    RangeHandler()
    Guess()

##Calls the game function to start the game
Game()
