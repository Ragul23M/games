import random
import math

# Inputs
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))

#generating random number based on input
x = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# no of attempt is given in the while loop condition
while count < math.log(upper - lower + 1, 2):
  #loop variable increment
	count += 1
  #Input
	guess = int(input("Enter the guessed number: "))

	#winning condition
	if x == guess:
		print("You guessed right in ", count, " try")
		break
  #guessed number is small
	elif x > guess:
		print("You guessed too small!")
  #guessed number is high
	elif x < guess:
		print("You Guessed too high!")
    
if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")
