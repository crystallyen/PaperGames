#IMPORTS
from .Number_Guesser import Number_Guesser
from .Tic_Tac_Toe import TicTacToe

#CODE
Input = input(Welcome to π PaperGames!
β It's a simple app aimed at containing a collection of simple games.
π¨ Made by Crystallyen
π Version 0.3.1
[1] π’ Number Guesser
        β Think of a number and say if it is above or below my number from which I will try to guess it!
        π¨ Singleplayer
[2] π Tic Tac Toe
        β A classic game where there are two players assigned with  X  or  O  and the first one to make 3 cells in a line in a 3 x 3 square containing their symbol wins!
        π¨ Multiplayer
 Type the number to the side of their name to play it!  )

def GameHandler()
    global Input
    try
        Input = int(Input)
    except
        print(Invalid input Type a valid integer [1 or 2])
        print()
        GameHandler()
    if Input == 1
        del Input
        Number_Guesser()
    elif Input == 2
        del Input
        TicTacToe()
    else
        print(Invalid input Type a valid integer [1 or 2])
        print()
        GameHandler()

GameHandler()

def GameMenu()
    global Input
    Input = input(πPaperGames  Menu
[1] π’Number Guesser
        β Think of a number and say if it is above or below my number from which I will try to guess it!
        π§βπ€βπ§ Singleplayer
[2] πTic Tac Toe
        β A classic game where there are two players assigned with X or O and the first one to make 3 cells in a row containing their symbol wins!
        π§βπ€βπ§ Multiplayer
 Type the number to the side of their name to play it! )
    try
        Input = int(Input)
        if Input == 1
            del Input
            Number_Guesser()
        elif Input == 2
            del Input
            TicTacToe()
        else
            print(Invalid input Type a valid integer [1 or 2])
            print()
            GameHandler()
    except
        print(Invalid input Type a valid integer [1 or 2])
        print()
        GameHandler()
