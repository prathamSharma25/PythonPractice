import random

def check_user_input(func_input):
    '''
    Function to check and parse user's input into required form.
    '''
    if func_input[0]=="'" and func_input[-1]=="'":
        func_input = func_input.strip('\'')
    elif func_input[0]=='"' and func_input[-1]=='"':
        func_input = func_input.strip('\"')
    elif (func_input[0]=="'" and func_input[-1]!="'") or (func_input[0]!="'" and func_input[-1]=="'"):
        print("User Passed Unbalanced quotes. Please pass Balanced quotes or no quotes at all.")
    else:
        pass

def result(pair):
    '''
    Function to check and display the result of the game.
    User's and Computer's choice is passed to the function as the argument 'pair'.
    User's choice is the first element in the tuple 'pair' and Computer's choice is the second.
    '''
    # Display user's and computer's choice
    print("User's Choice: {}".format(pair[0]))
    print("Computer's Choice: {}".format(pair[1]))
    # If any draw condition is satisfied
    if pair in draw:
        print("Its a draw. Both selected {}.".format(pair[0]))
    # If win condition for User is satisfied
    elif pair in win:
        print("User WON the game as {} beats {}.".format(pair[0], pair[1]))
    # Else Computer wins
    else:
        print("Computer WON the game as {} beats {}.".format(pair[1], pair[0]))
        
# User's and Computer's choice is denoted as a tuple => (users_choice, computer_choice)
# Condition for a draw between User and Computer
draw = [('Rock', 'Rock'), ('Paper', 'Paper'), ('Scissors', 'Scissors')]
# Condition for a win for User
win = [('Paper', 'Rock'), ('Scissors', 'Paper'), ('Rock', 'Scissors')]

# Read and check User's input
user = input("Make a Guess: ")
check_user_input(user)
# Computer selects a tool at random from the list of tools
computer = random.choice(['Rock', 'Paper', 'Scissors'])
# Get result for the game; User's and Computer's choice is passed as a tuple => (user, computer)
result((user, computer))