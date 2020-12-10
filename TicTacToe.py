'''
This is a Python implementation of TicTacToe game.
User (O) plays against Computer (X). Game rounds continue till user quits.
'''

import random
from itertools import combinations    

def instructions():
    '''
    This function displays the general instructions for playing TicTacToe when game is started.
    '''
    print("\n------------- Welcome to TIC-TAC-TOE -------------")
    print("\nCells in the Tic-Tac-Toe grid are numbered as follows:")
    print("\n\t\t1 | 2 | 3")
    print("\t\t---------")
    print("\t\t4 | 5 | 6")
    print("\t\t---------")
    print("\t\t7 | 8 | 9")
    print("\nUser is 'O' and Computer is 'X'. User must select a number between 1 and 9 to place 'O' in that cell.")
    print("Computer selects a grid cell at random and places 'X' if that cell is available.")
    print("User starts the game in each round. At the end of each round, user must select 'y' to play a new game or 'n' to quit.")

def show_grid(grid):
    '''
    Function to display the current state of the TicTacToe grid.
    '''
    print("\n")
    print("{} | {} | {}".format(grid[0], grid[1], grid[2]))
    print("----------")
    print("{} | {} | {}".format(grid[3], grid[4], grid[5]))
    print("----------")
    print("{} | {} | {}".format(grid[6], grid[7], grid[8]))
    print("\n")
    
def user_place():
    '''
    Function to allow user to place 'O' in desired cell. The function asks user to select grid cell by taking integer input.
    The function checks if the selected grid cell is available using the cell_available(cell_num) function.
    If cell is available, 'O' is placed in that cell. Otherwise, user is asked to select different cell number.
    '''
    cell_num = int(input("Where do you wish to place 'O'? Enter a number between 1 and 9: "))
    if cell_num>=1 and cell_num<=9:
        if cell_available(cell_num):
            grid[cell_num-1] = 'O'
            user.append(cell_num)
        else:
            print("Selected cell is already filled. Select different cell.")
            user_place()
    else:
        print("Please enter a number between 1 and 9 only.")
        user_place()
 
def computer_place():
    '''
    Function to place computer's 'X' in the TicTacToe grid. Computer selects a random number between 1 and 9 to place 'X'.
    Cell availability is checked using the cell_available(cell_num) function.
    If cell is available, 'X' is placed in that cell. Otherwise, computer_place() function is called again.
    '''
    cell_num = random.randint(1, 9)
    if cell_available(cell_num):
        grid[cell_num-1] = 'X'
        computer.append(cell_num)
        print("Computer placed 'X' in cell {}".format(cell_num))
    else:
        computer_place()
   
def cell_available(cell_num):
    '''
    Function to check if given cell is available or already filled.
    '''
    return grid[cell_num-1]==' '  

def check_grid_full():
    return (' ' not in grid)

def check_win(user, computer):
    '''
    Function to check if either user or computer has won.
    '''
    # List of combinations of grid positions that result in a win
    win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    
    if len(user)<3 or len(computer)<3:
        return 0
    else:
        # Sort user list
        user.sort()
        # Generate all combinations of length 3 for user
        user_comb = list(combinations(user, 3))
        # For each user combintion, check if it is a winning combination and retur 1 (True) is user wins
        for comb in user_comb:
            if comb in win:
                print("User Wins!")
                user_win=1
                return 1
        # Sort computer list
        computer.sort()
        # Generate all combinations of length 3 for computer
        computer_comb = list(combinations(computer, 3))
        # For each computer combintion, check if it is a winning combination and return 1 (True) is computer wins
        for comb in computer_comb:
            if comb in win:
                print("Computer Wins!")
                computer_win=1
                return 1
        # Return 0 (False) if no one wins
        return 0

def check_draw():
    '''
    Can you help me with the logic for identifying a draw?
    '''
    if check_win(user, computer) == 0 and len(user)+len(computer)==9:
        print("Its a draw. Neither User nor Computer won the game.")
        return 1
    else:
        return 0
  

# Main code
# Set boolean variable playing as True to start game
playing = True
# Display instructions
instructions()

while(playing):
    # Empty lists to store grid positions occupied by User and Computer
    user, computer = [], []
    # List of length 9 to denote the TicTacToe grid
    grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print("\n\n------------- Let's Play TIC-TAC-TOE -------------")
    # Show grid before game starts
    show_grid(grid)
    
    # Play round till User or Computer wins or grid is completely filled
    while True:
        # Check if grid is not full
        if not check_grid_full():
            # Let user place 'O'
            user_place()
            show_grid(grid)
            # Check for win or draw and end round if either is true
            if check_win(user, computer) or check_draw():
                break
        # If grid is full end round
        else:
            break
        
        # Check if grid is not full
        if not check_grid_full():
            # Let Computer place 'X'
            computer_place()
            show_grid(grid)
            # Check for win or draw and end round if either is true
            if check_win(user, computer) or check_draw():
                break
        # If grid is full end round
        else:
            break
            
    new_round = input("Play again? (y/n): ")
    # Set boolean variable according to user input for new round
    playing = (new_round=='y')
