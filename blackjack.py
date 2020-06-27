from random import randrange

def main():
	global number_of_players
	#Find out number of players
	number_of_players = player_count()


	#Register player name and deal cards 
	for p in range(number_of_players):
		player(input("Player {}'s name:".format(p+1)))
		player_list[p].deal_card()
	print_all()


	#Check for Blackjack
	check = False
	for p in range(number_of_players):
		if player_list[p].sum == 21: 
			print("Blackjack! ", player_list[p].name, " has won!" )
			check = True
	if check == True: return True #Game End
			

	#hit or stand
	for p in range(number_of_players):
		player_list[p].hit_or_stand(p)
		print_all()


	#Find the winner 
	find_winner()



#counters and data
number_of_players = 0
player_list = []


#player class to input name, player_tag, sum of cards, cards recieved
#add players into player_list
#printing function to show cards recieved and sum 
class player:
	def __init__(self,name):
		self.name = name
		self.sum = 0 # total value of cards in hand
		self.cards = [] #list of the names of the card, acts as key to the poker deck 
		self.card_count = len(self.cards)
		self.ace = 0  # keeps track of number of aces that has value 11
		player_list.append(self)
		


	#deal first 2 cards 
	def deal_card(self):
		for i in range(2): 
			#Prevent same card from being drawn out 
			n = 0
			while True:
				n = randrange(52)
				if n in poker_deck.keys(): break
				else : continue

			#Draw card from the deck
			drawn = poker_deck.pop(n)

			#register card name
			self.cards.append(drawn[0])

			#Find value of hand 
			#Accounting for value of non-ace card
			if not drawn[1] == 'ace':
				self.sum += int(drawn[1])
			#Accounting for different values of ace
			else: 
				self.ace += 1
				#Double Ace scenario
				if self.ace == 2:
					self.sum = 21
				#Single ace scenario
				else: 
					self.sum += 11



	#Option to draw additional cards to increase sum
	def hit_or_stand(self, player_index):
		option = ' '

		while option != 'n' and self.card_count < 5:   #Cannot draw more than 5 cards in blackjack
			#input check
			while True:
				option = input("{}, do you wish to draw another card? (y/n)".format(self.name)).lower()
				if not option in ["y", "n"]: continue
				else: break

			#don't draw one more card
			if option == 'n': 
				print("\n")
				break

			#draw one more card
			else: 
				#Prevent same card from being drawn out 
				n = 0
				while True:
					n = randrange(52)
					if n in poker_deck.keys(): break
					else : continue

				#Draw card from the deck
				drawn = poker_deck.pop(n)

				#register card name
				self.cards.append(drawn[0])

				#Find value of hand 
				#Accounting for value of non-ace card
				if not drawn[1] == 'ace':
					self.sum += int(drawn[1])
				#Accounting for different values of ace
				else: 
					self.ace += 1 
					self.sum += 11

				#changing necessary amount of ace to 1 such that sum is below or equals to 21
				while self.ace>0 and self.sum>21:
					self.sum -=10 
					self.ace -= 1	

				#results of new draw
				self.print()
				if self.sum > 21: 
					print(self.name, "has busted!")
					break #Game End for this player

				print("\n")


	#printing out cards drawn and sum
	def print(self):
		print(self.name,': ', self.cards, self.sum)




#functions
#Number of players 
def player_count(): 
	#Guard against erronous inputs
	while True: 
		try: 
			player_count = int(input("Please enter number of players (2-26):"))
			if player_count > 1 and player_count < 27: 
				return player_count
			elif player_count < 2: 
				print("Too little players!") #Too little players to play 
				break 
			elif player_count > 26: 
				print("Too many players!") #Too little cards for all players
				break

		#Ask again if user does not input integer 
		except ValueError: 
			print("Only numbers from 2 to 26 accepted!")
			continue


#Printing out the cards and sum of all players
def print_all():
	global number_of_players
	print("\n")
	for p in range(number_of_players):
		player_list[p].print()
	
	print("\n")


#Finding players with the highest sum 
def find_winner():
	tmp = 0
	winner = []
	for p in range(number_of_players):
		#immediately declare those with 21 points as winners
		if player_list[p].sum == 21:
			#those in winner list also has 21 points
			if tmp == 21:
				winner.append(player_list[p].name)
			#those in winner list does not have 21 points
			elif tmp < 21:
				tmp = 21
				winner.clear()
				winner.append(player_list[p].name)


		elif player_list[p].sum < 21: 
			#current player sum is higher than players in front
			if player_list[p].sum > tmp:
				tmp = player_list[p].sum 
				winner.clear()
				winner.append(player_list[p].name)
			#current player sum is as high as the highest sum in front 
			elif player_list[p].sum == tmp:
				winner.append(player_list[p].name)
			#5 card charlie
			elif player_list[p].sum < 21 and player_list[p].card_count == 5:
				winner.append(player_list[p].name)

	#print winners
	for w in winner: 
		print(w, "has won!")


#dictionary that simulates a real poker deck 
poker_deck = {
	0 : ['Ace Diamond', 'ace'],
	1 : ['2 Diamond', '2'],
	2 : ['3 Diamond', '3'],
	3 : ['4 Diamond', '4'],
	4 : ['5 Diamond', '5'],
	5 : ['6 Diamond', '6'],
	6 : ['7 Diamond', '7'],
	7 : ['8 Diamond', '8'],
	8 : ['9 Diamond', '9'],
	9 : ['10 Diamond', '10'],
	10 : ['Jack Diamond', '10'],
	11 : ['Queen Diamond', '10'],
	12 : ['King Diamond', '10'],
	13: ['Ace Club', 'ace'],
	14: ['2 Club', '2'],
	15: ['3 Club', '3'],
	16 : ['4 Club', '4'],
	17 : ['5 Club', '5'],
	18: ['6 Club', '6'],
	19: ['7 Club', '7'],
	20: ['8 Club', '8'],
	21: ['9 Club', '9'],
	22: ['10 Club', '10'],
	23 : ['Jack Club', '10'],
	24 : ['Queen Club', '10'],
	25 : ['King Club', '10'],
	26 : ['Ace Heart', 'ace'],
	27 : ['2 Heart', '2'],
	28 : ['3 Heart', '3'],
	29: ['4 Heart', '4'],
	30 : ['5 Heart', '5'],
	31 : ['6 Heart', '6'],
	32 : ['7 Heart', '7'],
	33 : ['8 Heart', '8'],
	34 : ['9 Heart', '9'],
	35 : ['10 Heart', '10'],
	36 : ['Jack Heart', '10'],
	37 : ['Queen Heart', '10'],
	38 : ['King Heart', '10'],
	39 : ['Ace Spade', 'ace'],
	40 : ['2 Spade', '2'],
	41 : ['3 Spade', '3'],
	42 : ['4 Spade', '4'],
	43 : ['5 Spade', '5'],
	44: ['6 Spade', '6'],
	45: ['7 Spade', '7'],
	46 : ['8 Spade', '8'],
	47 : ['9 Spade', '9'],
	48 : ['10 Spade', '10'],
	49 : ['Jack Spade', '10'],
	50 : ['Queen Spade', '10'],
	51 : ['King Spade', '10'],
}

main()


