import random
random_list=['Rock','Paper','Scissors']
def check_user_input(func_input):
    if func_input[0]=="'" and func_input[-1]=="'":
        func_input=func_input.strip('\'')
    elif func_input[0]=='"' and func_input[-1]=='"':
        func_input=func_input.strip('\"')
    elif (func_input[0]=="'" and func_input[-1]!="'") or (func_input[0]!="'" and func_input[-1]=="'"):
        print("User Passed Unbalanced quotes. Please pass Balanced quotes or no quotes at all.")
    else:
        pass

    if func_input in random_list:
        print("Users Choice: "+func_input)
        print("Computers Choice: "+r)
        if (func_input=='Paper' and r=='Paper') or (func_input=='Rock' and r=='Rock') or (func_input=='Scissors' and r=='Scissors'):
            print("Its a draw. Both selected "+func_input)
        elif func_input=='Paper' and r=='Rock':
            print("User WON the game as Paper Covers Rock")
        elif func_input=='Rock' and r=='Scissors':
            print("User WON the game as Rock Blunts the Scissors")
        elif func_input=='Scissors' and r=='Paper':
            print("User WON the game as Scissors cut the Paper")
        elif r=='Paper' and func_input=='Rock':
            print("Computer WON the game as Paper Covers Rock")
        elif r=='Rock' and func_input=='Scissors':
            print("Computer WON the game as Rock Blunts the Scissors")
        elif r=='Scissors' and func_input=='Paper':
            print("Computer WON the game as Scissors cut the Paper")
    else:
        print("Please pass a value from these three ONLY: Rock Paper Scissors. You passed:: "+func_input)

user_input=input("Make a Guess:")
r=random.choice(random_list)
check_user_input(user_input)