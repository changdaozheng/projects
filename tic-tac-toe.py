#Game flow
def tic_tac_toe():
	print("Tic-Tac-Toe\n")
	print("Please enter the names of 2 players below.")
	
	player1 = player(input("Player 1:"), 1)
	player2 = player(input("Player 2:"), 2)


	

	draw_board()

	while True:

		print(player1.player_name,"'s turn.")
		play(player1)
		draw_board()
		if win(player1):
			print(player1.player_name," has won.")
			break
		else: pass

		print(player2.player_name,"'s turn.")
		play(player2)
		draw_board()
		if win(player2):
			print(player1.player_name," has won.")
			break
		else: pass


		








# Game Data 
cells = {
	'0a': (0,0),
	'0b': (0,1),
	'0c': (0,2),
	'1a': (1,0),
	'1b': (1,1),
	'1c': (1,2),
	'2a': (2,0),
	'2b': (2,1),
	'2c': (2,2),
	}

game = [[' ', ' ', ' '], 
		[' ', ' ', ' '],
		[' ', ' ', ' ']]


#Draws game board on the screen 
def draw_board():
	print('\n')
	print("    a    b    c")
	for count, row in enumerate(game):
		print(count, row)


#Inputs the player's choice into gameboard
def play(player):
	cell = ''
	while True:
		cell = input("Please enter a cell (e.g. 0a, 2c) :")

		if cell in cells.keys():
			break
		else: 
			print("Please enter a valid cell.")

	(r,c) = cells[cell]

	game[r][c] = player.player_symbol



#winning criteria
def win(player):
	symbol = player.player_symbol

	#There are a total of 8 ways to win tic-tac-toe. 3 vertical, 3 horizontal and 2 diagonal. 

	#verticals
	for column in range(3):
		count = 0
		for row in range(3):
			if game[row][column] == symbol:
				count += 1
		if count == 3:
			print(count)
			return True
		else: pass

	#horizontals
	for row in range(3):
		count = 0
		for column in range(3):
			if game[row][column] == symbol:
				count += 1
		if count == 3:
			return True
		else: pass

	#diagonals
	if game[0][0] == symbol and game[1][1] == symbol and game[2][2] == symbol:
		return True
	
	if game[0][2] == symbol and game[1][1] == symbol and game[2][0] == symbol: 
		return True

	return False 





class player:
	def __init__(self, player_name, player_number):
		self.player_name = player_name
		self.player_number= player_number
		
		if self.player_number == 1:
			self.player_symbol = 'x'
		elif self.player_number == 2:
			self.player_symbol = 'o'




	

tic_tac_toe()
