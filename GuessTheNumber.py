import random

def check(guess):
    '''
    Function to check whether user's guess is correct and display appropriate message.
    Function returns 1 (True) if user has guessed correctly. Otherwise, the function returns 0 (False).
    '''
    if guess==random_num:
        print("Great Job -- You guessed the number correctly!")
        return 1
    else:
        if guess>random_num:
            print("Your number was Greater than Random Number.")
        else:
            print("Your number was Smaller than Random Number.")
        return 0

# generate random integer between 0 and 20 using randint function
random_num = random.randint(0, 20)
print("Computer has selected a Random Number between 0 and 20. Guess the number computer has selected!!")
# set lives equal to 5
lives = 5
# let user guess 5 times
while lives>0:
    print("\nLives remaining: ", lives)
    guess = int(input("Make a guess: "))
    # if user guesses correctly, check(guess) will return 1 and if will be executed
    if check(guess):
        break
    # if user guesses incorrectly, else will be executed
    else:
        # decrement lives by 1
        lives = lives - 1
        # if user has lives remaining, try again
        if lives:
            print("Try again.")
# if all lives are used
if not lives:
    print("The random number selected was: ", random_num)
=======
import random

def check(guess):
    '''
    Function to check whether user's guess is correct and display appropriate message.
    Function returns 1 (True) if user has guessed correctly. Otherwise, the function returns 0 (False).
    '''
    if guess==random_num:
        print("Great Job -- You guessed the number correctly!")
        return 1
    else:
        if guess>random_num:
            print("Your number was Greater than Random Number.")
        else:
            print("Your number was Smaller than Random Number.")
        return 0

# generate random integer between 0 and 20 using randint function
random_num = random.randint(0, 20)
print("Computer has selected a Random Number between 0 and 20. Guess the number computer has selected!!")
# set lives equal to 5
lives = 5
# let user guess 5 times
while lives>0:
    print("\nLives remaining: ", lives)
    guess = int(input("Make a guess: "))
    # if user guesses correctly, check(guess) will return 1 and if will be executed
    if check(guess):
        break
    # if user guesses incorrectly, else will be executed
    else:
        # decrement lives by 1
        lives = lives - 1
        # if user has lives remaining, try again
        if lives:
            print("Try again.")
# if all lives are used
if not lives:
    print("The random number selected was: ", random_num)
