
# This is going to be a tic tac toe game



winner = False

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

def playgame():
	pass