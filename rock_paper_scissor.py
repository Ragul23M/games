
import random

print('Rules of the game ROCK PAPER SCISSORS are :\n'
  + "ROCK defeats SCISSORS\n"
	+ "PAPER defeats ROCK\n"
	+ "SCISSORS defeats PAPER\n")

while True:
	print("Choices \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
	
	# Input
	choice=int(input("Enter your choice :"))
	
	# invalid choice loop
	while choice > 3 or choice <1:
	  choice=int(input('Enter a valid choice please '))
    
	if choice == 1:
		choice_name= 'Rock'
	elif choice == 2:
		choice_name= 'Paper'
	else:
		choice_name= 'Scissors'
		
	print('You have chosen \n',choice_name)
	print('Computer\'s Turn....')
	comp_choice = random.randint(1,3)
		
	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'Paper'
	else:
		comp_choice_name = 'Scissor'
	print("Computer choice is \n", comp_choice_name)
	print(choice_name,'Vs',comp_choice_name)
	#draw
	if choice == comp_choice:
		print('Its a Draw',end="")
		result="DRAW"
	#win paper
	if (choice==1 and comp_choice==2):
		print('paper wins =>',end="")
		result='Paper'
	elif (choice==2 and comp_choice==1):
		print('paper wins =>',end="")
		result='Paper'	
  #win rock
	if (choice==1 and comp_choice==3):
		print('Rock wins =>\n',end= "")
		result='Rock'
	elif (choice==3 and comp_choice==1):
		print('Rock wins =>\n',end= "")
		result='Rock'
  #win Scissors
	if (choice==2 and comp_choice==3):
		print('Scissors wins =>',end="")
		result='Scissors'
	elif (choice==3 and comp_choice==2):
		print('Scissors wins =>',end="")
		result='Scissors'

	#result
	if result == 'DRAW':
		print("<== Its a tie ==>")
	if result == choice_name:
		print("<== User wins ==>")
	else:
		print("<== Computer wins ==>")
	print("play again? (Y/N)")
	#exit
	ans = input().lower()
	if ans=='n':
		break
print("thanks for playing")
