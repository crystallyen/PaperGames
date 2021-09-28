#FUNCTIONS
#Goes through the database values and checkes if someone has won by comparing 3 cell values aligned in different ways
def winchecker():
    if database["a1"] == database["a2"] == database["a3"] and database["a1"] != "":
        return True
    elif database["b1"] == database["b2"] == database["b3"] and database["b1"] != "":
            return True
    elif database["c1"] == database["c2"] == database["c3"] and database["c1"] != "":
            return True
    elif database["a1"] == database["b1"] == database["c1"] and database["a1"] != "":
            return True
    elif database["a2"] == database["b2"] == database["c2"] and database["a2"] != "":
            return True
    elif database["a3"] == database["b3"] == database["c3"] and database["a3"] != "":
            return True
    elif database["a1"] == database["b2"] == database["c3"] and database["a1"] != "":
            return True
    elif database["c1"] == database["b2"] == database["a3"] and database["c1"] != "":
            return True
    else:
        return False

#Goes through the database values and checks if the match has ended in a draw
def drawchecker():
    if database["a1"] != "" and database["a2"] != "" and database["a3"] != "" and database["b1"] != "" and database["b2"] != "" and database["b3"] != "" and database["c1"] != "" and database["c2"] != "" and database["c3"] != "":
        return True
    else:
        return False

#Checks the cell and if a cell has no value, it returns a space but if it has a value then it returns with the original value. Used for aligning the UI
def spc(valuee):
    if len(valuee) == 0:
        return " "
    else:
        return valuee

#Returns the letter of the player whose turn it is to play
def playerturn():
    if database["count"] % 2 == 1:
        return "X"
    else:
        return "O"

#Returns the name of the of the player whose turn it is to play
def playerturnname():
    if database["count"] % 2 == 1:
        return XPlayer
    else:
        return OPlayer

#Checks if the cell address input follows the requirements and saves it to the database
def cellwork(cellc):
    for allowedValue in allowedValues:
        if cellc.lower() == allowedValue:
            if database[cellc] == "":
                database[cellc] = playerturn()
                return True

#Reads the database and displays it in Tic-Tac-Toe format
def display():
    print("""
┌──1──┬──2──┬──3──┐
a  """ + spc(database["a1"]) + """  │  """ + spc(database["a2"]) + """  │  """ + spc(database["a3"]) + """  │
├─────┼─────┼─────┤
b  """ + spc(database["b1"]) + """  │  """ + spc(database["b2"]) + """  │  """ + spc(database["b3"]) + """  │
├─────┼─────┼─────┤
c  """ + spc(database["c1"]) + """  │  """ + spc(database["c2"]) + """  │  """ + spc(database["c3"]) + """  │
└─────┴─────┴─────┘""")

#DEFINING VALUES

#Defines the database with empty/default values
database = {
    "a1": "",
    "a2": "",
    "a3": "",
    "b1": "",
    "b2": "",
    "b3": "",
    "c1": "",
    "c2": "",
    "c3": "",
    "count": 1,
}

#sets the player name to an empty string
XPlayer = OPlayer = ""

#Specifies the values the input can be
allowedValues = ("a1","a2","a3","b1","b2","b3","c1","c2","c3")

#CODE

#Introduction
print("Welcome to the game of Tic-Tac-toe! This game was coded in python by Anirudh")
print("")

#Name Selector for player X
print("Write the name of the player who will play X")
XPlayer = input("")
print("Hello " + XPlayer + ", you will be playing as X")

#Name selector for player O
print("Write the name of the player who will play O")
OPlayer = input("")
print("Hello " + OPlayer + ", you will be playing as O")

#The game logic
while winchecker() == False and drawchecker() == False: #Checks if the game can be continued
    print("Move number: " + str(database["count"]) + " | Turn for " + playerturn()) #Says how many moves have been done and which player's turn it is
    display()
    cells = input(playerturnname() + ", type the cell address where you want to put " + playerturn() + ": ") #Asks the playing player to make a move
    if cellwork(cells) is True: #Checks if the input of the player has been accepted
        database["count"] = database["count"] + 1 #Increments the move number by one
        continue
else:
    if drawchecker() is True: #Checks if the game has resulted in a draw with the draw checking funtion
        print("Draw in " + str(database["count"]) + " moves! No one wins")
    else: #Congratulates the player who won if the game has not ended in a draw
        if database["count"] % 2 == 1:
            print(OPlayer + " Wins! Defeated " + XPlayer + " in " + str(database["count"]) + " moves!")
        else:
            print(XPlayer + " Wins! Defeated " + OPlayer + " in " + str(database["count"]) + " moves!")
    display()
    database = { #Resets the database
    "a1": "",
    "a2": "",
    "a3": "",
    "b1": "",
    "b2": "",
    "b3": "",
    "c1": "",
    "c2": "",
    "c3": "",
    "count": 1
    }