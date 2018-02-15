row1 = ['_','_','_'] # Start off the rows empty 
row2 = ['_','_','_']
row3 = ['_','_','_']
matrix = [row1,row2,row3] # turn the rows into a matrix
player1 = ['1',' ']
player2 = ['2',' ']
done = False
nturns = 0
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

def print_board(): # prints the board which is a combination of row 1 2 3 
	for i in matrix:
		print(i)

#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

def user_turn(player_turn):
	global matrix
	global turn
	global player1
	global player2

	print("Player ", player_turn[0], "'s turn\n")

	while 1:
		row = int(input("Pick a position (Row): ")) # ask users to input a column and row for their symbol
		col = int(input("Pick a position (Col): "))
		if col > 2 or row > 2:
			print("Out of bounds...(values are from 0 to 2), Try again..")
		elif matrix[row][col] != '_':
			print("\nAlready occupied, try something thats not...\n")
		else:
			break;

	if player_turn[1] == 'X' or player_turn[1] == 'x':
		matrix[row][col] = 'X'
		if turn == player2:
			turn = player1
		else:
			turn = player2

	elif player_turn[1] == 'O' or player_turn[1] == 'o':
		matrix[row][col] = 'O'
		if turn == player2:
			turn = player1
		else:
			turn = player2
	else: 
		print("Error, please try again...")
	pass

#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
def check_winner():
	global done
	global turn
	global player1
	global player2

	if turn == player1:
		turn = player2
	else:
		turn = player1

	if matrix[1][0] == matrix[1][1] == matrix[1][2] and matrix[1][0] != '_': # if it isnt _ than it is either a o or x
		done = True                                                       # checks win as a row, column, or diagonally
		print('\n')
		print_board()
		print("\nPlayer ",turn[0],"s' the winner!")
	elif matrix[2][0] == matrix[2][1] == matrix[2][2] and matrix[2][0] != '_':		
		done = True
		print('\n')
		print_board()
		print("\nPlayer ",turn[0],"s' the winner!")
	elif matrix[0][0] == matrix[0][1] == matrix[0][2] and matrix[0][0] != '_':
		done = True
		print('\n')
		print_board()
		print("\nPlayer ",turn[0],"s' the winner!")
	elif matrix[0][0] == matrix[1][0] == matrix[2][0] and matrix[2][0] != '_':
		done = True
		print('\n')
		print_board()
		print("\nPlayer ",turn[0],"s' the winner!")
	elif matrix[0][1] == matrix[1][1] == matrix[2][1] and matrix[0][1] != '_':
		done = True
		print('\n')
		print_board()
		print("\nPlayer ",turn[0],"s' the winner!")
	elif matrix[0][2] == matrix[1][2] == matrix[2][2] and matrix[0][2] != '_':
		done = True
		print('\n')
		print_board()
		print("\nPlayer ",turn[0],"s' the winner!")


	elif matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != '_':
		done = True
		print('\n')
		print_board()
		print("\nPlayer ",turn[0],"s' the winner!")
	elif matrix[2][0] == matrix[1][1] == matrix[0][2] and matrix[0][2] != '_':
		done = True
		print('\n')
		print_board()
		print("\nPlayer ",turn[0],"s' the winner!")
	pass

	if turn == player1:
		turn = player2
	else:
		turn = player1

#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

while 1:

	first_turn = input("Player 1 select (X,O): ")
	if first_turn == 'x' or first_turn == 'X' or first_turn == 'o' or first_turn == 'O':
		player1[1] = first_turn
		turn = player1

		if turn[1] == 'x' or turn[1] == 'X':
			player2[1] = 'o'
		else:
			player2[1] = 'x'

		break
	else:
		print("Invalid value, please try again...")

while done!= True: 
	print('\n')
	print_board()
	print('\n')

	if done != True:
		user_turn(turn)

	check_winner()  # constantly checks if we have a winner
	nturns += 1

	if nturns == 9: # cant fill out more than 9 slots, so if nobody won by then its a cats game
		print("Cats Game!")
		break;
