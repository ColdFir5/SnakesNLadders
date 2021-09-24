# Libraries
import numpy as np
from random import *

# Functions
## Creates a 10x10 grid filled with numbers from 1-100 in zigzag formation # made by Michael
def CreateGrid():
    SetSize = 10 # Sets base size for x and y axis
    grid = [] # Makes the grid

    # Adds the rows and columns for the grid
    for row in range(0, SetSize):
        grid.append([])
        for column in range(0, SetSize):
            grid[row].append(" ")

    # Left to right display
    ## Sets Variables
    Count = 1
    Current_Row = 9
    Current_Column = 0

    # Does 50 loops that are divided by 5
    for num in range(1, 51):
        # Places the numbers in the grid
        grid[Current_Row][Current_Column] = Count

        # Makes all numbers 3 digits with 0s in front
        if len(str(grid[Current_Row][Current_Column])) == 1:
            grid[Current_Row][Current_Column] = f"00{grid[Current_Row][Current_Column]}"
        elif len(str(grid[Current_Row][Current_Column])) == 2:
            grid[Current_Row][Current_Column] = f"0{grid[Current_Row][Current_Column]}"

        # Goes to the next number and next position(column)
        Current_Column += 1
        Count += 1

        # If the pointer is past position 9 in the list it will increase the count by 10
        if Current_Column % 10 == 0:
            Current_Column = 0
            Count += 10

        # If the num is divisible by 10 then go up to columns to the next 'left to right' display of numbers
        if num % 10 == 0:
            Current_Row -= 2

    # Right to left display
    ## Sets Variables
    Count = 11
    Current_Row = 8
    Current_Column = 9

    # Does 50 loops that are divided by 5
    for num in range(1, 51):
        # Places the numbers in the grid
        grid[Current_Row][Current_Column] = Count

        # Makes all numbers 3 digits with 0s in front
        if len(str(grid[Current_Row][Current_Column])) == 2:
            grid[Current_Row][Current_Column] = f"0{grid[Current_Row][Current_Column]}"
        
        # Goes to the next number and next position(column)
        Current_Column -= 1
        Count += 1

        # If the pointer is past position 9 in the list it will increase the count by 10
        if Current_Column == -1:
            Current_Column = 9
            Count += 10
        
        # If the num is divisible by 10 then go up to columns to the next 'left to right' display of numbers
        if num % 10 == 0:
            Current_Row -= 2

    ## Sends the grid data back to where the function is called
    return grid

## Places all snakes and ladders on the grid # made by Michael
def SnakesAndLadders(S, L, Grid):
    # Sets Variables
    Ladders = L
    Snakes = S
    grid = Grid

    Count = 1 # Sets Count to 1
    for Ladder in Ladders:
        # Sets the first(start) pos of the ladder(ladder_pos1) to the row and column stated in Ladder[0]
        ladder_pos1 = Ladder[0]
        # Sets the second(end) pos of the ladder(ladder_pos2) to the row and column stated in Ladder[1]
        ladder_pos2 = Ladder[1]

        # Adds the ladder to the grid based on the value of 'count'
        ## First Pos
        grid[int(ladder_pos1[0])][int(ladder_pos1[1])] = f"L|{Count}"
        ## Second Pos
        grid[int(ladder_pos2[0])][int(ladder_pos2[1])] = f"L|{Count}"

        # Increments 'Count'
        Count += 1

    Count = 1 # Sets Count to 1
    for Snake in Snakes:
        # Sets the first(start) pos of the snake(snake_pos1) to the row and column stated in Snake[0]
        snake_pos1 = Snake[0]
        # Sets the second(end) pos of the snake(snake_pos2) to the row and column stated in Snake[1]
        snake_pos2 = Snake[1]

        # Adds the ladder to the grid based on the value of 'count'
        ## First Pos
        grid[int(snake_pos1[0])][int(snake_pos1[1])] = f"S|{Count}"
        ## Second Pos
        grid[int(snake_pos2[0])][int(snake_pos2[1])] = f"S|{Count}"

        # Increments 'Count'
        Count += 1

## Calculates the movements for the players when moving from left to right on the grid #done by meerko
def LeftToRightMove(player):
    # Sets Variables
    Win = "None"
    game_over = False

    # Player One
    if player == "P1":
        Moves = player1_move
        for i in range(player1_move):
            # If the player's column value is in range of 0-9
            if player1_pos[1] in range(10):
                player1_pos[1] += 1 # Increments column value by 1
                Moves -= 1
                pass
        # If the player's column is equal to 10
        if player1_pos[1] == 10:
            # Sets Row to Row-1(Up one)
            player1_pos[0] -= 1
            # Sets Column to the last value in the list(9)
            player1_pos[1] = 9

        ## Sends all this data back to where the function is called
        return player1_pos[0], player1_pos[1], Moves, Win, game_over

    # Player Two
    elif player == "P2":
        Moves = player2_move
        for i in range(player2_move):
            # If the player's column value is in range of 0-9
            if player2_pos[1] in range(10):
                player2_pos[1] += 1 # Increments column value by 1
                Moves -= 1
                pass
        # If the player's column is equal to 10
        if player2_pos[1] == 10:
            # Sets Row to Row-1(Up one)
            player2_pos[0] -= 1
            # Sets Column to the last value in the list(9)
            player2_pos[1] = 9

        ## Sends all this data back to where the function is called
        return player2_pos[0], player2_pos[1], Moves, Win, game_over

## Calculates the movements for the players when moving from right to left on the grid #done by meerko
def RightToLeftMove(player):
    # Sets Variables
    Win = "None"
    game_over = False

    # Player One
    if player == "P1":
        Moves = player1_move
        for i in range(player1_move):
            # If the player's column value is in range of 0-9
            if player1_pos[1] in range(10) and (player1_pos[0] > 0 or player1_pos[1] > 0):
                player1_pos[1] -= 1 # Increments column value by 1
                Moves -= 1
                pass
            # If Player's position within the column is within the range of 0-9 and their position is equal to 0,0(100)
            elif player1_pos[1] in range(10) and player1_pos[0] == 0 and player1_pos[1] == 0:
                game_over = True
                Moves = 0
                Win = "Player One"

        # If the player's column is equal to -1
        if player1_pos[1] == -1:
            player1_pos[0] -= 1
            player1_pos[1] = 0

        ## Sends all this data back to where the function is called
        return player1_pos[0], player1_pos[1], Moves, Win, game_over

    # Player Two
    elif player == "P2":
        Moves = player2_move
        for i in range(player2_move):
            # If the player's column value is in range of 0-9
            if player2_pos[1] in range(10) and (player2_pos[0] > 0 or player2_pos[1] > 0):
                player2_pos[1] -= 1 # Increments column value by 1
                Moves -= 1
                pass
            # If Player's position within the column is within the range of 0-9 and their position is equal to 0,0(100)            
            elif player2_pos[1] in range(10) and player2_pos[0] == 0 and player2_pos[1] == 0:
                game_over = True
                Moves = 0
                Win = "Player Two"

        # If the player's column is equal to -1
        if player2_pos[1] == -1:
            player2_pos[0] -= 1
            player2_pos[1] = 0

        ## Sends all this data back to where the function is called
        return player2_pos[0], player2_pos[1], Moves, Win, game_over

# Variables #
Ladders = [
  [[9, 1], [6, 2]],
  [[9, 7], [7, 9]],
  [[7, 0], [5, 1]],
  [[5, 9], [3, 6]]
] ## List of all the ladders start and end position

Snakes = [
  [[9, 3], [8, 6]],
  [[7, 7], [2, 4]],
  [[2, 9], [0, 8]],
  [[2, 0], [0, 2]]
] ## List of all the snakes start and end positions

player1_pos = [9, 0] ## Player two starting position
player2_pos = [9, 0] ## Player two starting position

previous_pos_val1 = "001" ## Previous position value of player one
previous_pos_val2 = "001" ## Previous position value of player two

previous_pos1 = [9, 0] ## Previous position of player one
previous_pos2 = [9, 0] ## Previous position of player two

Moves = 0
Roll = 0
Win = "None"
Turn = "P1"

game_over = False

grid = CreateGrid()

# Main Code
## Add snakes and ladders to grid
SnakesAndLadders(Snakes, Ladders, grid)

## Checks if Player One position is the same as Player Two's position
if player1_pos[0] == player2_pos[0] and player1_pos[1] == player2_pos[1]:
    grid[int(player1_pos[0])][int(player1_pos[1])] = "👾 👽" ## Sets that position to display both players

## Displays the grid with the players on the grid (with numbers)  
print(np.matrix(grid))
print("Player 1 will be using 👾 and player 2 will be using 👽") #done by meerko
## If the game is not over
while not game_over:
    ## If its Player One's turn and the dice rolls is not equal to 2
    # Code for player 1 (made by Lucas)
    if Turn == "P1" and Roll != 2:
        ## Set Variables
        player1_move = 0
        Count = 1

        ## Dice roll
        input(f"\nPlayer One:\nPress Enter to roll the die...(Roll:{Roll + 1})")
        player1_move = randrange(1,7)
        print(f"Player 1 has rolled a {player1_move}")
        print(f"Player One has moved {player1_move} spaces forward.\n")

        ## Continue moving player until Player One's moves is equal to 0
        while player1_move != 0:
            ## Left to right movements
            if player1_pos[0] in range(9, 0, -2):
                ## Store data on when the player moves
                Data = LeftToRightMove("P1")
                
                ## Sets these variables to the data obtained from the player's move
                player1_pos[0], player1_pos[1], player1_move, Win, game_over = Data[0], Data[1], Data[2], Data[3], Data[
                    4]

            if player1_pos[0] in range(8, -2, -2):
                ## Store data on when the player moves
                Data = RightToLeftMove("P1")

                ## Sets these variables to the data obtained from the player's move
                player1_pos[0], player1_pos[1], player1_move, Win, game_over = Data[0], Data[1], Data[2], Data[3], Data[
                    4]

                if game_over:
                    player1_pos = [0, 0] ## Setplayer position back to 0,0(100)
                    break
        
        ## Checks if Player One position is the same as Player Two's position
        if player1_pos[0] == player2_pos[0] and player1_pos[1] == player2_pos[1]:
            ## If the Player One's previous position is 9,0(001)
            if previous_pos1 == [9, 0]:
                ## Sets the previous position of Player One on the grid to equal 001
                grid[int(previous_pos1[0])][int(previous_pos1[1])] = "001"
            else:
                ## Sets the previous position of Player One on the grid to equal the value placed at the previous Player One position
                grid[int(previous_pos1[0])][int(previous_pos1[1])] = previous_pos_val1

            ## Sets Player One's previous position value on the grid to be the value of the previous position of Player Two
            previous_pos_val1 = previous_pos_val2

            ## Sets the previous position of Player One to be the current position of Player One
            previous_pos1[0] = player1_pos[0]
            previous_pos1[1] = player1_pos[1]

            ## Sets that position to display both players
            grid[int(player1_pos[0])][int(player1_pos[1])] = "👾 👽"
        else:
            for Ladder in Ladders:
                ## If player lands on the start of a ladder they get moved to the other end of the ladder
                if player1_pos[0] == Ladder[0][0] and player1_pos[1] == Ladder[0][1]:
                    player1_pos[0] = Ladder[1][0]
                    player1_pos[1] = Ladder[1][1]
                    print("Well done! Player one has climbed a ladder!\n")
                    break

            for Snake in Snakes:
                ## If player lands on the start of a snake they get moved to the other end of the snake
                if player1_pos[0] == Snake[1][0] and player1_pos[1] == Snake[1][1]:
                    player1_pos[0] = Snake[0][0]
                    player1_pos[1] = Snake[0][1]
                    print("Oh no! Player one has slid down a snake!\n")
                    break

            ## Sets the previous position of Player One on the grid to equal the value placed at the previous Player One position     
            grid[int(previous_pos1[0])][int(previous_pos1[1])] = previous_pos_val1

            ## If previous position of Player One is equal to 9,0(001)
            if previous_pos1 == [9, 0]:
                ## Sets the previous position of Player One on the grid to equal 001                
                grid[int(previous_pos1[0])][int(previous_pos1[1])] = "001"

            ## Sets Player One's previous position value on the grid to be the value located at Player One's current position
            previous_pos_val1 = grid[int(player1_pos[0])][int(player1_pos[1])]

            ## Sets the previous position of Player One to be the current position of Player One
            previous_pos1[0] = player1_pos[0]
            previous_pos1[1] = player1_pos[1]

            ## Sets Player One's current position value to be "!" on the grid
            grid[int(player1_pos[0])][int(player1_pos[1])] = " 👾 "

            ## Sets Player Two's current position value to be "?" on the grid
            grid[int(player2_pos[0])][int(player2_pos[1])] = " 👽 "

            for Positions in range(len(Ladders)):
                ## If Player One & Player Two's current position is not equal to the end of the ladders position
                if player1_pos != Ladders[Positions][1] and player2_pos != Ladders[Positions][1]:
                    grid[int(Ladders[Positions][1][0])][int(Ladders[Positions][1][1])] = f"L|{Count}"
                
                ## If Player One & Player Two's current position is not equal to the end of the snake position
                if player1_pos != Snakes[Positions][0] and player2_pos != Snakes[Positions][0]:
                    grid[int(Snakes[Positions][0][0])][int(Snakes[Positions][0][1])] = f"S|{Count}"
                
                ## Checks if Player One position is the same as Player Two's position              
                if player1_pos[0] == player2_pos[0] and player1_pos[1] == player2_pos[1]:
                    grid[int(player1_pos[0])][int(player1_pos[1])] = "👾 👽" ## Sets that position to display both players
                    
                Count += 1 ## Increment 'Count' by 1

        ## Displays the grid with the players on the grid (with numbers)
        print(np.matrix(grid))

        if game_over:
            Roll = 2
        else:
            Roll += 1

        if Roll == 2:
            Turn = "P2"
            Roll = 0
    #End of player 1 code made by Lucas
    ## If its Player Two's turn and the dice rolls is not equal to 2 (made by Michael)
    elif Turn == "P2" and Roll != 2:
        ## Set Variables
        player2_move = 0
        Count = 1 
        ## Dice roll # Michael
        input(f"\nPlayer Two:\nPress Enter to roll the die...(Roll:{Roll + 1})")
        player2_move = randrange(1,7)
        print(f"Player Two has rolled a {player2_move}")
        print(f"Player Two has moved {player2_move} spaces forward.\n")
        
        ## Continue moving player until Player Two's moves is equal to 0
        while player2_move != 0:
            ## Left to right movements
            if player2_pos[0] in range(9, 0, -2):
                ## Store data on when the player moves # Michael
                Data = LeftToRightMove("P2")

                ## Sets these variables to the data obtained from the player's move
                player2_pos[0], player2_pos[1], player2_move, Win, game_over = Data[0], Data[1], Data[2], Data[3], Data[
                    4]

            if player2_pos[0] in range(8, -2, -2):
                ## Store data on when the player moves
                Data = RightToLeftMove("P2")

                ## Sets these variables to the data obtained from the player's move
                player2_pos[0], player2_pos[1], player2_move, Win, game_over = Data[0], Data[1], Data[2], Data[3], Data[
                    4]

                if game_over:
                    player2_pos = [0, 0] ## Setplayer position back to 0,0(100)
                    break

        ## Checks if Player Two position is the same as Player One's position
        if player2_pos[0] == player1_pos[0] and player2_pos[1] == player1_pos[1]:
            ## If the Player Two's previous position is 9,0(001)
            if previous_pos2 == [9, 0]:
                ## Sets the previous position of Player Two on the grid to equal 001
                grid[int(previous_pos2[0])][int(previous_pos2[1])] = "001"
            else:
                ## Sets the previous position of Player Two on the grid to equal the value placed at the previous Player Two position
                grid[int(previous_pos2[0])][int(previous_pos2[1])] = previous_pos_val2
            ## Sets Player Two's previous position value on the grid to be the value of the previous position of Player One
            previous_pos_val2 = previous_pos_val1

            ## Sets the previous position of Player Two to be the current position of Player Two
            previous_pos2[0] = player2_pos[0]
            previous_pos2[1] = player2_pos[1]
            
            ## Sets that position to display both players
            grid[int(player1_pos[0])][int(player1_pos[1])] = "👾 👽"
        else:
            for Ladder in Ladders:
                ## If player lands on the start of a ladder they get moved to the other end of the ladder
                if player2_pos[0] == Ladder[0][0] and player2_pos[1] == Ladder[0][1]:
                    player2_pos[0] = Ladder[1][0]
                    player2_pos[1] = Ladder[1][1]
                    print("Well done! Player two has climbed a ladder!\n")
                    break
                    #done by meerko

            for Snake in Snakes:
                ## If player lands on the start of a snake they get moved to the other end of the snake
                if player2_pos[0] == Snake[1][0] and player2_pos[1] == Snake[1][1]:
                    player2_pos[0] = Snake[0][0]
                    player2_pos[1] = Snake[0][1]
                    print("Oh no! Player two has slid down a snake!\n")
                    break
                    #done by meerko
            ## Sets the previous position of Player Two on the grid to equal the value placed at the previous Player Two position
            grid[int(previous_pos2[0])][int(previous_pos2[1])] = previous_pos_val2

            ## If previous position of Player Two is equal to 9,0(001)
            if previous_pos2 == [9, 0]:
                ## Sets the previous position of Player Two on the grid to equal 001 
                grid[int(previous_pos2[0])][int(previous_pos2[1])] = "001"

            ## Sets Player Two's previous position value on the grid to be the value located at Player Two's current position
            previous_pos_val2 = grid[int(player2_pos[0])][int(player2_pos[1])]
            
            ## Sets the previous position of Player Two to be the current position of Player Two
            previous_pos2[0] = player2_pos[0]
            previous_pos2[1] = player2_pos[1]

            ## Sets Player One's current position value to be "!" on the grid
            grid[int(player1_pos[0])][int(player1_pos[1])] = " 👾 "

            ## Sets Player Two's current position value to be "?" on the grid
            grid[int(player2_pos[0])][int(player2_pos[1])] = " 👽 "

            for Positions in range(len(Ladders)):
                ## If Player One & Player Two's current position is not equal to the end of the ladders position # Michael
                if player1_pos != Ladders[Positions][1] and player2_pos != Ladders[Positions][1]:
                    grid[int(Ladders[Positions][1][0])][int(Ladders[Positions][1][1])] = f"L|{Count}"
                
                ## If Player One & Player Two's current position is not equal to the end of the snake position
                if player1_pos != Snakes[Positions][0] and player2_pos != Snakes[Positions][0]:
                    grid[int(Snakes[Positions][0][0])][int(Snakes[Positions][0][1])] = f"S|{Count}"
                
                ## Checks if Player One position is the same as Player Two's position 
                if player1_pos[0] == player2_pos[0] and player1_pos[1] == player2_pos[1]:
                    grid[int(player1_pos[0])][int(player1_pos[1])] = "👾 👽" ## Sets that position to display both players
                    
                Count += 1 ## Increment 'Count' by 1
        
        ## Displays the grid with the players on the grid (with numbers)
        print(np.matrix(grid))

        if game_over:
            Roll = 2
        else:
            Roll += 1

        if Roll == 2:
            Turn = "P1"
            Roll = 0

## Display the winner
print(f"\n{Win} Wins")