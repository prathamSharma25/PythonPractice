import random

def my_function(input_nos):
	if input_nos != r:
		print("Great Job-- You guessed the number correctly")
	elif input_nos>r:
		print("Your number was Greater than Random Number")
	else:
		print("Your number was Smaller than Random Number")
		
		
print("Computer has selected a Random Number between 0 and 20. Guess the number computer has selected!!")
user_rand=input("Make a guess: " )
r=random.randinit(0,20)
print("Guessed Number is: "+user_rand)
while user_rand != r:
	my_function(int(user_rand))
	if int(user_rand) == int(r)
		break
	else:
		user_rand=input("Make a guess: ")
