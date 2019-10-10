import random
# This is going to be a tic tac toe game

test_board = ["#","X","O","X","","X","O","O","","X"]

# Displays our game board
def display_board(gameboard):
	print(gameboard[1:4])
	print(gameboard[4:7])
	print(gameboard[7:10])

# Playerdata is our function to determine which player is X and which is O
def playerdata():
	player1 = input("Would you like to be X or O: ").upper()
	player2 = ''
	if player1 == "X":
		player2 = "O"
	else: player2 ="X"
	print(f"Player 1 is {player1}.\nPlayer 2 is {player2}")

	player_list = [player1, player2]
	return player_list

players = playerdata()
print(players)

def place_marker(board,marker,position):
	position = int(input("Where would you like to go: "))
	board[position] = marker
	return board

def win_check(board, mark):
	if board[1] == board [2] == board[3] == mark:
		return True
	elif board[3] == board[5] == board[7] == mark:
		return True
	elif board[1] == board[4] == board[7] == mark:
		return True
	elif board[7] == board[8] == board[9] == mark:
		return True
	elif board[9] == board[6] == board[3] == mark:
		return True
	elif board[1] == board[5] == board[9] == mark:
		return True
	else:
		return False

# Function that uses the random.randint() module to decide which player goes first
def choose_first():
	pass



# Returns a boolean indicating whether a space on board is freely available
def space_check(board,position):
	if board[position]:
		return True

# Function that checks if the board is full and returns a boolean value. True if full, False otherwise
def full_board_check(board):
	pass

# Function asking for player's next position and uses the space_check function to check if it's a free position.
# If it is free, return for later use
def player_choice(board):
	print("Please choose your position: ")
	pass

# Asks if player wants to play again and returns Boolean True if they do
def replay():
	play_again = input("Would you like to play again")
	if "y" in play_again.lower():
		return True
	else:
		return False




display_board(test_board)
#place_marker(test_board,'$',8)
display_board(test_board)
print(win_check(test_board,"X"))
